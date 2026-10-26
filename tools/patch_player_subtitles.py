"""
Patches apps/edapp_player.html to support:
1. Native WebVTT Subtitles / Closed Captions (en-IN, hi-IN, ta-IN)
2. Interactive CC ON/OFF toggle button in the player bar
3. Styled video::cue captions
4. Buffer-stall resilient HLS.js configuration
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PLAYER_HTML = BASE_DIR / "apps" / "edapp_player.html"

def patch():
    with open(PLAYER_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add video::cue CSS
    cue_css = """    /* Subtitles & Closed Captions Styling */
    video::cue {
      background: rgba(15, 23, 42, 0.92) !important;
      color: #F8FAFC !important;
      font-family: ui-sans-serif, system-ui, -apple-system, sans-serif !important;
      font-size: 15px !important;
      line-height: 1.4 !important;
      font-weight: 600 !important;
      border-radius: 8px !important;
      padding: 5px 12px !important;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9) !important;
    }
"""
    if "/* Subtitles & Closed Captions Styling */" not in content:
        target_css = ".video-shield {"
        content = content.replace(target_css, f"{cue_css}\n    {target_css}", 1)

    # 2. Add CC Toggle Button next to Trilingual Switcher
    cc_button_html = """          <!-- Subtitles / Closed Captions Toggle -->
          <div class="flex items-center space-x-1 bg-slate-900 border border-slate-800 px-2 py-1 rounded-xl text-xs">
            <button id="subtitlesToggleBtn" onclick="toggleSubtitles()" class="px-2 py-0.5 rounded text-[11px] font-bold bg-sky-600 text-white flex items-center space-x-1 transition" title="Toggle Subtitles / Closed Captions">
              <i class="fa-solid fa-closed-captioning"></i>
              <span id="subtitlesBtnLabel">CC ON</span>
            </button>
          </div>
"""
    if "id=\"subtitlesToggleBtn\"" not in content:
        target_btn = "<!-- Dimension Switcher (2D vs 3D) -->"
        content = content.replace(target_btn, f"{cc_button_html}\n          {target_btn}", 1)

    # 3. Add JS Subtitle State and Functions
    subtitle_js = """    // Subtitles & Closed Captions Engine
    let subtitlesEnabled = true;

    function toggleSubtitles() {
      subtitlesEnabled = !subtitlesEnabled;
      const btn = document.getElementById('subtitlesToggleBtn');
      const label = document.getElementById('subtitlesBtnLabel');
      if (btn && label) {
        if (subtitlesEnabled) {
          btn.className = 'px-2 py-0.5 rounded text-[11px] font-bold bg-sky-600 text-white flex items-center space-x-1 transition';
          label.innerText = 'CC ON';
        } else {
          btn.className = 'px-2 py-0.5 rounded text-[11px] font-bold bg-slate-800 text-slate-400 hover:text-white flex items-center space-x-1 transition';
          label.innerText = 'CC OFF';
        }
      }
      updateSubtitleTracks();
    }

    function updateSubtitleTracks() {
      const video = document.getElementById('mainVideoPlayer');
      if (!video) return;

      // Remove existing tracks
      const existing = video.querySelectorAll('track');
      existing.forEach(t => video.removeChild(t));

      if (!subtitlesEnabled || !currentConcept) return;

      const vttLang = currentLang === 'en' ? 'en-IN' : (currentLang === 'hi' ? 'hi-IN' : 'ta-IN');
      const vttPath = `/output/beat_audio/${currentConcept.canonical_id}_${vttLang}/${currentConcept.canonical_id}_${vttLang}.vtt`;

      const track = document.createElement('track');
      track.kind = 'subtitles';
      track.label = currentLang === 'en' ? 'English' : (currentLang === 'hi' ? 'Hindi' : 'Tamil');
      track.srclang = currentLang;
      track.src = vttPath;
      track.default = true;
      video.appendChild(track);

      // Force showing mode
      const setMode = () => {
        if (video.textTracks && video.textTracks.length > 0) {
          for (let i = 0; i < video.textTracks.length; i++) {
            video.textTracks[i].mode = subtitlesEnabled ? 'showing' : 'hidden';
          }
        }
      };
      track.addEventListener('load', setMode);
      setTimeout(setMode, 100);
    }
"""
    if "function toggleSubtitles()" not in content:
        target_js = "// 7. Secure HLS Playback Engine"
        content = content.replace(target_js, f"{subtitle_js}\n    {target_js}", 1)

    # 4. Enhance Hls configuration & call updateSubtitleTracks
    old_hls = """        hlsInstance = new Hls({
          xhrSetup: function(xhr, url) {"""

    new_hls = """        hlsInstance = new Hls({
          maxBufferHole: 0.5,
          nudgeOffset: 0.2,
          nudgeMaxRetry: 10,
          xhrSetup: function(xhr, url) {"""

    if "maxBufferHole: 0.5" not in content and old_hls in content:
        content = content.replace(old_hls, new_hls, 1)

    # 5. Call updateSubtitleTracks inside loadSecureStream and setLanguage
    if "updateSubtitleTracks();" not in content:
        target_call = "hlsInstance.attachMedia(video);"
        content = content.replace(target_call, f"{target_call}\n        updateSubtitleTracks();", 1)

    with open(PLAYER_HTML, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Successfully patched edapp_player.html with subtitle engine and CC toggle!")

if __name__ == "__main__":
    patch()
