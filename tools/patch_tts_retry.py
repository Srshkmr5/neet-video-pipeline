import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
runner_path = BASE_DIR / "tools" / "render_multilingual_unit2.py"

with open(runner_path, "r", encoding="utf-8") as f:
    text = f.read()

old_block = '''            if not b_file.exists() or b_file.stat().st_size == 0:
                audio_engine.generate_narration(
                    text=text,
                    output_path=b_file,
                    provider="edge_tts",
                    voice_id=voice,
                    language=lang,
                    use_cache=True
                )'''

new_block = '''            if not b_file.exists() or b_file.stat().st_size == 0:
                for attempt in range(4):
                    try:
                        audio_engine.generate_narration(
                            text=text,
                            output_path=b_file,
                            provider="edge_tts",
                            voice_id=voice,
                            language=lang,
                            use_cache=True
                        )
                        break
                    except Exception as e:
                        if attempt == 3:
                            raise
                        print(f"      [!] TTS retry {attempt+1}/3 after network warning: {e}")
                        time.sleep(2.5)'''

if old_block in text:
    text = text.replace(old_block, new_block)
    with open(runner_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Added TTS network retry mechanism to render_multilingual_unit2.py!")
else:
    print("Could not find old_block")
