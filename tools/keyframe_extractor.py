"""
Keyframe Extractor Tool
Extracts metadata and evenly-spaced keyframes from reference videos for visual deconstruction.
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

def get_video_metadata(video_path: Path) -> Dict[str, Any]:
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,duration,r_frame_rate,nb_frames:format=duration",
        "-of", "json",
        str(video_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(result.stdout)
    
    stream = data.get("streams", [{}])[0]
    fmt = data.get("format", {})
    
    width = int(stream.get("width", 1920))
    height = int(stream.get("height", 1080))
    
    # Duration could be in stream or format
    duration_str = stream.get("duration") or fmt.get("duration") or "10.0"
    duration = float(duration_str)
    
    # Calculate aspect ratio string
    aspect_ratio = "16:9"
    if height > width:
        aspect_ratio = "9:16 (Shorts/Reels)"
    elif width == height:
        aspect_ratio = "1:1 (Square)"
    elif abs(width / height - (16 / 9)) < 0.05:
        aspect_ratio = "16:9 (Landscape)"
        
    return {
        "width": width,
        "height": height,
        "duration": duration,
        "aspect_ratio": aspect_ratio,
        "video_path": str(video_path)
    }

def extract_keyframes(video_path: Path, output_dir: Path, num_frames: int = 6) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    meta = get_video_metadata(video_path)
    duration = meta["duration"]
    
    # Calculate timestamps (spaced within the video, avoiding 0.0 or the very last frame)
    step = duration / (num_frames + 1)
    timestamps = [step * (i + 1) for i in range(num_frames)]
    
    extracted_paths = []
    for idx, t in enumerate(timestamps, start=1):
        out_frame = output_dir / f"frame_{idx:02d}_{t:.2f}s.png"
        cmd = [
            "ffmpeg",
            "-y",
            "-ss", f"{t:.3f}",
            "-i", str(video_path),
            "-vframes", "1",
            "-q:v", "2",
            str(out_frame)
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        if out_frame.exists():
            extracted_paths.append(out_frame)
            
    return extracted_paths

if __name__ == "__main__":
    if len(sys.argv) > 1:
        v_path = Path(sys.argv[1])
        out_d = v_path.parent / "extracted_frames" / v_path.stem
        frames = extract_keyframes(v_path, out_d)
        print(f"Extracted {len(frames)} frames to {out_d}")
    else:
        print("Usage: python tools/keyframe_extractor.py <path_to_video>")
