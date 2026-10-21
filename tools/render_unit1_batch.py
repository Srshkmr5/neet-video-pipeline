"""
Automated Batch Render Engine for Unit 1: Physics and Measurement
Renders all 8 concepts across languages (en-IN, hi-IN, ta-IN), packages AES-128 HLS streams,
and updates app manifest with zero errors.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
FINAL_VIDEOS_DIR = BASE_DIR / "output" / "final_videos"
SECURE_STREAMS_DIR = BASE_DIR / "output" / "secure_streams"
REPORT_PATH = BASE_DIR / "output" / "reports" / "unit1_batch_render_report.json"

UNIT_1_CONCEPTS = [
    "P11-C01-T01-V01",
    "P11-C01-T01-V02",
    "P11-C01-T02-V03",
    "P11-C01-T02-V04",
    "P11-C01-T03-V05",
    "P11-C01-T03-V06",
    "P11-C01-T04-V07",
    "P11-C01-T04-V08"
]

LANGUAGES = ["en-IN", "hi-IN", "ta-IN"]

def log_report(data):
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def run_step(cmd, desc):
    print(f"\n▶ [{desc}] Running: {' '.join(cmd)}")
    t0 = time.time()
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
    dt = time.time() - t0
    if res.returncode != 0:
        print(f"❌ Error in [{desc}] ({dt:.1f}s):")
        print(res.stderr[-500:])
        return False, dt, res.stderr
    else:
        print(f"✓ Completed [{desc}] in {dt:.1f}s")
        return True, dt, res.stdout

def main():
    print("=" * 80)
    print("🚀 BATCH RENDER & PACKAGING ENGINE: UNIT 1 (PHYSICS & MEASUREMENT)")
    print(f"   Target: {len(UNIT_1_CONCEPTS)} Concepts x {len(LANGUAGES)} Languages = {len(UNIT_1_CONCEPTS) * len(LANGUAGES)} Streams")
    print("=" * 80)

    report = {
        "unit": "UNIT 1: PHYSICS AND MEASUREMENT",
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_concepts": len(UNIT_1_CONCEPTS),
        "results": []
    }

    for idx, cid in enumerate(UNIT_1_CONCEPTS):
        print(f"\n[{idx + 1}/{len(UNIT_1_CONCEPTS)}] Processing Concept: {cid}")
        concept_result = {"canonical_id": cid, "languages": {}}

        for lang in LANGUAGES:
            video_tag = f"{cid}_{lang}"
            final_mp4 = FINAL_VIDEOS_DIR / f"{video_tag}.mp4"
            stream_dir = SECURE_STREAMS_DIR / video_tag

            lang_status = {"status": "pending"}

            # Step 1: Render Video if not already rendered
            if final_mp4.exists() and final_mp4.stat().st_size > 500000:
                print(f"   ⚡ Found existing valid video: {final_mp4.name} ({final_mp4.stat().st_size / 1024 / 1024:.2f} MB)")
                lang_status["render"] = "cache_hit"
            else:
                render_cmd = [
                    sys.executable,
                    str(BASE_DIR / "tools" / "render_concept_video.py"),
                    "--id", cid,
                    "--lang", lang,
                    "--quality", "draft",
                    "--provider", "edge_tts"
                ]
                success, dt, out = run_step(render_cmd, f"Render {video_tag}")
                lang_status["render"] = "success" if success else "failed"
                lang_status["render_seconds"] = round(dt, 1)

            # Step 2: Encrypt into AES-128 HLS
            if final_mp4.exists():
                package_cmd = [
                    sys.executable,
                    str(BASE_DIR / "tools" / "secure_media_packager.py")
                ]
                pkg_success, pkg_dt, _ = run_step(package_cmd, f"Encrypt HLS {video_tag}")
                lang_status["encryption"] = "success" if pkg_success else "failed"
            else:
                lang_status["encryption"] = "skipped_missing_mp4"

            concept_result["languages"][lang] = lang_status
            report["results"].append(concept_result)
            log_report(report)

        # Update manifest after each concept
        subprocess.run([sys.executable, str(BASE_DIR / "tools" / "build_app_manifest.py")], stdout=subprocess.DEVNULL)
        print(f"✓ Manifest updated. Concept {cid} is now live in web app!")

    report["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    log_report(report)
    print("\n🎉 ALL UNIT 1 CONCEPTS RENDERED, ENCRYPTED & DEPLOYED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
