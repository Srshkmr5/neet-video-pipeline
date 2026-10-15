# NEET UG Video Engine: End-to-End Operational Playbook

This playbook provides the simple, practical workflow connecting **NotebookLM**, your **Google Sheet**, and the **Antigravity Render Engine**.

---

## The 5-Step Production Workflow

```
[1. NotebookLM (Fact Extraction)] 
       ⬇
[2. Master Google Sheet (Review & Store)] 
       ⬇ (Download as CSV)
[3. Antigravity Importer (`llm/curriculum_importer.py`)] 
       ⬇ (Auto-generates Multilingual Scripts & JSON)
[4. Antigravity Render Engine (`python main.py`)] 
       ⬇
[5. Finished 1080p MP4 (3 Audio Tracks + 3 Soft Subtitles)]
```

---

## Step 1: Set Up Your Sources in NotebookLM

1. Open [Google NotebookLM](https://notebooklm.google.com).
2. Create a Notebook named **`NEET UG Physics`** (or Chemistry / Biology).
3. Upload your source PDFs:
   - NCERT Class 11 & Class 12 Textbooks
   - NCERT Exemplars
   - NEET UG / AIPMT Past Year Questions (2016–2026)
   - Author reference books (HC Verma *Concepts of Physics*, DC Pandey)

---

## Step 2: Extract Facts Using the Universal Prompt

Open the chat in NotebookLM, paste the extraction prompt from [`llm/prompts/notebooklm_extractor.md`](file:///c:/Software%20check/neet-video-pipeline_1/llm/prompts/notebooklm_extractor.md), and specify your topic:

> *"Target Topic: Horizontal Range in Projectile Motion*  
> *Chapter: Motion in a Plane, Class 11"*

NotebookLM will return the structured facts:
- **Canonical ID**: `P11-C04-T02-V02`
- **Concept Title**: Horizontal Range and Complementary Angles
- **Template**: `FormulaWithGraph`
- **Formula**: $R = \frac{v_0^2 \sin(2\theta)}{g}$
- **NCERT Citation**: `NCERT Class 11 Part 1, Ch 4, Page 79`
- **NCERT Core Rule**: *Horizontal range is identical for complementary projection angles $\theta$ and $(90^\circ - \theta)$ at the same speed.*
- **Author Book Nuance**: *HCV Ch 3: Although ranges are equal, maximum heights and times of flight are strictly unequal.*
- **NEET Trap Point**: *Assuming time of flight and maximum height are also equal when ranges are equal for complementary angles.*
- **PYQ Years**: `2017, 2020, 2023`

---

## Step 3: Paste into Your Master Google Sheet

1. In Google Drive, create a new Google Sheet named **`NEET_Curriculum_Master`**.
2. Go to **File $\rightarrow$ Import** and upload [`queue/curriculum_master_template.csv`](file:///c:/Software%20check/neet-video-pipeline_1/queue/curriculum_master_template.csv).
3. Paste NotebookLM's outputs into the matching columns.
4. When you finish a batch of concepts, click **File $\rightarrow$ Download $\rightarrow$ Comma Separated Values (.csv)**.

---

## Step 4: Import into Antigravity (Zero JSON Writing)

Place your exported CSV in the `queue/` folder (or keep `queue/curriculum_master_template.csv`) and run:

```powershell
python -m llm.curriculum_importer --csv queue/curriculum_master_template.csv
```

### What happens automatically:
1. Validates all canonical IDs and registered templates.
2. Injects the 6 beat tiers (`settle`, `context`, `concept`, `trap`, `capsule`, `release`).
3. Formulates clean, natural, phonetically normalized narrations for **English**, **Hindi**, and **Tamil** incorporating the NCERT rule, author nuance, and trap warnings.
4. Saves directly into [`queue/concepts.json`](file:///c:/Software%20check/neet-video-pipeline_1/queue/concepts.json).

---

## Step 5: Render Your Videos

### Test / Validate Without Rendering (Dry-Run):
```powershell
python main.py --all --dry-run
```

### Render a Single Concept Video:
```powershell
python main.py --concept P11-C04-T02-V03
```

### Render an Entire Batch:
```powershell
python main.py --all
```

---

## Step 6: Review Your Finished Videos

Your exported MP4s are saved deterministically in:
`output/final/[CanonicalID]_[SanitizedTitle].mp4`

Each video features:
- **1080p @ 30 FPS H.264 Video** with Manim animations, trajectory plots, apex callouts, and 15-second exam revision capsules.
- **3 Audio Tracks**: English (`eng`), Hindi (`hin`), and Tamil (`tam`) normalized to -14 LUFS.
- **3 Soft Subtitle Tracks**: English, Hindi, and Tamil switchable subtitles.
