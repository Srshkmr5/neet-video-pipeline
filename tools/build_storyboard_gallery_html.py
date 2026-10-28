"""
Builds an interactive high-fidelity Storyboard Proof Review Gallery for Unit 3 (Laws of Motion).
Allows instant inspection of all 55 proof frames across all 11 concepts and 5 beats.
"""

from pathlib import Path
import json
import csv

import sys
BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
sys.path.insert(0, str(BASE_DIR))
OUT_HTML = BASE_DIR / "output" / "unit_03_storyboard_gallery.html"

from tools.render_multilingual_unit3 import ARCHETYPE_SCENE_MAP, load_concept_row

CONCEPTS = [
    ("P11-C03-T01-V01", "1. First Law, Inertia & Free-Body Diagrams"),
    ("P11-C03-T01-V02", "2. Second Law, Elevators & Pseudo Forces"),
    ("P11-C03-T01-V03", "3. Third Law, Action-Reaction & Atwood Machine"),
    ("P11-C03-T02-V04", "4. Linear Momentum, Impulse & F-t Curve"),
    ("P11-C03-T02-V05", "5. Momentum Conservation & Rocket Thrust"),
    ("P11-C03-T02-V06", "6. Concurrent Equilibrium & Lami's Theorem"),
    ("P11-C03-T03-V07", "7. Static vs Kinetic Friction & Graphs"),
    ("P11-C03-T03-V08", "8. Rough Incline, Angle of Repose & Deceleration"),
    ("P11-C03-T03-V09", "9. Two-Block Friction & Relative Slip Threshold"),
    ("P11-C03-T04-V10", "10. Centripetal Force & Level Curved Road Dynamics"),
    ("P11-C03-T04-V11", "11. Engineered Banking of Roads & Vertical Circles")
]

BEATS = [
    ("beat_1_intro.png", "Beat 1: NCERT Evergreen Intro Card"),
    ("beat_2_hero.png", "Beat 2: Hero Stage & Core Law"),
    ("beat_3_scenarios.png", "Beat 3: Analytical Deep-Dive & Derivation"),
    ("beat_4_trap.png", "Beat 4: NEET Trap Card (Zero PYQ Years)"),
    ("beat_5_teaser.png", "Beat 5: Next Video End Card")
]

