"""
Master Launcher for NEET UG Secure Triad EdApp
Validates secure packages, compiles curriculum manifest, starts the authenticated streaming server,
and launches the application in the default browser.
Derived from Master Blueprint Security Layer v2.0
"""

import os
import sys
import webbrowser
import threading
import time
from pathlib import Path

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent
TOOLS_DIR = BASE_DIR / "tools"
SERVER_DIR = BASE_DIR / "server"

def banner():
    print("=" * 68)
    print("       🚀 NEET UG MASTERCLASS — SECURE TRIAD EDAPP v2.0       ")
    print("=" * 68)
    print("  🛡️  Security Profile: 5-Layer Anti-Piracy Architecture")
    print("  🔒 Video Encryption: AES-128 HLS Segmented Streams")
    print("  🔑 Key Exchange   : Server-Gated HMAC-SHA256 Token Auth")
    print("  👁️  Forensic Leak  : Dynamic Floating Watermark Engine")
    print("  🚫 Anti-Scraping  : Direct Download Tools (IDM/yt-dlp) Blocked")
    print("=" * 68)

def main():
    banner()

    # Step 1: Secure Media Packaging Check
    print("\n[1/4] 🔒 Verifying AES-128 HLS Encryption on Rendered Videos...")
    from tools.secure_media_packager import package_all_videos
    pkg_stats = package_all_videos(force=False)
    print(f"      Status: {pkg_stats['total']} total videos verified ({pkg_stats['encrypted']} newly packaged, {pkg_stats['skipped']} already encrypted).")

    # Step 2: Curriculum Manifest Compilation
    print("\n[2/4] 📑 Verifying Dynamic Curriculum Manifest...")
    from tools.build_app_manifest import build_manifest
    manifest = build_manifest()
    print(f"      Status: {manifest['total_concepts']} concepts loaded, {manifest['active_stream_concepts']} active stream nodes available.")

    # Step 3: Start Secure Streaming & Auth Server
    port = 8080
    print(f"\n[3/4] 🛡️  Launching Secure Server on http://localhost:{port} ...")
    from server.secure_server import run_server

    server_thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()

    time.sleep(1.0)

    # Step 4: Open Browser
    app_url = f"http://localhost:{port}/apps/edapp_player.html"
    print(f"\n[4/4] 🌐 Opening EdApp Player in browser: {app_url}\n")
    print("Press Ctrl+C in this terminal at any time to shut down the server.\n")
    
    try:
        webbrowser.open(app_url)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nShutting down NEET EdApp Secure Server. Goodbye!")

if __name__ == "__main__":
    main()
