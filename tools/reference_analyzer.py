"""
Reference Analyzer Tool
Orchestrates keyframe extraction, palette analysis, and Manim draft template generation
from any social media / educational reference video or image collection.
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, Any, List
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from tools.keyframe_extractor import extract_keyframes, get_video_metadata
from tools.palette_extractor import extract_palette_from_images

def to_snake_case(name: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def generate_manim_draft_code(template_name: str, theme: dict, metadata: dict) -> str:
    bg = theme["background"]
    text_color = theme["text_primary"]
    accent1 = theme["accent_primary"]
    accent2 = theme["accent_secondary"]
    accent3 = theme["accent_tertiary"]
    
    code = f'''"""
Draft Template: {template_name}
Synthesized from reference video by Reference Analyzer.
Aspect Ratio: {metadata.get("aspect_ratio", "16:9")}
"""

from manim import *
import numpy as np
from render.templates.base import BaseNeetScene, TEXT_WHITE, MUTED_TEXT

# Extracted Visual Style
PALETTE = {{
    "bg": "{bg}",
    "text": "{text_color}",
    "accent_1": "{accent1}",
    "accent_2": "{accent2}",
    "accent_3": "{accent3}",
}}

class {template_name}Scene(BaseNeetScene):
    def render_concept_beats(self):
        # 1. Custom Background Theme Override
        self.camera.background_color = PALETTE["bg"]
        
        # 2. Dynamic Visual Elements
        formula_str = self.parameters.get("latexFormula", r"v^2 = u^2 + 2as")
        plain_formula = self.parameters.get("plainFormula", "v^2 = u^2 + 2as")
        trap_text = self.parameters.get("trapWarning", "Pay close attention to vector direction & signs!")

        # --- BEAT 1: SETTLE ---
        settle_text = Text(self.serial_title, font_size=26, weight=BOLD, color=PALETTE["accent_1"])
        settle_text.move_to(ORIGIN + UP * 0.5)
        self.play(FadeIn(settle_text), run_time=1.5)
        self.wait(1.0)
        self.play(FadeOut(settle_text), run_time=0.8)

        # --- BEAT 2: CONTEXT / GRAPH SETUP ---
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6.5,
            y_length=3.8,
            axis_config={{"color": MUTED_TEXT, "stroke_width": 2}}
        ).to_edge(DOWN, buff=1.2)
        
        self.play(Create(axes), run_time=1.5)

        # --- BEAT 3: CRITICAL CONCEPT & MOTION ARC ---
        formula = self.create_formula_mobject(formula_str, plain_formula, font_size=38, color_val=PALETTE["accent_2"]).to_edge(UP, buff=1.2)
        self.play(Write(formula), run_time=1.8)

        # Reference-inspired motion curve & particle
        curve = axes.plot(lambda x: 1.5 * np.sin(x), color=PALETTE["accent_3"])
        dot = Dot(color=PALETTE["accent_1"], radius=0.1).move_to(axes.c2p(-2.5, 1.5 * np.sin(-2.5)))
        
        self.play(Create(curve), run_time=1.5)
        self.play(MoveAlongPath(dot, curve), run_time=2.5, rate_func=linear)

        # --- BEAT 4: NEET TRAP CALLOUT ---
        trap_box = Rectangle(
            width=9.5, height=1.1,
            fill_color="#18181B", fill_opacity=0.92,
            stroke_color=PALETTE["accent_1"], stroke_width=2
        ).to_edge(DOWN, buff=0.8)
        warning_icon = Text("⚠️ NEET TRAP:", font_size=16, weight=BOLD, color=PALETTE["accent_1"]).next_to(trap_box.get_left(), RIGHT, buff=0.3)
        trap_msg = Text(trap_text[:65], font_size=15, color=TEXT_WHITE).next_to(warning_icon, RIGHT, buff=0.2)
        trap_group = VGroup(trap_box, warning_icon, trap_msg)

        self.play(FadeIn(trap_group, shift=UP * 0.2), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(trap_group), run_time=0.8)

        # --- BEAT 5: CAPSULE SUMMARY ---
        self.wait(1.5)

        # --- BEAT 6: RELEASE / UP NEXT TEASER ---
        self.render_release_teaser(duration=3.5)
'''
    return code

def analyze_reference(input_path: Path, template_name: str) -> Dict[str, Any]:
    print(f"🎬 Analyzing Reference: {input_path}")
    
    ref_dir = BASE_DIR / "media" / "references"
    frames_dir = ref_dir / "extracted_frames" / input_path.stem
    frames_dir.mkdir(parents=True, exist_ok=True)
    
    metadata = {}
    if input_path.is_file() and input_path.suffix.lower() in [".mp4", ".mov", ".mkv", ".webm"]:
        metadata = get_video_metadata(input_path)
        print(f"   ✓ Video Metadata: {metadata['width']}x{metadata['height']}, {metadata['duration']:.2f}s, {metadata['aspect_ratio']}")
        keyframe_paths = extract_keyframes(input_path, frames_dir, num_frames=6)
        print(f"   ✓ Extracted {len(keyframe_paths)} keyframes.")
    elif input_path.is_dir():
        keyframe_paths = list(input_path.glob("*.png")) + list(input_path.glob("*.jpg"))
        metadata = {"aspect_ratio": "16:9", "duration": 10.0}
    elif input_path.is_file() and input_path.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]:
        keyframe_paths = [input_path]
        metadata = {"aspect_ratio": "16:9", "duration": 10.0}
    else:
        raise ValueError(f"Unsupported input reference: {input_path}")
        
    print(f"🎨 Extracting Aesthetic Palette & Contrast Ratios...")
    theme = extract_palette_from_images(keyframe_paths)
    print(f"   ✓ Background: {theme['background']} ({'Dark' if theme['is_dark_theme'] else 'Light'})")
    print(f"   ✓ Primary Text: {theme['text_primary']}")
    print(f"   ✓ Primary Accent: {theme['accent_primary']}")
    print(f"   ✓ Secondary Accent: {theme['accent_secondary']}")
    
    # Generate Draft Template File
    draft_dir = BASE_DIR / "render" / "templates" / "drafts"
    draft_dir.mkdir(parents=True, exist_ok=True)
    snake_name = to_snake_case(template_name)
    draft_file = draft_dir / f"{snake_name}.py"
    
    draft_code = generate_manim_draft_code(template_name, theme, metadata)
    with open(draft_file, "w", encoding="utf-8") as f:
        f.write(draft_code)
    print(f"📝 Generated Draft Manim Template: {draft_file}")
    
    # Generate Vision LLM Prompt File for Deconstruction
    prompt_file = frames_dir / "vision_analysis_prompt.txt"
    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(f"""SYSTEM: You are an expert Mathematical Animation Engineer specializing in Manim (Community Edition) and NEET UG pedagogical video production.

