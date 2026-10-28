"""
build_unit3_sim_hub_v3.py
Compiles ultra-high fidelity interactive simulation lab for Unit 3 (Laws of Motion - P11-C03).
Covers all 11 concepts across 4 major modules:
1. Newton's Laws & FBD (Concepts 1, 2, 3)
2. Friction & Incline Mechanics (Concepts 7, 8, 9)
3. Momentum & Impulse (Concepts 4, 5, 6)
4. Circular Dynamics & Banked Roads (Concepts 10, 11)

Guarantees 100% live visual parameter coupling (Rule 21): zero decorative/static sliders.
Every slider scales geometry, alters motion physics, or shifts dynamic thresholds visibly.
"""

from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
target_html = BASE_DIR / "simulations" / "unit_03_laws_of_motion_lab.html"

def generate_html():
    return r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NEET Physics • Unit 03: Laws of Motion Interactive Hub</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    body {
      background-color: #020408;
      color: #f8fafc;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      margin: 0;
      overflow: hidden;
    }
    .glass-panel {
      background: rgba(10, 15, 29, 0.88);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(56, 189, 248, 0.2);
    }
    .glass-card {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(148, 163, 184, 0.15);
    }
    .active-tab {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.25) 0%, rgba(37, 99, 235, 0.3) 100%);
      border-color: #38bdf8 !important;
      color: #38bdf8 !important;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
    }
    .sub-preset-btn.active {
      background: rgba(56, 189, 248, 0.2);
      border-color: #38bdf8;
      color: #38bdf8;
      font-weight: 700;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
    }
    .sub-preset-btn {
      background: rgba(30, 41, 59, 0.6);
      border-color: rgba(148, 163, 184, 0.2);
      color: #94a3b8;
    }
    input[type=range] {
      accent-color: #38bdf8;
    }
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(15, 23, 42, 0.6);
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }
  </style>
