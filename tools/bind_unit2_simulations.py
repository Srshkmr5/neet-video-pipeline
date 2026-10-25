import json
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
manifest_path = BASE_DIR / "apps" / "curriculum_manifest.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

sim_mapping = {
    "P11-C02-T01-V01": "/simulations/unit_02_kinematics_lab.html?mode=graphs",
    "P11-C02-T02-V01": "/simulations/unit_02_kinematics_lab.html?mode=vectors",
    "P11-C02-T03-V01": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T03-V02": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T03-V03": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T03-V04": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T04-V01": "/simulations/unit_02_kinematics_lab.html?mode=circular",
    "P11-C02-T03-V08": "/simulations/unit_02_kinematics_lab.html?mode=graphs",
    "P11-C02-T03-V09": "/simulations/unit_02_kinematics_lab.html?mode=vectors",
    "P11-C02-T04-V10": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T04-V11": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T04-V12": "/simulations/unit_02_kinematics_lab.html?mode=projectile",
    "P11-C02-T05-V13": "/simulations/unit_02_kinematics_lab.html?mode=circular",
    "P11-C02-T05-V14": "/simulations/unit_02_kinematics_lab.html?mode=circular",
}

updated = 0
for concept in manifest["concepts"]:
    cid = concept.get("canonical_id")
    if cid in sim_mapping:
        concept["simulation"] = sim_mapping[cid]
        updated += 1

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Updated {updated} concepts in curriculum_manifest.json with dedicated Kinematics simulations!")
