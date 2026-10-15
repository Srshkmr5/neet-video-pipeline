# Migration Guide: Moving the Project & Antigravity to a New Computer / New ID

Migrating this project and Antigravity to a new computer—even with a **new User ID / Google Account**—is clean, safe, and straightforward because the entire architecture was designed to be **100% self-contained and repository-centric**.

---

## 1. What Happens to Antigravity When You Change Computer & ID?

- **Antigravity itself is not locked to your machine's hardware.** You can install it on any number of computers.
- **Changing your ID (Google Account):** Simply means downloading Antigravity on the new computer and signing in with your new email/account.
- **The AI's "Memory" of the Project:** The AI does not rely on a hidden cloud state. It reads the local repository files:
  - `.antigravity/rules.md` (all 7 rules, including permissions, math unicode, and voice personas)
  - `MASTER_BLUEPRINT.md` (full architectural specifications)
  - `VERSION.md` (current version and release log)
  - `queue/curriculum_master_full_665.csv` (all 665 concepts)
  
As soon as you open the folder in Antigravity under your new ID, the agent reads these files and immediately knows everything about the project.

---

## 2. Step-by-Step Migration Process

### Step 1: Copy the Project to the New Computer
You can transfer the project folder (`neet-video-pipeline_1` or `neet-video-pipeline_2`) via:
- **Option A (Fastest & Simplest):** Copy the folder to an external USB drive or SSD, and paste it onto the new computer (e.g., at `C:\Software check\neet-video-pipeline_1` or `D:\neet-video-pipeline_1`).
- **Option B (Zip Archive):** Right-click `neet-video-pipeline_1` $\to$ Compress to ZIP $\to$ transfer via Google Drive/OneDrive $\to$ Extract on the new machine.
- **Option C (Private Git Remote):** Since we initialized Git, you can push it to a private GitHub/GitLab repository:
  ```bash
  git remote add origin <your-private-repo-url>
  git push -u origin master --tags
  ```

---

### Step 2: Set Up System Prerequisites on the New Computer
On your new computer, install the following 3 standard tools (takes ~5 minutes):

1. **Python (version 3.11 recommended):**
   - Download from [python.org](https://www.python.org/downloads/)
   - *Important:* Check the box **"Add python.exe to PATH"** during installation.

2. **FFmpeg (Media Encoder):**
   - Download FFmpeg (from `ffmpeg.org` or via `winget install Gyan.FFmpeg` in PowerShell).
   - Ensure `ffmpeg` is available in your system PATH (verify by typing `ffmpeg -version` in PowerShell).

3. **Install Python Libraries (1-Click):**
   - Open PowerShell/Terminal in the project folder and run:
     ```bash
     pip install -r requirements.txt
     ```
   *(We have created `requirements.txt` containing `manim`, `edge-tts>=7.3.1`, `gtts`, `pydub`, `pyyaml`, `pillow`, etc.)*

---

### Step 3: Install Antigravity & Sign In with Your New ID
1. Install **Antigravity** (or Antigravity IDE) on the new computer.
2. Launch it and sign in with your **new User ID / Google Account**.
3. Click **Open Folder / Open Project** and select the transferred project folder (e.g., `C:\Software check\neet-video-pipeline_1`).

---

### Step 4: Configure Permissions on the New Computer (1-Time)
Just like you did on this computer:
1. In the bottom chat status bar, set the Execution Policy dropdown to **"Always Proceed"** (or **"Auto"**).
2. Go to **Settings (⚙️)** $\to$ **Agent Settings** $\to$ set **Tool Execution Policy** and **Artifact Review Mode** to **`always-proceed`**.

---

### Step 5 (Optional): Bringing Along Past Conversation Logs & Artifacts
If you want your exact chat trajectory and markdown artifacts from this current session transferred over:
- Copy the folder:
  `C:\Users\DELL\.gemini\antigravity\brain`
- Paste it into your new computer's profile path:
  `C:\Users\<YourNewUsername>\.gemini\antigravity\brain`
*(Note: This is completely optional. Even without it, the agent reads `VERSION.md`, `rules.md`, and `curriculum_master_full_665.csv` and knows the exact state.)*

---

## 3. Verification on the New Machine
Once set up on the new computer, test by running a quick verification command in the chat:
```text
python tools/render_concept_video.py --id P11-C02-T03-V01 --lang en-IN
```
If this runs and reports success, your new machine and new ID are 100% operational!
