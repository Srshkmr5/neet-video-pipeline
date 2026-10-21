"""
Secure Streaming & Authentication Server for NEET EdApp
Implements AES-128 Key Exchange Gating, HMAC Session Authentication, and Anti-Scraping Defenses.
Derived from Master Blueprint Security Layer v2.0
"""

import os
import sys
import json
import time
import hmac
import hashlib
import secrets
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import urllib.parse

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent
KEYS_DIR = BASE_DIR / "server" / "security" / "keys"
SECURE_STREAMS_DIR = BASE_DIR / "output" / "secure_streams"

# Master Server Secret for Session HMACs (rotates on reboot or set via env)
SERVER_SECRET = os.environ.get("NEET_SERVER_SECRET", secrets.token_hex(32)).encode("utf-8")

# Blocked / Scraper User Agents
BLOCKED_USER_AGENTS = [
    "yt-dlp", "youtube-dl", "idm", "aria2", "curl", "wget", "python-requests", "httpie", "postman"
]

def generate_session_token(student_id: str, ttl_seconds: int = 14400) -> str:
    """Generates an HMAC-signed token expiring in ttl_seconds (default 4 hours)"""
    expires_at = int(time.time()) + ttl_seconds
    payload = f"{student_id}:{expires_at}"
    sig = hmac.new(SERVER_SECRET, payload.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"{payload}:{sig}"

def verify_session_token(token: str) -> bool:
    """Verifies that the session token has a valid HMAC signature and has not expired"""
    if not token:
        return False
    try:
        parts = token.split(":")
        if len(parts) != 3:
            return False
        student_id, expires_at_str, sig = parts
        expires_at = int(expires_at_str)
        if time.time() > expires_at:
            return False  # Expired
        
        expected_payload = f"{student_id}:{expires_at}"
        expected_sig = hmac.new(SERVER_SECRET, expected_payload.encode("utf-8"), hashlib.sha256).hexdigest()
        return hmac.compare_digest(sig, expected_sig)
    except Exception:
        return False


class SecureEdAppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format, *args):
        # Clean terminal logging for streaming chunks
        msg = format % args
        if "/api/stream/key/" in msg:
            print(f"🔑 [KEY EXCHANGE] {self.client_address[0]} - {msg}")
        elif "403" in msg or "401" in msg:
            print(f"⛔ [BLOCKED ACCESS] {self.client_address[0]} - {msg}")

    def get_token_from_request(self) -> str:
        # Check Authorization header
        auth_header = self.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            return auth_header[7:].strip()

        # Check URL query parameter (?token=...)
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        if "token" in query:
            return query["token"][0]

        # Check Cookie (session_token=...)
        cookie = self.headers.get("Cookie", "")
        for item in cookie.split(";"):
            if "session_token=" in item:
                return item.split("session_token=")[1].strip()

        return ""

    def send_json(self, status_code: int, data: dict):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
        self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/auth/login":
            length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(length) if length > 0 else b"{}"
            try:
                data = json.loads(post_data.decode("utf-8")) if post_data else {}
            except Exception:
                data = {}

            student_id = data.get("student_id", "").strip() or "NEET-2026-AIR1"
            student_name = data.get("student_name", "").strip() or "Dr. Aspirant"
            roll_no = data.get("roll_no", "").strip() or "NEET-TN-0941"

            token = generate_session_token(student_id)
            client_ip = self.client_address[0]

            self.send_json(200, {
                "status": "authenticated",
                "token": token,
                "student": {
                    "id": student_id,
                    "name": student_name,
                    "roll": roll_no,
                    "ip": client_ip,
                    "expires_in": 14400
                }
            })
            return

        self.send_error(404, "Endpoint not found")

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        user_agent = self.headers.get("User-Agent", "").lower()

        # Check Scraper / Downloader block
        is_downloader = any(ua in user_agent for ua in BLOCKED_USER_AGENTS)
        token = self.get_token_from_request()

        if is_downloader and not verify_session_token(token):
            self.send_error(403, "Direct tool download is prohibited.")
            return

        # 1. API: Key Exchange Endpoint for HLS AES-128
        if path.startswith("/api/stream/key/"):
            video_stem = path.replace("/api/stream/key/", "").strip()
            
            # Authenticate session
            if not verify_session_token(token):
                self.send_json(403, {"error": "Forbidden: Invalid or expired student playback token."})
                return

            key_file = KEYS_DIR / f"{video_stem}.key"
            if not key_file.exists():
                self.send_error(404, "Encryption key not found.")
                return

            with open(key_file, "rb") as kf:
                key_bytes = kf.read()

            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Length", str(len(key_bytes)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Headers", "Authorization")
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            self.send_header("Pragma", "no-cache")
            self.end_headers()
            self.wfile.write(key_bytes)
            return

        # 2. API: Serve HLS Master Playlist & TS Segments
        if path.startswith("/api/stream/"):
            rel_path = path.replace("/api/stream/", "").strip()
            stream_file = SECURE_STREAMS_DIR / rel_path

            if not stream_file.exists() or not stream_file.is_file():
                self.send_error(404, "Stream chunk not found.")
                return

            # Determine content type
            if stream_file.name.endswith(".m3u8"):
                content_type = "application/vnd.apple.mpegurl"
            elif stream_file.name.endswith(".ts"):
                content_type = "video/mp2t"
            else:
                content_type = "application/octet-stream"

            with open(stream_file, "rb") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(content)
            return

        # 3. Serve standard web app assets (HTML, JS, CSS, JSON, images)
        if path == "/" or path == "/index.html":
            self.path = "/apps/edapp_player.html"

        super().do_GET()


def run_server(port: int = 8080):
    server_address = ("", port)
    httpd = ThreadingHTTPServer(server_address, SecureEdAppHandler)
    print(f"\n=======================================================")
    print(f"🔒 NEET UG Secure EdApp Server Active on http://localhost:{port}")
    print(f"🛡️  AES-128 Key Exchange Gatekeeper: ACTIVE")
    print(f"🛡️  HMAC Token Authentication: ACTIVE")
    print(f"🛡️  Anti-Scraping / Direct Download Defense: ACTIVE")
    print(f"=======================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping secure server...")
        httpd.server_close()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
