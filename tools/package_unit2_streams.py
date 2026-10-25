import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from tools.secure_media_packager import package_all_videos

if __name__ == "__main__":
    u2_dir = BASE_DIR / "output" / "unit_02_kinematics"
    print(f"Packaging videos from {u2_dir}...")
    res = package_all_videos(force=True, input_dirs=[u2_dir])
    print("Result:", res)