</head>
<body class="h-screen flex flex-col select-none">

  <!-- ======================================================== -->
  <!-- TOP HEADER & MODULE TABS                                 -->
  <!-- ======================================================== -->
  <header class="glass-panel border-b px-5 py-2.5 flex items-center justify-between z-20 shrink-0">
    <div class="flex items-center space-x-3">
      <div class="w-8 h-8 rounded-lg bg-sky-500/20 border border-sky-400/40 flex items-center justify-center text-sky-400">
        <i class="fa-solid fa-atom text-base"></i>
      </div>
      <div>
        <h1 class="text-sm font-bold tracking-wide uppercase text-slate-100 flex items-center space-x-2">
          <span>NEET Physics Lab</span>
          <span class="text-slate-500">•</span>
          <span class="text-sky-400 font-mono">Unit 03: Laws of Motion</span>
          <span class="text-xs px-2 py-0.5 rounded bg-sky-950 border border-sky-800 text-sky-300 font-mono">P11-C03</span>
        </h1>
        <p class="text-[11px] text-slate-400">Real-Time Interactive Physics Simulation Hub • Dynamic Parameter Coupling</p>
      </div>
    </div>

    <!-- 4 Main Module Tabs -->
    <nav class="flex items-center space-x-1.5 p-1 rounded-xl bg-slate-900/80 border border-slate-800 text-xs">
      <button id="tabNewton" onclick="switchMode('newton')" class="active-tab px-3.5 py-1.5 rounded-lg border border-transparent font-medium transition flex items-center space-x-1.5">
        <i class="fa-solid fa-compass-drafting text-[11px]"></i>
        <span>1. Newton &amp; FBD</span>
      </button>
      <button id="tabFriction" onclick="switchMode('friction')" class="px-3.5 py-1.5 rounded-lg border border-transparent text-slate-400 font-medium hover:text-slate-200 transition flex items-center space-x-1.5">
        <i class="fa-solid fa-chart-line text-[11px]"></i>
        <span>2. Friction &amp; Incline</span>
      </button>
      <button id="tabMomentum" onclick="switchMode('momentum')" class="px-3.5 py-1.5 rounded-lg border border-transparent text-slate-400 font-medium hover:text-slate-200 transition flex items-center space-x-1.5">
        <i class="fa-solid fa-shuttle-space text-[11px]"></i>
        <span>3. Momentum &amp; Impulse</span>
      </button>
      <button id="tabCircular" onclick="switchMode('circular')" class="px-3.5 py-1.5 rounded-lg border border-transparent text-slate-400 font-medium hover:text-slate-200 transition flex items-center space-x-1.5">
        <i class="fa-solid fa-circle-notch text-[11px]"></i>
        <span>4. Circular &amp; Banking</span>
      </button>
    </nav>

    <!-- Global Controls -->
    <div class="flex items-center space-x-2">
      <span class="text-[11px] text-emerald-400 font-mono flex items-center space-x-1">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span>60 FPS Active</span>
      </span>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- MAIN WORKSPACE CONTAINER                                 -->
  <!-- ======================================================== -->
  <main class="flex-1 flex overflow-hidden relative">

    <!-- ======================================================== -->
    <!-- ENGINE 1: NEWTON LAWS, FBD & ELEVATOR (CONCEPTS 1-3)     -->
    <!-- ======================================================== -->
    <section id="engineNewton" class="flex-1 flex overflow-hidden">
      <!-- Left Visual Canvas Area -->
      <div class="flex-1 flex flex-col p-4">
        <!-- Sub-Preset Concept Toolbar -->
        <div class="flex items-center justify-between mb-3 shrink-0">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
            <button id="subNewtonFbdBtn" onclick="setNewtonConcept('fbd')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
              Concept 1: Free-Body Diagram &amp; Vector Resolver
            </button>
            <button id="subNewtonElevatorBtn" onclick="setNewtonConcept('elevator')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 2: Elevator &amp; Apparent Weight
            </button>
            <button id="subNewtonTensionBtn" onclick="setNewtonConcept('tension')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 3: Atwood Machine &amp; Tension
            </button>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="triggerNewtonAction()" id="newtonActionBtn" class="px-2.5 py-1 rounded bg-sky-500/20 hover:bg-sky-500/30 border border-sky-400/40 text-sky-300 text-xs font-medium transition flex items-center space-x-1">
              <i class="fa-solid fa-arrows-rotate"></i>
              <span id="newtonActionLabel">Reset Motion</span>
            </button>
          </div>
        </div>

        <!-- Canvas Container -->
        <div id="newtonCanvasContainer" class="flex-1 rounded-xl border border-slate-800 bg-[#070b14] relative overflow-hidden flex items-center justify-center shadow-inner">
          <canvas id="newtonCanvas" class="w-full h-full block"></canvas>
          <div id="newtonLiveBadge" class="absolute top-3 left-4 text-xs font-mono text-sky-400 bg-slate-900/80 px-2.5 py-1 rounded-md border border-sky-500/30">
            FBD Vector Resolver Active
          </div>
        </div>
      </div>

      <!-- Right Control & Metrics Sidebar -->
      <aside class="w-96 glass-panel border-l p-4 flex flex-col overflow-y-auto space-y-4 shrink-0">
        <div>
          <div id="newtonHeader" class="text-xs font-mono text-sky-400 uppercase tracking-wider">CONCEPT 1 • FREE-BODY DIAGRAM</div>
          <h2 id="newtonTitle" class="text-base font-bold text-slate-100 mt-0.5">FBD Orthogonal Vector Resolver</h2>
          <p id="newtonFormula" class="text-xs font-mono text-slate-400 mt-1 bg-slate-900/80 p-2 rounded border border-slate-800">
            ΣF_x = m·a_x • ΣF_y = 0 • N = mg - F·sinθ
          </p>
        </div>

        <!-- Interactive Sliders -->
        <div class="space-y-3.5 glass-card p-3.5 rounded-xl">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center justify-between">
            <span>Physical Parameters</span>
            <span class="text-[10px] text-sky-400 font-mono">LIVE SLIDERS</span>
          </div>

          <!-- Parameter 1 -->
          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="newtonParam1Label" class="text-slate-300 font-medium">Body Mass (m):</span>
              <span id="newtonParam1Val" class="text-sky-400 font-mono font-bold">5.0 kg</span>
            </div>
            <input type="range" id="newtonSlider1" min="1" max="25" step="0.5" value="5" oninput="updateNewton()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <!-- Parameter 2 -->
          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="newtonParam2Label" class="text-slate-300 font-medium">Pulling Force (F):</span>
              <span id="newtonParam2Val" class="text-sky-400 font-mono font-bold">40 N</span>
            </div>
            <input type="range" id="newtonSlider2" min="0" max="120" step="1" value="40" oninput="updateNewton()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <!-- Parameter 3 -->
          <div id="newtonBlock3">
            <div class="flex justify-between text-xs mb-1">
              <span id="newtonParam3Label" class="text-slate-300 font-medium">Pull Angle (θ):</span>
              <span id="newtonParam3Val" class="text-sky-400 font-mono font-bold">30°</span>
            </div>
            <input type="range" id="newtonSlider3" min="0" max="80" step="1" value="30" oninput="updateNewton()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>
        </div>

        <!-- Live Metrics & Status -->
        <div class="space-y-2.5">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Dynamic Physics Readout</div>
          
          <div class="grid grid-cols-2 gap-2 text-xs font-mono">
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="newtonMet1Label" class="text-[11px] text-slate-400">Normal Force (N):</div>
              <div id="newtonMet1Val" class="text-sm font-bold text-emerald-400 mt-0.5">29.0 N</div>
            </div>
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="newtonMet2Label" class="text-[11px] text-slate-400">Horizontal Pull F_x:</div>
              <div id="newtonMet2Val" class="text-sm font-bold text-sky-400 mt-0.5">34.6 N</div>
            </div>
          </div>

          <div class="glass-card p-2.5 rounded-lg border border-slate-800 text-xs font-mono">
            <div id="newtonMet3Label" class="text-[11px] text-slate-400">Net Acceleration (a):</div>
            <div id="newtonMet3Val" class="text-sm font-bold text-amber-400 mt-0.5">6.93 m/s²</div>
          </div>

          <div id="newtonStatusCard" class="glass-card p-3 rounded-lg border border-sky-500/30 bg-sky-950/20 text-xs font-mono">
            <div class="text-[10px] text-slate-400 uppercase tracking-wider">Physical State / Regime</div>
            <div id="newtonStateVal" class="text-xs font-bold text-sky-300 mt-1 flex items-center space-x-1.5">
              <span>ACCELERATING HORIZONTALLY ON FLOOR</span>
            </div>
          </div>
        </div>
      </aside>
    </section>

    <!-- ======================================================== -->
    <!-- ENGINE 2: FRICTION, INCLINE & TWO-BLOCK (CONCEPTS 7-9)   -->
    <!-- ======================================================== -->
    <section id="engineFriction" class="flex-1 flex overflow-hidden hidden">
      <!-- Left Visual Canvas Area -->
      <div class="flex-1 flex flex-col p-4">
        <!-- Sub-Preset Toolbar -->
        <div class="flex items-center justify-between mb-3 shrink-0">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
            <button id="subFrictionGraphBtn" onclick="setFrictionConcept('graph')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
              Concept 7: Static vs Kinetic Friction Graph
            </button>
            <button id="subFrictionInclineBtn" onclick="setFrictionConcept('incline')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 8: Angle of Repose &amp; Incline
            </button>
            <button id="subFrictionTwoBlockBtn" onclick="setFrictionConcept('twoblock')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 9: Two-Block Relative Slip Threshold
            </button>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="triggerFrictionAction()" id="fricActionBtn" class="px-2.5 py-1 rounded bg-sky-500/20 hover:bg-sky-500/30 border border-sky-400/40 text-sky-300 text-xs font-medium transition flex items-center space-x-1">
              <i class="fa-solid fa-play"></i>
              <span id="fricActionLabel">Release / Test Slip</span>
            </button>
          </div>
        </div>

        <!-- Canvas Container -->
        <div id="frictionCanvasContainer" class="flex-1 rounded-xl border border-slate-800 bg-[#070b14] relative overflow-hidden flex items-center justify-center shadow-inner">
          <canvas id="frictionCanvas" class="w-full h-full block"></canvas>
          <div id="fricLiveBadge" class="absolute top-3 left-4 text-xs font-mono text-sky-400 bg-slate-900/80 px-2.5 py-1 rounded-md border border-sky-500/30">
            Friction Dynamics Active
          </div>
        </div>
      </div>

      <!-- Right Sidebar -->
      <aside class="w-96 glass-panel border-l p-4 flex flex-col overflow-y-auto space-y-4 shrink-0">
        <div>
          <div id="frictionHeader" class="text-xs font-mono text-sky-400 uppercase tracking-wider">CONCEPT 7 • FRICTION MECHANICS</div>
          <h2 id="frictionTitle" class="text-base font-bold text-slate-100 mt-0.5">Self-Adjusting Static vs Kinetic Graph</h2>
          <p id="frictionFormula" class="text-xs font-mono text-slate-400 mt-1 bg-slate-900/80 p-2 rounded border border-slate-800">
            f_s ≤ μ_s·N • f_k = μ_k·N (μ_k &lt; μ_s)
          </p>
        </div>

        <!-- Sliders -->
        <div class="space-y-3.5 glass-card p-3.5 rounded-xl">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center justify-between">
            <span>Physical Parameters</span>
            <span class="text-[10px] text-sky-400 font-mono">LIVE SLIDERS</span>
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="fricParam1Label" class="text-slate-300 font-medium">Static Coeff (μ_s):</span>
              <span id="fricParam1Val" class="text-sky-400 font-mono font-bold">0.60</span>
            </div>
            <input type="range" id="fricSlider1" min="0.10" max="0.90" step="0.05" value="0.60" oninput="updateFriction()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="fricParam2Label" class="text-slate-300 font-medium">Kinetic Coeff (μ_k):</span>
              <span id="fricParam2Val" class="text-sky-400 font-mono font-bold">0.40</span>
            </div>
            <input type="range" id="fricSlider2" min="0.05" max="0.85" step="0.05" value="0.40" oninput="updateFriction()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div id="fricBlock3">
            <div class="flex justify-between text-xs mb-1">
              <span id="fricParam3Label" class="text-slate-300 font-medium">Applied Pull (F_app):</span>
              <span id="fricParam3Val" class="text-sky-400 font-mono font-bold">20 N</span>
            </div>
            <input type="range" id="fricSlider3" min="0" max="120" step="1" value="20" oninput="updateFriction()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div id="fricBlock4">
            <div class="flex justify-between text-xs mb-1">
              <span id="fricParam4Label" class="text-slate-300 font-medium">Block Mass (m):</span>
              <span id="fricParam4Val" class="text-sky-400 font-mono font-bold">5.0 kg</span>
            </div>
            <input type="range" id="fricSlider4" min="1" max="20" step="0.5" value="5" oninput="updateFriction()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>
        </div>

        <!-- Metrics -->
        <div class="space-y-2.5">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Dynamic Friction Metrics</div>

          <div class="grid grid-cols-2 gap-2 text-xs font-mono">
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="fricMet1Label" class="text-[11px] text-slate-400">Limiting Friction (f_s,max):</div>
              <div id="fricMet1Val" class="text-sm font-bold text-amber-400 mt-0.5">29.4 N</div>
            </div>
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="fricMet2Label" class="text-[11px] text-slate-400">Kinetic Friction (f_k):</div>
              <div id="fricMet2Val" class="text-sm font-bold text-emerald-400 mt-0.5">19.6 N</div>
            </div>
          </div>

          <div class="glass-card p-2.5 rounded-lg border border-slate-800 text-xs font-mono">
            <div id="fricMet3Label" class="text-[11px] text-slate-400">Active Friction Force (f):</div>
            <div id="fricMet3Val" class="text-sm font-bold text-sky-400 mt-0.5">20.0 N (Self-Adjusting)</div>
          </div>

          <div id="fricStatusCard" class="glass-card p-3 rounded-lg border border-emerald-500/30 bg-emerald-950/20 text-xs font-mono">
            <div class="text-[10px] text-slate-400 uppercase tracking-wider">Physical Motion Status</div>
            <div id="fricStateVal" class="text-xs font-bold text-emerald-300 mt-1">
              STATIC REST: Applied Pull &lt; Limiting Friction
            </div>
          </div>
        </div>
      </aside>
    </section>

    <!-- ======================================================== -->
    <!-- ENGINE 3: MOMENTUM & IMPULSE (CONCEPTS 4-6)              -->
    <!-- ======================================================== -->
    <section id="engineMomentum" class="flex-1 flex overflow-hidden hidden">
      <!-- Left Visual Canvas Area -->
      <div class="flex-1 flex flex-col p-4">
        <!-- Sub-Preset Toolbar -->
        <div class="flex items-center justify-between mb-3 shrink-0">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
            <button id="subMomImpulseBtn" onclick="setMomentumConcept('impulse')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
              Concept 4: Impulse-Momentum Theorem &amp; Wall Collision
            </button>
            <button id="subMomRocketBtn" onclick="setMomentumConcept('rocket')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 5: Rocket Thrust &amp; Variable Mass
            </button>
            <button id="subMomLamiBtn" onclick="setMomentumConcept('lami')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 6: Equilibrium &amp; Lami's Theorem
            </button>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="triggerMomentumAction()" id="momActionBtn" class="px-2.5 py-1 rounded bg-sky-500/20 hover:bg-sky-500/30 border border-sky-400/40 text-sky-300 text-xs font-medium transition flex items-center space-x-1">
              <i class="fa-solid fa-play"></i>
              <span id="momActionLabel">Fire Ball Impact</span>
            </button>
          </div>
        </div>

        <!-- Canvas Container -->
        <div id="momentumCanvasContainer" class="flex-1 rounded-xl border border-slate-800 bg-[#070b14] relative overflow-hidden flex items-center justify-center shadow-inner">
          <canvas id="momentumCanvas" class="w-full h-full block"></canvas>
          <div id="momLiveBadge" class="absolute top-3 left-4 text-xs font-mono text-sky-400 bg-slate-900/80 px-2.5 py-1 rounded-md border border-sky-500/30">
            Impulse-Momentum Active
          </div>
        </div>
      </div>

      <!-- Right Sidebar -->
      <aside class="w-96 glass-panel border-l p-4 flex flex-col overflow-y-auto space-y-4 shrink-0">
        <div>
          <div id="momHeader" class="text-xs font-mono text-sky-400 uppercase tracking-wider">CONCEPT 4 • IMPULSE &amp; MOMENTUM</div>
          <h2 id="momTitle" class="text-base font-bold text-slate-100 mt-0.5">Area Under F-t Curve = Δp</h2>
          <p id="momFormula" class="text-xs font-mono text-slate-400 mt-1 bg-slate-900/80 p-2 rounded border border-slate-800">
            J = ∫F dt = Δp = m·(v_f - v_i) = 2mv
          </p>
        </div>

        <!-- Sliders -->
        <div class="space-y-3.5 glass-card p-3.5 rounded-xl">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center justify-between">
            <span>Physical Parameters</span>
            <span class="text-[10px] text-sky-400 font-mono">LIVE SLIDERS</span>
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="momParam1Label" class="text-slate-300 font-medium">Approach Speed (v):</span>
              <span id="momParam1Val" class="text-sky-400 font-mono font-bold">15.0 m/s</span>
            </div>
            <input type="range" id="momSlider1" min="5" max="35" step="1" value="15" oninput="updateMomentum()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="momParam2Label" class="text-slate-300 font-medium">Ball Mass (m):</span>
              <span id="momParam2Val" class="text-sky-400 font-mono font-bold">0.50 kg</span>
            </div>
            <input type="range" id="momSlider2" min="0.10" max="2.50" step="0.05" value="0.50" oninput="updateMomentum()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div id="momBlock3">
            <div class="flex justify-between text-xs mb-1">
              <span id="momParam3Label" class="text-slate-300 font-medium">Contact Duration (Δt):</span>
              <span id="momParam3Val" class="text-sky-400 font-mono font-bold">0.020 s</span>
            </div>
            <input type="range" id="momSlider3" min="0.005" max="0.050" step="0.005" value="0.020" oninput="updateMomentum()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>
        </div>

        <!-- Metrics -->
        <div class="space-y-2.5">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Dynamic Momentum Readout</div>

          <div class="grid grid-cols-2 gap-2 text-xs font-mono">
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="momMet1Label" class="text-[11px] text-slate-400">Initial Momentum (p_i):</div>
              <div id="momMet1Val" class="text-sm font-bold text-sky-400 mt-0.5">+7.50 kg·m/s</div>
            </div>
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="momMet2Label" class="text-[11px] text-slate-400">Rebound Momentum (p_f):</div>
              <div id="momMet2Val" class="text-sm font-bold text-rose-400 mt-0.5">-7.50 kg·m/s</div>
            </div>
          </div>

          <div class="glass-card p-2.5 rounded-lg border border-slate-800 text-xs font-mono">
            <div id="momMet3Label" class="text-[11px] text-slate-400">Total Impulse (J = Δp):</div>
            <div id="momMet3Val" class="text-sm font-bold text-amber-400 mt-0.5">15.00 N·s (Doubled Direction)</div>
          </div>

          <div id="momStatusCard" class="glass-card p-3 rounded-lg border border-sky-500/30 bg-sky-950/20 text-xs font-mono">
            <div class="text-[10px] text-slate-400 uppercase tracking-wider">Peak Impact Force (F_avg)</div>
            <div id="momStateVal" class="text-xs font-bold text-sky-300 mt-1">
              F_avg = 750 N • Wall Compressing Elastic Layer
            </div>
          </div>
        </div>
      </aside>
    </section>

    <!-- ======================================================== -->
    <!-- ENGINE 4: CIRCULAR DYNAMICS & BANKING (CONCEPTS 10-11)   -->
    <!-- ======================================================== -->
    <section id="engineCircular" class="flex-1 flex overflow-hidden hidden">
      <!-- Left Visual Canvas Area -->
      <div class="flex-1 flex flex-col p-4">
        <!-- Sub-Preset Toolbar -->
        <div class="flex items-center justify-between mb-3 shrink-0">
          <div class="flex items-center space-x-2">
            <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
            <button id="subCircFlatBtn" onclick="setCircConcept('flat')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
              Concept 10: Level Circular Road Skidding
            </button>
            <button id="subCircBankedBtn" onclick="setCircConcept('banked')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 11: Engineered Banked Road Dynamics
            </button>
            <button id="subCircLoopBtn" onclick="setCircConcept('loop')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
              Concept 11-B: Vertical Circular Loop Dynamics
            </button>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="triggerCircAction()" id="circActionBtn" class="px-2.5 py-1 rounded bg-sky-500/20 hover:bg-sky-500/30 border border-sky-400/40 text-sky-300 text-xs font-medium transition flex items-center space-x-1">
              <i class="fa-solid fa-gauge-high"></i>
              <span id="circActionLabel">Test Drift Grip</span>
            </button>
          </div>
        </div>

        <!-- Canvas Container -->
        <div id="circularCanvasContainer" class="flex-1 rounded-xl border border-slate-800 bg-[#070b14] relative overflow-hidden flex items-center justify-center shadow-inner">
          <canvas id="circularCanvas" class="w-full h-full block"></canvas>
          <div id="circLiveBadge" class="absolute top-3 left-4 text-xs font-mono text-sky-400 bg-slate-900/80 px-2.5 py-1 rounded-md border border-sky-500/30">
            Circular Dynamics Active
          </div>
        </div>
      </div>

      <!-- Right Sidebar -->
      <aside class="w-96 glass-panel border-l p-4 flex flex-col overflow-y-auto space-y-4 shrink-0">
        <div>
          <div id="circHeader" class="text-xs font-mono text-sky-400 uppercase tracking-wider">CONCEPT 10 • LEVEL CIRCULAR ROAD</div>
          <h2 id="circTitle" class="text-base font-bold text-slate-100 mt-0.5">Static Friction Supplies Centripetal Force</h2>
          <p id="circFormula" class="text-xs font-mono text-slate-400 mt-1 bg-slate-900/80 p-2 rounded border border-slate-800">
            f_s = m·v²/r ≤ μ_s·m·g => v_max = √(μ_s·r·g)
          </p>
        </div>

        <!-- Sliders -->
        <div class="space-y-3.5 glass-card p-3.5 rounded-xl">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center justify-between">
            <span>Physical Parameters</span>
            <span class="text-[10px] text-sky-400 font-mono">LIVE SLIDERS</span>
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="circParam1Label" class="text-slate-300 font-medium">Turn Radius (r):</span>
              <span id="circParam1Val" class="text-sky-400 font-mono font-bold">50 m</span>
            </div>
            <input type="range" id="circSlider1" min="20" max="150" step="5" value="50" oninput="updateCircular()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div>
            <div class="flex justify-between text-xs mb-1">
              <span id="circParam2Label" class="text-slate-300 font-medium">Road Friction (μ_s):</span>
              <span id="circParam2Val" class="text-sky-400 font-mono font-bold">0.50</span>
            </div>
            <input type="range" id="circSlider2" min="0.10" max="0.90" step="0.05" value="0.50" oninput="updateCircular()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div id="circBlock3">
            <div class="flex justify-between text-xs mb-1">
              <span id="circParam3Label" class="text-slate-300 font-medium">Car Speed (v):</span>
              <span id="circParam3Val" class="text-sky-400 font-mono font-bold">50 km/h</span>
            </div>
            <input type="range" id="circSlider3" min="10" max="150" step="2" value="50" oninput="updateCircular()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>

          <div id="circBlock4" class="hidden">
            <div class="flex justify-between text-xs mb-1">
              <span id="circParam4Label" class="text-slate-300 font-medium">Banking Angle (θ):</span>
              <span id="circParam4Val" class="text-sky-400 font-mono font-bold">20°</span>
            </div>
            <input type="range" id="circSlider4" min="5" max="45" step="1" value="20" oninput="updateCircular()" class="w-full h-1.5 bg-slate-700 rounded-lg cursor-pointer">
          </div>
        </div>

        <!-- Metrics -->
        <div class="space-y-2.5">
          <div class="text-xs font-semibold text-slate-300 uppercase tracking-wider">Dynamic Speeds &amp; Traction</div>

          <div class="grid grid-cols-2 gap-2 text-xs font-mono">
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="circMet1Label" class="text-[11px] text-slate-400">Max Safe Speed (v_max):</div>
              <div id="circMet1Val" class="text-sm font-bold text-amber-400 mt-0.5">56.4 km/h</div>
            </div>
            <div class="glass-card p-2.5 rounded-lg border border-slate-800">
              <div id="circMet2Label" class="text-[11px] text-slate-400">Current Velocity:</div>
              <div id="circMet2Val" class="text-sm font-bold text-sky-400 mt-0.5">50.0 km/h (13.9 m/s)</div>
            </div>
          </div>

          <div class="glass-card p-2.5 rounded-lg border border-slate-800 text-xs font-mono">
            <div id="circMet3Label" class="text-[11px] text-slate-400">Centripetal Force vs Limit:</div>
            <div id="circMet3Val" class="text-sm font-bold text-emerald-400 mt-0.5">78% of Max Tire Grip</div>
          </div>

          <div id="circStatusCard" class="glass-card p-3 rounded-lg border border-emerald-500/30 bg-emerald-950/20 text-xs font-mono">
            <div class="text-[10px] text-slate-400 uppercase tracking-wider">Traction Safety State</div>
            <div id="circStateVal" class="text-xs font-bold text-emerald-300 mt-1">
              ✓ SAFE TRACTION: Friction supplies centripetal force
            </div>
          </div>
        </div>
      </aside>
    </section>

  </main>

  <!-- ======================================================== -->
  <!-- JAVASCRIPT SIMULATION CORE & RENDERING ENGINES           -->
  <!-- ======================================================== -->
  <script>
    // State management
    let currentMode = 'newton';
    let currentNewtonConcept = 'fbd';
    let currentFrictionConcept = 'graph';
    let currentMomentumConcept = 'impulse';
    let currentCircConcept = 'flat';

    // Canvas references
    const nCanvas = document.getElementById('newtonCanvas');
    const nCtx = nCanvas.getContext('2d');
    const fCanvas = document.getElementById('frictionCanvas');
    const fCtx = fCanvas.getContext('2d');
    const mCanvas = document.getElementById('momentumCanvas');
    const mCtx = mCanvas.getContext('2d');
    const cCanvas = document.getElementById('circularCanvas');
    const cCtx = cCanvas.getContext('2d');

    // Utility: Handle High-DPI
    function resizeCanvas(canvas) {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      if (canvas.width !== Math.floor(rect.width * dpr) || canvas.height !== Math.floor(rect.height * dpr)) {
        canvas.width = Math.floor(rect.width * dpr);
        canvas.height = Math.floor(rect.height * dpr);
      }
      const ctx = canvas.getContext('2d');
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    // Utility: Draw crisp vector arrow
    function drawArrow(ctx, fromx, fromy, tox, toy, color, label, headlen = 10, isDashed = false) {
      const dx = tox - fromx;
      const dy = toy - fromy;
      const angle = Math.atan2(dy, dx);
      const len = Math.hypot(dx, dy);
      if (len < 2) return;

      ctx.save();
      ctx.strokeStyle = color;
      ctx.fillStyle = color;
      ctx.lineWidth = 2.5;
      if (isDashed) ctx.setLineDash([4, 4]);

      ctx.beginPath();
      ctx.moveTo(fromx, fromy);
      ctx.lineTo(tox, toy);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.beginPath();
      ctx.moveTo(tox, toy);
      ctx.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
      ctx.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
      ctx.closePath();
      ctx.fill();

      if (label) {
        ctx.font = 'bold 11px Consolas, monospace';
        const midX = (fromx + tox) / 2 + 10 * Math.sin(angle);
        const midY = (fromy + toy) / 2 - 10 * Math.cos(angle);
        ctx.fillText(label, midX, midY);
      }
      ctx.restore();
    }

    // Switch Main Mode Tabs
    function switchMode(mode) {
      currentMode = mode;
      ['newton', 'friction', 'momentum', 'circular'].forEach(m => {
        const eng = document.getElementById('engine' + m.charAt(0).toUpperCase() + m.slice(1));
        const tab = document.getElementById('tab' + m.charAt(0).toUpperCase() + m.slice(1));
        if (m === mode) {
          eng.classList.remove('hidden');
          tab.className = 'active-tab px-3.5 py-1.5 rounded-lg border border-transparent font-medium transition flex items-center space-x-1.5';
        } else {
          eng.classList.add('hidden');
          tab.className = 'px-3.5 py-1.5 rounded-lg border border-transparent text-slate-400 font-medium hover:text-slate-200 transition flex items-center space-x-1.5';
        }
      });

      if (mode === 'newton') { updateNewton(); drawNewtonCanvas(); }
      else if (mode === 'friction') { updateFriction(); drawFrictionCanvas(); }
      else if (mode === 'momentum') { updateMomentum(); drawMomentumCanvas(); }
      else if (mode === 'circular') { updateCircular(); drawCircularCanvas(); }
    }

    // ========================================================
    // ENGINE 1: NEWTON LAWS, FBD & ELEVATOR
    // ========================================================
    let fbdPos = 0;
    let elevatorCabinY = 0;
    let atwoodY = 0;
    let atwoodSpeed = 0;

    function setNewtonConcept(sub) {
      currentNewtonConcept = sub;
      document.getElementById('subNewtonFbdBtn').className = sub === 'fbd' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subNewtonElevatorBtn').className = sub === 'elevator' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subNewtonTensionBtn').className = sub === 'tension' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      const s1 = document.getElementById('newtonSlider1');
      const s2 = document.getElementById('newtonSlider2');
      const s3 = document.getElementById('newtonSlider3');
      const b3 = document.getElementById('newtonBlock3');

      if (sub === 'fbd') {
        document.getElementById('newtonHeader').innerText = "CONCEPT 1 • FREE-BODY DIAGRAM";
        document.getElementById('newtonTitle').innerText = "FBD Orthogonal Vector Resolver";
        document.getElementById('newtonFormula').innerText = "ΣF_x = m·a_x • ΣF_y = 0 • N = mg - F·sinθ";
        document.getElementById('newtonParam1Label').innerText = "Body Mass (m):";
        document.getElementById('newtonParam2Label').innerText = "Pulling Force (F):";
        document.getElementById('newtonParam3Label').innerText = "Pull Angle (θ):";
        document.getElementById('newtonMet1Label').innerText = "Normal Force (N):";
        document.getElementById('newtonMet2Label').innerText = "Horizontal Pull F_x:";
        document.getElementById('newtonMet3Label').innerText = "Net Acceleration (a):";
        document.getElementById('newtonActionLabel').innerText = "Reset Position";
        b3.classList.remove('hidden');
        s1.min = 1; s1.max = 25; s1.step = 0.5; s1.value = 5;
        s2.min = 0; s2.max = 120; s2.step = 1; s2.value = 40;
        s3.min = 0; s3.max = 80; s3.step = 1; s3.value = 30;
      } else if (sub === 'elevator') {
        document.getElementById('newtonHeader').innerText = "CONCEPT 2 • ELEVATORS & PSEUDO FORCE";
        document.getElementById('newtonTitle').innerText = "Apparent Weight Scale in Accelerated Frame";
        document.getElementById('newtonFormula').innerText = "F_pseudo = -m·a_frame • N_app = m(g ± a)";
        document.getElementById('newtonParam1Label').innerText = "Passenger Mass (m):";
        document.getElementById('newtonParam2Label').innerText = "Elevator Accel a (-9.8 to +8):";
        document.getElementById('newtonMet1Label').innerText = "True Weight W = mg:";
        document.getElementById('newtonMet2Label').innerText = "Pseudo Force (-m·a):";
        document.getElementById('newtonMet3Label').innerText = "Scale Reading (N_app):";
        document.getElementById('newtonActionLabel').innerText = "Drop to Free Fall";
        b3.classList.add('hidden');
        s1.min = 20; s1.max = 120; s1.step = 5; s1.value = 60;
        s2.min = -9.8; s2.max = 8.0; s2.step = 0.2; s2.value = 2.0;
      } else if (sub === 'tension') {
        document.getElementById('newtonHeader').innerText = "CONCEPT 3 • ATWOOD MACHINE & TENSION";
        document.getElementById('newtonTitle').innerText = "Two-Body Pulley System Equilibrium & String Tension";
        document.getElementById('newtonFormula').innerText = "a = |m1 - m2|g / (m1 + m2) • T = 2m1·m2·g / (m1 + m2)";
        document.getElementById('newtonParam1Label').innerText = "Left Mass 1 (m1):";
        document.getElementById('newtonParam2Label').innerText = "Right Mass 2 (m2):";
        document.getElementById('newtonMet1Label').innerText = "System Acceleration (a):";
        document.getElementById('newtonMet2Label').innerText = "String Tension (T):";
        document.getElementById('newtonMet3Label').innerText = "Pulley Support Load (2T):";
        document.getElementById('newtonActionLabel').innerText = "Release / Invert Masses";
        b3.classList.add('hidden');
        s1.min = 1; s1.max = 25; s1.step = 0.5; s1.value = 14;
        s2.min = 1; s2.max = 25; s2.step = 0.5; s2.value = 6;
      }
      updateNewton();
    }

    function triggerNewtonAction() {
      if (currentNewtonConcept === 'fbd') {
        fbdPos = 0;
      } else if (currentNewtonConcept === 'elevator') {
        const s2 = document.getElementById('newtonSlider2');
        s2.value = (parseFloat(s2.value) === -9.8) ? 0 : -9.8;
        updateNewton();
      } else if (currentNewtonConcept === 'tension') {
        const s1 = document.getElementById('newtonSlider1');
        const s2 = document.getElementById('newtonSlider2');
        const tmp = s1.value;
        s1.value = s2.value;
        s2.value = tmp;
        atwoodY = 0;
        atwoodSpeed = 0;
        updateNewton();
      }
    }

    function updateNewton() {
      const s1 = parseFloat(document.getElementById('newtonSlider1').value);
      const s2 = parseFloat(document.getElementById('newtonSlider2').value);
      const s3 = parseFloat(document.getElementById('newtonSlider3').value);
      const g = 9.8;

      if (currentNewtonConcept === 'fbd') {
        const m = s1;
        const F = s2;
        const theta = s3;
        const rad = theta * Math.PI / 180;
        const fy = F * Math.sin(rad);
        const fx = F * Math.cos(rad);
        const N = Math.max(0, m * g - fy);
        const a = fx / m;

        document.getElementById('newtonParam1Val').innerText = m.toFixed(1) + ' kg';
        document.getElementById('newtonParam2Val').innerText = F.toFixed(0) + ' N';
        document.getElementById('newtonParam3Val').innerText = theta.toFixed(0) + '°';
        document.getElementById('newtonMet1Val').innerText = N.toFixed(1) + ' N';
        document.getElementById('newtonMet2Val').innerText = fx.toFixed(1) + ' N';
        document.getElementById('newtonMet3Val').innerText = a.toFixed(2) + ' m/s²';

        if (N === 0) {
          document.getElementById('newtonStateVal').innerText = "★ LIFT-OFF DETECTED: F·sinθ ≥ mg => Block airborne!";
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-amber-300 mt-1";
          document.getElementById('newtonLiveBadge').innerText = "Lift-Off Active (N = 0)";
        } else {
          document.getElementById('newtonStateVal').innerText = `ACCELERATING: a = ${a.toFixed(2)} m/s² across horizontal floor`;
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-sky-300 mt-1";
          document.getElementById('newtonLiveBadge').innerText = "FBD Vector Resolver Active";
        }
      } else if (currentNewtonConcept === 'elevator') {
        const m = s1;
        const aElev = s2;
        const W = m * g;
        const N_app = Math.max(0, m * (g + aElev));
        const F_pseudo = -m * aElev;

        document.getElementById('newtonParam1Val').innerText = m.toFixed(0) + ' kg';
        document.getElementById('newtonParam2Val').innerText = (aElev >= 0 ? '+' : '') + aElev.toFixed(1) + ' m/s² ' + (aElev > 0 ? '(Upward)' : aElev < 0 ? '(Downward)' : '(Rest)');
        document.getElementById('newtonMet1Val').innerText = W.toFixed(1) + ' N';
        document.getElementById('newtonMet2Val').innerText = (F_pseudo >= 0 ? '+' : '') + F_pseudo.toFixed(1) + ' N';
        document.getElementById('newtonMet3Val').innerText = N_app.toFixed(1) + ' N (' + (N_app / g).toFixed(1) + ' kg)';

        if (N_app === 0) {
          document.getElementById('newtonStateVal').innerText = "★ FREE-FALL / ZERO-G: Passenger floating weightless off scale!";
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-amber-300 mt-1";
          document.getElementById('newtonLiveBadge').innerText = "Weightless Float (0-G)";
        } else if (aElev > 3.0) {
          document.getElementById('newtonStateVal').innerText = "HEAVY G-FORCE: Heavy scale spring compression (N_app > mg)";
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-rose-400 mt-1";
          document.getElementById('newtonLiveBadge').innerText = "Elevator Heavy G-Force";
        } else {
          document.getElementById('newtonStateVal').innerText = "NORMAL ACCELERATED FRAME: Spring scale reads m(g + a)";
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('newtonLiveBadge').innerText = "Elevator Apparent Weight";
        }
      } else if (currentNewtonConcept === 'tension') {
        const m1 = s1;
        const m2 = s2;
        const a = Math.abs(m1 - m2) * g / (m1 + m2);
        const T = (2 * m1 * m2 * g) / (m1 + m2);

        document.getElementById('newtonParam1Val').innerText = m1.toFixed(1) + ' kg';
        document.getElementById('newtonParam2Val').innerText = m2.toFixed(1) + ' kg';
        document.getElementById('newtonMet1Val').innerText = a.toFixed(2) + ' m/s²';
        document.getElementById('newtonMet2Val').innerText = T.toFixed(1) + ' N';
        document.getElementById('newtonMet3Val').innerText = (2 * T).toFixed(1) + ' N';

        if (m1 === m2) {
          document.getElementById('newtonStateVal').innerText = "✓ PERFECT EQUILIBRIUM: m1 = m2 => a = 0 (Static Balance)";
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('newtonLiveBadge').innerText = "Atwood Balanced (a = 0)";
        } else {
          const heavy = m1 > m2 ? "Left (m1)" : "Right (m2)";
          document.getElementById('newtonStateVal').innerText = `UNBALANCED: ${heavy} mass accelerates downward at ${a.toFixed(2)} m/s²`;
          document.getElementById('newtonStateVal').className = "text-xs font-bold text-sky-300 mt-1";
          document.getElementById('newtonLiveBadge').innerText = `Atwood Accelerating (${a.toFixed(1)} m/s²)`;
        }
      }
      drawNewtonCanvas();
    }

    function drawNewtonCanvas() {
      resizeCanvas(nCanvas);
      const w = nCanvas.width / (window.devicePixelRatio || 1);
      const h = nCanvas.height / (window.devicePixelRatio || 1);
      if (!w || !h) return;
      nCtx.clearRect(0, 0, w, h);

      const cx = w / 2;
      const cy = h / 2 + 15;
      const g = 9.8;

      if (currentNewtonConcept === 'fbd') {
        const m = parseFloat(document.getElementById('newtonSlider1').value);
        const F = parseFloat(document.getElementById('newtonSlider2').value);
        const theta = parseFloat(document.getElementById('newtonSlider3').value);
        const rad = theta * Math.PI / 180;
        const fy = F * Math.sin(rad);
        const fx = F * Math.cos(rad);
        const N = Math.max(0, m * g - fy);
        const a = fx / m;

        // Block dimensions scale noticeably with mass m!
        const side = 38 + Math.sqrt(m) * 9.5;
        const floorY = cy + 55;

        // Textured Floor
        nCtx.strokeStyle = '#475569';
        nCtx.lineWidth = 2.5;
        nCtx.beginPath();
        nCtx.moveTo(cx - 200, floorY);
        nCtx.lineTo(cx + 200, floorY);
        nCtx.stroke();

        for (let x = cx - 190; x <= cx + 190; x += 15) {
          nCtx.beginPath();
          nCtx.moveTo(x, floorY);
          nCtx.lineTo(x - 10, floorY + 10);
          nCtx.strokeStyle = '#334155';
          nCtx.stroke();
        }

        // Animated Position for Block when Fx > 0
        const bx = cx - side / 2 + (a > 0.05 ? fbdPos : 0);
        const liftOffset = (N === 0 ? 25 : 0);
        const by = floorY - side - liftOffset;

        // Block Body
        nCtx.fillStyle = '#1e293b';
        nCtx.strokeStyle = N === 0 ? '#facc15' : '#38bdf8';
        nCtx.lineWidth = 2.5;
        nCtx.fillRect(bx, by, side, side);
        nCtx.strokeRect(bx, by, side, side);

        nCtx.fillStyle = '#ffffff';
        nCtx.font = 'bold 12px Consolas, monospace';
        nCtx.fillText(`m=${m.toFixed(1)}kg`, bx + 6, by + side / 2 + 4);

        if (N === 0) {
          nCtx.fillStyle = '#facc15';
          nCtx.font = 'bold 12px Consolas, monospace';
          nCtx.fillText('★ AIRBORNE LIFT-OFF (N = 0) ★', bx - 35, by - 30);
        }

        // Vector 1: W = mg (Rose)
        const mgLen = Math.min(100, 25 + m * 3.0);
        drawArrow(nCtx, bx + side / 2, by + side / 2, bx + side / 2, by + side / 2 + mgLen, '#F43F5E', `W=mg (${(m * g).toFixed(0)}N)`);

        // Vector 2: Normal Force N (Emerald)
        if (N > 0) {
          const nLen = Math.min(100, (N / (m * g)) * mgLen);
          drawArrow(nCtx, bx + side / 2, by + side, bx + side / 2, by + side - nLen, '#4ADE80', `N=${N.toFixed(0)}N`);
        }

        // Vector 3: Pull F (Gold) with resolved components
        if (F > 0) {
          const fLen = Math.min(120, 20 + F * 0.85);
          const fEndx = bx + side + Math.cos(rad) * fLen;
          const fEndy = by + side / 2 - Math.sin(rad) * fLen;
          drawArrow(nCtx, bx + side, by + side / 2, fEndx, fEndy, '#FACC15', `F=${F.toFixed(0)}N`);

          // Arc
          nCtx.strokeStyle = '#FACC15';
          nCtx.beginPath();
          nCtx.arc(bx + side, by + side / 2, 25, 0, -rad, true);
          nCtx.stroke();
          nCtx.fillStyle = '#FACC15';
          nCtx.font = '11px Consolas, monospace';
          nCtx.fillText(`θ=${theta}°`, bx + side + 30, by + side / 2 - 8);

          // Component lines
          nCtx.strokeStyle = '#38bdf8';
          nCtx.setLineDash([2, 2]);
          nCtx.beginPath();
          nCtx.moveTo(fEndx, by + side / 2);
          nCtx.lineTo(fEndx, fEndy);
          nCtx.stroke();
          nCtx.setLineDash([]);
          drawArrow(nCtx, bx + side, by + side / 2, fEndx, by + side / 2, '#38bdf8', `Fx=${fx.toFixed(0)}N`, 10);
        }

        // Acceleration Arrow
        if (a > 0.05) {
          const aLen = Math.min(80, a * 6 + 15);
          drawArrow(nCtx, bx, by - 12, bx + aLen, by - 12, '#38bdf8', `a=${a.toFixed(1)}m/s²`, 11);
        }

      } else if (currentNewtonConcept === 'elevator') {
        const m = parseFloat(document.getElementById('newtonSlider1').value);
        const aElev = parseFloat(document.getElementById('newtonSlider2').value);
        const W = m * g;
        const N_app = Math.max(0, m * (g + aElev));

        // Elevator Shaft Walls
        nCtx.strokeStyle = '#334155';
        nCtx.lineWidth = 2;
        nCtx.beginPath();
        nCtx.moveTo(cx - 130, 20);
        nCtx.lineTo(cx - 130, h - 20);
        nCtx.moveTo(cx + 130, 20);
        nCtx.lineTo(cx + 130, h - 20);
        nCtx.stroke();

        // Moving Shaft Floor markers to create visual vertical motion
        const scrollOffset = elevatorCabinY % 40;
        nCtx.strokeStyle = '#1e293b';
        nCtx.lineWidth = 1;
        for (let y = scrollOffset; y < h; y += 40) {
          nCtx.beginPath();
          nCtx.moveTo(cx - 130, y);
          nCtx.lineTo(cx - 145, y);
          nCtx.moveTo(cx + 130, y);
          nCtx.lineTo(cx + 145, y);
          nCtx.stroke();
        }

        // Elevator Cabin
        const cageW = 200;
        const cageH = 230;
        const cageTop = cy - cageH / 2;

        nCtx.strokeStyle = '#64748b';
        nCtx.lineWidth = 3.5;
        nCtx.strokeRect(cx - cageW / 2, cageTop, cageW, cageH);

        // Suspension Cable
        nCtx.strokeStyle = '#94a3b8';
        nCtx.lineWidth = 4;
        nCtx.beginPath();
        nCtx.moveTo(cx, cageTop);
        nCtx.lineTo(cx, 0);
        nCtx.stroke();

        // Dual Steel Springs supporting weighing scale platform:
        // Physical spring compression directly scales with actual load N_app!
        const maxExpectedN = 120 * (9.8 + 8.0); // ~2136 N
        const springComp = Math.min(26, (N_app / maxExpectedN) * 26);
        const scaleBaseY = cy + cageH / 2 - 35;
        const scaleY = scaleBaseY + springComp;

        // Springs
        nCtx.strokeStyle = '#94a3b8';
        nCtx.lineWidth = 2.5;
        [-40, 40].forEach(ox => {
          nCtx.beginPath();
          nCtx.moveTo(cx + ox, scaleBaseY + 28);
          const segs = 5;
          const springH = (scaleBaseY + 28) - (scaleY + 14);
          for (let s = 0; s <= segs; s++) {
            const sy = (scaleBaseY + 28) - (s / segs) * springH;
            const sx = cx + ox + (s > 0 && s < segs ? (s % 2 === 0 ? 6 : -6) : 0);
            nCtx.lineTo(sx, sy);
          }
          nCtx.stroke();
        });

        // Scale Body
        nCtx.fillStyle = '#0f172a';
        nCtx.strokeStyle = '#38bdf8';
        nCtx.lineWidth = 2;
        nCtx.fillRect(cx - 70, scaleY, 140, 22);
        nCtx.strokeRect(cx - 70, scaleY, 140, 22);

        // Live Scale LED Display
        nCtx.fillStyle = N_app === 0 ? '#facc15' : '#38bdf8';
        nCtx.font = 'bold 12px Consolas, monospace';
        nCtx.fillText(`SCALE: ${N_app.toFixed(1)} N (${(N_app / g).toFixed(1)} kg)`, cx - 64, scaleY + 15);

        // Passenger Body: Visibly scales with mass m!
        const pW = 32 + (m / 120) * 28;
        const pH = 55 + (m / 120) * 22;
        const isFloating = N_app === 0;
        const pY = isFloating ? scaleY - pH - 30 : scaleY - pH; // floats up when weightless!

        // Passenger Figure
        nCtx.fillStyle = isFloating ? '#1e1b4b' : '#1e293b';
        nCtx.strokeStyle = isFloating ? '#facc15' : '#4ade80';
        nCtx.lineWidth = 2.5;
        nCtx.fillRect(cx - pW / 2, pY, pW, pH);
        nCtx.strokeRect(cx - pW / 2, pY, pW, pH);

        // Head
        const headR = 12 + (m / 120) * 5;
        nCtx.beginPath();
        nCtx.arc(cx, pY - headR - 2, headR, 0, Math.PI * 2);
        nCtx.fillStyle = '#334155';
        nCtx.fill();
        nCtx.strokeStyle = isFloating ? '#facc15' : '#4ade80';
        nCtx.stroke();

        // Mass tag on torso
        nCtx.fillStyle = '#ffffff';
        nCtx.font = 'bold 11px Consolas, monospace';
        nCtx.fillText(`${m}kg`, cx - 13, pY + pH / 2 + 4);

        if (isFloating) {
          nCtx.fillStyle = '#facc15';
          nCtx.font = 'bold 12px Consolas, monospace';
          nCtx.fillText('★ WEIGHTLESS FLOAT (N_app = 0) ★', cx - 85, pY - 25);
        }

        // Vectors
        // W = mg (Rose)
        const wLen = 30 + (m / 120) * 50;
        drawArrow(nCtx, cx, pY + pH / 2, cx, pY + pH / 2 + wLen, '#F43F5E', `W=mg (${W.toFixed(0)}N)`);

        // N_app (Emerald)
        if (N_app > 0) {
          const nLen = Math.max(12, (N_app / W) * wLen);
          drawArrow(nCtx, cx, pY + pH / 2, cx, pY + pH / 2 - nLen, '#4ADE80', `N=${N_app.toFixed(0)}N`);
        }

        // Elevator acceleration arrow on side
        if (aElev !== 0) {
          const aLen = Math.abs(aElev) * 10;
          const aDir = aElev > 0 ? -1 : 1;
          drawArrow(nCtx, cx + cageW / 2 + 25, cy, cx + cageW / 2 + 25, cy + aDir * aLen, aElev > 0 ? '#38bdf8' : '#F43F5E', `a = ${aElev.toFixed(1)}`);
        }

      } else if (currentNewtonConcept === 'tension') {
        const m1 = parseFloat(document.getElementById('newtonSlider1').value);
        const m2 = parseFloat(document.getElementById('newtonSlider2').value);
        const a = Math.abs(m1 - m2) * g / (m1 + m2);
        const T = (2 * m1 * m2 * g) / (m1 + m2);

        // Center Pulley Wheel
        const pulleyR = 36;
        const pulleyY = cy - 90;
        nCtx.beginPath();
        nCtx.arc(cx, pulleyY, pulleyR, 0, Math.PI * 2);
        nCtx.fillStyle = '#1e293b';
        nCtx.fill();
        nCtx.strokeStyle = '#94a3b8';
        nCtx.lineWidth = 3.5;
        nCtx.stroke();

        // Spinning Spokes
        const spokeAng = atwoodY * 0.08;
        for (let i = 0; i < 4; i++) {
          const aSp = spokeAng + (i * Math.PI / 2);
          nCtx.beginPath();
          nCtx.moveTo(cx, pulleyY);
          nCtx.lineTo(cx + pulleyR * Math.cos(aSp), pulleyY + pulleyR * Math.sin(aSp));
          nCtx.strokeStyle = '#64748b';
          nCtx.stroke();
        }

        // Pulley Support Stand
        nCtx.strokeStyle = '#475569';
        nCtx.lineWidth = 4;
        nCtx.beginPath();
        nCtx.moveTo(cx, pulleyY);
        nCtx.lineTo(cx, 15);
        nCtx.stroke();

        // Dynamic Heights for Left and Right masses
        const leftH = cy - 10 + atwoodY;
        const rightH = cy - 10 - atwoodY;

        // String
        nCtx.strokeStyle = '#f8fafc';
        nCtx.lineWidth = 2.5;
        nCtx.beginPath();
        nCtx.moveTo(cx - pulleyR, pulleyY);
        nCtx.lineTo(cx - pulleyR, leftH);
        nCtx.moveTo(cx + pulleyR, pulleyY);
        nCtx.lineTo(cx + pulleyR, rightH);
        nCtx.stroke();

        // Block 1 (Left - m1) - Visibly scales with m1!
        const b1Side = 28 + Math.sqrt(m1) * 9;
        nCtx.fillStyle = '#1e293b';
        nCtx.strokeStyle = '#38bdf8';
        nCtx.lineWidth = 2.5;
        nCtx.fillRect(cx - pulleyR - b1Side / 2, leftH, b1Side, b1Side);
        nCtx.strokeRect(cx - pulleyR - b1Side / 2, leftH, b1Side, b1Side);
        nCtx.fillStyle = '#ffffff';
        nCtx.font = 'bold 11px Consolas, monospace';
        nCtx.fillText(`m1=${m1.toFixed(1)}kg`, cx - pulleyR - b1Side / 2 + 4, leftH + b1Side / 2 + 4);

        // Block 2 (Right - m2) - Visibly scales with m2!
        const b2Side = 28 + Math.sqrt(m2) * 9;
        nCtx.fillStyle = '#1e293b';
        nCtx.strokeStyle = '#facc15';
        nCtx.lineWidth = 2.5;
        nCtx.fillRect(cx + pulleyR - b2Side / 2, rightH, b2Side, b2Side);
        nCtx.strokeRect(cx + pulleyR - b2Side / 2, rightH, b2Side, b2Side);
        nCtx.fillStyle = '#ffffff';
        nCtx.fillText(`m2=${m2.toFixed(1)}kg`, cx + pulleyR - b2Side / 2 + 4, rightH + b2Side / 2 + 4);

        // Tension Arrows (Upward)
        const tLen = Math.min(55, 15 + T * 0.35);
        drawArrow(nCtx, cx - pulleyR, leftH, cx - pulleyR, leftH - tLen, '#4ADE80', `T=${T.toFixed(0)}N`, 10);
        drawArrow(nCtx, cx + pulleyR, rightH, cx + pulleyR, rightH - tLen, '#4ADE80', `T=${T.toFixed(0)}N`, 10);

        // Weight Arrows (Downward)
        const w1Len = Math.min(65, 15 + m1 * 2.2);
        const w2Len = Math.min(65, 15 + m2 * 2.2);
        drawArrow(nCtx, cx - pulleyR, leftH + b1Side, cx - pulleyR, leftH + b1Side + w1Len, '#F43F5E', `${(m1 * g).toFixed(0)}N`, 10);
        drawArrow(nCtx, cx + pulleyR, rightH + b2Side, cx + pulleyR, rightH + b2Side + w2Len, '#F43F5E', `${(m2 * g).toFixed(0)}N`, 10);
      }
    }

    // ========================================================
    // ENGINE 2: FRICTION, INCLINE & TWO-BLOCK
    // ========================================================
    let slideX = 0;
    let inclineBlockPos = 0;
    let twoBlockX = 0;
    let twoBlockRelSlip = 0;

    function setFrictionConcept(sub) {
      currentFrictionConcept = sub;
      document.getElementById('subFrictionGraphBtn').className = sub === 'graph' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subFrictionInclineBtn').className = sub === 'incline' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subFrictionTwoBlockBtn').className = sub === 'twoblock' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      const s1 = document.getElementById('fricSlider1');
      const s2 = document.getElementById('fricSlider2');
      const s3 = document.getElementById('fricSlider3');
      const s4 = document.getElementById('fricSlider4');
      const b3 = document.getElementById('fricBlock3');
      const b4 = document.getElementById('fricBlock4');

      if (sub === 'graph') {
        document.getElementById('frictionHeader').innerText = "CONCEPT 7 • FRICTION MECHANICS";
        document.getElementById('frictionTitle').innerText = "Self-Adjusting Static vs Kinetic Graph";
        document.getElementById('frictionFormula').innerText = "f_s ≤ μ_s·N • f_k = μ_k·N (μ_k < μ_s)";
        document.getElementById('fricParam1Label').innerText = "Static Coeff (μ_s):";
        document.getElementById('fricParam2Label').innerText = "Kinetic Coeff (μ_k):";
        document.getElementById('fricParam3Label').innerText = "Applied Pull (F_app):";
        document.getElementById('fricParam4Label').innerText = "Block Mass (m):";
        document.getElementById('fricMet1Label').innerText = "Limiting Friction (f_s,max):";
        document.getElementById('fricMet2Label').innerText = "Kinetic Friction (f_k):";
        document.getElementById('fricMet3Label').innerText = "Active Friction Force (f):";
        document.getElementById('fricActionLabel').innerText = "Pull to Threshold";
        b3.classList.remove('hidden');
        b4.classList.remove('hidden');
        s1.min = 0.10; s1.max = 0.90; s1.step = 0.05; s1.value = 0.60;
        s2.min = 0.05; s2.max = 0.85; s2.step = 0.05; s2.value = 0.40;
        s3.min = 0; s3.max = 120; s3.step = 1; s3.value = 20;
        s4.min = 1; s4.max = 20; s4.step = 0.5; s4.value = 5.0;
      } else if (sub === 'incline') {
        document.getElementById('frictionHeader').innerText = "CONCEPT 8 • ANGLE OF REPOSE";
        document.getElementById('frictionTitle').innerText = "Motion on Rough Incline & Angle of Repose";
        document.getElementById('frictionFormula').innerText = "tan θ_R = μ_s • a_down = g(sinθ - μ_k·cosθ)";
        document.getElementById('fricParam1Label').innerText = "Incline Angle (θ):";
        document.getElementById('fricParam2Label').innerText = "Static Coeff (μ_s):";
        document.getElementById('fricParam3Label').innerText = "Kinetic Coeff (μ_k):";
        document.getElementById('fricParam4Label').innerText = "Block Mass (m):";
        document.getElementById('fricMet1Label').innerText = "Angle of Repose (θ_R):";
        document.getElementById('fricMet2Label').innerText = "Downslope Gravity mg·sinθ:";
        document.getElementById('fricMet3Label').innerText = "Active Friction:";
        document.getElementById('fricActionLabel').innerText = "Set Angle to Repose";
        b3.classList.remove('hidden');
        b4.classList.remove('hidden');
        s1.min = 0; s1.max = 75; s1.step = 1; s1.value = 25;
        s2.min = 0.10; s2.max = 0.90; s2.step = 0.05; s2.value = 0.50;
        s3.min = 0.05; s3.max = 0.85; s3.step = 0.05; s3.value = 0.35;
        s4.min = 1; s4.max = 15; s4.step = 0.5; s4.value = 5.0;
      } else if (sub === 'twoblock') {
        document.getElementById('frictionHeader').innerText = "CONCEPT 9 • TWO-BLOCK SYSTEM";
        document.getElementById('frictionTitle').innerText = "Relative Slipping Force Threshold";
        document.getElementById('frictionFormula').innerText = "a_max = μ_s·g • F_max = (m1 + m2)·μ_s·g";
        document.getElementById('fricParam1Label').innerText = "Top Mass (m1):";
        document.getElementById('fricParam2Label').innerText = "Bottom Mass (m2):";
        document.getElementById('fricParam3Label').innerText = "Interface Friction (μ_s):";
        document.getElementById('fricParam4Label').innerText = "Pull on Bottom (F):";
        document.getElementById('fricMet1Label').innerText = "Slip Threshold (F_max):";
        document.getElementById('fricMet2Label').innerText = "Max Common Accel (a_max):";
        document.getElementById('fricMet3Label').innerText = "Active Pull Force (F):";
        document.getElementById('fricActionLabel').innerText = "Pull Above Slip F_max";
        b3.classList.remove('hidden');
        b4.classList.remove('hidden');
        s1.min = 1; s1.max = 10; s1.step = 0.5; s1.value = 2.0;
        s2.min = 2; s2.max = 20; s2.step = 0.5; s2.value = 4.0;
        s3.min = 0.10; s3.max = 0.90; s3.step = 0.05; s3.value = 0.50;
        s4.min = 0; s4.max = 120; s4.step = 1; s4.value = 20;
      }
      updateFriction();
    }

    function triggerFrictionAction() {
      if (currentFrictionConcept === 'graph') {
        const muS = parseFloat(document.getElementById('fricSlider1').value);
        const m = parseFloat(document.getElementById('fricSlider4').value);
        const fs_max = muS * m * 9.8;
        document.getElementById('fricSlider3').value = Math.min(120, Math.round(fs_max + 15));
        updateFriction();
      } else if (currentFrictionConcept === 'incline') {
        const muS = parseFloat(document.getElementById('fricSlider2').value);
        const thetaR = Math.atan(muS) * 180 / Math.PI;
        document.getElementById('fricSlider1').value = Math.round(thetaR + 3);
        updateFriction();
      } else if (currentFrictionConcept === 'twoblock') {
        const m1 = parseFloat(document.getElementById('fricSlider1').value);
        const m2 = parseFloat(document.getElementById('fricSlider2').value);
        const muS = parseFloat(document.getElementById('fricSlider3').value);
        const F_max = (m1 + m2) * muS * 9.8;
        document.getElementById('fricSlider4').value = Math.min(120, Math.round(F_max + 20));
        updateFriction();
      }
    }

    function updateFriction() {
      const s1 = parseFloat(document.getElementById('fricSlider1').value);
      const s2 = parseFloat(document.getElementById('fricSlider2').value);
      const s3 = parseFloat(document.getElementById('fricSlider3').value);
      const s4 = parseFloat(document.getElementById('fricSlider4').value);
      const g = 9.8;

      if (currentFrictionConcept === 'graph') {
        const muS = s1;
        const muK = Math.min(muS - 0.05, s2);
        const F_app = s3;
        const m = s4;
        const N = m * g;
        const fs_max = muS * N;
        const fk = muK * N;

        document.getElementById('fricParam1Val').innerText = muS.toFixed(2);
        document.getElementById('fricParam2Val').innerText = muK.toFixed(2);
        document.getElementById('fricParam3Val').innerText = F_app.toFixed(0) + ' N';
        document.getElementById('fricParam4Val').innerText = m.toFixed(1) + ' kg';
        document.getElementById('fricMet1Val').innerText = fs_max.toFixed(1) + ' N';
        document.getElementById('fricMet2Val').innerText = fk.toFixed(1) + ' N';

        if (F_app <= fs_max) {
          document.getElementById('fricMet3Val').innerText = F_app.toFixed(1) + ' N (Self-Adjusting Static)';
          document.getElementById('fricStateVal').innerText = "STATIC REST: f_s balances F_app exactly (f_s = F)";
          document.getElementById('fricStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('fricLiveBadge').innerText = "Static Regime (f_s = F)";
        } else {
          const a = (F_app - fk) / m;
          document.getElementById('fricMet3Val').innerText = fk.toFixed(1) + ' N (Constant Kinetic fk)';
          document.getElementById('fricStateVal').innerText = `★ SLIDING ACCELERATION: a = ${a.toFixed(2)} m/s² (f_k drops to μ_k·N)`;
          document.getElementById('fricStateVal').className = "text-xs font-bold text-amber-300 mt-1";
          document.getElementById('fricLiveBadge').innerText = `Kinetic Sliding (a = ${a.toFixed(1)} m/s²)`;
        }
      } else if (currentFrictionConcept === 'incline') {
        const theta = s1;
        const muS = s2;
        const muK = Math.min(muS - 0.05, s3);
        const m = s4;
        const thetaR = Math.atan(muS) * 180 / Math.PI;
        const rad = theta * Math.PI / 180;
        const downslope = m * g * Math.sin(rad);

        document.getElementById('fricParam1Val').innerText = theta.toFixed(0) + '°';
        document.getElementById('fricParam2Val').innerText = muS.toFixed(2);
        document.getElementById('fricParam3Val').innerText = muK.toFixed(2);
        document.getElementById('fricParam4Val').innerText = m.toFixed(1) + ' kg';
        document.getElementById('fricMet1Val').innerText = thetaR.toFixed(1) + '°';
        document.getElementById('fricMet2Val').innerText = downslope.toFixed(1) + ' N';

        if (theta <= thetaR) {
          document.getElementById('fricMet3Val').innerText = downslope.toFixed(1) + ' N (Static mg·sinθ)';
          document.getElementById('fricStateVal').innerText = `STATIONARY: Slope θ (${theta}°) ≤ Repose θ_R (${thetaR.toFixed(1)}°)`;
          document.getElementById('fricStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('fricLiveBadge').innerText = "Incline At Rest (θ ≤ θ_R)";
        } else {
          const aDown = g * (Math.sin(rad) - muK * Math.cos(rad));
          const fk = muK * m * g * Math.cos(rad);
          document.getElementById('fricMet3Val').innerText = fk.toFixed(1) + ' N (Kinetic Opposition)';
          document.getElementById('fricStateVal').innerText = `★ SLIDING DOWNHILL: a = ${Math.max(0, aDown).toFixed(2)} m/s² (θ > θ_R)`;
          document.getElementById('fricStateVal').className = "text-xs font-bold text-amber-300 mt-1";
          document.getElementById('fricLiveBadge').innerText = `Sliding Downhill (${aDown.toFixed(1)} m/s²)`;
        }
      } else if (currentFrictionConcept === 'twoblock') {
        const m1 = s1;
        const m2 = s2;
        const muS = s3;
        const F = s4;
        const a_max = muS * g;
        const F_max = (m1 + m2) * a_max;
        const isSlipping = F > F_max;

        document.getElementById('fricParam1Val').innerText = m1.toFixed(1) + ' kg';
        document.getElementById('fricParam2Val').innerText = m2.toFixed(1) + ' kg';
        document.getElementById('fricParam3Val').innerText = muS.toFixed(2);
        document.getElementById('fricParam4Val').innerText = F.toFixed(0) + ' N';
        document.getElementById('fricMet1Val').innerText = F_max.toFixed(1) + ' N';
        document.getElementById('fricMet2Val').innerText = a_max.toFixed(2) + ' m/s²';
        document.getElementById('fricMet3Val').innerText = F.toFixed(0) + ' N';

        if (!isSlipping) {
          const aCommon = F / (m1 + m2);
          document.getElementById('fricStateVal').innerText = `✓ NO RELATIVE SLIP: F ≤ F_max => Both blocks move together at ${aCommon.toFixed(2)} m/s²`;
          document.getElementById('fricStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('fricLiveBadge').innerText = "Locked Motion (F ≤ F_max)";
        } else {
          const a1 = muS * g;
          const a2 = (F - muS * m1 * g) / m2;
          document.getElementById('fricStateVal').innerText = `★ RELATIVE SLIPPING ACTIVE: Bottom block outpaces top (a2=${a2.toFixed(1)} > a1=${a1.toFixed(1)})`;
          document.getElementById('fricStateVal').className = "text-xs font-bold text-rose-400 mt-1";
          document.getElementById('fricLiveBadge').innerText = "Relative Slip Active!";
        }
      }
      drawFrictionCanvas();
    }

    function drawFrictionCanvas() {
      resizeCanvas(fCanvas);
      const w = fCanvas.width / (window.devicePixelRatio || 1);
      const h = fCanvas.height / (window.devicePixelRatio || 1);
      if (!w || !h) return;
      fCtx.clearRect(0, 0, w, h);

      const cx = w / 2;
      const cy = h / 2 + 10;
      const g = 9.8;

      if (currentFrictionConcept === 'graph') {
        const muS = parseFloat(document.getElementById('fricSlider1').value);
        const muK = Math.min(muS - 0.05, parseFloat(document.getElementById('fricSlider2').value));
        const F_app = parseFloat(document.getElementById('fricSlider3').value);
        const m = parseFloat(document.getElementById('fricSlider4').value);
        const fs_max = muS * m * g;
        const fk = muK * m * g;

        // TOP HALF: Physical Sliding Block on Textured Surface
        const floorY = cy - 45;
        // Surface roughness ridges scale with static friction muS!
        fCtx.strokeStyle = '#475569';
        fCtx.lineWidth = 2.5;
        fCtx.beginPath();
        fCtx.moveTo(cx - 200, floorY);
        fCtx.lineTo(cx + 200, floorY);
        fCtx.stroke();

        const ridgeStep = Math.max(8, 24 - muS * 16);
        for (let x = cx - 190; x <= cx + 190; x += ridgeStep) {
          fCtx.beginPath();
          fCtx.moveTo(x, floorY);
          fCtx.lineTo(x - 6, floorY + 8 * muS);
          fCtx.strokeStyle = muS > 0.6 ? '#f59e0b' : '#38bdf8';
          fCtx.stroke();
        }

        // Block dimensions visibly scale with mass m!
        const bW = 45 + Math.sqrt(m) * 8.5;
        const bH = 35 + Math.sqrt(m) * 6;
        const bx = cx - bW / 2 + slideX;
        const by = floorY - bH;

        fCtx.fillStyle = '#1e293b';
        fCtx.strokeStyle = F_app > fs_max ? '#f59e0b' : '#38bdf8';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(bx, by, bW, bH);
        fCtx.strokeRect(bx, by, bW, bH);

        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 12px Consolas, monospace';
        fCtx.fillText(`m=${m.toFixed(1)}kg`, bx + 10, by + bH / 2 + 4);

        // Pull arrow
        if (F_app > 0) {
          const pLen = Math.min(85, 15 + F_app * 0.6);
          drawArrow(fCtx, bx + bW, by + bH / 2, bx + bW + pLen, by + bH / 2, '#FACC15', `F=${F_app}N`, 10);
        }

        // Opposing friction arrow
        const actFric = F_app <= fs_max ? F_app : fk;
        if (actFric > 0) {
          const fLen = Math.min(85, 15 + actFric * 0.6);
          drawArrow(fCtx, bx, by + bH - 10, bx - fLen, by + bH - 10, '#F43F5E', `f=${actFric.toFixed(0)}N`, 10);
        }

        // Sliding Sparks when F_app > fs_max
        if (F_app > fs_max) {
          fCtx.fillStyle = '#facc15';
          for (let p = 0; p < 6; p++) {
            const px = bx - Math.random() * 25;
            const py = floorY - Math.random() * 8;
            fCtx.fillRect(px, py, 2, 2);
          }
        }

        // BOTTOM HALF: Dynamic Friction Graph
        const ox = 75;
        const oy = h - 35;
        const gw = w - 150;
        const gh = 90;

        fCtx.strokeStyle = '#475569';
        fCtx.lineWidth = 2;
        fCtx.beginPath();
        fCtx.moveTo(ox, oy);
        fCtx.lineTo(ox + gw, oy);
        fCtx.moveTo(ox, oy);
        fCtx.lineTo(ox, oy - gh);
        fCtx.stroke();

        fCtx.fillStyle = '#94a3b8';
        fCtx.font = '10px Consolas, monospace';
        fCtx.fillText('Applied Force F →', ox + gw - 80, oy + 20);
        fCtx.fillText('Friction f ↑', ox - 50, oy - gh + 10);

        // Graph heights scale dynamically with fs_max and fk!
        const maxGraphF = 150;
        const peakX = ox + gw * (fs_max / maxGraphF);
        const peakY = oy - gh * (fs_max / maxGraphF);
        const dropY = oy - gh * (fk / maxGraphF);

        // Static Region (45 deg line)
        fCtx.strokeStyle = '#38bdf8';
        fCtx.lineWidth = 3;
        fCtx.beginPath();
        fCtx.moveTo(ox, oy);
        fCtx.lineTo(peakX, peakY);
        fCtx.stroke();

        // Kinetic Region (drop and horizontal plateau)
        fCtx.strokeStyle = '#f59e0b';
        fCtx.beginPath();
        fCtx.moveTo(peakX, peakY);
        fCtx.lineTo(peakX + 10, dropY);
        fCtx.lineTo(ox + gw, dropY);
        fCtx.stroke();

        // Peak Label
        fCtx.fillStyle = '#38bdf8';
        fCtx.font = 'bold 10px Consolas, monospace';
        fCtx.fillText(`Peak f_s,max=${fs_max.toFixed(0)}N`, peakX - 30, peakY - 8);

        // Live Operating Tracker Ball on Graph
        const curPlotF = Math.min(maxGraphF, F_app);
        let curX, curY;
        if (F_app <= fs_max) {
          curX = ox + (F_app / fs_max) * (peakX - ox);
          curY = oy - (F_app / fs_max) * (oy - peakY);
        } else {
          curX = Math.min(ox + gw, peakX + 10 + ((F_app - fs_max) / (maxGraphF - fs_max)) * (gw - (peakX - ox)));
          curY = dropY;
        }

        fCtx.fillStyle = F_app > fs_max ? '#f59e0b' : '#4ade80';
        fCtx.beginPath();
        fCtx.arc(curX, curY, 6, 0, Math.PI * 2);
        fCtx.fill();
        fCtx.strokeStyle = '#ffffff';
        fCtx.lineWidth = 1.5;
        fCtx.stroke();

      } else if (currentFrictionConcept === 'incline') {
        const theta = parseFloat(document.getElementById('fricSlider1').value);
        const muS = parseFloat(document.getElementById('fricSlider2').value);
        const muK = Math.min(muS - 0.05, parseFloat(document.getElementById('fricSlider3').value));
        const m = parseFloat(document.getElementById('fricSlider4').value);
        const rad = theta * Math.PI / 180;
        const thetaR = Math.atan(muS) * 180 / Math.PI;
        const radR = thetaR * Math.PI / 180;
        const rampLen = Math.min(340, w * 0.58);

        // Incline coordinates: base at bottom, tilted up to left
        const rx = cx - rampLen / 2;
        const ry = cy + 70;
        const topX = rx;
        const topY = ry - rampLen * Math.sin(rad);
        const botX = rx + rampLen * Math.cos(rad);
        const botY = ry;

        // Incline Wedge
        fCtx.strokeStyle = '#38bdf8';
        fCtx.lineWidth = 3;
        fCtx.beginPath();
        fCtx.moveTo(rx, ry);
        fCtx.lineTo(topX, topY);
        fCtx.lineTo(botX, botY);
        fCtx.closePath();
        fCtx.fillStyle = 'rgba(30, 41, 59, 0.45)';
        fCtx.fill();
        fCtx.stroke();

        // Distinct Repose Angle Guide Line: Directly shifts when muS slider moves!
        const reposeTopX = rx;
        const reposeTopY = ry - rampLen * Math.sin(radR);
        const reposeBotX = rx + rampLen * Math.cos(radR);
        fCtx.strokeStyle = '#facc15';
        fCtx.lineWidth = 2;
        fCtx.setLineDash([5, 5]);
        fCtx.beginPath();
        fCtx.moveTo(rx, ry);
        fCtx.lineTo(reposeBotX, ry);
        fCtx.lineTo(reposeTopX, reposeTopY);
        fCtx.closePath();
        fCtx.stroke();
        fCtx.setLineDash([]);

        fCtx.fillStyle = '#facc15';
        fCtx.font = 'bold 11px Consolas, monospace';
        fCtx.fillText(`★ Repose Guide θ_R = ${thetaR.toFixed(1)}°`, rx + 20, ry + 22);

        // Current Angle Arc θ
        fCtx.strokeStyle = '#38bdf8';
        fCtx.beginPath();
        fCtx.arc(botX, botY, 40, Math.PI, Math.PI - rad, false);
        fCtx.stroke();
        fCtx.fillStyle = '#38bdf8';
        fCtx.font = 'bold 12px Consolas, monospace';
        fCtx.fillText(`θ=${theta}°`, botX - 70, botY - 10);

        // Block on the slope (d measured down from top apex)
        const isSliding = theta > thetaR;
        const bSide = 30 + Math.sqrt(m) * 6;
        const d = (rampLen * 0.25) + (isSliding ? inclineBlockPos : 0);
        const bx = topX + d * Math.cos(rad);
        const by = topY + d * Math.sin(rad);

        fCtx.save();
        fCtx.translate(bx, by);
        fCtx.rotate(rad);
        fCtx.fillStyle = isSliding ? '#f59e0b' : '#1e293b';
        fCtx.strokeStyle = isSliding ? '#F43F5E' : '#4ade80';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(-bSide / 2, -bSide, bSide, bSide);
        fCtx.strokeRect(-bSide / 2, -bSide, bSide, bSide);

        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 11px Consolas, monospace';
        fCtx.fillText(`m=${m.toFixed(1)}kg`, -bSide / 2 + 4, -bSide / 2 + 4);

        // Friction arrow pointing UP the slope
        const fArrowLen = isSliding ? Math.min(50, 15 + muK * 40) : Math.min(50, 15 + Math.sin(rad) * 45);
        drawArrow(fCtx, 0, -bSide / 2, -fArrowLen, -bSide / 2, '#F43F5E', 'f_friction', 10);
        fCtx.restore();

        // Normal Force N (Perpendicular to slope)
        const nLen = Math.min(70, 20 + m * Math.cos(rad) * 4);
        drawArrow(fCtx, bx, by, bx + Math.sin(rad) * nLen, by - Math.cos(rad) * nLen, '#4ADE80', 'N', 10);

        // Gravity W = mg (Straight Down)
        const gLen = Math.min(80, 25 + m * 4);
        drawArrow(fCtx, bx, by, bx, by + gLen, '#F43F5E', 'mg', 10);

      } else if (currentFrictionConcept === 'twoblock') {
        const m1 = parseFloat(document.getElementById('fricSlider1').value);
        const m2 = parseFloat(document.getElementById('fricSlider2').value);
        const muS = parseFloat(document.getElementById('fricSlider3').value);
        const F = parseFloat(document.getElementById('fricSlider4').value);
        const a_max = muS * g;
        const F_max = (m1 + m2) * a_max;
        const isSlipping = F > F_max;

        const floorY = cy + 60;
        fCtx.strokeStyle = '#475569';
        fCtx.lineWidth = 2.5;
        fCtx.beginPath();
        fCtx.moveTo(cx - 200, floorY);
        fCtx.lineTo(cx + 200, floorY);
        fCtx.stroke();

        // Bottom Block m2 (Blue) - Scales with m2!
        const b2W = 100 + Math.sqrt(m2) * 14;
        const b2H = 45;
        const b2X = cx - b2W / 2 + twoBlockX;
        const b2Y = floorY - b2H;

        fCtx.fillStyle = '#1e293b';
        fCtx.strokeStyle = '#38bdf8';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(b2X, b2Y, b2W, b2H);
        fCtx.strokeRect(b2X, b2Y, b2W, b2H);
        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 12px Consolas, monospace';
        fCtx.fillText(`Bottom m2 (${m2.toFixed(1)}kg)`, b2X + 10, b2Y + 28);

        // Pull arrow F on bottom block
        if (F > 0) {
          const fLen = Math.min(90, 15 + F * 0.6);
          drawArrow(fCtx, b2X + b2W, b2Y + b2H / 2, b2X + b2W + fLen, b2Y + b2H / 2, '#FACC15', `F=${F}N`, 11);
        }

        // Top Block m1 (Amber) - Scales with m1!
        const b1W = 60 + Math.sqrt(m1) * 12;
        const b1H = 38;
        // Top block lags behind when slipping!
        const b1X = b2X + (b2W - b1W) / 2 - (isSlipping ? twoBlockRelSlip : 0);
        const b1Y = b2Y - b1H;

        fCtx.fillStyle = '#334155';
        fCtx.strokeStyle = isSlipping ? '#F43F5E' : '#facc15';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(b1X, b1Y, b1W, b1H);
        fCtx.strokeRect(b1X, b1Y, b1W, b1H);
        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 11px Consolas, monospace';
        fCtx.fillText(`Top m1 (${m1.toFixed(1)}kg)`, b1X + 8, b1Y + 23);

        // Interface Roughness & Sparks when Slipping
        fCtx.strokeStyle = isSlipping ? '#F43F5E' : '#4ADE80';
        fCtx.lineWidth = 2;
        fCtx.beginPath();
        fCtx.moveTo(b1X, b2Y);
        fCtx.lineTo(b1X + b1W, b2Y);
        fCtx.stroke();

        if (isSlipping) {
          fCtx.fillStyle = '#F43F5E';
          fCtx.font = 'bold 12px Consolas, monospace';
          fCtx.fillText('★ RELATIVE SLIPPING ACTIVE! (F > F_max) ★', cx - 120, cy - 65);

          // Friction sparks at interface
          fCtx.fillStyle = '#facc15';
          for (let p = 0; p < 8; p++) {
            const sx = b1X + Math.random() * b1W;
            const sy = b2Y + (Math.random() * 4 - 2);
            fCtx.fillRect(sx, sy, 2, 2);
          }
        } else {
          fCtx.fillStyle = '#4ADE80';
          fCtx.font = 'bold 12px Consolas, monospace';
          fCtx.fillText('✓ LOCKED TOGETHER (F ≤ F_max)', cx - 90, cy - 65);
        }

        // Live Slip Threshold Meter Bar
        const barW = 160;
        const barH = 10;
        const barX = cx - barW / 2;
        const barY = cy - 45;
        fCtx.fillStyle = '#1e293b';
        fCtx.fillRect(barX, barY, barW, barH);
        fCtx.strokeStyle = '#475569';
        fCtx.strokeRect(barX, barY, barW, barH);

        const fillRatio = Math.min(1.0, F / (F_max * 1.5 || 1));
        fCtx.fillStyle = isSlipping ? '#F43F5E' : '#4ADE80';
        fCtx.fillRect(barX, barY, barW * fillRatio, barH);

        // Threshold Notch
        const notchX = barX + barW * (F_max / (F_max * 1.5));
        fCtx.strokeStyle = '#facc15';
        fCtx.lineWidth = 2;
        fCtx.beginPath();
        fCtx.moveTo(notchX, barY - 3);
        fCtx.lineTo(notchX, barY + barH + 3);
        fCtx.stroke();
        fCtx.fillStyle = '#facc15';
        fCtx.font = '10px Consolas, monospace';
        fCtx.fillText('F_max', notchX - 12, barY - 6);
      }
    }

    // ========================================================
    // ENGINE 3: MOMENTUM & IMPULSE
    // ========================================================
    let ballX = 140;
    let ballV = -15;
    let ballDeform = 1.0;
    let rocketAlt = 0;

    function setMomentumConcept(sub) {
      currentMomentumConcept = sub;
      document.getElementById('subMomImpulseBtn').className = sub === 'impulse' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subMomRocketBtn').className = sub === 'rocket' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subMomLamiBtn').className = sub === 'lami' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      const s1 = document.getElementById('momSlider1');
      const s2 = document.getElementById('momSlider2');
      const s3 = document.getElementById('momSlider3');

      if (sub === 'impulse') {
        document.getElementById('momHeader').innerText = "CONCEPT 4 • IMPULSE & MOMENTUM";
        document.getElementById('momTitle').innerText = "Area Under F-t Curve = Δp";
        document.getElementById('momFormula').innerText = "J = ∫F dt = Δp = m·(v_f - v_i) = 2mv";
        document.getElementById('momParam1Label').innerText = "Approach Speed (v):";
        document.getElementById('momParam2Label').innerText = "Ball Mass (m):";
        document.getElementById('momParam3Label').innerText = "Contact Duration (Δt):";
        document.getElementById('momMet1Label').innerText = "Initial Momentum (p_i):";
        document.getElementById('momMet2Label').innerText = "Rebound Momentum (p_f):";
        document.getElementById('momMet3Label').innerText = "Total Impulse J = Δp:";
        document.getElementById('momActionLabel').innerText = "Re-fire Ball Impact";
        s1.min = 5; s1.max = 35; s1.step = 1; s1.value = 15;
        s2.min = 0.10; s2.max = 2.50; s2.step = 0.05; s2.value = 0.50;
        s3.min = 0.005; s3.max = 0.050; s3.step = 0.005; s3.value = 0.020;
      } else if (sub === 'rocket') {
        document.getElementById('momHeader').innerText = "CONCEPT 5 • CONSERVATION OF MOMENTUM";
        document.getElementById('momTitle').innerText = "Rocket Thrust & Propulsion Dynamics";
        document.getElementById('momFormula').innerText = "F_thrust = u·(dm/dt) • a = (u/m)(dm/dt) - g";
        document.getElementById('momParam1Label').innerText = "Exhaust Velocity u (m/s):";
        document.getElementById('momParam2Label').innerText = "Fuel Burn dm/dt (kg/s):";
        document.getElementById('momParam3Label').innerText = "Rocket Mass M (kg):";
        document.getElementById('momMet1Label').innerText = "Upward Thrust Force:";
        document.getElementById('momMet2Label').innerText = "Rocket Gravity W=Mg:";
        document.getElementById('momMet3Label').innerText = "Net Acceleration (a):";
        document.getElementById('momActionLabel').innerText = "Ignite Boost Thrust";
        s1.min = 1000; s1.max = 4000; s1.step = 100; s1.value = 2200;
        s2.min = 5; s2.max = 60; s2.step = 2; s2.value = 20;
        s3.min = 200; s3.max = 1500; s3.step = 50; s3.value = 500;
      } else if (sub === 'lami') {
        document.getElementById('momHeader').innerText = "CONCEPT 6 • LAMI'S THEOREM";
        document.getElementById('momTitle').innerText = "Equilibrium of Three Concurrent Forces";
        document.getElementById('momFormula').innerText = "F1 / sin α = F2 / sin β = F3 / sin γ";
        document.getElementById('momParam1Label').innerText = "Force F1 (N):";
        document.getElementById('momParam2Label').innerText = "Angle α (between F2-F3):";
        document.getElementById('momParam3Label').innerText = "Angle β (between F1-F3):";
        document.getElementById('momMet1Label').innerText = "Computed Force F2:";
        document.getElementById('momMet2Label').innerText = "Computed Force F3:";
        document.getElementById('momMet3Label').innerText = "Third Angle γ:";
        document.getElementById('momActionLabel').innerText = "Symmetric 120° Balance";
        s1.min = 10; s1.max = 120; s1.step = 2; s1.value = 50;
        s2.min = 100; s2.max = 160; s2.step = 2; s2.value = 125;
        s3.min = 100; s3.max = 160; s3.step = 2; s3.value = 115;
      }
      updateMomentum();
    }

    function triggerMomentumAction() {
      if (currentMomentumConcept === 'impulse') {
        ballX = 140;
        ballV = -Math.abs(parseFloat(document.getElementById('momSlider1').value));
        ballDeform = 1.0;
      } else if (currentMomentumConcept === 'rocket') {
        document.getElementById('momSlider2').value = 45;
        updateMomentum();
      } else if (currentMomentumConcept === 'lami') {
        document.getElementById('momSlider2').value = 120;
        document.getElementById('momSlider3').value = 120;
        updateMomentum();
      }
    }

    function updateMomentum() {
      const s1 = parseFloat(document.getElementById('momSlider1').value);
      const s2 = parseFloat(document.getElementById('momSlider2').value);
      const s3 = parseFloat(document.getElementById('momSlider3').value);

      if (currentMomentumConcept === 'impulse') {
        const v = s1;
        const m = s2;
        const dt = s3;
        const p_i = m * v;
        const p_f = -m * v;
        const J = 2 * m * v;
        const F_avg = J / dt;

        document.getElementById('momParam1Val').innerText = v.toFixed(1) + ' m/s';
        document.getElementById('momParam2Val').innerText = m.toFixed(2) + ' kg';
        document.getElementById('momParam3Val').innerText = dt.toFixed(3) + ' s';
        document.getElementById('momMet1Val').innerText = '+' + p_i.toFixed(2) + ' kg·m/s';
        document.getElementById('momMet2Val').innerText = p_f.toFixed(2) + ' kg·m/s';
        document.getElementById('momMet3Val').innerText = J.toFixed(2) + ' N·s (Doubled)';
        document.getElementById('momStateVal').innerText = `F_avg = ${F_avg.toFixed(0)} N • Shorter Δt => Greater Impact Force`;
        document.getElementById('momLiveBadge').innerText = `Impulse Active (J = ${J.toFixed(1)} N·s)`;
      } else if (currentMomentumConcept === 'rocket') {
        const u = s1;
        const dmdt = s2;
        const M = s3;
        const F_thrust = u * dmdt;
        const W = M * 9.8;
        const a_net = Math.max(0, (F_thrust - W) / M);

        document.getElementById('momParam1Val').innerText = u.toFixed(0) + ' m/s';
        document.getElementById('momParam2Val').innerText = dmdt.toFixed(0) + ' kg/s';
        document.getElementById('momParam3Val').innerText = M.toFixed(0) + ' kg';
        document.getElementById('momMet1Val').innerText = F_thrust.toFixed(0) + ' N';
        document.getElementById('momMet2Val').innerText = W.toFixed(0) + ' N';
        document.getElementById('momMet3Val').innerText = a_net.toFixed(2) + ' m/s²';

        if (F_thrust > W) {
          document.getElementById('momStateVal').innerText = `★ LIFT-OFF SUCCESS: Thrust (${F_thrust.toFixed(0)}N) > Weight (${W.toFixed(0)}N) => a = ${a_net.toFixed(2)} m/s²`;
          document.getElementById('momStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('momLiveBadge').innerText = `Rocket Accelerating (${a_net.toFixed(1)} m/s²)`;
        } else {
          document.getElementById('momStateVal').innerText = `ANCHORED ON PAD: Thrust (${F_thrust.toFixed(0)}N) ≤ Weight (${W.toFixed(0)}N) => Insufficient Thrust`;
          document.getElementById('momStateVal').className = "text-xs font-bold text-rose-400 mt-1";
          document.getElementById('momLiveBadge').innerText = "Rocket On Launchpad";
        }
      } else if (currentMomentumConcept === 'lami') {
        const F1 = s1;
        const alpha = s2 * Math.PI / 180;
        const beta = s3 * Math.PI / 180;
        const gamma = 2 * Math.PI - (alpha + beta);
        const gammaDeg = 360 - (s2 + s3);

        const F2 = Math.abs(F1 * Math.sin(beta) / Math.sin(alpha));
        const F3 = Math.abs(F1 * Math.sin(gamma) / Math.sin(alpha));

        document.getElementById('momParam1Val').innerText = F1.toFixed(0) + ' N';
        document.getElementById('momParam2Val').innerText = s2.toFixed(0) + '°';
        document.getElementById('momParam3Val').innerText = s3.toFixed(0) + '°';
        document.getElementById('momMet1Val').innerText = F2.toFixed(1) + ' N';
        document.getElementById('momMet2Val').innerText = F3.toFixed(1) + ' N';
        document.getElementById('momMet3Val').innerText = gammaDeg.toFixed(0) + '°';

        document.getElementById('momStateVal').innerText = "✓ EQUILIBRIUM: F1/sinα = F2/sinβ = F3/sinγ => ΣF = 0 (Closed Triangle)";
        document.getElementById('momStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
        document.getElementById('momLiveBadge').innerText = "Lami's Equilibrium (ΣF = 0)";
      }
      drawMomentumCanvas();
    }

    function drawMomentumCanvas() {
      resizeCanvas(mCanvas);
      const w = mCanvas.width / (window.devicePixelRatio || 1);
      const h = mCanvas.height / (window.devicePixelRatio || 1);
      if (!w || !h) return;
      mCtx.clearRect(0, 0, w, h);

      const cx = w / 2;
      const cy = h / 2 + 10;

      if (currentMomentumConcept === 'impulse') {
        const v = parseFloat(document.getElementById('momSlider1').value);
        const m = parseFloat(document.getElementById('momSlider2').value);
        const dt = parseFloat(document.getElementById('momSlider3').value);
        const J = 2 * m * v;
        const F_peak = (2 * J) / dt;

        // Rigid Wall on Left
        const wallX = 75;
        mCtx.fillStyle = '#334155';
        mCtx.fillRect(wallX - 22, cy - 85, 22, 170);
        mCtx.strokeStyle = '#94a3b8';
        mCtx.lineWidth = 2.5;
        mCtx.strokeRect(wallX - 22, cy - 85, 22, 170);

        // Elastic Cushion on Wall
        mCtx.fillStyle = '#0ea5e9';
        mCtx.fillRect(wallX - 4, cy - 75, 4, 150);

        // Wall Pressure Gauge Needle
        const gaugeR = 16;
        const gx = wallX - 11;
        const gy = cy - 50;
        mCtx.fillStyle = '#0f172a';
        mCtx.beginPath();
        mCtx.arc(gx, gy, gaugeR, 0, Math.PI * 2);
        mCtx.fill();
        mCtx.strokeStyle = '#64748b';
        mCtx.stroke();

        const needleAngle = -Math.PI / 2 + (ballDeform < 0.9 ? 1.5 : 0.2);
        mCtx.strokeStyle = ballDeform < 0.9 ? '#F43F5E' : '#4ADE80';
        mCtx.lineWidth = 2;
        mCtx.beginPath();
        mCtx.moveTo(gx, gy);
        mCtx.lineTo(gx + gaugeR * Math.cos(needleAngle), gy + gaugeR * Math.sin(needleAngle));
        mCtx.stroke();

        // Elastic Ball with Squash: Radius scales with mass m!
        const bRad = 15 + m * 11;
        const ballActualX = wallX + bRad * ballDeform + ballX;

        mCtx.save();
        mCtx.translate(ballActualX, cy);
        mCtx.scale(ballDeform, 1 / Math.sqrt(ballDeform || 1));
        mCtx.fillStyle = ballDeform < 0.9 ? '#F43F5E' : '#38bdf8';
        mCtx.beginPath();
        mCtx.arc(0, 0, bRad, 0, Math.PI * 2);
        mCtx.fill();
        mCtx.strokeStyle = '#ffffff';
        mCtx.lineWidth = 2;
        mCtx.stroke();
        mCtx.restore();

        // Ball Velocity Vector
        if (ballV < 0) {
          drawArrow(mCtx, ballActualX, cy - bRad - 12, ballActualX - 45, cy - bRad - 12, '#38bdf8', `+v (${v}m/s)`, 10);
        } else {
          drawArrow(mCtx, ballActualX, cy - bRad - 12, ballActualX + 45, cy - bRad - 12, '#F43F5E', `-v (Rebound)`, 10);
        }

        // F-t Curve on Right Side
        const ox = cx + 25;
        const oy = cy + 60;
        const gw = w - ox - 35;
        const gh = 115;

        mCtx.strokeStyle = '#475569';
        mCtx.lineWidth = 2;
        mCtx.beginPath();
        mCtx.moveTo(ox, oy);
        mCtx.lineTo(ox + gw, oy);
        mCtx.moveTo(ox, oy);
        mCtx.lineTo(ox, oy - gh);
        mCtx.stroke();

        mCtx.fillStyle = '#94a3b8';
        mCtx.font = '10px Consolas, monospace';
        mCtx.fillText('Time (t) →', ox + gw - 60, oy + 18);
        mCtx.fillText('Force F(t) ↑', ox - 20, oy - gh - 8);

        // Curve dimensions scale with dt and F_peak!
        const pWidth = Math.min(gw * 0.75, (dt / 0.05) * gw * 0.65 + 25);
        const pHeight = Math.min(gh * 0.85, (F_peak / 3000) * gh * 0.75 + 20);
        const pStart = ox + gw * 0.15;
        const pMid = pStart + pWidth / 2;
        const pEnd = pStart + pWidth;

        mCtx.fillStyle = ballDeform < 0.9 ? 'rgba(244, 63, 94, 0.45)' : 'rgba(74, 222, 128, 0.25)';
        mCtx.strokeStyle = ballDeform < 0.9 ? '#F43F5E' : '#4ade80';
        mCtx.lineWidth = 2.5;
        mCtx.beginPath();
        mCtx.moveTo(pStart, oy);
        mCtx.lineTo(pMid, oy - pHeight);
        mCtx.lineTo(pEnd, oy);
        mCtx.closePath();
        mCtx.fill();
        mCtx.stroke();

        mCtx.fillStyle = '#4ade80';
        mCtx.font = 'bold 11px Consolas, monospace';
        mCtx.fillText(`Area = J = Δp = ${J.toFixed(1)} N·s`, pMid - 55, oy - pHeight / 2);

      } else if (currentMomentumConcept === 'rocket') {
        const u = parseFloat(document.getElementById('momSlider1').value);
        const dmdt = parseFloat(document.getElementById('momSlider2').value);
        const M = parseFloat(document.getElementById('momSlider3').value);
        const F_thrust = u * dmdt;
        const W = M * 9.8;
        const a_net = Math.max(0, (F_thrust - W) / M);

        const rX = cx;
        const rY = cy + 50 - rocketAlt;

        // Exhaust Flame Plume: Scales prominently with F_thrust!
        const flameLen = Math.min(95, 20 + (F_thrust / 180000) * 85);
        const flameW = Math.min(36, 12 + (dmdt / 60) * 24);

        // Multi-layer Rocket Plume
        mCtx.fillStyle = '#f97316';
        mCtx.beginPath();
        mCtx.moveTo(rX - flameW / 2, rY + 45);
        mCtx.lineTo(rX + flameW / 2, rY + 45);
        mCtx.lineTo(rX, rY + 45 + flameLen);
        mCtx.closePath();
        mCtx.fill();

        // Inner hot core
        mCtx.fillStyle = '#fef08a';
        mCtx.beginPath();
        mCtx.moveTo(rX - flameW / 4, rY + 45);
        mCtx.lineTo(rX + flameW / 4, rY + 45);
        mCtx.lineTo(rX, rY + 45 + flameLen * 0.6);
        mCtx.closePath();
        mCtx.fill();

        // Rocket Body: Fuselage width & height scale with mass M!
        const rockW = 34 + Math.sqrt(M) * 1.8;
        const rockH = 85 + Math.sqrt(M) * 2.2;

        mCtx.fillStyle = '#1e293b';
        mCtx.strokeStyle = F_thrust > W ? '#38bdf8' : '#94a3b8';
        mCtx.lineWidth = 2.5;
        mCtx.beginPath();
        mCtx.moveTo(rX, rY - rockH / 2 - 25); // nose cone
        mCtx.lineTo(rX + rockW / 2, rY - rockH / 2);
        mCtx.lineTo(rX + rockW / 2, rY + rockH / 2);
        mCtx.lineTo(rX - rockW / 2, rY + rockH / 2);
        mCtx.lineTo(rX - rockW / 2, rY - rockH / 2);
        mCtx.closePath();
        mCtx.fill();
        mCtx.stroke();

        // Rocket Fins
        mCtx.fillStyle = '#0ea5e9';
        mCtx.beginPath();
        mCtx.moveTo(rX - rockW / 2, rY + rockH / 2 - 20);
        mCtx.lineTo(rX - rockW / 2 - 16, rY + rockH / 2 + 10);
        mCtx.lineTo(rX - rockW / 2, rY + rockH / 2);
        mCtx.closePath();
        mCtx.fill();

        mCtx.beginPath();
        mCtx.moveTo(rX + rockW / 2, rY + rockH / 2 - 20);
        mCtx.lineTo(rX + rockW / 2 + 16, rY + rockH / 2 + 10);
        mCtx.lineTo(rX + rockW / 2, rY + rockH / 2);
        mCtx.closePath();
        mCtx.fill();

        // Thrust and Weight Vectors
        drawArrow(mCtx, rX + rockW / 2 + 30, rY, rX + rockW / 2 + 30, rY - 60, '#38bdf8', `Thrust=${(F_thrust / 1000).toFixed(0)}kN`, 11);
        drawArrow(mCtx, rX - rockW / 2 - 30, rY, rX - rockW / 2 - 30, rY + 60, '#F43F5E', `W=${(W / 1000).toFixed(0)}kN`, 11);

      } else if (currentMomentumConcept === 'lami') {
        const F1 = parseFloat(document.getElementById('momSlider1').value);
        const alpha = parseFloat(document.getElementById('momSlider2').value) * Math.PI / 180;
        const beta = parseFloat(document.getElementById('momSlider3').value) * Math.PI / 180;
        const gamma = 2 * Math.PI - (alpha + beta);
        const F2 = Math.abs(F1 * Math.sin(beta) / Math.sin(alpha));
        const F3 = Math.abs(F1 * Math.sin(gamma) / Math.sin(alpha));

        const knotX = cx - 75;
        // Central Ring of Force Table
        mCtx.strokeStyle = '#94a3b8';
        mCtx.lineWidth = 1.5;
        mCtx.setLineDash([4, 4]);
        mCtx.beginPath();
        mCtx.arc(knotX, cy, 75, 0, Math.PI * 2);
        mCtx.stroke();
        mCtx.setLineDash([]);

        mCtx.fillStyle = '#38bdf8';
        mCtx.beginPath();
        mCtx.arc(knotX, cy, 6, 0, Math.PI * 2);
        mCtx.fill();

        // F1 (Upward)
        const l1 = Math.min(85, 20 + F1 * 0.65);
        drawArrow(mCtx, knotX, cy, knotX, cy - l1, '#38bdf8', `F1=${F1.toFixed(0)}N`, 11);

        // F2
        const ang2 = -Math.PI / 2 + beta;
        const l2 = Math.min(85, 20 + F2 * 0.65);
        drawArrow(mCtx, knotX, cy, knotX + l2 * Math.cos(ang2), cy + l2 * Math.sin(ang2), '#facc15', `F2=${F2.toFixed(0)}N`, 11);

        // F3
        const ang3 = -Math.PI / 2 - (2 * Math.PI - (beta + alpha));
        const l3 = Math.min(85, 20 + F3 * 0.65);
        drawArrow(mCtx, knotX, cy, knotX + l3 * Math.cos(ang3), cy + l3 * Math.sin(ang3), '#F43F5E', `F3=${F3.toFixed(0)}N`, 11);

        // Closed Vector Triangle on Right
        const tx = cx + 70;
        const ty = cy - 35;
        mCtx.strokeStyle = '#4ade80';
        mCtx.lineWidth = 2.5;
        mCtx.beginPath();
        mCtx.moveTo(tx, ty);
        mCtx.lineTo(tx, ty + l1 * 0.65);
        mCtx.lineTo(tx + 55, ty + l1 * 0.65 + 20);
        mCtx.closePath();
        mCtx.stroke();

        mCtx.fillStyle = '#4ade80';
        mCtx.font = 'bold 11px Consolas, monospace';
        mCtx.fillText('Closed Vector Triangle', tx - 20, ty + l1 * 0.65 + 40);
        mCtx.fillText('Σ F = 0 (Equilibrium)', tx - 15, ty + l1 * 0.65 + 56);
      }
    }

    // ========================================================
    // ENGINE 4: CIRCULAR DYNAMICS & BANKING
    // ========================================================
    let circCarAngle = 0;
    let loopCarAngle = 0;

    function setCircConcept(sub) {
      currentCircConcept = sub;
      document.getElementById('subCircFlatBtn').className = sub === 'flat' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subCircBankedBtn').className = sub === 'banked' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subCircLoopBtn').className = sub === 'loop' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      const s1 = document.getElementById('circSlider1');
      const s2 = document.getElementById('circSlider2');
      const s3 = document.getElementById('circSlider3');
      const s4 = document.getElementById('circSlider4');
      const b3 = document.getElementById('circBlock3');
      const b4 = document.getElementById('circBlock4');

      if (sub === 'flat') {
        document.getElementById('circHeader').innerText = "CONCEPT 10 • LEVEL CIRCULAR ROAD";
        document.getElementById('circTitle').innerText = "Static Friction Supplies Centripetal Force";
        document.getElementById('circFormula').innerText = "f_s = m·v²/r ≤ μ_s·m·g => v_max = √(μ_s·r·g)";
        document.getElementById('circParam1Label').innerText = "Turn Radius (r):";
        document.getElementById('circParam2Label').innerText = "Road Friction (μ_s):";
        document.getElementById('circParam3Label').innerText = "Car Speed (v):";
        document.getElementById('circMet1Label').innerText = "Max Safe Speed (v_max):";
        document.getElementById('circMet2Label').innerText = "Current Velocity:";
        document.getElementById('circMet3Label').innerText = "Tire Grip Margin:";
        document.getElementById('circActionLabel').innerText = "Speed Up to Drift";
        b3.classList.remove('hidden');
        b4.classList.add('hidden');
        s1.min = 20; s1.max = 150; s1.step = 5; s1.value = 50;
        s2.min = 0.10; s2.max = 0.90; s2.step = 0.05; s2.value = 0.50;
        s3.min = 10; s3.max = 150; s3.step = 2; s3.value = 50;
      } else if (sub === 'banked') {
        document.getElementById('circHeader').innerText = "CONCEPT 11 • ENGINEERED BANKED ROAD";
        document.getElementById('circTitle').innerText = "Optimal Speed & Normal Reaction Component";
        document.getElementById('circFormula').innerText = "v_opt = √(rg·tanθ) • v_max = √[rg(tanθ+μ)/(1-μ·tanθ)]";
        document.getElementById('circParam1Label').innerText = "Turn Radius (r):";
        document.getElementById('circParam2Label').innerText = "Road Friction (μ):";
        document.getElementById('circParam3Label').innerText = "Car Speed (v):";
        document.getElementById('circParam4Label').innerText = "Banking Angle (θ):";
        document.getElementById('circMet1Label').innerText = "Optimal Speed (v_opt):";
        document.getElementById('circMet2Label').innerText = "Max Speed w/ Friction:";
        document.getElementById('circMet3Label').innerText = "Lateral Friction Force:";
        document.getElementById('circActionLabel').innerText = "Set to Optimal Speed";
        b3.classList.remove('hidden');
        b4.classList.remove('hidden');
        s1.min = 20; s1.max = 150; s1.step = 5; s1.value = 50;
        s2.min = 0.00; s2.max = 0.60; s2.step = 0.05; s2.value = 0.30;
        s3.min = 10; s3.max = 160; s3.step = 2; s3.value = 60;
        s4.min = 5; s4.max = 45; s4.step = 1; s4.value = 20;
      } else if (sub === 'loop') {
        document.getElementById('circHeader').innerText = "CONCEPT 11-B • VERTICAL LOOP DYNAMICS";
        document.getElementById('circTitle').innerText = "Critical Speeds & Normal Force Variation";
        document.getElementById('circFormula').innerText = "v_bot ≥ √(5gR) • v_top ≥ √(gR) • N = mv²/R - mg·cosθ";
        document.getElementById('circParam1Label').innerText = "Loop Radius (R):";
        document.getElementById('circParam2Label').innerText = "Vehicle Mass (m):";
        document.getElementById('circParam3Label').innerText = "Speed at Bottom (v_0):";
        document.getElementById('circMet1Label').innerText = "Min Bottom Speed √(5gR):";
        document.getElementById('circMet2Label').innerText = "Min Top Speed √(gR):";
        document.getElementById('circMet3Label').innerText = "Loop Completion:";
        document.getElementById('circActionLabel').innerText = "Set Critical Speed";
        b3.classList.remove('hidden');
        b4.classList.add('hidden');
        s1.min = 10; s1.max = 50; s1.step = 2; s1.value = 20;
        s2.min = 200; s2.max = 1200; s2.step = 50; s2.value = 500;
        s3.min = 10; s3.max = 140; s3.step = 2; s3.value = 75;
      }
      updateCircular();
    }

    function triggerCircAction() {
      if (currentCircConcept === 'flat') {
        const r = parseFloat(document.getElementById('circSlider1').value);
        const mu = parseFloat(document.getElementById('circSlider2').value);
        const v_max_kmh = Math.sqrt(mu * r * 9.8) * 3.6;
        document.getElementById('circSlider3').value = Math.min(150, Math.round(v_max_kmh + 18));
        updateCircular();
      } else if (currentCircConcept === 'banked') {
        const r = parseFloat(document.getElementById('circSlider1').value);
        const theta = parseFloat(document.getElementById('circSlider4').value);
        const v_opt_kmh = Math.sqrt(r * 9.8 * Math.tan(theta * Math.PI / 180)) * 3.6;
        document.getElementById('circSlider3').value = Math.round(v_opt_kmh);
        updateCircular();
      } else if (currentCircConcept === 'loop') {
        const R = parseFloat(document.getElementById('circSlider1').value);
        const v_crit_kmh = Math.sqrt(5 * 9.8 * R) * 3.6;
        document.getElementById('circSlider3').value = Math.round(v_crit_kmh + 5);
        updateCircular();
      }
    }

    function updateCircular() {
      const s1 = parseFloat(document.getElementById('circSlider1').value);
      const s2 = parseFloat(document.getElementById('circSlider2').value);
      const s3 = parseFloat(document.getElementById('circSlider3').value);
      const s4 = parseFloat(document.getElementById('circSlider4').value);
      const g = 9.8;

      if (currentCircConcept === 'flat') {
        const r = s1;
        const mu = s2;
        const v_kmh = s3;
        const v_ms = v_kmh / 3.6;
        const v_max_ms = Math.sqrt(mu * r * g);
        const v_max_kmh = v_max_ms * 3.6;
        const isSkidding = v_ms > v_max_ms;

        document.getElementById('circParam1Val').innerText = r.toFixed(0) + ' m';
        document.getElementById('circParam2Val').innerText = mu.toFixed(2);
        document.getElementById('circParam3Val').innerText = v_kmh.toFixed(0) + ' km/h';
        document.getElementById('circMet1Val').innerText = v_max_kmh.toFixed(1) + ' km/h';
        document.getElementById('circMet2Val').innerText = `${v_kmh.toFixed(0)} km/h (${v_ms.toFixed(1)} m/s)`;

        const gripRatio = (v_ms * v_ms / (mu * r * g)) * 100;
        document.getElementById('circMet3Val').innerText = `${Math.min(100, gripRatio).toFixed(0)}% of Max Tire Grip`;

        if (isSkidding) {
          document.getElementById('circStateVal').innerText = `★ DRIFT / SKID ACTIVE: Car speed (${v_kmh.toFixed(0)}km/h) > v_max (${v_max_kmh.toFixed(1)}km/h)`;
          document.getElementById('circStateVal').className = "text-xs font-bold text-rose-400 mt-1";
          document.getElementById('circLiveBadge').innerText = "Tire Traction Lost!";
        } else {
          document.getElementById('circStateVal').innerText = "✓ SAFE TRACTION: Static friction supplies centripetal force";
          document.getElementById('circStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('circLiveBadge').innerText = "Level Road Safe Turn";
        }
      } else if (currentCircConcept === 'banked') {
        const r = s1;
        const mu = s2;
        const v_kmh = s3;
        const theta = s4;
        const rad = theta * Math.PI / 180;
        const v_opt_ms = Math.sqrt(r * g * Math.tan(rad));
        const v_opt_kmh = v_opt_ms * 3.6;

        const num = Math.tan(rad) + mu;
        const den = 1 - mu * Math.tan(rad);
        const v_max_kmh = den > 0 ? Math.sqrt(r * g * (num / den)) * 3.6 : 999;

        document.getElementById('circParam1Val').innerText = r.toFixed(0) + ' m';
        document.getElementById('circParam2Val').innerText = mu.toFixed(2);
        document.getElementById('circParam3Val').innerText = v_kmh.toFixed(0) + ' km/h';
        document.getElementById('circParam4Val').innerText = theta.toFixed(0) + '°';
        document.getElementById('circMet1Val').innerText = v_opt_kmh.toFixed(1) + ' km/h (No Friction)';
        document.getElementById('circMet2Val').innerText = v_max_kmh.toFixed(1) + ' km/h';

        if (Math.abs(v_kmh - v_opt_kmh) < 3) {
          document.getElementById('circMet3Val').innerText = "0.0 N (Zero Lateral Friction!)";
          document.getElementById('circStateVal').innerText = "★ OPTIMAL BANKING SPEED: N·sinθ provides 100% of centripetal force!";
          document.getElementById('circStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('circLiveBadge').innerText = "Optimal Banking Speed";
        } else if (v_kmh > v_opt_kmh) {
          document.getElementById('circMet3Val').innerText = "Points DOWN incline (Prevents outward skid)";
          document.getElementById('circStateVal').innerText = `HIGH SPEED: Friction points DOWN inclined road (v > v_opt)`;
          document.getElementById('circStateVal').className = "text-xs font-bold text-sky-300 mt-1";
          document.getElementById('circLiveBadge').innerText = "Banked Road High Speed";
        } else {
          document.getElementById('circMet3Val').innerText = "Points UP incline (Prevents inward slip)";
          document.getElementById('circStateVal').innerText = `LOW SPEED: Friction points UP inclined road (v < v_opt)`;
          document.getElementById('circStateVal').className = "text-xs font-bold text-amber-300 mt-1";
          document.getElementById('circLiveBadge').innerText = "Banked Road Low Speed";
        }
      } else if (currentCircConcept === 'loop') {
        const R = s1;
        const m = s2;
        const v0_kmh = s3;
        const v0_ms = v0_kmh / 3.6;
        const v_crit_bot_ms = Math.sqrt(5 * g * R);
        const v_crit_top_ms = Math.sqrt(g * R);

        document.getElementById('circParam1Val').innerText = R.toFixed(0) + ' m';
        document.getElementById('circParam2Val').innerText = m.toFixed(0) + ' kg';
        document.getElementById('circParam3Val').innerText = v0_kmh.toFixed(0) + ' km/h';
        document.getElementById('circMet1Val').innerText = (v_crit_bot_ms * 3.6).toFixed(1) + ' km/h';
        document.getElementById('circMet2Val').innerText = (v_crit_top_ms * 3.6).toFixed(1) + ' km/h';

        if (v0_ms >= v_crit_bot_ms) {
          document.getElementById('circMet3Val').innerText = "SUCCESS: Completes full 360° loop!";
          document.getElementById('circStateVal').innerText = "✓ LOOP COMPLETED: Speed at top exceeds √(gR) => Normal force N > 0";
          document.getElementById('circStateVal').className = "text-xs font-bold text-emerald-300 mt-1";
          document.getElementById('circLiveBadge').innerText = "Vertical Loop Success!";
        } else {
          document.getElementById('circMet3Val').innerText = "FAILS: Detaches before apex!";
          document.getElementById('circStateVal').innerText = "★ LOOP COLLAPSE: v_0 < √(5gR) => Vehicle falls from top!";
          document.getElementById('circStateVal').className = "text-xs font-bold text-rose-400 mt-1";
          document.getElementById('circLiveBadge').innerText = "Vertical Loop Fails";
        }
      }
      drawCircularCanvas();
    }

    function drawCircularCanvas() {
      resizeCanvas(cCanvas);
      const w = cCanvas.width / (window.devicePixelRatio || 1);
      const h = cCanvas.height / (window.devicePixelRatio || 1);
      if (!w || !h) return;
      cCtx.clearRect(0, 0, w, h);

      const cx = w / 2;
      const cy = h / 2 + 10;
      const g = 9.8;

      if (currentCircConcept === 'flat') {
        const r = parseFloat(document.getElementById('circSlider1').value);
        const mu = parseFloat(document.getElementById('circSlider2').value);
        const v_car_kmh = parseFloat(document.getElementById('circSlider3').value);
        const v_car_ms = v_car_kmh / 3.6;
        const v_max_ms = Math.sqrt(mu * r * g);
        const isSkidding = v_car_ms > v_max_ms;

        // Radius of drawn circular track scales noticeably with r!
        const plotR = Math.min(w * 0.38, 45 + r * 1.25);

        // Road Surface Texture: Reflects road friction mu!
        let roadColor = '#1e293b';
        let roadBorder = '#475569';
        if (mu < 0.25) {
          roadColor = '#0f2744'; // icy road
          roadBorder = '#38bdf8';
        } else if (mu > 0.65) {
          roadColor = '#181e29'; // dark grippy tarmac
          roadBorder = '#64748b';
        }

        cCtx.strokeStyle = roadColor;
        cCtx.lineWidth = 32;
        cCtx.beginPath();
        cCtx.arc(cx, cy, plotR, 0, Math.PI * 2);
        cCtx.stroke();

        // Track curbs
        cCtx.strokeStyle = roadBorder;
        cCtx.lineWidth = 2;
        cCtx.beginPath();
        cCtx.arc(cx, cy, plotR - 16, 0, Math.PI * 2);
        cCtx.arc(cx, cy, plotR + 16, 0, Math.PI * 2);
        cCtx.stroke();

        // Center line
        cCtx.strokeStyle = '#94a3b8';
        cCtx.lineWidth = 1.5;
        cCtx.setLineDash([6, 6]);
        cCtx.beginPath();
        cCtx.arc(cx, cy, plotR, 0, Math.PI * 2);
        cCtx.stroke();
        cCtx.setLineDash([]);

        // Car position: When skidding, drifts visibly outward!
        const drift = isSkidding ? 28 : 0;
        const carR = plotR + drift;
        const carX = cx + carR * Math.cos(circCarAngle);
        const carY = cy + carR * Math.sin(circCarAngle);

        // Stylized Race Car
        cCtx.save();
        cCtx.translate(carX, carY);
        cCtx.rotate(circCarAngle + Math.PI / 2);
        cCtx.fillStyle = isSkidding ? '#F43F5E' : '#38bdf8';
        cCtx.fillRect(-10, -16, 20, 32);
        cCtx.strokeStyle = '#ffffff';
        cCtx.lineWidth = 2;
        cCtx.strokeRect(-10, -16, 20, 32);

        // Windshield
        cCtx.fillStyle = '#0f172a';
        cCtx.fillRect(-7, -8, 14, 8);
        cCtx.restore();

        // Skid smoke / tire marks when skidding
        if (isSkidding) {
          cCtx.strokeStyle = 'rgba(244, 63, 94, 0.4)';
          cCtx.lineWidth = 3;
          cCtx.beginPath();
          cCtx.arc(cx, cy, plotR + 25, circCarAngle - 0.4, circCarAngle);
          cCtx.stroke();
        }

        // Centripetal / Friction Arrow
        const inX = -Math.cos(circCarAngle);
        const inY = -Math.sin(circCarAngle);
        const arrowLen = Math.min(55, (v_car_ms / v_max_ms) * 45);
        drawArrow(cCtx, carX, carY, carX + inX * arrowLen, carY + inY * arrowLen, isSkidding ? '#F43F5E' : '#4ADE80', isSkidding ? 'SLIP!' : 'f_s', 10);

        if (isSkidding) {
          cCtx.fillStyle = '#F43F5E';
          cCtx.font = 'bold 12px Consolas, monospace';
          cCtx.fillText('★ SKIDDING OUTWARD! (v > v_max)', cx - 95, cy - plotR - 30);
        } else {
          cCtx.fillStyle = '#4ADE80';
          cCtx.font = 'bold 12px Consolas, monospace';
          cCtx.fillText('✓ SAFE TIRE GRIP (f_s supplies mv²/r)', cx - 110, cy - plotR - 30);
        }

      } else if (currentCircConcept === 'banked') {
        const r = parseFloat(document.getElementById('circSlider1').value);
        const mu = parseFloat(document.getElementById('circSlider2').value);
        const v = parseFloat(document.getElementById('circSlider3').value);
        const theta = parseFloat(document.getElementById('circSlider4').value);
        const rad = theta * Math.PI / 180;
        const wedgeW = Math.min(300, w * 0.52);

        // Banked Road Cross-Section Wedge
        const wx = cx - wedgeW / 2;
        const wy = cy + 65;
        const wedgeH = wedgeW * Math.tan(rad);

        cCtx.strokeStyle = '#a855f7';
        cCtx.lineWidth = 3;
        cCtx.beginPath();
        cCtx.moveTo(wx, wy);
        cCtx.lineTo(wx + wedgeW, wy - wedgeH);
        cCtx.lineTo(wx + wedgeW, wy);
        cCtx.closePath();
        cCtx.fillStyle = 'rgba(168, 85, 247, 0.2)';
        cCtx.fill();
        cCtx.stroke();

        // Bank Angle Arc
        cCtx.strokeStyle = '#facc15';
        cCtx.beginPath();
        cCtx.arc(wx, wy, 45, 0, -rad, true);
        cCtx.stroke();
        cCtx.fillStyle = '#facc15';
        cCtx.font = 'bold 12px Consolas, monospace';
        cCtx.fillText(`θ = ${theta}°`, wx + 55, wy - 10);

        // Vehicle on Banked Surface
        const carMidX = wx + wedgeW * 0.5;
        const carMidY = wy - wedgeH * 0.5;

        cCtx.save();
        cCtx.translate(carMidX, carMidY);
        cCtx.rotate(-rad);
        cCtx.fillStyle = '#1e293b';
        cCtx.strokeStyle = '#38bdf8';
        cCtx.lineWidth = 2.5;
        cCtx.fillRect(-22, -32, 44, 32);
        cCtx.strokeRect(-22, -32, 44, 32);
        cCtx.fillStyle = '#ffffff';
        cCtx.font = 'bold 11px Consolas, monospace';
        cCtx.fillText('CAR', -11, -12);

        // Normal reaction perpendicular to road
        drawArrow(cCtx, 0, -16, 0, -70, '#4ADE80', 'N', 10);

        // Lateral Friction vector along incline: Shows whether f points UP or DOWN!
        const v_opt = Math.sqrt(r * g * Math.tan(rad)) * 3.6;
        if (Math.abs(v - v_opt) > 3) {
          const fDir = v > v_opt ? 1 : -1; // points down-slope if v > v_opt, up-slope if v < v_opt
          drawArrow(cCtx, 0, -2, fDir * 45, -2, '#facc15', 'f_friction', 10);
        }
        cCtx.restore();

        // Resolved Normal Components
        drawArrow(cCtx, carMidX, carMidY - 30, carMidX - 45, carMidY - 30, '#38bdf8', 'N·sinθ', 10);
        drawArrow(cCtx, carMidX, carMidY - 30, carMidX, carMidY - 75, '#4ADE80', 'N·cosθ=mg', 10);

      } else if (currentCircConcept === 'loop') {
        const R = parseFloat(document.getElementById('circSlider1').value);
        const v0 = parseFloat(document.getElementById('circSlider3').value);
        const loopRadiusPx = Math.min(105, 40 + R * 1.5);

        // Vertical Loop Ring
        cCtx.strokeStyle = '#38bdf8';
        cCtx.lineWidth = 3.5;
        cCtx.beginPath();
        cCtx.arc(cx, cy, loopRadiusPx, 0, Math.PI * 2);
        cCtx.stroke();

        // Track Entrance
        cCtx.strokeStyle = '#475569';
        cCtx.lineWidth = 3;
        cCtx.beginPath();
        cCtx.moveTo(cx - 150, cy + loopRadiusPx);
        cCtx.lineTo(cx - loopRadiusPx, cy + loopRadiusPx);
        cCtx.stroke();

        // Car traversing loop
        const carX = cx + loopRadiusPx * Math.cos(loopCarAngle);
        const carY = cy + loopRadiusPx * Math.sin(loopCarAngle);

        cCtx.save();
        cCtx.translate(carX, carY);
        cCtx.rotate(loopCarAngle + Math.PI / 2);
        cCtx.fillStyle = '#facc15';
        cCtx.fillRect(-10, -8, 20, 16);
        cCtx.strokeStyle = '#ffffff';
        cCtx.lineWidth = 2;
        cCtx.strokeRect(-10, -8, 20, 16);
        cCtx.restore();

        // Normal Force Vector towards center
        const toCx = (cx - carX) / loopRadiusPx;
        const toCy = (cy - carY) / loopRadiusPx;
        drawArrow(cCtx, carX, carY, carX + toCx * 35, carY + toCy * 35, '#4ADE80', 'N', 10);

        // Critical Speed indicators
        cCtx.fillStyle = '#94a3b8';
        cCtx.font = '10px Consolas, monospace';
        cCtx.fillText('v_top ≥ √(gR)', cx - 35, cy - loopRadiusPx - 10);
        cCtx.fillText('v_bot ≥ √(5gR)', cx - 40, cy + loopRadiusPx + 20);
      }
    }

    // ========================================================
    // UNIFIED MASTER PHYSICS ANIMATION LOOP (60 FPS)
    // ========================================================
    let lastT = performance.now();

    function masterPhysicsLoop(now) {
      const dt = Math.min(0.05, (now - lastT) / 1000);
      lastT = now;

      if (currentMode === 'newton') {
        if (currentNewtonConcept === 'fbd') {
          const s1 = parseFloat(document.getElementById('newtonSlider1').value);
          const s2 = parseFloat(document.getElementById('newtonSlider2').value);
          const s3 = parseFloat(document.getElementById('newtonSlider3').value);
          const fx = s2 * Math.cos(s3 * Math.PI / 180);
          const a = fx / s1;
          if (a > 0.05) {
            fbdPos = (fbdPos + a * dt * 10) % 140;
          } else {
            fbdPos = 0;
          }
          drawNewtonCanvas();
        } else if (currentNewtonConcept === 'elevator') {
          const aElev = parseFloat(document.getElementById('newtonSlider2').value);
          elevatorCabinY += aElev * dt * 25;
          drawNewtonCanvas();
        } else if (currentNewtonConcept === 'tension') {
          const m1 = parseFloat(document.getElementById('newtonSlider1').value);
          const m2 = parseFloat(document.getElementById('newtonSlider2').value);
          const a = (m1 - m2) * 9.8 / (m1 + m2);
          atwoodSpeed += a * dt * 8;
          atwoodY += atwoodSpeed * dt;
          // Smooth bounce cycle so motion never freezes!
          if (atwoodY > 65) { atwoodY = 65; atwoodSpeed = -atwoodSpeed * 0.9; }
          if (atwoodY < -65) { atwoodY = -65; atwoodSpeed = -atwoodSpeed * 0.9; }
          drawNewtonCanvas();
        }
      } else if (currentMode === 'friction') {
        if (currentFrictionConcept === 'graph') {
          const muS = parseFloat(document.getElementById('fricSlider1').value);
          const muK = Math.min(muS - 0.05, parseFloat(document.getElementById('fricSlider2').value));
          const F_app = parseFloat(document.getElementById('fricSlider3').value);
          const m = parseFloat(document.getElementById('fricSlider4').value);
          const fs_max = muS * m * 9.8;
          if (F_app > fs_max) {
            const a = (F_app - muK * m * 9.8) / m;
            slideX = (slideX + a * dt * 8) % 140;
          } else {
            slideX = 0;
          }
          drawFrictionCanvas();
        } else if (currentFrictionConcept === 'incline') {
          const theta = parseFloat(document.getElementById('fricSlider1').value);
          const muS = parseFloat(document.getElementById('fricSlider2').value);
          const muK = Math.min(muS - 0.05, parseFloat(document.getElementById('fricSlider3').value));
          const thetaR = Math.atan(muS) * 180 / Math.PI;
          if (theta > thetaR) {
            const aDown = 9.8 * (Math.sin(theta * Math.PI / 180) - muK * Math.cos(theta * Math.PI / 180));
            inclineBlockPos = (inclineBlockPos + Math.max(0.5, aDown) * dt * 25) % 190;
          } else {
            inclineBlockPos = 0;
          }
          drawFrictionCanvas();
        } else if (currentFrictionConcept === 'twoblock') {
          const m1 = parseFloat(document.getElementById('fricSlider1').value);
          const m2 = parseFloat(document.getElementById('fricSlider2').value);
          const muS = parseFloat(document.getElementById('fricSlider3').value);
          const F = parseFloat(document.getElementById('fricSlider4').value);
          const F_max = (m1 + m2) * muS * 9.8;
          if (F > 0) {
            twoBlockX = (twoBlockX + (F / (m1 + m2)) * dt * 6) % 110;
            if (F > F_max) {
              twoBlockRelSlip = Math.min(30, twoBlockRelSlip + dt * 20);
            } else {
              twoBlockRelSlip = Math.max(0, twoBlockRelSlip - dt * 25);
            }
          }
          drawFrictionCanvas();
        }
      } else if (currentMode === 'momentum') {
        if (currentMomentumConcept === 'impulse') {
          const v = parseFloat(document.getElementById('momSlider1').value);
          ballX += ballV * dt * 7;
          if (ballX <= 0) {
            ballX = 0;
            ballV = v; // rebound
            ballDeform = 0.55; // squash against wall
          } else if (ballX >= 160) {
            ballX = 160;
            ballV = -v; // return
          }
          if (ballDeform < 1.0) {
            ballDeform = Math.min(1.0, ballDeform + dt * 4.5);
          }
          drawMomentumCanvas();
        } else if (currentMomentumConcept === 'rocket') {
          const u = parseFloat(document.getElementById('momSlider1').value);
          const dmdt = parseFloat(document.getElementById('momSlider2').value);
          const M = parseFloat(document.getElementById('momSlider3').value);
          const a = Math.max(0, (u * dmdt - M * 9.8) / M);
          if (a > 0) {
            rocketAlt = (rocketAlt + a * dt * 6) % 150;
          } else {
            rocketAlt = 0;
          }
          drawMomentumCanvas();
        } else if (currentMomentumConcept === 'lami') {
          drawMomentumCanvas();
        }
      } else if (currentMode === 'circular') {
        if (currentCircConcept === 'flat') {
          const v = parseFloat(document.getElementById('circSlider3').value);
          circCarAngle = (circCarAngle + (v / 50) * dt * 2.8) % (Math.PI * 2);
          drawCircularCanvas();
        } else if (currentCircConcept === 'banked') {
          drawCircularCanvas();
        } else if (currentCircConcept === 'loop') {
          const v0 = parseFloat(document.getElementById('circSlider3').value);
          loopCarAngle = (loopCarAngle + (v0 / 50) * dt * 3.2) % (Math.PI * 2);
          drawCircularCanvas();
        }
      }

      requestAnimationFrame(masterPhysicsLoop);
    }
    requestAnimationFrame(masterPhysicsLoop);

    // ========================================================
    // RESIZEOBSERVER & POSTMESSAGE (RULE 18)
    // ========================================================
    const containers = [
      document.getElementById('newtonCanvasContainer'),
      document.getElementById('frictionCanvasContainer'),
      document.getElementById('momentumCanvasContainer'),
      document.getElementById('circularCanvasContainer')
    ];

    const resizeObserver = new ResizeObserver(() => {
      if (currentMode === 'newton') drawNewtonCanvas();
      else if (currentMode === 'friction') drawFrictionCanvas();
      else if (currentMode === 'momentum') drawMomentumCanvas();
      else if (currentMode === 'circular') drawCircularCanvas();
    });

    containers.forEach(c => { if (c) resizeObserver.observe(c); });

    window.addEventListener('message', (e) => {
      if (e.data && e.data.type === 'REDRAW_SIMULATION') {
        if (currentMode === 'newton') drawNewtonCanvas();
        else if (currentMode === 'friction') drawFrictionCanvas();
        else if (currentMode === 'momentum') drawMomentumCanvas();
        else if (currentMode === 'circular') drawCircularCanvas();
      }
    });

    // ========================================================
    // DEEP LINKING ROUTER (RULE 17: AT SCRIPT BOTTOM)
    // ========================================================
    function applyConceptOrMode() {
      const urlParams = new URLSearchParams(window.location.search);
      const conceptParam = urlParams.get('concept');
      const modeParam = urlParams.get('mode');

      if (conceptParam) {
        if (conceptParam === 'P11-C03-T01-V01') {
          switchMode('newton');
          setNewtonConcept('fbd');
        } else if (conceptParam === 'P11-C03-T01-V02') {
          switchMode('newton');
          setNewtonConcept('elevator');
        } else if (conceptParam === 'P11-C03-T01-V03') {
          switchMode('newton');
          setNewtonConcept('tension');
        } else if (conceptParam === 'P11-C03-T02-V04') {
          switchMode('momentum');
          setMomentumConcept('impulse');
        } else if (conceptParam === 'P11-C03-T02-V05') {
          switchMode('momentum');
          setMomentumConcept('rocket');
        } else if (conceptParam === 'P11-C03-T02-V06') {
          switchMode('momentum');
          setMomentumConcept('lami');
        } else if (conceptParam === 'P11-C03-T03-V07') {
          switchMode('friction');
          setFrictionConcept('graph');
        } else if (conceptParam === 'P11-C03-T03-V08') {
          switchMode('friction');
          setFrictionConcept('incline');
        } else if (conceptParam === 'P11-C03-T03-V09') {
          switchMode('friction');
          setFrictionConcept('twoblock');
        } else if (conceptParam === 'P11-C03-T04-V10') {
          switchMode('circular');
          setCircConcept('flat');
        } else if (conceptParam === 'P11-C03-T04-V11') {
          switchMode('circular');
          setCircConcept('banked');
        }
      } else if (modeParam) {
        switchMode(modeParam);
      } else {
        switchMode('newton');
        setNewtonConcept('fbd');
      }
    }

    applyConceptOrMode();
  </script>
</body>
</html>
'''

if __name__ == "__main__":
    html = generate_html()
    target_html.write_text(html, encoding="utf-8")
    print(f"Generated {target_html} with {len(html.splitlines())} lines.")
