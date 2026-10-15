# Universal NotebookLM Extraction Prompt for NEET UG Video Engine

Use this exact prompt inside **NotebookLM** where your NCERT textbooks, Exemplars, PYQs (2016–2026), and Author books (HC Verma / DC Pandey) are uploaded.

---

## The Master NotebookLM Extraction Prompt

Copy and paste the block below into your NotebookLM chat:

```text
You are a NEET UG Curriculum & Fact Extraction Assistant.
Based STRICTLY and ONLY on the uploaded sources (NCERT Class 11/12 Physics textbooks, Exemplars, NEET UG PYQs 2016-2026, and Author reference books like HC Verma / DC Pandey):

Target Topic: [REPLACE WITH TOPIC NAME, e.g., "Horizontal Range in Projectile Motion"]
Chapter: [REPLACE WITH CHAPTER NAME, e.g., "Motion in a Plane, Class 11"]

Extract the required details and output in the exact structured format below. Do not add conversational intro/outro.

1. canonical_id: [e.g. P11-C04-T02-V02]
2. concept_title: [Concise 3-5 word concept title]
3. template_name: [FormulaWithGraph | VectorDiagram | DerivationStep | WaveDiagram | TwoColumnCompare]
4. dimension: [2d | 3d]
5. latex_formula: [Exact primary formula in LaTeX math]
6. plain_formula: [Plain readable text format, e.g. R = (v_0^2 * sin(2θ)) / g]
7. ncert_citation: [Exact book, chapter number, page reference, e.g., NCERT Class 11 Part 1, Ch 4, Page 79]
8. ncert_core_rule: [1-2 sentences stating the fundamental physical principle verbatim from NCERT]
9. author_book_nuance: [1 crucial pedagogical insight from HC Verma or DC Pandey clarifying why students get confused]
10. neet_trap_point: [The exact deceptive distractor trick examiners use in NEET multiple choice options]
11. pyq_years: [List all NEET/AIPMT exam years and question numbers where this appeared, e.g., 2017, 2020, 2023]
```

---

## Example: Output from NotebookLM

When you query NotebookLM for *"Horizontal Range"*, it will return:

```text
1. canonical_id: P11-C04-T02-V02
2. concept_title: Horizontal Range and Complementary Angles
3. template_name: FormulaWithGraph
4. dimension: 2d
5. latex_formula: R = \frac{v_0^2 \sin(2\theta)}{g}
6. plain_formula: R = (v_0^2 * sin(2θ)) / g
7. ncert_citation: NCERT Class 11 Part 1, Ch 4, Page 79
8. ncert_core_rule: Horizontal range is identical for complementary projection angles θ and (90° - θ) at the same initial speed.
9. author_book_nuance: HCV Ch 3: Although ranges are equal for θ and 90°-θ, maximum heights and times of flight are strictly unequal.
10. neet_trap_point: Assuming time of flight and maximum height are also equal when ranges are equal for complementary angles.
11. pyq_years: 2017, 2020, 2023
```

---

## Batch Extraction Prompt (For an Entire Chapter Topic)

To extract an entire subtopic in one shot from NotebookLM, paste:

```text
For Chapter [Insert Chapter, e.g., "Motion in a Plane, Class 11"], list all atomic concept video nodes for Topic: [e.g., "Projectile Motion"]. 

Output as a CSV-formatted table with columns:
canonical_id,subject,grade,chapter_no,chapter_name,topic_no,topic_name,video_no,concept_title,template_name,dimension,latex_formula,plain_formula,ncert_citation,ncert_core_rule,author_book_nuance,neet_trap_point,pyq_years,status

Ensure every formula is verified against NCERT page citations and every trap point corresponds to a real NEET question option.
```