TASK:
Analyze the attached {len(keyframe_paths)} sequential keyframes from a reference educational animation.
Your objective is to reverse-engineer the animation mechanics so our automated engine can replicate the motion dynamics and aesthetic.

FRAMES:
""" + "\n".join([f"- Frame {i+1}: {p.name}" for i, p in enumerate(keyframe_paths)]) + f"""

EXTRACTED PALETTE:
- Background: {theme['background']}
- Text: {theme['text_primary']}
- Accents: {theme['accent_primary']}, {theme['accent_secondary']}, {theme['accent_tertiary']}

REQUIREMENTS FOR MANIM REPLICATION:
1. Identify all graphical primitives (axes, graphs, vectors, particles, callouts).
2. Trace the exact motion path or transition between each successive frame.
3. Provide refined Manim animation code for construct_scene() using `self.play(...)` and `self.wait(...)`.
4. Guarantee compliance with the 6-beat NEET video lifecycle (Settle, Hook, Concept, Trap, Capsule, Release).
""")
    print(f"💡 Generated Multimodal LLM Vision Prompt: {prompt_file}")
    
    # Save Report
    report = {
        "template_name": template_name,
        "input_source": str(input_path),
        "metadata": metadata,
        "theme": theme,
        "keyframe_paths": [str(p) for p in keyframe_paths],
        "draft_template_path": str(draft_file),
        "vision_prompt_path": str(prompt_file)
    }
    
    report_file = ref_dir / f"{snake_name}_analysis.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"📊 Analysis Report saved to: {report_file}")
    
    return report

def main():
    parser = argparse.ArgumentParser(description="Reference Video & Aesthetic Analyzer for Manim Engine")
    parser.add_argument("--input", type=str, required=True, help="Path to reference video (.mp4) or image")
    parser.add_argument("--name", type=str, default="ReferenceInspired", help="Target Template Class Name (e.g. ModernOscillator)")
    args = parser.parse_args()
    
    analyze_reference(Path(args.input), args.name)

if __name__ == "__main__":
    main()
