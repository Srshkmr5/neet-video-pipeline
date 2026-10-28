import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
target_html = BASE_DIR / "simulations" / "unit_03_laws_of_motion_lab.html"

html_content = r'''<!DOCTYPE html>
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
      background: rgba(10, 15, 29, 0.85);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(56, 189, 248, 0.2);
    }
    .engine-btn.active {
      background: linear-gradient(135deg, rgba(14, 165, 233, 0.35), rgba(2, 132, 199, 0.15));
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
    }
    .engine-btn {
      background: rgba(15, 23, 42, 0.6);
      border-color: rgba(51, 65, 85, 0.5);
      color: #94a3b8;
    }
    .sub-preset-btn.active {
      background: rgba(56, 189, 248, 0.25);
      border-color: #38bdf8;
      color: #38bdf8;
      font-weight: 700;
    }
    .sub-preset-btn {
      background: rgba(15, 23, 42, 0.7);
      border-color: rgba(71, 85, 105, 0.4);
      color: #cbd5e1;
    }
    input[type=range] {
      accent-color: #38bdf8;
    }
  </style>
</head>
<body class="flex flex-col h-screen select-none">

  <!-- TOP HEADER & ENGINE TABS -->
  <header class="px-5 py-3 glass-panel border-b border-slate-800 flex items-center justify-between z-20 shrink-0">
    <div class="flex items-center space-x-3">
      <div class="w-8 h-8 rounded-lg bg-sky-500/20 border border-sky-400/40 flex items-center justify-center text-sky-400 font-bold font-mono text-sm shadow-[0_0_12px_rgba(56,189,248,0.3)]">
        03
      </div>
      <div>
        <h1 class="text-sm font-bold text-white tracking-wide flex items-center space-x-2">
          <span>LAWS OF MOTION INTERACTIVE LAB</span>
          <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-sky-950/80 text-sky-300 border border-sky-500/30 font-normal">P11-C03 • 11 CONCEPTS</span>
        </h1>
        <p class="text-[11px] text-slate-400">Newton's Laws • FBD & Elevators • Friction & Inclines • Connected Pulleys • Circular Banking</p>
      </div>
    </div>

    <!-- 4 Main Engine Navigation Tabs -->
    <div class="flex items-center space-x-2">
      <button id="tabEngine1" onclick="switchMode('newton')" class="engine-btn active px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2">
        <i class="fa-solid fa-scale-balanced text-sky-400"></i>
        <span>1 • NEWTON & FBD</span>
      </button>
      <button id="tabEngine2" onclick="switchMode('friction')" class="engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2">
        <i class="fa-solid fa-hill-rockslide text-amber-400"></i>
        <span>2 • FRICTION & INCLINE</span>
      </button>
      <button id="tabEngine3" onclick="switchMode('momentum')" class="engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2">
        <i class="fa-solid fa-angles-right text-emerald-400"></i>
        <span>3 • MOMENTUM & IMPULSE</span>
      </button>
      <button id="tabEngine4" onclick="switchMode('circular')" class="engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2">
        <i class="fa-solid fa-arrows-spin text-purple-400"></i>
        <span>4 • CIRCULAR BANKING</span>
      </button>
    </div>
  </header>

  <!-- MAIN SIMULATION WORKSPACE -->
  <main class="flex-1 relative overflow-hidden flex">

    <!-- ======================================================== -->
    <!-- ENGINE 1: NEWTON LAWS, FBD & ELEVATOR (CONCEPTS 1-3)     -->
    <!-- ======================================================== -->
    <section id="engineNewton" class="flex-1 flex overflow-hidden">
      <!-- Left Visual Canvas -->
      <div class="flex-1 flex flex-col p-4">
        <!-- Sub-Preset Toolbar -->
        <div class="flex items-center space-x-2 mb-3 shrink-0">
          <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
          <button id="subNewtonFbdBtn" onclick="setNewtonConcept('fbd')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
            1. First Law & FBD Vector Resolving
          </button>
          <button id="subNewtonElevatorBtn" onclick="setNewtonConcept('elevator')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            2. Second Law: Elevator & Apparent Weight
          </button>
          <button id="subNewtonTensionBtn" onclick="setNewtonConcept('tension')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            3. Third Law: Atwood Machine & Tension
          </button>
        </div>

        <!-- Canvas Container -->
        <div class="flex-1 bg-slate-950/80 rounded-xl border border-slate-800 relative overflow-hidden min-h-0" id="newtonCanvasContainer">
          <canvas id="newtonCanvas" class="w-full h-full block"></canvas>
        </div>
      </div>

      <!-- Right Control & Telemetry Sidebar -->
      <aside class="w-80 glass-panel border-l border-slate-800 p-4 flex flex-col space-y-4 overflow-y-auto shrink-0">
        <div>
          <div class="text-[11px] font-mono text-sky-400 font-bold tracking-wider" id="newtonHeader">CONCEPT 1 • FREE-BODY DIAGRAM</div>
          <h2 class="text-sm font-bold text-white" id="newtonTitle">FBD Orthogonal Vector Resolver</h2>
          <div class="mt-1 text-[11px] font-mono text-slate-400" id="newtonFormula">ΣF_x = m·a_x • ΣF_y = 0 • N = mg - F·sinθ</div>
        </div>

        <!-- Dynamic Controls -->
        <div class="space-y-3 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="newtonMassLabel">Body Mass (m):</span>
              <span id="newtonMassVal" class="text-sky-400 font-bold">5.0 kg</span>
            </div>
            <input type="range" id="newtonMassSlider" min="1" max="25" step="0.5" value="5" oninput="updateNewton()" class="w-full">
          </div>

          <div id="newtonForceBlock">
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="newtonForceLabel">Pulling Force (F):</span>
              <span id="newtonForceVal" class="text-amber-400 font-bold">40 N</span>
            </div>
            <input type="range" id="newtonForceSlider" min="0" max="100" step="1" value="40" oninput="updateNewton()" class="w-full">
          </div>

          <div id="newtonAngleBlock">
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="newtonAngleLabel">Pull Angle (θ):</span>
              <span id="newtonAngleVal" class="text-emerald-400 font-bold">30°</span>
            </div>
            <input type="range" id="newtonAngleSlider" min="0" max="80" step="1" value="30" oninput="updateNewton()" class="w-full">
          </div>

          <!-- Elevator Specific Mode Slider -->
          <div id="newtonElevatorBlock" class="hidden">
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span>Elevator Accel (a_frame):</span>
              <span id="newtonElevAccVal" class="text-rose-400 font-bold">+2.0 m/s² (Up)</span>
            </div>
            <input type="range" id="newtonElevAccSlider" min="-9.8" max="8" step="0.2" value="2" oninput="updateNewton()" class="w-full">
            <div class="text-[10px] text-slate-400 mt-1 flex justify-between font-mono">
              <span>Free Fall (-9.8)</span>
              <span>Rest (0)</span>
              <span>Up (+8)</span>
            </div>
          </div>
        </div>

        <!-- Telemetry Results Box -->
        <div class="bg-slate-900/80 p-3 rounded-xl border border-sky-500/20 font-mono text-xs space-y-2">
          <div class="text-slate-400 text-[11px] font-bold border-b border-slate-800 pb-1">REAL-TIME PHYSICS TELEMETRY</div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="newtonMet1Label">Normal Force (N):</span>
            <span id="newtonMet1Val" class="text-emerald-400 font-bold">29.0 N</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="newtonMet2Label">Net Horizontal F_x:</span>
            <span id="newtonMet2Val" class="text-amber-400 font-bold">34.6 N</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="newtonMet3Label">Net Acceleration (a):</span>
            <span id="newtonMet3Val" class="text-sky-400 font-bold">6.93 m/s²</span>
          </div>
        </div>

        <!-- NEET Trap Warning Card -->
        <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40 text-xs">
          <div class="flex items-center space-x-2 text-rose-400 font-bold mb-1">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span id="newtonTrapTitle">NEET TRAP: NORMAL FORCE DOES NOT ALWAYS EQUAL mg</span>
          </div>
          <p id="newtonTrapBody" class="text-slate-300 text-[11px] leading-relaxed">
            When a pulling force is inclined upward at angle θ, the vertical component F·sinθ relieves ground pressure! Thus Normal reaction is <strong class="text-emerald-300">N = mg - F·sinθ</strong>, strictly less than weight mg!
          </p>
        </div>
      </aside>
    </section>

    <!-- ======================================================== -->
    <!-- ENGINE 2: FRICTION, INCLINE & TWO-BLOCK (CONCEPTS 7-9)   -->
    <!-- ======================================================== -->
    <section id="engineFriction" class="flex-1 flex overflow-hidden hidden">
      <div class="flex-1 flex flex-col p-4">
        <div class="flex items-center space-x-2 mb-3 shrink-0">
          <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
          <button id="subFrictionGraphBtn" onclick="setFrictionConcept('graph')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
            7. Static vs Kinetic Friction Curve
          </button>
          <button id="subFrictionInclineBtn" onclick="setFrictionConcept('incline')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            8. Angle of Repose & Incline Deceleration
          </button>
          <button id="subFrictionTwoBlockBtn" onclick="setFrictionConcept('twoblock')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            9. Two-Block Relative Slip Threshold
          </button>
        </div>

        <div class="flex-1 bg-slate-950/80 rounded-xl border border-slate-800 relative overflow-hidden min-h-0" id="frictionCanvasContainer">
          <canvas id="frictionCanvas" class="w-full h-full block"></canvas>
        </div>
      </div>

      <aside class="w-80 glass-panel border-l border-slate-800 p-4 flex flex-col space-y-4 overflow-y-auto shrink-0">
        <div>
          <div class="text-[11px] font-mono text-amber-400 font-bold tracking-wider" id="frictionHeader">CONCEPT 7 • FRICTION MECHANICS</div>
          <h2 class="text-sm font-bold text-white" id="frictionTitle">Self-Adjusting Static vs Constant Kinetic</h2>
          <div class="mt-1 text-[11px] font-mono text-slate-400" id="frictionFormula">f_s ≤ μ_s·N • f_k = μ_k·N (μ_k &lt; μ_s)</div>
        </div>

        <div class="space-y-3 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="fricParam1Label">Static Coeff (μ_s):</span>
              <span id="fricMuSVal" class="text-amber-400 font-bold">0.60</span>
            </div>
            <input type="range" id="fricMuSSlider" min="0.1" max="0.9" step="0.05" value="0.60" oninput="updateFriction()" class="w-full">
          </div>

          <div id="fricMuKBlock">
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="fricParam2Label">Kinetic Coeff (μ_k):</span>
              <span id="fricMuKVal" class="text-sky-400 font-bold">0.40</span>
            </div>
            <input type="range" id="fricMuKSlider" min="0.05" max="0.85" step="0.05" value="0.40" oninput="updateFriction()" class="w-full">
          </div>

          <div id="fricAppliedBlock">
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="fricAppliedLabel">Applied Force (F):</span>
              <span id="fricAppliedVal" class="text-emerald-400 font-bold">20 N</span>
            </div>
            <input type="range" id="fricAppliedSlider" min="0" max="100" step="1" value="20" oninput="updateFriction()" class="w-full">
          </div>

          <div id="fricInclineBlock" class="hidden">
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span>Incline Angle (θ):</span>
              <span id="fricInclineVal" class="text-purple-400 font-bold">25°</span>
            </div>
            <input type="range" id="fricInclineSlider" min="0" max="75" step="1" value="25" oninput="updateFriction()" class="w-full">
          </div>
        </div>

        <div class="bg-slate-900/80 p-3 rounded-xl border border-amber-500/20 font-mono text-xs space-y-2">
          <div class="text-slate-400 text-[11px] font-bold border-b border-slate-800 pb-1">FRICTION FORCES & STATE</div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="fricMet1Label">Limiting Friction (f_s,max):</span>
            <span id="fricLimitingVal" class="text-amber-400 font-bold">29.4 N</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="fricMet2Label">Actual Active Friction:</span>
            <span id="fricActualVal" class="text-emerald-400 font-bold">20.0 N (Static)</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-400">Motion State:</span>
            <span id="fricStateVal" class="text-sky-400 font-bold">AT REST (Equilibrium)</span>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40 text-xs">
          <div class="flex items-center space-x-2 text-rose-400 font-bold mb-1">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span id="fricTrapTitle">NEET TRAP: STATIC FRICTION IS SELF-ADJUSTING</span>
          </div>
          <p id="fricTrapBody" class="text-slate-300 text-[11px] leading-relaxed">
            Static friction is NOT fixed at μ_s·N! It precisely matches the applied force up to the threshold. If F_app = 10 N and f_s,max = 50 N, friction is strictly 10 N, NOT 50 N!
          </p>
        </div>
      </aside>
    </section>

    <!-- ======================================================== -->
    <!-- ENGINE 3: MOMENTUM, IMPULSE & CONCURRENT (CONCEPTS 4-6)  -->
    <!-- ======================================================== -->
    <section id="engineMomentum" class="flex-1 flex overflow-hidden hidden">
      <div class="flex-1 flex flex-col p-4">
        <div class="flex items-center space-x-2 mb-3 shrink-0">
          <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
          <button id="subMomImpulseBtn" onclick="setMomentumConcept('impulse')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
            4. F-t Area & Rebound Doubling
          </button>
          <button id="subMomRocketBtn" onclick="setMomentumConcept('rocket')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            5. Momentum Conservation & Rocket Thrust
          </button>
          <button id="subMomLamiBtn" onclick="setMomentumConcept('lami')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            6. Lami's Theorem for Concurrent Equilibrium
          </button>
        </div>

        <div class="flex-1 bg-slate-950/80 rounded-xl border border-slate-800 relative overflow-hidden min-h-0" id="momentumCanvasContainer">
          <canvas id="momentumCanvas" class="w-full h-full block"></canvas>
        </div>
      </div>

      <aside class="w-80 glass-panel border-l border-slate-800 p-4 flex flex-col space-y-4 overflow-y-auto shrink-0">
        <div>
          <div class="text-[11px] font-mono text-emerald-400 font-bold tracking-wider" id="momHeader">CONCEPT 4 • IMPULSE & MOMENTUM</div>
          <h2 class="text-sm font-bold text-white" id="momTitle">Area Under F-t Curve = Δp</h2>
          <div class="mt-1 text-[11px] font-mono text-slate-400" id="momFormula">J = ∫F dt = Δp = m·(v_f - v_i)</div>
        </div>

        <div class="space-y-3 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="momParam1Label">Collision Speed (v):</span>
              <span id="momSpeedVal" class="text-sky-400 font-bold">15.0 m/s</span>
            </div>
            <input type="range" id="momSpeedSlider" min="5" max="30" step="1" value="15" oninput="updateMomentum()" class="w-full">
          </div>

          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="momParam2Label">Ball Mass (m):</span>
              <span id="momMassVal" class="text-amber-400 font-bold">0.50 kg</span>
            </div>
            <input type="range" id="momMassSlider" min="0.1" max="2.0" step="0.05" value="0.50" oninput="updateMomentum()" class="w-full">
          </div>

          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="momParam3Label">Contact Duration (Δt):</span>
              <span id="momTimeVal" class="text-emerald-400 font-bold">0.020 s</span>
            </div>
            <input type="range" id="momTimeSlider" min="0.005" max="0.050" step="0.005" value="0.020" oninput="updateMomentum()" class="w-full">
          </div>
        </div>

        <div class="bg-slate-900/80 p-3 rounded-xl border border-emerald-500/20 font-mono text-xs space-y-2">
          <div class="text-slate-400 text-[11px] font-bold border-b border-slate-800 pb-1">PHYSICS DIAGNOSTICS</div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="momMet1Label">Initial Momentum (p_i):</span>
            <span id="momInitP" class="text-slate-300 font-bold">+7.5 kg·m/s</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="momMet2Label">Rebound Momentum (p_f):</span>
            <span id="momFinalP" class="text-sky-400 font-bold">-7.5 kg·m/s</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="momMet3Label">Total Impulse J = Δp:</span>
            <span id="momTotalJ" class="text-emerald-400 font-bold">15.0 N·s (Doubled)</span>
          </div>
          <div class="flex justify-between border-t border-slate-800/80 pt-1">
            <span class="text-slate-400" id="momMet4Label">Average Impact Force:</span>
            <span id="momAvgF" class="text-rose-400 font-bold">750 N</span>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40 text-xs">
          <div class="flex items-center space-x-2 text-rose-400 font-bold mb-1">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span id="momTrapTitle">NEET TRAP: REBOUND VELOCITY SIGN</span>
          </div>
          <p id="momTrapBody" class="text-slate-300 text-[11px] leading-relaxed">
            During elastic rebound, direction flips! Δp = m·v - (-m·v) = <strong class="text-emerald-300">2·m·v</strong>. Never subtract magnitudes and write Δp = 0!
          </p>
        </div>
      </aside>
    </section>

    <!-- ======================================================== -->
    <!-- ENGINE 4: CIRCULAR DYNAMICS & BANKING (CONCEPTS 10-11)   -->
    <!-- ======================================================== -->
    <section id="engineCircular" class="flex-1 flex overflow-hidden hidden">
      <div class="flex-1 flex flex-col p-4">
        <div class="flex items-center space-x-2 mb-3 shrink-0">
          <span class="text-xs font-mono text-slate-400 uppercase tracking-wider">Concepts:</span>
          <button id="subCircFlatBtn" onclick="setCircConcept('flat')" class="sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition">
            10. Level Road Centripetal vs Friction
          </button>
          <button id="subCircBankedBtn" onclick="setCircConcept('banked')" class="sub-preset-btn px-3 py-1 rounded-lg border text-xs transition">
            11. Engineered Banked Road & Vertical Loop
          </button>
        </div>

        <div class="flex-1 bg-slate-950/80 rounded-xl border border-slate-800 relative overflow-hidden min-h-0" id="circularCanvasContainer">
          <canvas id="circularCanvas" class="w-full h-full block"></canvas>
        </div>
      </div>

      <aside class="w-80 glass-panel border-l border-slate-800 p-4 flex flex-col space-y-4 overflow-y-auto shrink-0">
        <div>
          <div class="text-[11px] font-mono text-purple-400 font-bold tracking-wider" id="circHeader">CONCEPT 10 • LEVEL CIRCULAR ROAD</div>
          <h2 class="text-sm font-bold text-white" id="circTitle">Static Friction Provides Centripetal Force</h2>
          <div class="mt-1 text-[11px] font-mono text-slate-400" id="circFormula">f_s = m·v²/r ≤ μ_s·m·g => v_max = √(μ_s·r·g)</div>
        </div>

        <div class="space-y-3 bg-slate-900/60 p-3 rounded-xl border border-slate-800">
          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="circParam1Label">Turn Radius (r):</span>
              <span id="circRadiusVal" class="text-purple-400 font-bold">50 m</span>
            </div>
            <input type="range" id="circRadiusSlider" min="20" max="150" step="5" value="50" oninput="updateCircular()" class="w-full">
          </div>

          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="circParam2Label">Road Friction (μ_s):</span>
              <span id="circMuVal" class="text-amber-400 font-bold">0.50</span>
            </div>
            <input type="range" id="circMuSlider" min="0.1" max="0.9" step="0.05" value="0.50" oninput="updateCircular()" class="w-full">
          </div>

          <div>
            <div class="flex justify-between text-xs font-mono text-slate-300 mb-1">
              <span id="circParam3Label">Vehicle Speed (v):</span>
              <span id="circAngleVal" class="text-sky-400 font-bold">50 km/h</span>
            </div>
            <input type="range" id="circAngleSlider" min="10" max="120" step="2" value="50" oninput="updateCircular()" class="w-full">
          </div>
        </div>

        <div class="bg-slate-900/80 p-3 rounded-xl border border-purple-500/20 font-mono text-xs space-y-2">
          <div class="text-slate-400 text-[11px] font-bold border-b border-slate-800 pb-1">SPEED LIMITS & CENTRIPETAL</div>
          <div class="flex justify-between">
            <span class="text-slate-400" id="circSpeed1Label">Max Safe Speed (v_max):</span>
            <span id="circSpeed1Val" class="text-emerald-400 font-bold">15.8 m/s (56.9 km/h)</span>
          </div>
          <div class="flex justify-between" id="circOptRow">
            <span class="text-slate-400">Optimum Speed (Zero Friction):</span>
            <span id="circOptVal" class="text-sky-400 font-bold">13.4 m/s (48.2 km/h)</span>
          </div>
          <div class="flex justify-between border-t border-slate-800/80 pt-1">
            <span class="text-slate-400">Cornering Status:</span>
            <span id="circVertLoopVal" class="text-emerald-400 font-bold">SAFE (Grip Maintained)</span>
          </div>
        </div>

        <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40 text-xs">
          <div class="flex items-center space-x-2 text-rose-400 font-bold mb-1">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span>NEET TRAP: MASS INDEPENDENCE</span>
          </div>
          <p class="text-slate-300 text-[11px] leading-relaxed">
            Neither flat curve skidding speed <strong class="text-purple-300">v = √(μrg)</strong> nor optimum banking speed <strong class="text-sky-300">v = √(rg·tanθ)</strong> depends on vehicle mass! Heavy truck and light motorcycle have identical speed limits.
          </p>
        </div>
      </aside>
    </section>

  </main>

  <script>
    // ========================================================
    // GLOBAL STATE & NAVIGATION
    // ========================================================
    let currentMode = 'newton';
    let currentNewtonConcept = 'fbd';
    let currentFrictionConcept = 'graph';
    let currentMomentumConcept = 'impulse';
    let currentCircConcept = 'flat';

    // Canvas elements & contexts
    const nCanvas = document.getElementById('newtonCanvas');
    const nCtx = nCanvas.getContext('2d');
    const fCanvas = document.getElementById('frictionCanvas');
    const fCtx = fCanvas.getContext('2d');
    const mCanvas = document.getElementById('momentumCanvas');
    const mCtx = mCanvas.getContext('2d');
    const cCanvas = document.getElementById('circularCanvas');
    const cCtx = cCanvas.getContext('2d');

    // Dynamic High-DPI Canvas Resizing
    function resizeCanvas(canvas) {
      if (!canvas || !canvas.parentElement) return;
      const rect = canvas.parentElement.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      if (rect.width > 0 && rect.height > 0) {
        if (canvas.width !== Math.floor(rect.width * dpr) || canvas.height !== Math.floor(rect.height * dpr)) {
          canvas.width = Math.floor(rect.width * dpr);
          canvas.height = Math.floor(rect.height * dpr);
          const ctx = canvas.getContext('2d');
          ctx.resetTransform();
          ctx.scale(dpr, dpr);
        }
      }
    }

    // Tab Switching
    function switchMode(mode) {
      currentMode = mode;
      document.getElementById('engineNewton').classList.toggle('hidden', mode !== 'newton');
      document.getElementById('engineFriction').classList.toggle('hidden', mode !== 'friction');
      document.getElementById('engineMomentum').classList.toggle('hidden', mode !== 'momentum');
      document.getElementById('engineCircular').classList.toggle('hidden', mode !== 'circular');

      document.getElementById('tabEngine1').className = mode === 'newton' ? 'engine-btn active px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2' : 'engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2';
      document.getElementById('tabEngine2').className = mode === 'friction' ? 'engine-btn active px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2' : 'engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2';
      document.getElementById('tabEngine3').className = mode === 'momentum' ? 'engine-btn active px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2' : 'engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2';
      document.getElementById('tabEngine4').className = mode === 'circular' ? 'engine-btn active px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2' : 'engine-btn px-3.5 py-1.5 rounded-xl border text-xs font-bold transition flex items-center space-x-2';

      setTimeout(() => {
        if (mode === 'newton') updateNewton();
        else if (mode === 'friction') updateFriction();
        else if (mode === 'momentum') updateMomentum();
        else if (mode === 'circular') updateCircular();
      }, 50);
    }

    // Helper: Draw Arrow
    function drawArrow(ctx, fromx, fromy, tox, toy, color, label, fontSize = 11) {
      const dx = tox - fromx;
      const dy = toy - fromy;
      const len = Math.hypot(dx, dy);
      if (len < 1) return;
      ctx.strokeStyle = color;
      ctx.fillStyle = color;
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(fromx, fromy);
      ctx.lineTo(tox, toy);
      ctx.stroke();

      const headlen = Math.min(10, Math.max(5, len * 0.25));
      const angle = Math.atan2(dy, dx);
      ctx.beginPath();
      ctx.moveTo(tox, toy);
      ctx.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
      ctx.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
      ctx.closePath();
      ctx.fill();

      if (label) {
        ctx.font = `bold ${fontSize}px Consolas, monospace`;
        const lx = tox + 8 * Math.cos(angle);
        const ly = toy + 8 * Math.sin(angle);
        ctx.fillText(label, lx, ly);
      }
    }

    // ========================================================
    // ENGINE 1: NEWTON'S LAWS & FBD IMPLEMENTATION
    // ========================================================
    let atwoodY = 0;
    let atwoodSpeed = 0;
    let elevatorY = 0;

    function setNewtonConcept(sub) {
      currentNewtonConcept = sub;
      document.getElementById('subNewtonFbdBtn').className = sub === 'fbd' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subNewtonElevatorBtn').className = sub === 'elevator' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subNewtonTensionBtn').className = sub === 'tension' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      const forceBlock = document.getElementById('newtonForceBlock');
      const angleBlock = document.getElementById('newtonAngleBlock');
      const elevBlock = document.getElementById('newtonElevatorBlock');

      if (sub === 'fbd') {
        document.getElementById('newtonHeader').innerText = "CONCEPT 1 • FREE-BODY DIAGRAM";
        document.getElementById('newtonTitle').innerText = "FBD Orthogonal Vector Resolver";
        document.getElementById('newtonFormula').innerText = "ΣF_x = m·a_x • ΣF_y = 0 • N = mg - F·sinθ";
        document.getElementById('newtonMassLabel').innerText = "Body Mass (m):";
        document.getElementById('newtonForceLabel').innerText = "Pulling Force (F):";
        document.getElementById('newtonAngleLabel').innerText = "Pull Angle (θ):";
        document.getElementById('newtonMet1Label').innerText = "Normal Force (N):";
        document.getElementById('newtonMet2Label').innerText = "Horizontal Pull F_x:";
        document.getElementById('newtonMet3Label').innerText = "Net Acceleration (a):";
        forceBlock.classList.remove('hidden');
        angleBlock.classList.remove('hidden');
        elevBlock.classList.add('hidden');
        document.getElementById('newtonTrapTitle').innerText = "NEET TRAP: NORMAL FORCE DOES NOT ALWAYS EQUAL mg";
        document.getElementById('newtonTrapBody').innerHTML = "When pulling at angle θ upward, vertical pull lifts the block, reducing ground pressure: <strong class='text-emerald-300'>N = mg - F·sinθ</strong>!";
      } else if (sub === 'elevator') {
        document.getElementById('newtonHeader').innerText = "CONCEPT 2 • ELEVATORS & PSEUDO FORCE";
        document.getElementById('newtonTitle').innerText = "Apparent Weight Scale in Accelerated Frame";
        document.getElementById('newtonFormula').innerText = "F_pseudo = -m·a_frame • N_app = m(g ± a)";
        document.getElementById('newtonMassLabel').innerText = "Body Mass (m):";
        document.getElementById('newtonMet1Label').innerText = "True Weight W = mg:";
        document.getElementById('newtonMet2Label').innerText = "Pseudo Force (-m·a):";
        document.getElementById('newtonMet3Label').innerText = "Scale Reading (N_app):";
        forceBlock.classList.add('hidden');
        angleBlock.classList.add('hidden');
        elevBlock.classList.remove('hidden');
        document.getElementById('newtonTrapTitle').innerText = "NEET TRAP: ACCELERATION DIRECTION VS VELOCITY";
        document.getElementById('newtonTrapBody').innerHTML = "Moving UP while SLOWING DOWN has downward acceleration (<strong class='text-rose-400'>N = m(g - a)</strong>)! Never look at velocity arrow; look at acceleration!";
      } else if (sub === 'tension') {
        document.getElementById('newtonHeader').innerText = "CONCEPT 3 • ATWOOD MACHINE & TENSION";
        document.getElementById('newtonTitle').innerText = "Two-Body Pulley System Equilibrium & String Tension";
        document.getElementById('newtonFormula').innerText = "a = |m1 - m2|g / (m1 + m2) • T = 2m1·m2·g / (m1 + m2)";
        document.getElementById('newtonMassLabel').innerText = "Body 1 Mass (m1):";
        document.getElementById('newtonForceLabel').innerText = "Body 2 Mass (m2):";
        document.getElementById('newtonMet1Label').innerText = "System Acceleration (a):";
        document.getElementById('newtonMet2Label').innerText = "String Tension (T):";
        document.getElementById('newtonMet3Label').innerText = "Pulley Support Load (2T):";
        forceBlock.classList.remove('hidden');
        angleBlock.classList.add('hidden');
        elevBlock.classList.add('hidden');
        document.getElementById('newtonTrapTitle').innerText = "NEET TRAP: ACTION-REACTION CANNOT CANCEL";
        document.getElementById('newtonTrapBody').innerHTML = "Normal force and gravity act on the SAME body; they balance due to First Law equilibrium, NOT Third Law action-reaction!";
      }
      updateNewton();
    }

    function updateNewton() {
      const m = parseFloat(document.getElementById('newtonMassSlider').value);
      const F = parseFloat(document.getElementById('newtonForceSlider').value);
      const theta = parseFloat(document.getElementById('newtonAngleSlider').value);
      const aElev = parseFloat(document.getElementById('newtonElevAccSlider').value);
      const g = 9.8;

      document.getElementById('newtonMassVal').innerText = m.toFixed(1) + ' kg';
      document.getElementById('newtonForceVal').innerText = (currentNewtonConcept === 'tension' ? F.toFixed(1) + ' kg' : F.toFixed(0) + ' N');
      document.getElementById('newtonAngleVal').innerText = theta.toFixed(0) + '°';
      document.getElementById('newtonElevAccVal').innerText = (aElev >= 0 ? '+' : '') + aElev.toFixed(1) + ' m/s² ' + (aElev > 0 ? '(Up)' : aElev < 0 ? '(Down)' : '(Rest)');

      const rad = theta * Math.PI / 180;
      if (currentNewtonConcept === 'fbd') {
        const fy = F * Math.sin(rad);
        const fx = F * Math.cos(rad);
        const N = Math.max(0, m * g - fy);
        const a = fx / m;
        document.getElementById('newtonMet1Val').innerText = N.toFixed(1) + ' N';
        document.getElementById('newtonMet2Val').innerText = fx.toFixed(1) + ' N';
        document.getElementById('newtonMet3Val').innerText = a.toFixed(2) + ' m/s²';
      } else if (currentNewtonConcept === 'elevator') {
        const W = m * g;
        const N_app = Math.max(0, m * (g + aElev));
        const F_pseudo = -m * aElev;
        document.getElementById('newtonMet1Val').innerText = W.toFixed(1) + ' N';
        document.getElementById('newtonMet2Val').innerText = (F_pseudo >= 0 ? '+' : '') + F_pseudo.toFixed(1) + ' N';
        document.getElementById('newtonMet3Val').innerText = N_app.toFixed(1) + ' N (' + (N_app / g).toFixed(1) + ' kg)';
      } else if (currentNewtonConcept === 'tension') {
        const m1 = m;
        const m2 = Math.max(0.5, F / 4); // F slider maps 0-100 to 0.5-25kg
        document.getElementById('newtonForceVal').innerText = m2.toFixed(1) + ' kg';
        const a = Math.abs(m1 - m2) * g / (m1 + m2);
        const T = (2 * m1 * m2 * g) / (m1 + m2);
        document.getElementById('newtonMet1Val').innerText = a.toFixed(2) + ' m/s²';
        document.getElementById('newtonMet2Val').innerText = T.toFixed(1) + ' N';
        document.getElementById('newtonMet3Val').innerText = (2 * T).toFixed(1) + ' N';
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
      const cy = h / 2 + 20;
      const g = 9.8;

      if (currentNewtonConcept === 'fbd') {
        const m = parseFloat(document.getElementById('newtonMassSlider').value);
        const F = parseFloat(document.getElementById('newtonForceSlider').value);
        const theta = parseFloat(document.getElementById('newtonAngleSlider').value);
        const rad = theta * Math.PI / 180;
        const fy = F * Math.sin(rad);
        const fx = F * Math.cos(rad);
        const N = Math.max(0, m * g - fy);
        const a = fx / m;

        // Dynamic block size proportional to sqrt(m)
        const side = 40 + Math.sqrt(m) * 8;

        // Floor line
        nCtx.strokeStyle = '#475569';
        nCtx.lineWidth = 2.5;
        nCtx.beginPath();
        nCtx.moveTo(cx - 160, cy + side / 2);
        nCtx.lineTo(cx + 180, cy + side / 2);
        nCtx.stroke();

        // Floor hatching
        nCtx.strokeStyle = '#334155';
        nCtx.lineWidth = 1;
        for (let x = cx - 150; x <= cx + 170; x += 15) {
          nCtx.beginPath();
          nCtx.moveTo(x, cy + side / 2);
          nCtx.lineTo(x - 10, cy + side / 2 + 10);
          nCtx.stroke();
        }

        // Block
        nCtx.fillStyle = '#1e293b';
        nCtx.strokeStyle = N === 0 ? '#facc15' : '#38bdf8';
        nCtx.lineWidth = 2.5;
        nCtx.fillRect(cx - side / 2, cy - side / 2, side, side);
        nCtx.strokeRect(cx - side / 2, cy - side / 2, side, side);

        nCtx.fillStyle = '#ffffff';
        nCtx.font = 'bold 12px Consolas, monospace';
        nCtx.fillText(`m=${m.toFixed(1)}kg`, cx - 25, cy + 4);

        if (N === 0) {
          nCtx.fillStyle = '#facc15';
          nCtx.font = 'bold 11px Consolas, monospace';
          nCtx.fillText('★ LIFT-OFF (N=0)', cx - 45, cy - side / 2 - 25);
        }

        // Vector 1: mg (Gravity Downward - Rose)
        const mgLen = Math.min(110, 25 + m * 3.5);
        drawArrow(nCtx, cx, cy, cx, cy + side / 2 + mgLen, '#F43F5E', `W = mg (${(m * g).toFixed(0)}N)`);

        // Vector 2: Normal N (Upward - Emerald)
        if (N > 0) {
          const nLen = Math.min(110, (N / (m * g)) * mgLen);
          drawArrow(nCtx, cx, cy - side / 2, cx, cy - side / 2 - nLen, '#4ADE80', `N = ${N.toFixed(0)}N`);
        }

        // Vector 3: Pull F at angle theta (Gold)
        if (F > 0) {
          const fLen = Math.min(120, 20 + F * 1.0);
          const fEndx = cx + side / 2 + Math.cos(rad) * fLen;
          const fEndy = cy - Math.sin(rad) * fLen;
          drawArrow(nCtx, cx + side / 2, cy, fEndx, fEndy, '#FACC15', `F = ${F.toFixed(0)}N`);

          // Angle arc
          nCtx.strokeStyle = '#FACC15';
          nCtx.lineWidth = 1.5;
          nCtx.setLineDash([3, 3]);
          nCtx.beginPath();
          nCtx.moveTo(cx + side / 2, cy);
          nCtx.lineTo(cx + side / 2 + 50, cy);
          nCtx.stroke();
          nCtx.setLineDash([]);
          nCtx.beginPath();
          nCtx.arc(cx + side / 2, cy, 28, 0, -rad, true);
          nCtx.stroke();
          nCtx.fillStyle = '#FACC15';
          nCtx.fillText(`θ=${theta}°`, cx + side / 2 + 35, cy - 8);

          // Orthogonal Components
          nCtx.strokeStyle = '#38bdf8';
          nCtx.setLineDash([2, 2]);
          nCtx.beginPath();
          nCtx.moveTo(fEndx, cy);
          nCtx.lineTo(fEndx, fEndy);
          nCtx.stroke();
          nCtx.setLineDash([]);
          drawArrow(nCtx, cx + side / 2, cy, fEndx, cy, '#38bdf8', `Fx=${fx.toFixed(0)}N`, 10);
        }

        // Acceleration Arrow on top
        if (a > 0.05) {
          const aLen = Math.min(70, a * 6 + 15);
          drawArrow(nCtx, cx - side / 2, cy - side / 2 - 12, cx - side / 2 + aLen, cy - side / 2 - 12, '#38bdf8', `a = ${a.toFixed(1)} m/s²`, 11);
        }

      } else if (currentNewtonConcept === 'elevator') {
        const m = parseFloat(document.getElementById('newtonMassSlider').value);
        const aElev = parseFloat(document.getElementById('newtonElevAccSlider').value);
        const N_app = Math.max(0, m * (g + aElev));
        const W = m * g;

        // Elevator Frame
        const cageW = 190;
        const cageH = 220;
        const cageTop = cy - cageH / 2;

        nCtx.strokeStyle = '#64748b';
        nCtx.lineWidth = 3;
        nCtx.strokeRect(cx - cageW / 2, cageTop, cageW, cageH);

        // Suspension Cable
        nCtx.strokeStyle = '#94a3b8';
        nCtx.lineWidth = 4;
        nCtx.beginPath();
        nCtx.moveTo(cx, cageTop);
        nCtx.lineTo(cx, cageTop - 45);
        nCtx.stroke();

        // Weighing Scale Platform
        const scaleY = cy + cageH / 2 - 35;
        const scaleW = 120;
        const scaleH = 18;

        // Spring compression under scale
        const springComp = Math.min(10, (N_app / (m * g)) * 6);
        nCtx.fillStyle = '#0f172a';
        nCtx.strokeStyle = '#38bdf8';
        nCtx.lineWidth = 2;
        nCtx.fillRect(cx - scaleW / 2, scaleY + springComp, scaleW, scaleH);
        nCtx.strokeRect(cx - scaleW / 2, scaleY + springComp, scaleW, scaleH);

        // Scale digital readout
        nCtx.fillStyle = '#38bdf8';
        nCtx.font = 'bold 12px Consolas, monospace';
        nCtx.fillText(`SCALE: ${N_app.toFixed(1)} N (${(N_app / g).toFixed(1)} kg)`, cx - 65, scaleY + springComp + 13);

        // Person / Mass Block on scale
        const bW = 35 + Math.sqrt(m) * 5;
        const bH = 45 + Math.sqrt(m) * 4;
        const bY = (N_app === 0 ? scaleY - bH - 12 : scaleY + springComp - bH); // Floating if weightless!

        nCtx.fillStyle = N_app === 0 ? '#1e1b4b' : '#1e293b';
        nCtx.strokeStyle = N_app === 0 ? '#facc15' : '#4ade80';
        nCtx.lineWidth = 2;
        nCtx.fillRect(cx - bW / 2, bY, bW, bH);
        nCtx.strokeRect(cx - bW / 2, bY, bW, bH);

        nCtx.fillStyle = '#ffffff';
        nCtx.font = 'bold 12px Consolas, monospace';
        nCtx.fillText(`m=${m}kg`, cx - 22, bY + bH / 2 + 4);

        if (N_app === 0) {
          nCtx.fillStyle = '#facc15';
          nCtx.font = 'bold 12px Consolas, monospace';
          nCtx.fillText('★ WEIGHTLESS FLOAT ★', cx - 70, bY - 14);
        }

        // Vectors on the person
        // 1. Gravity W = mg (Rose Downward)
        const wLen = 30 + m * 1.5;
        drawArrow(nCtx, cx, bY + bH / 2, cx, bY + bH / 2 + wLen, '#F43F5E', `W = mg (${W.toFixed(0)}N)`);

        // 2. Normal reaction N_app (Emerald Upward)
        if (N_app > 0) {
          const nLen = Math.max(10, (N_app / W) * wLen);
          drawArrow(nCtx, cx, bY + bH / 2, cx, bY + bH / 2 - nLen, '#4ADE80', `N = ${N_app.toFixed(0)}N`);
        }

        // Frame acceleration arrow on side
        if (aElev !== 0) {
          const aLen = Math.abs(aElev) * 10;
          const aDir = aElev > 0 ? -1 : 1;
          drawArrow(nCtx, cx + cageW / 2 + 25, cy, cx + cageW / 2 + 25, cy + aDir * aLen, aElev > 0 ? '#38bdf8' : '#F43F5E', `a = ${aElev.toFixed(1)}`);
        }

      } else if (currentNewtonConcept === 'tension') {
        const m1 = parseFloat(document.getElementById('newtonMassSlider').value);
        const m2 = Math.max(0.5, parseFloat(document.getElementById('newtonForceSlider').value) / 4);
        const a = Math.abs(m1 - m2) * g / (m1 + m2);
        const T = (2 * m1 * m2 * g) / (m1 + m2);

        // Pulley at top
        const pulleyR = 32;
        const pulleyY = cy - 100;
        nCtx.beginPath();
        nCtx.arc(cx, pulleyY, pulleyR, 0, Math.PI * 2);
        nCtx.fillStyle = '#334155';
        nCtx.fill();
        nCtx.strokeStyle = '#94a3b8';
        nCtx.lineWidth = 3;
        nCtx.stroke();

        // Pulley Spokes
        const spokeAngle = (atwoodY * 0.05);
        for (let i = 0; i < 4; i++) {
          const ang = spokeAngle + (i * Math.PI / 2);
          nCtx.beginPath();
          nCtx.moveTo(cx, pulleyY);
          nCtx.lineTo(cx + pulleyR * Math.cos(ang), pulleyY + pulleyR * Math.sin(ang));
          nCtx.strokeStyle = '#64748b';
          nCtx.stroke();
        }

        // Dynamic Position
        const leftH = cy - 20 + atwoodY;
        const rightH = cy - 20 - atwoodY;

        // String
        nCtx.strokeStyle = '#f8fafc';
        nCtx.lineWidth = 2;
        nCtx.beginPath();
        nCtx.moveTo(cx - pulleyR, pulleyY);
        nCtx.lineTo(cx - pulleyR, leftH);
        nCtx.moveTo(cx + pulleyR, pulleyY);
        nCtx.lineTo(cx + pulleyR, rightH);
        nCtx.stroke();

        // Block 1 (Left - m1)
        const b1Side = 32 + Math.sqrt(m1) * 7;
        nCtx.fillStyle = '#1e293b';
        nCtx.strokeStyle = '#38bdf8';
        nCtx.lineWidth = 2;
        nCtx.fillRect(cx - pulleyR - b1Side / 2, leftH, b1Side, b1Side);
        nCtx.strokeRect(cx - pulleyR - b1Side / 2, leftH, b1Side, b1Side);
        nCtx.fillStyle = '#ffffff';
        nCtx.font = 'bold 11px Consolas, monospace';
        nCtx.fillText(`m1=${m1.toFixed(1)}kg`, cx - pulleyR - b1Side / 2 + 4, leftH + b1Side / 2 + 4);

        // Block 2 (Right - m2)
        const b2Side = 32 + Math.sqrt(m2) * 7;
        nCtx.fillStyle = '#1e293b';
        nCtx.strokeStyle = '#facc15';
        nCtx.lineWidth = 2;
        nCtx.fillRect(cx + pulleyR - b2Side / 2, rightH, b2Side, b2Side);
        nCtx.strokeRect(cx + pulleyR - b2Side / 2, rightH, b2Side, b2Side);
        nCtx.fillStyle = '#ffffff';
        nCtx.fillText(`m2=${m2.toFixed(1)}kg`, cx + pulleyR - b2Side / 2 + 4, rightH + b2Side / 2 + 4);

        // Tension Arrows (Upwards on both)
        const tLen = Math.min(45, 15 + T * 0.35);
        drawArrow(nCtx, cx - pulleyR, leftH, cx - pulleyR, leftH - tLen, '#4ADE80', `T=${T.toFixed(0)}N`, 10);
        drawArrow(nCtx, cx + pulleyR, rightH, cx + pulleyR, rightH - tLen, '#4ADE80', `T=${T.toFixed(0)}N`, 10);

        // Weight Arrows (Downwards)
        const w1Len = Math.min(55, 15 + m1 * 1.8);
        const w2Len = Math.min(55, 15 + m2 * 1.8);
        drawArrow(nCtx, cx - pulleyR, leftH + b1Side, cx - pulleyR, leftH + b1Side + w1Len, '#F43F5E', `${(m1 * g).toFixed(0)}N`, 10);
        drawArrow(nCtx, cx + pulleyR, rightH + b2Side, cx + pulleyR, rightH + b2Side + w2Len, '#F43F5E', `${(m2 * g).toFixed(0)}N`, 10);
      }
    }

    // ========================================================
    // ENGINE 2: FRICTION, INCLINE & TWO-BLOCK IMPLEMENTATION
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

      const appliedBlock = document.getElementById('fricAppliedBlock');
      const inclineBlock = document.getElementById('fricInclineBlock');

      if (sub === 'graph') {
        document.getElementById('frictionHeader').innerText = "CONCEPT 7 • FRICTION MECHANICS";
        document.getElementById('frictionTitle').innerText = "Self-Adjusting Static vs Constant Kinetic";
        document.getElementById('frictionFormula').innerText = "f_s ≤ μ_s·N • f_k = μ_k·N (μ_k < μ_s)";
        document.getElementById('fricParam1Label').innerText = "Static Coeff (μ_s):";
        document.getElementById('fricParam2Label').innerText = "Kinetic Coeff (μ_k):";
        document.getElementById('fricAppliedLabel').innerText = "Applied Pull (F_app):";
        document.getElementById('fricMet1Label').innerText = "Limiting Friction (f_s,max):";
        document.getElementById('fricMet2Label').innerText = "Active Friction (f):";
        appliedBlock.classList.remove('hidden');
        inclineBlock.classList.add('hidden');
      } else if (sub === 'incline') {
        document.getElementById('frictionHeader').innerText = "CONCEPT 8 • ANGLE OF REPOSE";
        document.getElementById('frictionTitle').innerText = "Motion on Rough Incline & Time Asymmetry";
        document.getElementById('frictionFormula').innerText = "tan θ_R = μ_s • a_down = g(sinθ - μ_k·cosθ)";
        document.getElementById('fricParam1Label').innerText = "Static Coeff (μ_s):";
        document.getElementById('fricParam2Label').innerText = "Kinetic Coeff (μ_k):";
        document.getElementById('fricMet1Label').innerText = "Angle of Repose (θ_R):";
        document.getElementById('fricMet2Label').innerText = "Active Friction:";
        appliedBlock.classList.add('hidden');
        inclineBlock.classList.remove('hidden');
      } else if (sub === 'twoblock') {
        document.getElementById('frictionHeader').innerText = "CONCEPT 9 • TWO-BLOCK SYSTEM";
        document.getElementById('frictionTitle').innerText = "Relative Slipping Force Threshold";
        document.getElementById('frictionFormula').innerText = "a_max = μ_s·g • F_max = (m1 + m2)·μ_s·g";
        document.getElementById('fricParam1Label').innerText = "Interface Friction (μ_s):";
        document.getElementById('fricParam2Label').innerText = "Kinetic Coeff (μ_k):";
        document.getElementById('fricAppliedLabel').innerText = "Pull on Bottom m2 (F):";
        document.getElementById('fricMet1Label').innerText = "Slip Threshold (F_max):";
        document.getElementById('fricMet2Label').innerText = "Interface Friction (f):";
        appliedBlock.classList.remove('hidden');
        inclineBlock.classList.add('hidden');
      }
      updateFriction();
    }

    function updateFriction() {
      const muS = parseFloat(document.getElementById('fricMuSSlider').value);
      const muK = Math.min(muS - 0.05, parseFloat(document.getElementById('fricMuKSlider').value));
      const F_app = parseFloat(document.getElementById('fricAppliedSlider').value);
      const theta = parseFloat(document.getElementById('fricInclineSlider').value);
      const m = 5.0;
      const g = 9.8;
      const N = m * g;

      document.getElementById('fricMuSVal').innerText = muS.toFixed(2);
      document.getElementById('fricMuKVal').innerText = muK.toFixed(2);
      document.getElementById('fricAppliedVal').innerText = F_app.toFixed(0) + ' N';
      document.getElementById('fricInclineVal').innerText = theta.toFixed(0) + '°';

      const f_s_max = muS * N;
      const f_k = muK * N;

      if (currentFrictionConcept === 'graph') {
        document.getElementById('fricLimitingVal').innerText = f_s_max.toFixed(1) + ' N';
        if (F_app <= f_s_max) {
          document.getElementById('fricActualVal').innerText = F_app.toFixed(1) + ' N (Static fs = F)';
          document.getElementById('fricStateVal').innerText = "STATIC REST (f_s = F_applied)";
        } else {
          document.getElementById('fricActualVal').innerText = f_k.toFixed(1) + ' N (Kinetic fk)';
          document.getElementById('fricStateVal').innerText = "SLIDING FORWARD (a = " + ((F_app - f_k) / m).toFixed(2) + " m/s²)";
        }
      } else if (currentFrictionConcept === 'incline') {
        const thetaRepose = Math.atan(muS) * 180 / Math.PI;
        document.getElementById('fricLimitingVal').innerText = thetaRepose.toFixed(1) + '°';
        if (theta <= thetaRepose) {
          const fs = m * g * Math.sin(theta * Math.PI / 180);
          document.getElementById('fricActualVal').innerText = fs.toFixed(1) + ' N (Static mg·sinθ)';
          document.getElementById('fricStateVal').innerText = "STATIONARY (θ ≤ θ_Repose)";
        } else {
          const aDown = g * (Math.sin(theta * Math.PI / 180) - muK * Math.cos(theta * Math.PI / 180));
          const fk = muK * m * g * Math.cos(theta * Math.PI / 180);
          document.getElementById('fricActualVal').innerText = fk.toFixed(1) + ' N (Kinetic fk)';
          document.getElementById('fricStateVal').innerText = "SLIDING DOWN (a = " + Math.max(0, aDown).toFixed(2) + " m/s²)";
        }
      } else if (currentFrictionConcept === 'twoblock') {
        const m1 = 2.0;
        const m2 = 4.0;
        const a_max = muS * g;
        const F_max = (m1 + m2) * a_max;
        document.getElementById('fricLimitingVal').innerText = F_max.toFixed(1) + " N";
        if (F_app <= F_max) {
          const a_com = F_app / (m1 + m2);
          const f_int = m1 * a_com;
          document.getElementById('fricActualVal').innerText = f_int.toFixed(1) + ' N (Static)';
          document.getElementById('fricStateVal').innerText = "MOVING TOGETHER (a = " + a_com.toFixed(2) + " m/s²)";
        } else {
          const fk_int = muK * m1 * g;
          const a1 = fk_int / m1;
          const a2 = (F_app - fk_int) / m2;
          document.getElementById('fricActualVal').innerText = fk_int.toFixed(1) + ' N (Kinetic Slip)';
          document.getElementById('fricStateVal').innerText = "RELATIVE SLIPPING! (a1=" + a1.toFixed(1) + ", a2=" + a2.toFixed(1) + ")";
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
      const muS = parseFloat(document.getElementById('fricMuSSlider').value);
      const muK = parseFloat(document.getElementById('fricMuKSlider').value);
      const g = 9.8;

      if (currentFrictionConcept === 'graph') {
        const F_app = parseFloat(document.getElementById('fricAppliedSlider').value);
        const m = 5.0;
        const N = m * g;
        const fs_max = muS * N;
        const fk = muK * N;

        // TOP HALF: Physical Sliding Block
        const floorY = cy - 40;
        fCtx.strokeStyle = '#475569';
        fCtx.lineWidth = 2;
        fCtx.beginPath();
        fCtx.moveTo(cx - 180, floorY);
        fCtx.lineTo(cx + 180, floorY);
        fCtx.stroke();

        // Block with position slideX
        const bx = cx - 35 + slideX;
        fCtx.fillStyle = '#1e293b';
        fCtx.strokeStyle = F_app > fs_max ? '#f59e0b' : '#38bdf8';
        fCtx.lineWidth = 2;
        fCtx.fillRect(bx, floorY - 50, 70, 50);
        fCtx.strokeRect(bx, floorY - 50, 70, 50);
        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 12px Consolas, monospace';
        fCtx.fillText(`m=5kg`, bx + 16, floorY - 22);

        // Pull arrow (Gold)
        if (F_app > 0) {
          const pullLen = Math.min(80, 15 + F_app * 0.9);
          drawArrow(fCtx, bx + 70, floorY - 25, bx + 70 + pullLen, floorY - 25, '#FACC15', `F=${F_app}N`, 10);
        }

        // Friction arrow (Red opposing to left)
        const actFric = F_app <= fs_max ? F_app : fk;
        if (actFric > 0) {
          const fricLen = Math.min(80, 15 + actFric * 0.9);
          drawArrow(fCtx, bx, floorY - 10, bx - fricLen, floorY - 10, '#F43F5E', `f=${actFric.toFixed(0)}N`, 10);
        }

        // BOTTOM HALF: Live Friction Curve Graph
        const ox = 70;
        const oy = h - 35;
        const gw = w - 140;
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
        fCtx.fillText('F_applied →', ox + gw - 65, oy + 20);
        fCtx.fillText('Friction f ↑', ox - 50, oy - gh + 10);

        const peakX = ox + gw * 0.45;
        const peakY = oy - gh * 0.85 * (muS / 0.9);
        const dropY = oy - gh * 0.85 * (muK / 0.9);

        // Static linear slope (fs = F)
        fCtx.strokeStyle = '#38bdf8';
        fCtx.lineWidth = 3;
        fCtx.beginPath();
        fCtx.moveTo(ox, oy);
        fCtx.lineTo(peakX, peakY);
        fCtx.stroke();

        // Kinetic drop and plateau
        fCtx.strokeStyle = '#f59e0b';
        fCtx.beginPath();
        fCtx.moveTo(peakX, peakY);
        fCtx.lineTo(peakX + 12, dropY);
        fCtx.lineTo(ox + gw, dropY);
        fCtx.stroke();

        // Active Marker on Graph
        const currNormX = ox + (F_app / 60) * (peakX - ox);
        let currNormY = oy;
        if (currNormX <= peakX) {
          currNormY = oy - (currNormX - ox) * ((oy - peakY) / (peakX - ox));
        } else {
          currNormY = dropY;
        }

        fCtx.fillStyle = '#4ade80';
        fCtx.beginPath();
        fCtx.arc(Math.min(ox + gw, currNormX), currNormY, 6, 0, Math.PI * 2);
        fCtx.fill();

      } else if (currentFrictionConcept === 'incline') {
        const theta = parseFloat(document.getElementById('fricInclineSlider').value);
        const rad = theta * Math.PI / 180;
        const thetaR = Math.atan(muS) * 180 / Math.PI;
        const rampLen = Math.min(320, w * 0.55);

        // Ramp Base Point
        const rx = cx - rampLen / 2;
        const ry = cy + 70;

        // Incline Triangle
        fCtx.strokeStyle = '#38bdf8';
        fCtx.lineWidth = 3;
        fCtx.beginPath();
        fCtx.moveTo(rx, ry);
        fCtx.lineTo(rx + rampLen * Math.cos(rad), ry - rampLen * Math.sin(rad));
        fCtx.lineTo(rx + rampLen * Math.cos(rad), ry);
        fCtx.closePath();
        fCtx.fillStyle = 'rgba(30, 41, 59, 0.4)';
        fCtx.fill();
        fCtx.stroke();

        // Angle Arc θ
        fCtx.strokeStyle = '#facc15';
        fCtx.beginPath();
        fCtx.arc(rx, ry, 35, 0, -rad, true);
        fCtx.stroke();
        fCtx.fillStyle = '#facc15';
        fCtx.font = 'bold 12px Consolas, monospace';
        fCtx.fillText(`θ=${theta}°`, rx + 45, ry - 8);

        // Angle of Repose Threshold Dashed Line
        fCtx.fillStyle = '#4ade80';
        fCtx.fillText(`θ_Repose=${thetaR.toFixed(1)}°`, rx + rampLen * 0.4, ry + 20);

        // Block on the Incline (with animated inclineBlockPos)
        const d = (rampLen * 0.35) + inclineBlockPos;
        const bx = rx + d * Math.cos(rad);
        const by = ry - d * Math.sin(rad);

        fCtx.save();
        fCtx.translate(bx, by);
        fCtx.rotate(-rad);
        fCtx.fillStyle = theta > thetaR ? '#f59e0b' : '#1e293b';
        fCtx.strokeStyle = theta > thetaR ? '#F43F5E' : '#4ade80';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(-25, -40, 50, 40);
        fCtx.strokeRect(-25, -40, 50, 40);
        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 11px Consolas, monospace';
        fCtx.fillText('m=5kg', -18, -16);

        // Friction vector pointing up slope
        const fLen = theta <= thetaR ? 25 : 35;
        drawArrow(fCtx, 0, -20, -fLen, -20, '#F43F5E', 'f_friction', 10);
        fCtx.restore();

        // Normal Force N vector perpendicular to incline
        const normAngle = rad + Math.PI / 2;
        drawArrow(fCtx, bx, by, bx - Math.sin(rad) * 45, by - Math.cos(rad) * 45, '#4ADE80', 'N', 10);

        // Gravity W = mg pointing straight down
        drawArrow(fCtx, bx, by, bx, by + 50, '#F43F5E', 'mg', 10);

      } else if (currentFrictionConcept === 'twoblock') {
        const F_app = parseFloat(document.getElementById('fricAppliedSlider').value);
        const m1 = 2.0;
        const m2 = 4.0;
        const a_max = muS * g;
        const F_max = (m1 + m2) * a_max;
        const isSlipping = F_app > F_max;

        // Floor
        fCtx.strokeStyle = '#475569';
        fCtx.lineWidth = 2.5;
        fCtx.beginPath();
        fCtx.moveTo(cx - 180, cy + 60);
        fCtx.lineTo(cx + 180, cy + 60);
        fCtx.stroke();

        // Bottom Block m2 (Blue) - moved by twoBlockX
        const b2W = 140;
        const b2H = 45;
        const b2X = cx - b2W / 2 + twoBlockX;
        const b2Y = cy + 15;

        fCtx.fillStyle = '#1e293b';
        fCtx.strokeStyle = '#38bdf8';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(b2X, b2Y, b2W, b2H);
        fCtx.strokeRect(b2X, b2Y, b2W, b2H);
        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 12px Consolas, monospace';
        fCtx.fillText(`Bottom Block B (m2=4kg)`, b2X + 10, b2Y + 28);

        // Pull Force F on bottom block
        if (F_app > 0) {
          const fLen = Math.min(80, 15 + F_app * 0.6);
          drawArrow(fCtx, b2X + b2W, b2Y + b2H / 2, b2X + b2W + fLen, b2Y + b2H / 2, '#FACC15', `F=${F_app}N`, 11);
        }

        // Top Block m1 (Amber) - displaced backward by twoBlockRelSlip when slipping
        const b1W = 80;
        const b1H = 40;
        const b1X = b2X + (b2W - b1W) / 2 - twoBlockRelSlip;
        const b1Y = b2Y - b1H;

        fCtx.fillStyle = '#334155';
        fCtx.strokeStyle = isSlipping ? '#F43F5E' : '#facc15';
        fCtx.lineWidth = 2.5;
        fCtx.fillRect(b1X, b1Y, b1W, b1H);
        fCtx.strokeRect(b1X, b1Y, b1W, b1H);
        fCtx.fillStyle = '#ffffff';
        fCtx.font = 'bold 11px Consolas, monospace';
        fCtx.fillText(`Top A (m1=2kg)`, b1X + 8, b1Y + 24);

        if (isSlipping) {
          fCtx.fillStyle = '#F43F5E';
          fCtx.font = 'bold 11px Consolas, monospace';
          fCtx.fillText('★ SLIPPING ACTIVE! (F > F_max)', cx - 80, cy - 60);

          // Friction vectors between blocks
          drawArrow(fCtx, b1X + 20, b1Y + b1H, b1X + 60, b1Y + b1H, '#4ADE80', 'f_k on A', 9);
          drawArrow(fCtx, b1X + 60, b2Y, b1X + 20, b2Y, '#F43F5E', 'f_k on B', 9);
        } else {
          fCtx.fillStyle = '#4ADE80';
          fCtx.font = 'bold 11px Consolas, monospace';
          fCtx.fillText('✓ LOCKED TOGETHER (F ≤ F_max)', cx - 75, cy - 60);
        }
      }
    }

    // ========================================================
    // ENGINE 3: MOMENTUM, IMPULSE & CONCURRENT IMPLEMENTATION
    // ========================================================
    let ballImpactX = 0;
    let ballDir = -1;
    let rocketH = 0;

    function setMomentumConcept(sub) {
      currentMomentumConcept = sub;
      document.getElementById('subMomImpulseBtn').className = sub === 'impulse' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subMomRocketBtn').className = sub === 'rocket' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subMomLamiBtn').className = sub === 'lami' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      if (sub === 'impulse') {
        document.getElementById('momHeader').innerText = "CONCEPT 4 • IMPULSE & MOMENTUM";
        document.getElementById('momTitle').innerText = "Area Under F-t Curve = Δp";
        document.getElementById('momFormula').innerText = "J = ∫F dt = Δp = m·(v_f - v_i) = 2mv";
        document.getElementById('momParam1Label').innerText = "Collision Speed (v):";
        document.getElementById('momParam2Label').innerText = "Ball Mass (m):";
        document.getElementById('momParam3Label').innerText = "Contact Duration (Δt):";
        document.getElementById('momMet1Label').innerText = "Initial Momentum (p_i):";
        document.getElementById('momMet2Label').innerText = "Rebound Momentum (p_f):";
        document.getElementById('momMet3Label').innerText = "Total Impulse J = Δp:";
        document.getElementById('momMet4Label').innerText = "Average Impact Force:";
      } else if (sub === 'rocket') {
        document.getElementById('momHeader').innerText = "CONCEPT 5 • CONSERVATION OF MOMENTUM";
        document.getElementById('momTitle').innerText = "Rocket Thrust & Recoil Dynamics";
        document.getElementById('momFormula').innerText = "F_thrust = u·(dm/dt) • a = (u/m)(dm/dt) - g";
        document.getElementById('momParam1Label').innerText = "Exhaust Velocity u (m/s):";
        document.getElementById('momParam2Label').innerText = "Fuel Burn dm/dt (kg/s):";
        document.getElementById('momParam3Label').innerText = "Rocket Mass M (x100kg):";
        document.getElementById('momMet1Label').innerText = "Upward Thrust Force:";
        document.getElementById('momMet2Label').innerText = "Rocket Gravity W:";
        document.getElementById('momMet3Label').innerText = "Net Acceleration (a):";
        document.getElementById('momMet4Label').innerText = "Recoil Velocity (V_rifle):";
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
        document.getElementById('momMet4Label').innerText = "Net Resultant Vector:";
      }
      updateMomentum();
    }

    function updateMomentum() {
      const v = parseFloat(document.getElementById('momSpeedSlider').value);
      const m = parseFloat(document.getElementById('momMassSlider').value);
      const dt = parseFloat(document.getElementById('momTimeSlider').value);

      document.getElementById('momSpeedVal').innerText = (currentMomentumConcept === 'rocket' ? (v * 100).toFixed(0) + ' m/s' : currentMomentumConcept === 'lami' ? v.toFixed(0) + ' N' : v.toFixed(1) + ' m/s');
      document.getElementById('momMassVal').innerText = (currentMomentumConcept === 'rocket' ? (m * 25).toFixed(1) + ' kg/s' : currentMomentumConcept === 'lami' ? (100 + m * 30).toFixed(0) + '°' : m.toFixed(2) + ' kg');
      document.getElementById('momTimeVal').innerText = (currentMomentumConcept === 'rocket' ? (dt * 15000).toFixed(0) + ' kg' : currentMomentumConcept === 'lami' ? (100 + dt * 1000).toFixed(0) + '°' : dt.toFixed(3) + ' s');

      if (currentMomentumConcept === 'impulse') {
        const p_i = m * v;
        const p_f = -m * v;
        const J = 2 * m * v;
        const F_avg = J / dt;
        document.getElementById('momInitP').innerText = '+' + p_i.toFixed(2) + ' kg·m/s';
        document.getElementById('momFinalP').innerText = p_f.toFixed(2) + ' kg·m/s';
        document.getElementById('momTotalJ').innerText = J.toFixed(2) + ' N·s (Doubled)';
        document.getElementById('momAvgF').innerText = F_avg.toFixed(0) + ' N';
      } else if (currentMomentumConcept === 'rocket') {
        const u = v * 100;
        const dmdt = m * 25;
        const M = Math.max(100, dt * 15000);
        const F_thrust = u * dmdt;
        const W = M * 9.8;
        const a_net = Math.max(0, (F_thrust - W) / M);
        document.getElementById('momInitP').innerText = F_thrust.toFixed(0) + ' N';
        document.getElementById('momFinalP').innerText = W.toFixed(0) + ' N';
        document.getElementById('momTotalJ').innerText = a_net.toFixed(2) + ' m/s²';
        document.getElementById('momAvgF').innerText = `V_recoil = -${((0.02 * 600) / 4).toFixed(1)} m/s`;
      } else if (currentMomentumConcept === 'lami') {
        const F1 = v;
        const alpha = (100 + m * 30) * Math.PI / 180;
        const beta = (100 + dt * 1000) * Math.PI / 180;
        const gamma = 2 * Math.PI - (alpha + beta);
        const F2 = F1 * Math.sin(beta) / Math.sin(alpha);
        const F3 = F1 * Math.sin(gamma) / Math.sin(alpha);
        document.getElementById('momInitP').innerText = Math.abs(F2).toFixed(1) + ' N';
        document.getElementById('momFinalP').innerText = Math.abs(F3).toFixed(1) + ' N';
        document.getElementById('momTotalJ').innerText = ((gamma * 180 / Math.PI)).toFixed(0) + '°';
        document.getElementById('momAvgF').innerText = '0.00 N (Zero Net Loop)';
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
        const v = parseFloat(document.getElementById('momSpeedSlider').value);
        const m = parseFloat(document.getElementById('momMassSlider').value);
        const dt = parseFloat(document.getElementById('momTimeSlider').value);
        const J = 2 * m * v;
        const F_peak = Math.min(1000, J / dt);

        // LEFT: Elastic Wall & Rebounding Ball
        const wallX = 60;
        mCtx.fillStyle = '#475569';
        mCtx.fillRect(wallX - 15, cy - 80, 15, 160);
        mCtx.strokeStyle = '#94a3b8';
        mCtx.strokeRect(wallX - 15, cy - 80, 15, 160);

        // Moving Ball
        const bRad = 15 + m * 10;
        const ballPos = wallX + bRad + ballImpactX;

        mCtx.fillStyle = '#38bdf8';
        mCtx.beginPath();
        mCtx.arc(ballPos, cy, bRad, 0, Math.PI * 2);
        mCtx.fill();
        mCtx.strokeStyle = '#ffffff';
        mCtx.lineWidth = 2;
        mCtx.stroke();

        // Vector arrow on ball
        if (ballDir === -1) {
          drawArrow(mCtx, ballPos, cy - bRad - 12, ballPos - 35, cy - bRad - 12, '#38bdf8', `+v (${v}m/s)`, 10);
        } else {
          drawArrow(mCtx, ballPos, cy - bRad - 12, ballPos + 35, cy - bRad - 12, '#F43F5E', `-v (Rebound)`, 10);
        }

        // RIGHT: Dynamic F-t Pulse Curve
        const ox = cx + 20;
        const oy = cy + 60;
        const gw = w - ox - 35;
        const gh = 120;

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

        // Pulse width proportional to dt, height proportional to F_peak
        const pWidth = Math.min(gw * 0.7, (dt / 0.05) * gw * 0.6 + 25);
        const pHeight = Math.min(gh * 0.85, (F_peak / 1000) * gh * 0.8 + 20);
        const pStart = ox + gw * 0.15;
        const pMid = pStart + pWidth / 2;
        const pEnd = pStart + pWidth;

        mCtx.fillStyle = 'rgba(74, 222, 128, 0.25)';
        mCtx.strokeStyle = '#4ade80';
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
        mCtx.fillText(`Area = J = Δp = ${J.toFixed(1)} N·s`, pMid - 40, oy - pHeight / 2);

      } else if (currentMomentumConcept === 'rocket') {
        // ROCKET ANIMATION
        const rX = cx;
        const rY = cy + 20 - rocketH;

        // Exhaust flame
        const flameLen = 30 + (Math.sin(Date.now() * 0.02) * 8) + 20;
        mCtx.fillStyle = '#f59e0b';
        mCtx.beginPath();
        mCtx.moveTo(rX - 12, rY + 45);
        mCtx.lineTo(rX + 12, rY + 45);
        mCtx.lineTo(rX, rY + 45 + flameLen);
        mCtx.closePath();
        mCtx.fill();

        // Inner blue flame core
        mCtx.fillStyle = '#38bdf8';
        mCtx.beginPath();
        mCtx.moveTo(rX - 6, rY + 45);
        mCtx.lineTo(rX + 6, rY + 45);
        mCtx.lineTo(rX, rY + 45 + flameLen * 0.6);
        mCtx.closePath();
        mCtx.fill();

        // Rocket Body
        mCtx.fillStyle = '#1e293b';
        mCtx.strokeStyle = '#38bdf8';
        mCtx.lineWidth = 2.5;
        mCtx.beginPath();
        mCtx.moveTo(rX, rY - 45);
        mCtx.lineTo(rX + 18, rY - 15);
        mCtx.lineTo(rX + 18, rY + 45);
        mCtx.lineTo(rX - 18, rY + 45);
        mCtx.lineTo(rX - 18, rY - 15);
        mCtx.closePath();
        mCtx.fill();
        mCtx.stroke();

        // Fins
        mCtx.fillStyle = '#475569';
        mCtx.beginPath();
        mCtx.moveTo(rX - 18, rY + 20);
        mCtx.lineTo(rX - 32, rY + 45);
        mCtx.lineTo(rX - 18, rY + 45);
        mCtx.closePath();
        mCtx.fill();

        mCtx.beginPath();
        mCtx.moveTo(rX + 18, rY + 20);
        mCtx.lineTo(rX + 32, rY + 45);
        mCtx.lineTo(rX + 18, rY + 45);
        mCtx.closePath();
        mCtx.fill();

        // Thrust vector arrow (Up)
        drawArrow(mCtx, rX + 45, rY, rX + 45, rY - 50, '#4ADE80', 'F_thrust = u(dm/dt)', 11);

        // Exhaust velocity arrow (Down)
        drawArrow(mCtx, rX - 45, rY + 45, rX - 45, rY + 45 + 40, '#f59e0b', 'u_exhaust', 10);

      } else if (currentMomentumConcept === 'lami') {
        const F1 = parseFloat(document.getElementById('momSpeedSlider').value);
        const m = parseFloat(document.getElementById('momMassSlider').value);
        const dt = parseFloat(document.getElementById('momTimeSlider').value);
        const alpha = (100 + m * 30) * Math.PI / 180;
        const beta = (100 + dt * 1000) * Math.PI / 180;
        const gamma = 2 * Math.PI - (alpha + beta);
        const F2 = Math.abs(F1 * Math.sin(beta) / Math.sin(alpha));
        const F3 = Math.abs(F1 * Math.sin(gamma) / Math.sin(alpha));

        // Knot at center
        mCtx.fillStyle = '#ffffff';
        mCtx.beginPath();
        mCtx.arc(cx - 50, cy, 6, 0, Math.PI * 2);
        mCtx.fill();

        // Force 1 (Pointing Straight Up)
        const l1 = Math.min(80, 20 + F1 * 0.7);
        drawArrow(mCtx, cx - 50, cy, cx - 50, cy - l1, '#38bdf8', `F1=${F1.toFixed(0)}N`, 11);

        // Force 2 (At angle alpha relative to F3, or beta from F1)
        const ang2 = -Math.PI / 2 + beta;
        const l2 = Math.min(80, 20 + F2 * 0.7);
        drawArrow(mCtx, cx - 50, cy, cx - 50 + l2 * Math.cos(ang2), cy + l2 * Math.sin(ang2), '#facc15', `F2=${F2.toFixed(0)}N`, 11);

        // Force 3
        const ang3 = -Math.PI / 2 - (2 * Math.PI - (beta + alpha));
        const l3 = Math.min(80, 20 + F3 * 0.7);
        drawArrow(mCtx, cx - 50, cy, cx - 50 + l3 * Math.cos(ang3), cy + l3 * Math.sin(ang3), '#F43F5E', `F3=${F3.toFixed(0)}N`, 11);

        // Closed Vector Triangle Proof on Right
        const tx = cx + 80;
        const ty = cy - 30;
        mCtx.strokeStyle = '#4ade80';
        mCtx.lineWidth = 2;
        mCtx.beginPath();
        mCtx.moveTo(tx, ty);
        mCtx.lineTo(tx, ty + l1 * 0.7);
        mCtx.lineTo(tx + 50, ty + l1 * 0.7 + 25);
        mCtx.closePath();
        mCtx.stroke();
        mCtx.fillStyle = '#4ade80';
        mCtx.font = 'bold 11px Consolas, monospace';
        mCtx.fillText('Closed Vector Triangle', tx - 20, ty + l1 * 0.7 + 45);
        mCtx.fillText('Σ F = 0', tx + 10, ty + l1 * 0.7 + 60);
      }
    }

    // ========================================================
    // ENGINE 4: CIRCULAR DYNAMICS & BANKING IMPLEMENTATION
    // ========================================================
    let circCarAngle = 0;

    function setCircConcept(sub) {
      currentCircConcept = sub;
      document.getElementById('subCircFlatBtn').className = sub === 'flat' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';
      document.getElementById('subCircBankedBtn').className = sub === 'banked' ? 'sub-preset-btn active px-3 py-1 rounded-lg border text-xs transition' : 'sub-preset-btn px-3 py-1 rounded-lg border text-xs transition';

      const optRow = document.getElementById('circOptRow');

      if (sub === 'flat') {
        document.getElementById('circHeader').innerText = "CONCEPT 10 • LEVEL CIRCULAR ROAD";
        document.getElementById('circTitle').innerText = "Static Friction Provides Centripetal Force";
        document.getElementById('circFormula').innerText = "f_s = m·v²/r ≤ μ_s·m·g => v_max = √(μ_s·r·g)";
        document.getElementById('circParam1Label').innerText = "Turn Radius (r):";
        document.getElementById('circParam2Label').innerText = "Road Friction (μ_s):";
        document.getElementById('circParam3Label').innerText = "Car Speed (v):";
        document.getElementById('circSpeed1Label').innerText = "Max Safe Speed (v_max):";
        optRow.classList.add('hidden');
      } else {
        document.getElementById('circHeader').innerText = "CONCEPT 11 • ENGINEERED BANKED ROAD";
        document.getElementById('circTitle').innerText = "Optimal Speed & Vertical Circle Loop";
        document.getElementById('circFormula').innerText = "v_opt = √(rg·tanθ) • v_max = √[rg(tanθ+μ)/(1-μ·tanθ)]";
        document.getElementById('circParam1Label').innerText = "Turn Radius (r):";
        document.getElementById('circParam2Label').innerText = "Road Friction (μ):";
        document.getElementById('circParam3Label').innerText = "Banking Angle (θ):";
        document.getElementById('circSpeed1Label').innerText = "Max Speed w/ Friction:";
        optRow.classList.remove('hidden');
      }
      updateCircular();
    }

    function updateCircular() {
      const r = parseFloat(document.getElementById('circRadiusSlider').value);
      const mu = parseFloat(document.getElementById('circMuSlider').value);
      const param3 = parseFloat(document.getElementById('circAngleSlider').value);
      const g = 9.8;

      document.getElementById('circRadiusVal').innerText = r.toFixed(0) + ' m';
      document.getElementById('circMuVal').innerText = mu.toFixed(2);

      if (currentCircConcept === 'flat') {
        const v_car_kmh = param3;
        const v_car_ms = v_car_kmh / 3.6;
        document.getElementById('circAngleVal').innerText = v_car_kmh.toFixed(0) + ' km/h';

        const v_max_ms = Math.sqrt(mu * r * g);
        const v_max_kmh = v_max_ms * 3.6;
        document.getElementById('circSpeed1Val').innerText = v_max_ms.toFixed(1) + ' m/s (' + v_max_kmh.toFixed(1) + ' km/h)';

        if (v_car_ms <= v_max_ms) {
          document.getElementById('circVertLoopVal').innerText = "SAFE (Grip Maintained)";
          document.getElementById('circVertLoopVal').className = "text-emerald-400 font-bold";
        } else {
          document.getElementById('circVertLoopVal').innerText = "SKIDDING HAZARD! (Exceeds v_max)";
          document.getElementById('circVertLoopVal').className = "text-rose-400 font-bold animate-pulse";
        }
      } else {
        const theta = param3;
        const rad = theta * Math.PI / 180;
        document.getElementById('circAngleVal').innerText = theta.toFixed(0) + '°';

        const v_opt = Math.sqrt(r * g * Math.tan(rad));
        document.getElementById('circOptVal').innerText = v_opt.toFixed(1) + ' m/s (' + (v_opt * 3.6).toFixed(1) + ' km/h)';

        const num = Math.tan(rad) + mu;
        const den = 1 - mu * Math.tan(rad);
        const v_max = den > 0 ? Math.sqrt(r * g * (num / den)) : 999;
        document.getElementById('circSpeed1Val').innerText = v_max.toFixed(1) + ' m/s (' + (v_max * 3.6).toFixed(1) + ' km/h)';

        document.getElementById('circVertLoopVal').innerText = 'Loop Bottom ≥ √(5gr) = ' + Math.sqrt(5 * g * (r / 5)).toFixed(1) + ' m/s';
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
      const r = parseFloat(document.getElementById('circRadiusSlider').value);
      const mu = parseFloat(document.getElementById('circMuSlider').value);
      const g = 9.8;

      if (currentCircConcept === 'flat') {
        const v_car_kmh = parseFloat(document.getElementById('circAngleSlider').value);
        const v_car_ms = v_car_kmh / 3.6;
        const v_max_ms = Math.sqrt(mu * r * g);
        const isSkidding = v_car_ms > v_max_ms;

        // Circular Road
        const plotR = Math.min(w * 0.38, 50 + r * 1.2);
        cCtx.strokeStyle = '#334155';
        cCtx.lineWidth = 26;
        cCtx.beginPath();
        cCtx.arc(cx, cy, plotR, 0, Math.PI * 2);
        cCtx.stroke();

        // Center line
        cCtx.strokeStyle = '#64748b';
        cCtx.lineWidth = 1.5;
        cCtx.setLineDash([5, 5]);
        cCtx.beginPath();
        cCtx.arc(cx, cy, plotR, 0, Math.PI * 2);
        cCtx.stroke();
        cCtx.setLineDash([]);

        // Car position (if skidding, drifts outward)
        const drift = isSkidding ? 18 : 0;
        const carR = plotR + drift;
        const carX = cx + carR * Math.cos(circCarAngle);
        const carY = cy + carR * Math.sin(circCarAngle);

        // Car body
        cCtx.fillStyle = isSkidding ? '#F43F5E' : '#38bdf8';
        cCtx.beginPath();
        cCtx.arc(carX, carY, 9, 0, Math.PI * 2);
        cCtx.fill();
        cCtx.strokeStyle = '#ffffff';
        cCtx.lineWidth = 2;
        cCtx.stroke();

        // Centripetal friction vector arrow (toward center)
        const inX = -Math.cos(circCarAngle);
        const inY = -Math.sin(circCarAngle);
        const arrowLen = Math.min(45, (v_car_ms / v_max_ms) * 35);
        drawArrow(cCtx, carX, carY, carX + inX * arrowLen, carY + inY * arrowLen, isSkidding ? '#F43F5E' : '#4ADE80', isSkidding ? 'SLIP!' : 'f_s', 10);

        if (isSkidding) {
          cCtx.fillStyle = '#F43F5E';
          cCtx.font = 'bold 12px Consolas, monospace';
          cCtx.fillText('★ SKIDDING OUTWARD! (v > v_max)', cx - 90, cy - plotR - 25);
        } else {
          cCtx.fillStyle = '#4ADE80';
          cCtx.font = 'bold 12px Consolas, monospace';
          cCtx.fillText('✓ SAFE TIRE GRIP (f_s supplies mv²/r)', cx - 100, cy - plotR - 25);
        }

      } else if (currentCircConcept === 'banked') {
        const theta = parseFloat(document.getElementById('circAngleSlider').value);
        const rad = theta * Math.PI / 180;
        const wedgeW = Math.min(280, w * 0.5);

        // Banked Road Cross-Section Wedge
        const wx = cx - wedgeW / 2;
        const wy = cy + 60;
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
        cCtx.arc(wx, wy, 40, 0, -rad, true);
        cCtx.stroke();
        cCtx.fillStyle = '#facc15';
        cCtx.font = 'bold 12px Consolas, monospace';
        cCtx.fillText(`θ = ${theta}°`, wx + 50, wy - 10);

        // Vehicle on Banked Surface
        const carMidX = wx + wedgeW * 0.5;
        const carMidY = wy - wedgeH * 0.5;

        cCtx.save();
        cCtx.translate(carMidX, carMidY);
        cCtx.rotate(-rad);
        cCtx.fillStyle = '#1e293b';
        cCtx.strokeStyle = '#38bdf8';
        cCtx.lineWidth = 2.5;
        cCtx.fillRect(-20, -30, 40, 30);
        cCtx.strokeRect(-20, -30, 40, 30);
        cCtx.fillStyle = '#ffffff';
        cCtx.font = 'bold 10px Consolas, monospace';
        cCtx.fillText('CAR', -10, -12);

        // Normal reaction perpendicular to road
        drawArrow(cCtx, 0, -15, 0, -65, '#4ADE80', 'N (Normal)', 10);
        cCtx.restore();

        // Normal Force Components (drawn in global space)
        drawArrow(cCtx, carMidX, carMidY - 30, carMidX - 45, carMidY - 30, '#38bdf8', 'N·sinθ (Centripetal)', 10);
        drawArrow(cCtx, carMidX, carMidY - 30, carMidX, carMidY - 70, '#4ADE80', 'N·cosθ = mg', 10);
      }
    }

    // ========================================================
    // SMOOTH UNIFIED ANIMATION ENGINE
    // ========================================================
    let lastTime = performance.now();

    function masterPhysicsLoop(now) {
      const dt = Math.min(0.1, (now - lastTime) / 1000);
      lastTime = now;

      if (currentMode === 'newton') {
        if (currentNewtonConcept === 'tension') {
          const m1 = parseFloat(document.getElementById('newtonMassSlider').value);
          const m2 = Math.max(0.5, parseFloat(document.getElementById('newtonForceSlider').value) / 4);
          const a = (m1 - m2) * 9.8 / (m1 + m2);
          atwoodSpeed += a * dt * 4;
          atwoodY += atwoodSpeed * dt;
          if (atwoodY > 40) { atwoodY = 40; atwoodSpeed = -atwoodSpeed * 0.6; }
          if (atwoodY < -40) { atwoodY = -40; atwoodSpeed = -atwoodSpeed * 0.6; }
          drawNewtonCanvas();
        }
      } else if (currentMode === 'friction') {
        if (currentFrictionConcept === 'graph') {
          const F_app = parseFloat(document.getElementById('fricAppliedSlider').value);
          const muS = parseFloat(document.getElementById('fricMuSSlider').value);
          const fs_max = muS * 5.0 * 9.8;
          if (F_app > fs_max) {
            slideX = (slideX + (F_app - fs_max) * dt * 3) % 120;
          } else {
            slideX = 0;
          }
          drawFrictionCanvas();
        } else if (currentFrictionConcept === 'incline') {
          const theta = parseFloat(document.getElementById('fricInclineSlider').value);
          const muS = parseFloat(document.getElementById('fricMuSSlider').value);
          const muK = parseFloat(document.getElementById('fricMuKSlider').value);
          const thetaR = Math.atan(muS) * 180 / Math.PI;
          if (theta > thetaR) {
            const aDown = 9.8 * (Math.sin(theta * Math.PI / 180) - muK * Math.cos(theta * Math.PI / 180));
            inclineBlockPos = (inclineBlockPos + Math.max(0.5, aDown) * dt * 18) % 100;
          } else {
            inclineBlockPos = 0;
          }
          drawFrictionCanvas();
        } else if (currentFrictionConcept === 'twoblock') {
          const F_app = parseFloat(document.getElementById('fricAppliedSlider').value);
          const muS = parseFloat(document.getElementById('fricMuSSlider').value);
          const F_max = 6.0 * muS * 9.8;
          if (F_app > 0) {
            twoBlockX = (twoBlockX + (F_app / 6.0) * dt * 2) % 100;
            if (F_app > F_max) {
              twoBlockRelSlip = Math.min(25, twoBlockRelSlip + dt * 15);
            } else {
              twoBlockRelSlip = Math.max(0, twoBlockRelSlip - dt * 20);
            }
          }
          drawFrictionCanvas();
        }
      } else if (currentMode === 'momentum') {
        if (currentMomentumConcept === 'impulse') {
          const v = parseFloat(document.getElementById('momSpeedSlider').value);
          ballImpactX += ballDir * v * dt * 8;
          if (ballImpactX < -80) {
            ballImpactX = -80;
            ballDir = 1;
          } else if (ballImpactX > 120) {
            ballImpactX = 120;
            ballDir = -1;
          }
          drawMomentumCanvas();
        } else if (currentMomentumConcept === 'rocket') {
          rocketH = (rocketH + dt * 25) % 120;
          drawMomentumCanvas();
        }
      } else if (currentMode === 'circular') {
        const v = parseFloat(document.getElementById('circAngleSlider').value);
        circCarAngle = (circCarAngle + (v / 60) * dt * 3) % (Math.PI * 2);
        drawCircularCanvas();
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
    // DEEP-LINK URL ROUTER DISPATCH AT SCRIPT BOTTOM (RULE 17)
    // ========================================================
    function applyConceptOrMode() {
      const params = new URLSearchParams(window.location.search);
      const conceptParam = params.get('concept');
      const modeParam = params.get('mode');

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

    // Trigger router at initialization
    applyConceptOrMode();
  </script>
</body>
</html>
'''

target_html.write_text(html_content, encoding="utf-8")
print(f"Successfully generated {target_html} with {len(html_content.splitlines())} lines.")
