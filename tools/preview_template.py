"""
Template Previewer Tool
Fast draft compiler to visually preview any draft or registered template
with realistic NEET physics parameters.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from config import RAW_VIDEO_DIR

def preview_template(template_target: str, resolution: str = "1280,720", fps: int = 30):
    t_start = time.time()
    preview_dir = BASE_DIR / "output" / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    
    # Resolve target file or class
    target_path = Path(template_target)
    if target_path.exists() and target_path.suffix == ".py":
        module_path = target_path
        template_name = target_path.stem
        # Derive ClassName e.g. modern_trajectory -> ModernTrajectoryScene
        class_name = "".join(word.capitalize() for word in template_name.split("_")) + "Scene"
    else:
        # Check drafts first, then render/templates
        snake_name = "".join(["_" + c.lower() if c.isupper() else c for c in template_target]).lstrip("_")
        draft_file = BASE_DIR / "render" / "templates" / "drafts" / f"{snake_name}.py"
        prod_file = BASE_DIR / "render" / "templates" / f"{snake_name}.py"
        
        if draft_file.exists():
            module_path = draft_file
        elif prod_file.exists():
            module_path = prod_file
        else:
            raise FileNotFoundError(f"Could not locate template file for: {template_target}")
            
        template_name = template_target
        class_name = f"{template_target}Scene" if not template_target.endswith("Scene") else template_target

    print(f"🎬 Previewing Template: {class_name} from {module_path.name}")
    print(f"   Settings: {resolution} @ {fps}fps")

    dummy_node = {
        "videoId": f"PREVIEW_{template_name}",
        "prompt_version": "v1",
        "serialTitle": f"Reference Preview: {template_name}",
        "subject": "Physics",
        "grade": 11,
        "templateName": template_name,
        "dimension": "2d",
        "parameters": {
            "latexFormula": r"v^2 = u^2 + 2as",
            "plainFormula": "v^2 = u^2 + 2as",
            "trapWarning": "Deceleration requires negative sign for acceleration!",
            "graphPlot": "2*x - 0.2*x**2",
            "xRange": [0, 6],
            "yRange": [0, 5],
            "seqChapterStr": "Concept 04 of 14 in Kinematics"
        },
        "durations": {
            "settle": 1.0,
            "hook": 2.0,
            "concept": 3.0,
            "trap": 2.5,
            "capsule": 2.0,
            "release": 3.5
        },
        "next_video_id": "P11-C02-T03-V03",
        "next_video_title": "Horizontal Range and Complementary Angles",
        "seq_chapter": 4,
        "total_chapter_videos": 14
    }

    temp_json = BASE_DIR / "render" / f"_temp_preview_{template_name}.json"
    temp_runner = BASE_DIR / "render" / f"_temp_preview_runner_{template_name}.py"

    with open(temp_json, "w", encoding="utf-8") as f:
        json.dump(dummy_node, f, ensure_ascii=False)

    runner_code = f'''import sys
import json
from pathlib import Path

sys.path.insert(0, {repr(str(BASE_DIR))})
sys.path.insert(0, {repr(str(module_path.parent))})

import importlib.util
spec = importlib.util.spec_from_file_location("template_module", {repr(str(module_path))})
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

TargetSceneClass = getattr(module, {repr(class_name)}, None)
if TargetSceneClass is None:
    # Fallback to finding any subclass of NEETVideoScene in module
    from render.templates.base import NEETVideoScene
    for attr in dir(module):
        obj = getattr(module, attr)
        if isinstance(obj, type) and issubclass(obj, NEETVideoScene) and obj is not NEETVideoScene:
            TargetSceneClass = obj
            break

if TargetSceneClass is None:
    raise AttributeError(f"Could not find scene class in {repr(str(module_path))}")

with open({repr(str(temp_json))}, "r", encoding="utf-8") as f:
    node_data = json.load(f)

class ActivePreviewScene(TargetSceneClass):
    def __init__(self, **kwargs):
        super().__init__(node_data=node_data, **kwargs)
'''
    with open(temp_runner, "w", encoding="utf-8") as f:
        f.write(runner_code)

    media_dir = preview_dir / "manim_temp"
    out_video_name = f"{template_name}_preview.mp4"
    final_output_path = preview_dir / out_video_name

    cmd = [
        "manim",
        "render",
        "-r", resolution,
        "--fps", str(fps),
        "--media_dir", str(media_dir),
        "-o", out_video_name,
        str(temp_runner),
        "ActivePreviewScene"
    ]

    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError as err:
        print(f"❌ Preview Compilation Failed!\nSTDOUT:\n{err.stdout}\nSTDERR:\n{err.stderr}")
        return None
    finally:
        if temp_runner.exists():
            temp_runner.unlink()
        if temp_json.exists():
            temp_json.unlink()

    # Move rendered file from manim media dir to preview_dir
    found_renders = list(media_dir.glob(f"**/{out_video_name}"))
    if found_renders:
        shutil.move(str(found_renders[0]), str(final_output_path))
        if media_dir.exists():
            shutil.rmtree(media_dir, ignore_errors=True)
            
    elapsed = time.time() - t_start
    print(f"✅ Preview Video Rendered in {elapsed:.1f}s!")
    print(f"   Saved to: {final_output_path}")
    return final_output_path

def main():
    parser = argparse.ArgumentParser(description="Fast Preview Compiler for Manim Templates")
    parser.add_argument("--template", type=str, required=True, help="Template name (e.g. ModernTrajectory) or file path")
    parser.add_argument("--res", type=str, default="1280,720", help="Resolution width,height (default: 1280,720)")
    parser.add_argument("--fps", type=int, default=30, help="Framerate (default: 30)")
    args = parser.parse_args()

    preview_template(args.template, args.res, args.fps)

if __name__ == "__main__":
    main()