FIX_NOTES = {
    "P11-C03-T01-V01": "Beat 2 shows First Law & Equilibrium; Beat 3 shows FBD pull angle derivation. Zero overflows.",
    "P11-C03-T01-V02": "Beat 2 shows Apparent Weight; Beat 3 shows Pseudo Force & Free Fall weightlessness. Aligned to voiceover.",
    "P11-C03-T01-V03": "Beat 2 shows Third Law action-reaction duality; Beat 3 shows Atwood Machine equations. PYQ purged.",
    "P11-C03-T02-V04": "Beat 2 shows Impulse-Momentum Theorem & F-t area; Beat 3 shows Rebound vector impulse. Axes lifted.",
    "P11-C03-T02-V05": "Beat 2 shows Rifle Recoil; Beat 3 shows Rocket Thrust & Tsiolkovsky equation. Thrust arrow clamped inside card.",
    "P11-C03-T02-V06": "Formula box widened to 5.8 to fit Lami equation. Beat 3 shows symmetric string tension and theta -> 90° limit.",
    "P11-C03-T03-V07": "Graph axes lifted 0.35 units off card floor. Static, limiting peak, and kinetic plateau clearly separated.",
    "P11-C03-T03-V08": "Text wrapped inside 5.6 card width. Beat 2 shows Angle of Repose; Beat 3 shows Asymmetric times.",
    "P11-C03-T03-V09": "Top block pull arrow lowered. Formula box widened. Slipping thresholds for bottom vs top pull separated.",
    "P11-C03-T04-V10": "Bullet points line-wrapped. Mass independence v_max = sqrt(mu_s r g) clearly highlighted.",
    "P11-C03-T04-V11": "Multi-line banking equations formatted cleanly. Beat 3 clearly contrasts String vs Rigid Rod loop thresholds."
}

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unit 3 Storyboard Proof Review Gallery • NEET UG Physics</title>
<style>
  :root {{
    --bg-dark: #090D16;
    --card-bg: #111827;
    --card-border: #1E293B;
    --accent-blue: #38BDF8;
    --accent-gold: #FBBF24;
    --accent-green: #34D399;
    --accent-red: #F87171;
    --text-main: #F3F4F6;
    --text-muted: #94A3B8;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg-dark);
    color: var(--text-main);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    display: flex;
    height: 100vh;
    overflow: hidden;
  }}
  #sidebar {{
    width: 380px;
    background: #0B1120;
    border-right: 1px solid var(--card-border);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
  }}
  .header-box {{
    padding: 20px;
    border-bottom: 1px solid var(--card-border);
    background: #0D1527;
  }}
  .badge {{
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}
  .badge-proof {{ background: #064E3B; color: var(--accent-green); border: 1px solid var(--accent-green); }}
  .header-box h1 {{
    font-size: 17px;
    margin-top: 8px;
    color: var(--text-main);
    font-weight: 700;
  }}
  .header-box p {{
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 4px;
  }}
  .concept-list {{
    flex: 1;
    overflow-y: auto;
    padding: 10px;
  }}
  .concept-item {{
    padding: 12px 14px;
    border-radius: 8px;
    margin-bottom: 6px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.15s ease;
  }}
  .concept-item:hover {{
    background: #1E293B;
  }}
  .concept-item.active {{
    background: #1E293B;
    border-color: var(--accent-blue);
  }}
  .concept-item .cid {{
    font-size: 11px;
    color: var(--accent-gold);
    font-weight: 600;
    font-family: monospace;
  }}
  .concept-item .title {{
    font-size: 13px;
    font-weight: 600;
    color: var(--text-main);
    margin-top: 2px;
  }}
  #main {{
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }}
  .top-bar {{
    padding: 14px 24px;
    background: #0B1120;
    border-bottom: 1px solid var(--card-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .top-bar .info h2 {{
    font-size: 18px;
    color: var(--accent-blue);
  }}
  .top-bar .info p {{
    font-size: 13px;
    color: var(--text-muted);
    margin-top: 3px;
  }}
  .beat-tabs {{
    display: flex;
    gap: 8px;
    padding: 12px 24px;
    background: #0D1527;
    border-bottom: 1px solid var(--card-border);
  }}
  .beat-tab {{
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    background: #1E293B;
    color: var(--text-muted);
    border: 1px solid transparent;
    transition: all 0.15s ease;
  }}
  .beat-tab:hover {{
    color: var(--text-main);
  }}
  .beat-tab.active {{
    background: #0369A1;
    color: #FFF;
    border-color: var(--accent-blue);
  }}
  .viewer-container {{
    flex: 1;
    padding: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow-y: auto;
    background: #060911;
  }}
  .frame-card {{
    background: #000;
    border: 1px solid var(--card-border);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    max-width: 1200px;
    width: 100%;
    display: flex;
    flex-direction: column;
  }}
  .frame-card img {{
    width: 100%;
    height: auto;
    display: block;
    aspect-ratio: 16/9;
    background: #000;
  }}
  .frame-footer {{
    padding: 12px 20px;
    background: #0F172A;
    border-top: 1px solid var(--card-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .frame-footer .fix-text {{
    font-size: 12.5px;
    color: var(--accent-green);
    font-weight: 500;
  }}
  .nav-controls {{
    display: flex;
    gap: 10px;
  }}
  .nav-btn {{
    padding: 6px 14px;
    border-radius: 6px;
    background: #1E293B;
    border: 1px solid #334155;
    color: var(--text-main);
    font-size: 12px;
    cursor: pointer;
    font-weight: 600;
  }}
  .nav-btn:hover {{
    background: #334155;
  }}
</style>
</head>
<body>

<div id="sidebar">
  <div class="header-box">
    <span class="badge badge-proof">Visual Confirmation Protocol</span>
    <h1>Unit 3 Storyboard Gallery</h1>
    <p>11 Concepts • 55 1080p Still Proof Frames</p>
  </div>
  <div class="concept-list" id="conceptList"></div>
</div>

<div id="main">
  <div class="top-bar">
    <div class="info">
      <h2 id="conceptHeading">Select a Concept</h2>
      <p id="conceptSub">Canonical ID & NCERT Citation</p>
    </div>
    <div class="nav-controls">
      <button class="nav-btn" onclick="prevBeat()">◀ Prev Beat [←]</button>
      <button class="nav-btn" onclick="nextBeat()">Next Beat [→] ▶</button>
    </div>
  </div>

  <div class="beat-tabs" id="beatTabs"></div>

  <div class="viewer-container">
    <div class="frame-card">
      <img id="proofImage" src="" alt="Proof Frame">
      <div class="frame-footer">
        <span class="fix-text" id="fixText">Audited & Verified against Visual Confirmation Rules</span>
        <span style="font-size:12px; color:var(--text-muted);" id="beatIndicator">Beat 1 of 5</span>
      </div>
    </div>
  </div>
</div>

<script>
const CONCEPTS = {json.dumps(CONCEPTS)};
const BEATS = {json.dumps(BEATS)};
const FIX_NOTES = {json.dumps(FIX_NOTES)};

let currentConceptIdx = 0;
let currentBeatIdx = 0;

function init() {{
  const listEl = document.getElementById("conceptList");
  CONCEPTS.forEach((c, idx) => {{
    const item = document.createElement("div");
    item.className = "concept-item" + (idx === 0 ? " active" : "");
    item.innerHTML = `<div class="cid">${{c[0]}}</div><div class="title">${{c[1]}}</div>`;
    item.onclick = () => selectConcept(idx);
    listEl.appendChild(item);
  }});

  const tabsEl = document.getElementById("beatTabs");
  BEATS.forEach((b, idx) => {{
    const tab = document.createElement("div");
    tab.className = "beat-tab" + (idx === 0 ? " active" : "");
    tab.textContent = b[1];
    tab.onclick = () => selectBeat(idx);
    tabsEl.appendChild(tab);
  }});

  updateView();

  window.addEventListener("keydown", (e) => {{
    if (e.key === "ArrowLeft") prevBeat();
    if (e.key === "ArrowRight") nextBeat();
    if (e.key === "ArrowUp") selectConcept(Math.max(0, currentConceptIdx - 1));
    if (e.key === "ArrowDown") selectConcept(Math.min(CONCEPTS.length - 1, currentConceptIdx + 1));
  }});
}}

function selectConcept(idx) {{
  currentConceptIdx = idx;
  document.querySelectorAll(".concept-item").forEach((el, i) => {{
    el.classList.toggle("active", i === idx);
  }});
  updateView();
}}

function selectBeat(idx) {{
  currentBeatIdx = idx;
  document.querySelectorAll(".beat-tab").forEach((el, i) => {{
    el.classList.toggle("active", i === idx);
  }});
  updateView();
}}

function prevBeat() {{
  if (currentBeatIdx > 0) selectBeat(currentBeatIdx - 1);
  else if (currentConceptIdx > 0) {{
    selectConcept(currentConceptIdx - 1);
    selectBeat(4);
  }}
}}

function nextBeat() {{
  if (currentBeatIdx < 4) selectBeat(currentBeatIdx + 1);
  else if (currentConceptIdx < CONCEPTS.length - 1) {{
    selectConcept(currentConceptIdx + 1);
    selectBeat(0);
  }}
}}

function updateView() {{
  const cid = CONCEPTS[currentConceptIdx][0];
  const title = CONCEPTS[currentConceptIdx][1];
  const beatFile = BEATS[currentBeatIdx][0];
  const beatName = BEATS[currentBeatIdx][1];

  document.getElementById("conceptHeading").textContent = title;
  document.getElementById("conceptSub").textContent = `${{cid}} • ${{beatName}}`;
  document.getElementById("fixText").textContent = "✓ Fix: " + (FIX_NOTES[cid] || "Zero overflows, evergreen citation, and synchronized narration.");
  document.getElementById("beatIndicator").textContent = `Beat ${{currentBeatIdx + 1}} of 5`;

  const imgPath = `storyboards_unit3/${{cid}}/${{beatFile}}`;
  document.getElementById("proofImage").src = imgPath;
}}

window.onload = init;
</script>
</body>
</html>
'''

OUT_HTML.write_text(html, encoding="utf-8")
print(f"Generated {OUT_HTML} ({len(html)} bytes)")
