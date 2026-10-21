import csv
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "queue" / "curriculum_master_full_665.csv"

UNIT_1_UPDATES = {
    "P11-C01-T01-V01": {
        "concept_title": "SI Base Quantities & Supplementary Units",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"d\theta = \frac{ds}{r} \text{ [rad]}, \quad d\Omega = \frac{dA}{r^2} \text{ [sr]}",
        "plain_formula": "dθ = ds / r (rad), dΩ = dA / r² (sr)",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 16-18",
        "ncert_core_rule": "7 fundamental SI base quantities define all physical measurement. Radian and steradian are supplementary dimensionless units.",
        "author_book_nuance": "H.C. Verma: A quantity can possess units without dimensions (rad, sr), but no quantity can possess dimensions without units.",
        "neet_trap_point": "Students assume all quantities with units have dimensions. Plane angle has unit radian but dimension [M^0 L^0 T^0].",
        "pyq_years": "2022, 2019",
        "status": "ready"
    },
    "P11-C01-T01-V02": {
        "concept_title": "Derived Units & Standard Metric Prefixes",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"1\text{ N} = 1\text{ kg}\cdot\text{m}\cdot\text{s}^{-2}, \quad 1\text{ J} = 1\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-2}",
        "plain_formula": "1 N = 1 kg·m/s², 1 J = 1 kg·m²/s²",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 17-20",
        "ncert_core_rule": "Derived units are algebraic combinations of base units. SI prefixes represent powers of 10 from 10^-15 to 10^12.",
        "author_book_nuance": "D.C. Pandey: Double prefixes are strictly forbidden in SI rules (e.g., write pF, never μμF).",
        "neet_trap_point": "Attaching prefixes to kilogram instead of gram. Since kg already has 'kilo', write 1 mg for 10^-6 kg, not 1 μkg.",
        "pyq_years": "2021, 2020",
        "status": "ready"
    },
    "P11-C01-T02-V03": {
        "concept_title": "Dimensions of Physical Quantities & Common Equivalences",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"[h] = [L] = [M L^2 T^{-1}], \quad [P] = [\text{Stress}] = [\text{Energy Density}] = [M L^{-1} T^{-2}]",
        "plain_formula": "[h] = [L] = [M L² T⁻¹], [Stress] = [Pressure] = [Energy Density] = [M L⁻¹ T⁻²]",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 22-24",
        "ncert_core_rule": "Dimensions of a physical quantity are powers to which base units are raised to represent that quantity.",
        "author_book_nuance": "Halliday & Resnick: Torque and Work share identical dimensions [M L^2 T^-2] but are fundamentally different: Torque is a vector, Work is a scalar.",
        "neet_trap_point": "Confusing quantities that share identical dimensions with being physically identical. Never equate their physical nature.",
        "pyq_years": "2023, 2022, 2020, 2019",
        "status": "ready"
    },
    "P11-C01-T02-V04": {
        "concept_title": "Principle of Homogeneity of Dimensions",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"\left[P + \frac{a}{V^2}\right] \implies [a] = [P][V^2] = [M L^5 T^{-2}], \quad [b] = [V] = [L^3]",
        "plain_formula": "[a] = [P][V²] = [M L⁵ T⁻²], [b] = [V] = [L³]",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 24-26",
        "ncert_core_rule": "Physical quantities having identical dimensions alone can be added, subtracted, or equated. Arguments of trig, exp, and log functions must be dimensionless.",
        "author_book_nuance": "I.E. Irodov: In (P + a/V^2)(V - b) = RT, dimensional homogeneity dictates [a/V^2] = [P] and [b] = [V].",
        "neet_trap_point": "Assuming dimensional consistency guarantees physical correctness. Pure numbers (like 1/2 or 2π) cannot be derived or checked by dimensional analysis.",
        "pyq_years": "2021, 2018, 2017",
        "status": "ready"
    },
    "P11-C01-T03-V05": {
        "concept_title": "Classification of Errors & Mean Absolute Error",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"a_{\text{mean}} = \frac{1}{n}\sum_{i=1}^n a_i, \quad \Delta a_{\text{mean}} = \frac{1}{n}\sum_{i=1}^n |\Delta a_i|",
        "plain_formula": "a_mean = (Σ a_i) / n, Δa_mean = (Σ |a_mean - a_i|) / n",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 20-22",
        "ncert_core_rule": "Systematic errors are unidirectional and eliminated by calibration. Random errors fluctuate and are minimized by taking the arithmetic mean of repeated readings.",
        "author_book_nuance": "H.C. Verma: Absolute error is always positive. The sum of signed deviations from the mean is always identically zero.",
        "neet_trap_point": "Taking the algebraic sum of deviations instead of the magnitude |Δa_i|, which falsely gives zero mean error.",
        "pyq_years": "2023, 2020",
        "status": "ready"
    },
    "P11-C01-T03-V06": {
        "concept_title": "Combination & Propagation of Errors (Power Rule)",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"Z = \frac{A^p B^q}{C^r} \implies \frac{\Delta Z}{Z} = p\frac{\Delta A}{A} + q\frac{\Delta B}{B} + r\frac{\Delta C}{C}",
        "plain_formula": "Z = (A^p * B^q) / C^r  ==>  ΔZ/Z = p*(ΔA/A) + q*(ΔB/B) + r*(ΔC/C)",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 22-24",
        "ncert_core_rule": "In worst-case error estimation, fractional errors for product, quotient, and power relations always add with their positive power coefficients.",
        "author_book_nuance": "D.C. Pandey: Even if C is in the denominator (C^r), its fractional error is added with coefficient +r, never subtracted!",
        "neet_trap_point": "Subtracting errors for quantities in the denominator. Errors always accumulate in maximum uncertainty analysis.",
        "pyq_years": "2023, 2022, 2021, 2019, 2013",
        "status": "ready"
    },
    "P11-C01-T04-V07": {
        "concept_title": "Measuring Instruments: Vernier Callipers & Screw Gauge",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"LC = \frac{\text{Pitch}}{\text{No. of Circular Divisions}}, \quad \text{True} = \text{Observed} - (\pm\text{Zero Error})",
        "plain_formula": "LC = Pitch / Circular Divisions, True = Observed - (±Zero Error)",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2 Appendix & Practical Manual",
        "ncert_core_rule": "Vernier LC = 1 MSD - 1 VSD. Screw gauge LC = Pitch / Total circular divisions. True reading = Observed reading - (Zero Error).",
        "author_book_nuance": "NCERT Lab Manual: Positive zero error is SUBTRACTED; negative zero error is ADDED (- (-e) = +e).",
        "neet_trap_point": "Inverting zero error signs: Positive zero error (+e) must be subtracted, while negative zero error (-e) must be added.",
        "pyq_years": "2024, 2023, 2021, 2020, 2018",
        "status": "ready"
    },
    "P11-C01-T04-V08": {
        "concept_title": "Significant Figures & Arithmetic Rounding Rules",
        "template_name": "FormulaWithGraph",
        "dimension": "2d",
        "storyboard_ui_archetype": "ORTHOGONAL_SPLIT",
        "latex_formula": r"\text{Add/Sub: Least Decimal Places}, \quad \text{Mul/Div: Least Significant Figures}",
        "plain_formula": "Add/Sub: Retain least decimal places | Mul/Div: Retain least significant figures",
        "ncert_citation": "NCERT Class 11 Part 1, Chapter 2, Pages 27-30",
        "ncert_core_rule": "Significant figures reflect measurement precision. Leading zeros are never significant; trailing zeros with a decimal point are significant.",
        "author_book_nuance": "H.C. Verma: In addition 100.1 + 0.003 = 100.103 -> 100.1 (1 decimal place). Do not count total significant figures in addition/subtraction.",
        "neet_trap_point": "Applying the multiplication rule (least sig figs) to addition/subtraction, which is governed strictly by the least decimal places.",
        "pyq_years": "2022, 2020, 2019, 2018",
        "status": "ready"
    }
}

def update_curriculum():
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = list(rows[0].keys())
    updated_count = 0

    for r in rows:
        cid = r.get("canonical_id")
        if cid in UNIT_1_UPDATES:
            updates = UNIT_1_UPDATES[cid]
            for k, v in updates.items():
                r[k] = v
            updated_count += 1

    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ Successfully updated {updated_count} Unit 1 concepts in {CSV_PATH.name}")

if __name__ == "__main__":
    update_curriculum()
