"""
Unified Concept Video Compiler (One-Command Pilot & Production Render)
Derived from IMPLEMENTATION_RULES_v1.0.md

Executes the complete pipeline:
1. Concept metadata retrieval from curriculum_master_full_665.csv
2. Curated & normalized educational script generation (English / Tamil)
3. Pronunciation shield processing (e.g. NEET -> நீட்)
4. Audio narration synthesis via AudioEngine (Edge-TTS / Google / ElevenLabs)
5. Obsidian-Neon Manim scene compilation via ManimCompiler
6. Audio-Visual synchronization and FFmpeg high-definition muxing
7. Minimalist thumbnail generation and validation
"""

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from config import (
    RAW_AUDIO_DIR, RAW_VIDEO_DIR, FINAL_DIR, LOCALES,
    BRAND_NAME, BRAND_COPYRIGHT, BRAND_WATERMARK_ENABLED,
    BRAND_WATERMARK_TYPE, BRAND_WATERMARK_TEXT, BRAND_WATERMARK_OPACITY,
    BRAND_WATERMARK_FONT_SIZE, BRAND_WATERMARK_FONT_PATH, BRAND_WATERMARK_POSITION,
    BRAND_LOGO_PATH
)
from audio.engine import AudioEngine
from llm.script_engine import ScriptEngine
from render.manim_compiler import ManimCompiler
from tools.generate_thumbnail import generate_thumbnail_image


FINAL_VIDEOS_DIR = BASE_DIR / "output" / "final_videos"
FINAL_VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
RAW_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
RAW_VIDEO_DIR.mkdir(parents=True, exist_ok=True)

CURRICULUM_CSV = BASE_DIR / "queue" / "curriculum_master_full_665.csv"

# Curated High-Yield Pedagogical Scripts for Flagship Concepts
FLAGSHIP_SCRIPTS = {
    "P11-C02-T03-V01": {
        "en": (
            "Welcome to Kinematics. In projectile motion, the time of flight T represents the total duration the projectile remains in the air before landing at y equals zero. "
            "This flight duration is governed strictly by the vertical velocity component, v-naught sine theta. The horizontal velocity vx has zero acceleration and exerts zero influence on how long the object stays airborne. "
            "The governing formula is T equals 2 v-naught sine theta divided by g. Now observe the classic NEET Trap: if an exam problem specifies the angle theta with the vertical axis instead of the horizontal, "
            "the vertical velocity becomes v-naught cosine theta! Always swap sine theta for cosine theta when the angle is measured from the vertical. The transformed formula becomes T equals 2 v-naught cosine theta divided by g. "
            "Master this rule to secure your five marks!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். எறிபொருள் இயக்கத்தில், பறக்கும் நேரம் T என்பது எறிபொருள் காற்றில் இருக்கும் மொத்த நேரத்தைக் குறிக்கிறது. "
            "இது முழுக்க முழுக்க ஆரம்ப திசைவேகத்தின் செங்குத்து கூறான v-naught sine theta-வை மட்டுமே சார்ந்துள்ளது. கிடைமட்ட திசைவேகம் இதில் எந்த தாக்கத்தையும் ஏற்படுத்துவதில்லை. "
            "இதன் முதன்மை சமன்பாடு: T equals 2 v-naught sine theta divided by g. இப்போது நீட் தேர்வின் மிக முக்கிய பொறி எச்சரிக்கை: வினாவில் கோணம் செங்குத்து அச்சுடன் கொடுக்கப்பட்டால், "
            "sine theta-விற்கு பதிலாக cosine theta என மாறும்! அப்போது சரியான சமன்பாடு T equals 2 v-naught cosine theta divided by g ஆகும். கிடைமட்டம் என்றால் sine; செங்குத்து என்றால் cosine. "
            "இந்த முக்கிய விதியை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "प्रक्षेप्य गति (Projectile Motion) में आपका स्वागत है। उड्डयन काल (Time of Flight) T वह कुल समय है जब तक प्रक्षेप्य हवा में रहता है। "
            "यह समय पूरी तरह से प्रारंभिक वेग के ऊर्ध्वाधर घटक v-naught sine theta पर निर्भर करता है। क्षैतिज वेग का उड्डयन काल पर कोई प्रभाव नहीं पड़ता। "
            "इसका मानक सूत्र है: T equals 2 v-naught sine theta divided by g। अब नीट परीक्षा का मुख्य ट्रैप पॉइंट: यदि प्रश्न में प्रक्षेपण कोण क्षैतिज के बजाय ऊर्ध्वाधर अक्ष से दिया गया हो, "
            "तो sine theta के स्थान पर cosine theta आएगा! तब सही सूत्र होगा T equals 2 v-naught cosine theta divided by g। क्षैतिज से कोण हो तो sine; ऊर्ध्वाधर से हो तो cosine। "
            "परीक्षा में पूरे अंक पाने के लिए इस नियम को हमेशा याद रखें!"
        )
    },
    "P11-C02-T03-V02": {
        "en": (
            "Welcome to Kinematics. In projectile motion, maximum height H-max depends strictly on the vertical velocity component. "
            "At the apex, vertical velocity drops to zero, while horizontal velocity remains constant. The standard formula is H-max "
            "equals v-naught squared sine squared theta divided by 2g, where theta is measured from the horizontal ground. "
            "Now here is the crucial NEET Trap: if an exam question tricks you by giving the angle theta relative to the vertical axis, "
            "vertical velocity becomes v-naught cosine theta! Therefore, replace sine squared with cosine squared. The exact formula "
            "becomes H-max equals v-naught squared cosine squared theta divided by 2g. Horizontal uses sine squared; vertical uses cosine squared. "
            "Master this trap to secure your five marks!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். எறிபொருள் இயக்கத்தில், பெரும உயரம் H-max என்பது எறிபொருள் அடையும் உச்ச செங்குத்து "
            "இடப்பெயர்ச்சி ஆகும். இந்த உச்சியில், செங்குத்து திசைவேகம் பூஜ்ஜியமாக மாறும், ஆனால் கிடைமட்ட திசைவேகம் மாறாமல் இருக்கும். "
            "இதன் முதன்மை சமன்பாடு, H-max equals v-naught squared sine squared theta divided by 2g ஆகும். இப்போது நீட் தேர்வின் மிக "
            "முக்கிய பொறி எச்சரிக்கை: கோணம் கிடைமட்டத்திற்கு பதில் செங்குத்திலிருந்து கொடுக்கப்பட்டால், செங்குத்து திசைவேகம் "
            "v-naught cosine theta ஆக மாறும்! அப்போது சரியான விடை: sine squared-க்கு பதிலாக cosine squared theta என மாறும்! அதாவது "
            "H-max equals v-naught squared cosine squared theta divided by 2g. கிடைமட்டம் என்றால் sine squared; செங்குத்து என்றால் cosine squared. "
            "இந்த ஐந்து மதிப்பெண் பொறியை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "प्रक्षेप्य गति (Projectile Motion) में आपका स्वागत है। अधिकतम ऊँचाई H-max केवल ऊर्ध्वाधर वेग घटक पर निर्भर करती है। "
            "शीर्ष बिंदु पर, ऊर्ध्वाधर वेग शून्य हो जाता है, जबकि क्षैतिज वेग v-naught cosine theta स्थिर रहता है। इसका मानक सूत्र है "
            "H-max equals v-naught squared sine squared theta divided by 2g, जहाँ theta क्षैतिज सतह से मापा गया कोण है। "
            "अब नीट परीक्षा का मुख्य ट्रैप पॉइंट: यदि परीक्षा में कोण क्षैतिज के बजाय ऊर्ध्वाधर अक्ष से दिया गया हो, तो ऊर्ध्वाधर वेग "
            "v-naught cosine theta बन जाता है! इसलिए sine squared के स्थान पर cosine squared आएगा। सही सूत्र होगा "
            "H-max equals v-naught squared cosine squared theta divided by 2g। क्षैतिज से कोण हो तो sine squared; ऊर्ध्वाधर से हो तो cosine squared। "
            "पाँच अंक पक्के करने के लिए इस ट्रैप को हमेशा याद रखें!"
        )
    },
    "P11-C02-T03-V03": {
        "en": (
            "Welcome to Kinematics. In projectile motion, the horizontal range R is the total distance traveled along the ground before impact. "
            "The governing textbook formula is R equals v-naught squared sine 2-theta divided by g. Now examine the fundamental physical principle of complementary projection angles: "
            "for identical initial launch speeds, the horizontal range is exactly identical for projection angle theta and 90 degrees minus theta! For example, launch angles of 30 degrees and 60 degrees achieve the exact same landing distance. "
            "Now heed the high-frequency NEET Trap: students frequently assume that because ranges are equal, the maximum height H and time of flight T must also be equal. "
            "This is completely false! The steeper angle always attains a greater maximum height and spends more time in the air. Only the horizontal range is identical. Master this distinction to conquer NEET PYQs!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். எறிபொருள் இயக்கத்தில் கிடைமட்ட வீச்சு R என்பது தரைமட்டத்தில் எறிபொருள் கடக்கும் மொத்த கிடைமட்ட தூரம் ஆகும். "
            "இதன் முதன்மை சமன்பாடு: R equals v-naught squared sine 2-theta divided by g. இதன் மிக முக்கிய இயற்பியல் ரகசியம் நிரப்புக் கோணங்கள் ஆகும்: ஒரே ஆரம்ப வேகத்தில், "
            "theta மற்றும் 90 minus theta ஆகிய இரு கோணங்களுக்கும் கிடைமட்ட வீச்சு சமமாக இருக்கும்! எடுத்துக்காட்டாக, 30 டிகிரி மற்றும் 60 டிகிரி இரண்டிற்கும் ஒரே வீச்சு கிடைக்கும். "
            "ஆனால் நீட் தேர்வு பொறி எச்சரிக்கை: வீச்சு சமமாக இருந்தாலும், பெரும உயரம் H மற்றும் பறக்கும் நேரம் T இரண்டும் கண்டிப்பாக சமமாக இருக்காது! "
            "வீச்சு மட்டுமே சமம், உயரமும் நேரமும் வெவ்வேறானவை. இந்த நுணுக்கத்தை மறக்காதீர்கள்!"
        ),
        "hi": (
            "प्रक्षेप्य गति में आपका स्वागत है। क्षैतिज परास (Horizontal Range) R वह कुल क्षैतिज दूरी है जो प्रक्षेप्य तय करता है। "
            "इसका सूत्र है: R equals v-naught squared sine 2-theta divided by g। इसका सबसे महत्वपूर्ण भौतिकी नियम है पूरक कोण (Complementary Angles): "
            "समान प्रारंभिक चाल पर, कोण theta और 90 minus theta दोनों के लिए क्षैतिज परास बिल्कुल बराबर होता है! उदाहरण के लिए, 30 डिग्री और 60 डिग्री पर समान रेंज मिलेगी। "
            "लेकिन नीट परीक्षा का प्रमुख ट्रैप पॉइंट: परास समान होने पर भी अधिकतम ऊँचाई H और उड्डयन काल T कभी समान नहीं होते! केवल परास बराबर होता है, ऊँचाई और समय अलग-अलग होते हैं। परीक्षा में यह गलती कभी न करें!"
        )
    },
    "P11-C02-T03-V04": {
        "en": (
            "Welcome to Kinematics. In projectile motion, the equation of trajectory relates the vertical position y directly to horizontal position x, proving the path is a parabola. "
            "The standard formulation is y equals x tan theta minus g x squared divided by 2 v-naught squared cosine squared theta. "
            "Notice that the alternative factorized form, y equals x tan theta times 1 minus x over R, enables solving complex range-based NEET problems in seconds. "
            "Now pay close attention to the critical NEET Trap: when comparing empirical trajectory curves, students often confuse the tan theta leading coefficient with cotangent or invert terms. "
            "Remember that the trajectory parabola starts with positive linear term x tan theta. Master both forms of the trajectory equation to secure your victory in NEET Kinematics!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். எறிபொருளின் பாதை சமன்பாடு என்பது செங்குத்து ஆயத்தொலைவு y மற்றும் கிடைமட்ட ஆயத்தொலைவு x-க்கு இடையேயான பரவளைய தொடர்பை விளக்குகிறது. "
            "இதன் அடிப்படை சமன்பாடு: y equals x tan theta minus g x squared divided by 2 v-naught squared cosine squared theta ஆகும். "
            "இதன் சுருக்கமான வடிவம் y equals x tan theta times 1 minus x by R ஆகும், இது பல நீட் வினாக்களை சில வினாடிகளில் தீர்க்க உதவும். "
            "நீட் தேர்வு பொறி எச்சரிக்கை: சோதனைக் கணக்கீடுகளில் tan theta காரணிக்கு பதிலாக cot theta என்று குழப்பிக் கொள்ளாதீர்கள். "
            "பரவளையத்தின் முதல் உறுப்பு எப்போதும் x tan theta மட்டுமே. இந்த சமன்பாட்டை மாஸ்டர் செய்யுங்கள்!"
        ),
        "hi": (
            "प्रक्षेप्य गति में आपका स्वागत है। प्रक्षेप्य पथ का समीकरण (Equation of Trajectory) ऊर्ध्वाधर निर्देशांक y और क्षैतिज निर्देशांक x के बीच परवलयाकार संबंध को दर्शाता है। "
            "इसका मानक सूत्र है: y equals x tan theta minus g x squared divided by 2 v-naught squared cosine squared theta। "
            "इसका दूसरा रूप y equals x tan theta times 1 minus x by R कई कठिन नीट प्रश्नों को चुटकियों में हल कर देता है। "
            "नीट परीक्षा का मुख्य ट्रैप पॉइंट: तुलनात्मक प्रश्नों में tan theta की जगह cot theta मानकर गलती न करें। पहला पद हमेशा x tan theta ही होता है। इस परवलय समीकरण को अच्छी तरह याद रखें!"
        )
    }
}

def load_concept_record(canonical_id: str) -> Dict[str, Any]:
    """Retrieves concept metadata row from 665 CSV."""
    if not CURRICULUM_CSV.exists():
        raise FileNotFoundError(f"Curriculum master not found at: {CURRICULUM_CSV}")

    with open(CURRICULUM_CSV, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("canonical_id") == canonical_id:
                return row

    raise ValueError(f"Concept '{canonical_id}' not found in {CURRICULUM_CSV}")

def get_media_duration(file_path: Path) -> float:
    """Uses ffprobe to inspect exact duration in seconds."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        raise RuntimeError(f"Could not probe duration for {file_path}: {e}")

def get_script_for_concept(concept: Dict[str, Any], lang: str) -> str:
    """
    Returns curated script if available, or dynamically crafts a high-yield
    concise pedagogy script adhering to the 6 pedagogical beats.
    """
    canonical_id = concept["canonical_id"]
    lang_lower = lang.lower()
    if "ta" in lang_lower:
        lang_key = "ta"
    elif "hi" in lang_lower:
        lang_key = "hi"
    else:
        lang_key = "en"

    # Check curated scripts
    if canonical_id in FLAGSHIP_SCRIPTS and lang_key in FLAGSHIP_SCRIPTS[canonical_id]:
        return FLAGSHIP_SCRIPTS[canonical_id][lang_key]

    # Dynamic generation fallback (clean catalog citations for natural teacher speech)
    ch_name = concept.get("chapter_name", "Physics")
    title = concept.get("concept_title", "Key Concept")
    rule = re.sub(r"^(?:NCERT|HCV)[^:]*:\s*", "", concept.get("ncert_core_rule", "")).strip()
    formula = concept.get("plain_formula", "")
    trap = concept.get("neet_trap_point", "")
    nuance = re.sub(r"^(?:HCV|NCERT)[^:]*:\s*", "", concept.get("author_book_nuance", "")).strip()

    if lang_key == "ta":
        script = (
            f"{ch_name} பாடத்திற்கு வரவேற்கிறோம். இன்று நாம் {title} பற்றி கற்கப் போகிறோம். "
            f"முக்கிய விதி: {rule} இதன் முதன்மை சமன்பாடு {formula}. "
            f"நீட் பொறி எச்சரிக்கை: {trap}. முக்கிய குறிப்பு: {nuance} இதை எப்போதும் நினைவில் நிறுத்துங்கள்."
        )
    elif lang_key == "hi":
        script = (
            f"{ch_name} में आपका स्वागत है। आज हम समझेंगे: {title}। "
            f"एनसीईआरटी नियम: {rule}। मुख्य सूत्र: {formula}। "
            f"नीट ट्रैप पॉइंट: {trap}। महत्वपूर्ण बिंदु: {nuance}। इसे हमेशा याद रखें।"
        )
    else:
        script = (
            f"Welcome to {ch_name}. In this session, we analyze {title}. "
            f"The core principle states: {rule}. The governing formula is {formula}. "
            f"NEET Trap alert: {trap}. Key insight to remember: {nuance}. Master this for your exam."
        )
    return script

def render_concept_video(
    canonical_id: str,
    lang: str = "en-IN",
    quality: str = "hd",
    provider: str = "edge_tts",
    voice_id: Optional[str] = None,
    dimension: str = "auto",
    theme: Optional[str] = None,
    skip_cache: bool = False
) -> Dict[str, Any]:
    t_start = time.time()
    from config import DEFAULT_THEME
    effective_theme = (theme or DEFAULT_THEME).strip().lower()

    # 1. Fetch Metadata
    concept = load_concept_record(canonical_id)
    title = concept.get("concept_title", "Concept")
    template_name = concept.get("template_name", "FormulaWithGraph")

    # Resolve dimension (auto reads CSV column 'dimension')
    csv_dim = concept.get("dimension", "2d").lower()
    effective_dim = dimension.lower() if dimension in ["2d", "3d"] else (csv_dim if csv_dim in ["2d", "3d"] else "2d")

    print("=" * 80)
    print(f"🚀 NEET UG CONCEPT COMPILER: {canonical_id} [{lang.upper()}] | [{effective_dim.upper()} MODE] | [THEME: {effective_theme.upper()}]")
    print(f"   Quality: {quality.upper()} | TTS Provider: {provider.upper()}")
    print("=" * 80)
    print(f"📖 Loaded Concept: {canonical_id} - '{title}'")
    print(f"   Chapter: {concept.get('chapter_name')} (Grade {concept.get('grade')})")
    print(f"   Template: {template_name} | Archetype: {concept.get('storyboard_ui_archetype')}")
    print(f"   Dimension: {effective_dim.upper()} (Requested: '{dimension}', CSV Default: '{csv_dim}')")

    # 2. Script & Pronunciation Shield
    lang_lower = lang.lower()
    if "ta" in lang_lower:
        lang_key = "ta"
    elif "hi" in lang_lower:
        lang_key = "hi"
    else:
        lang_key = "en"

    raw_script = get_script_for_concept(concept, lang)
    normalized_script = ScriptEngine.normalize_for_tts(raw_script, lang=lang_key)
    
    print(f"\n🎙️ Narration Script ({lang}):")
    print(f"   Raw        : \"{raw_script[:90]}...\"")
    print(f"   Normalized : \"{normalized_script[:90]}...\"")

    # 3. Audio Narration Synthesis
    raw_audio_path = RAW_AUDIO_DIR / f"{canonical_id}_{lang}.mp3"
    # Fallback to alternate cached naming conventions if present
    if not skip_cache and not raw_audio_path.exists():
        alt_paths = [
            RAW_AUDIO_DIR / f"{canonical_id}_{lang_key}.mp3",
            RAW_AUDIO_DIR / canonical_id / f"{canonical_id}_{lang_key}.mp3",
            RAW_AUDIO_DIR / canonical_id / f"{canonical_id}_{lang}.mp3",
            RAW_AUDIO_DIR / canonical_id / f"{canonical_id}_{lang_key}_raw.mp3"
        ]
        for ap in alt_paths:
            if ap.exists():
                raw_audio_path = ap
                break

    print(f"\n🔊 Synthesizing Audio Narration via {provider}...")
    audio_engine = AudioEngine(default_provider=provider)
    
    # Choose voice if not specified
    if not voice_id:
        if lang_key == "ta":
            voice_id = "ta-IN-ValluvarNeural"
        elif lang_key == "hi":
            voice_id = "hi-IN-MadhurNeural"
        else:
            voice_id = "en-IN-NeerjaExpressiveNeural"

    if not skip_cache and raw_audio_path.exists():
        print(f"   Using existing audio cache: {raw_audio_path.name}")
    else:
        audio_engine.generate_narration(
            text=normalized_script,
            output_path=raw_audio_path,
            provider=provider,
            voice_id=voice_id,
            language=lang,
            use_cache=not skip_cache
        )
    audio_duration = get_media_duration(raw_audio_path)
    print(f"   Audio Duration: {audio_duration:.2f}s")

    # 4. Thumbnail Verification / Generation
    thumbnail_path = BASE_DIR / "output" / "thumbnails" / f"{canonical_id}_thumbnail.png"
    if not thumbnail_path.exists():
        print(f"\n🖼️ Generating Minimalist Thumbnail for {canonical_id}...")
        generate_thumbnail_image(concept, thumbnail_path)
    print(f"   Thumbnail Verified: {thumbnail_path.name}")

    # 5. Manim Animation Rendering
    print(f"\n🎥 Compiling Obsidian-Neon Manim Animation ({quality}) [{effective_dim.upper()}]...")
    target_duration = max(32.0, audio_duration + 4.5)
    video_tag = f"{canonical_id}_{lang}" if effective_dim == "2d" else f"{canonical_id}_3d_{lang}"
    node_data = {
        "videoId": video_tag,
        "serialTitle": title,
        "subject": concept.get("subject", "Physics"),
        "grade": int(concept.get("grade", 11)),
        "templateName": template_name,
        "dimension": effective_dim,
        "theme": effective_theme,
        "storyboard_ui_archetype": concept.get("storyboard_ui_archetype", "ORTHOGONAL_SPLIT"),
        "chapter_no": int(concept.get("chapter_no", 2)),
        "topic_no": int(concept.get("topic_no", 3)),
        "video_no": int(concept.get("video_no", 2)),
        "neet_code": f"{concept.get('chapter_no', 2)}.{concept.get('topic_no', 3)}.{concept.get('video_no', 2)}",
        "seq_chapter": int(concept.get("chapter_seq", 1)),
        "total_chapter_videos": int(concept.get("total_chapter_videos", 14)),
        "next_video_id": concept.get("next_video_id", ""),
        "next_video_title": concept.get("next_video_title", ""),
        "target_duration": target_duration,
        "parameters": {
            "latexFormula": concept.get("latex_formula", ""),
            "plainFormula": concept.get("plain_formula", ""),
            "trapWarning": concept.get("neet_trap_point", ""),
            "ncertRule": concept.get("ncert_core_rule", ""),
            "authorNuance": concept.get("author_book_nuance", ""),
            "ncertCitation": concept.get("ncert_citation", ""),
            "pyqBadge": f"NEET PYQ: {concept.get('pyq_years')}" if concept.get("pyq_years") else "HIGH YIELD",
            "conceptTitle": title,
            "topicName": concept.get("topic_name", ""),
            "chapterName": concept.get("chapter_name", ""),
            "target_duration": round(target_duration, 1)
        }
    }

    # Map quality
    manim_quality = "draft" if quality == "draft" else "draft"  # 'draft' renders at 1920x1080 30fps
    raw_video_path_str, was_cached = ManimCompiler.compile_scene(
        concept_node=node_data,
        quality=manim_quality,
        skip_cache=skip_cache
    )
    raw_video_path = Path(raw_video_path_str)
    video_duration = get_media_duration(raw_video_path)
    cache_badge = "[CACHE HIT]" if was_cached else "[NEW RENDER]"
    print(f"   Video Compiled {cache_badge}: {raw_video_path.name} ({video_duration:.2f}s)")

    # 6. Audio-Visual Synchronization & FFmpeg Muxing
    filename_stem = f"{canonical_id}_{lang}" if effective_dim == "2d" else f"{canonical_id}_3d_{lang}"
    output_final_path = FINAL_VIDEOS_DIR / f"{filename_stem}.mp4"
    print(f"\n🎬 Muxing Audio + Video + Metadata Container...")
    print(f"   Video Duration : {video_duration:.2f}s")
    print(f"   Audio Duration : {audio_duration:.2f}s")
    
    # Watermark & Audio-Visual filter setup
    filter_complex_parts = []
    video_map = "0:v:0"
    reencode_video = False

    if BRAND_WATERMARK_ENABLED:
        reencode_video = True
        pos_map = {
            "bottom_right": "x=w-tw-45:y=h-th-35",
            "bottom_left": "x=45:y=h-th-35",
            "top_right": "x=w-tw-45:y=35",
            "top_left": "x=45:y=35"
        }
        pos_str = pos_map.get(BRAND_WATERMARK_POSITION, "x=w-tw-45:y=h-th-35")

        if BRAND_WATERMARK_TYPE == "text" and BRAND_WATERMARK_TEXT:
            try:
                rel_font_bold = BRAND_WATERMARK_FONT_PATH.relative_to(BASE_DIR).as_posix()
            except Exception:
                rel_font_bold = "assets/fonts/Inter-Bold.otf"
            rel_font_reg = "assets/fonts/Inter-Regular.otf"
            
            # Stacked Broadcast Watermark at Bottom-Right:
            # Line 1: Brand Bug (e.g. NEET UG)
            # Line 2: Taxonomy Reference ID (e.g. P11-C02-T03-V02) directly beneath it
            if BRAND_WATERMARK_POSITION == "bottom_right":
                watermark_filter = (
                    f"drawtext=text='{BRAND_WATERMARK_TEXT}':fontfile={rel_font_bold}:fontsize={BRAND_WATERMARK_FONT_SIZE}:fontcolor=white@{BRAND_WATERMARK_OPACITY}:x=w-tw-45:y=h-50,"
                    f"drawtext=text='{canonical_id}':fontfile={rel_font_reg}:fontsize=12:fontcolor=white@{BRAND_WATERMARK_OPACITY}:x=w-tw-45:y=h-26"
                )
            else:
                watermark_filter = (
                    f"drawtext=text='{BRAND_WATERMARK_TEXT}':fontfile={rel_font_bold}:fontsize={BRAND_WATERMARK_FONT_SIZE}:fontcolor=white@{BRAND_WATERMARK_OPACITY}:{pos_str}"
                )
            
            filter_complex_parts.append(f"[0:v]{watermark_filter}[v]")
            video_map = "[v]"


    # Sync strategy:
    # If audio is shorter than video, pad audio with clean silence using apad
    # so that the 6s End Revision Capsule & Up-Next Teaser can be studied in focused hold.
    if lang_key == "ta":
        lang_code = "tam"
        lang_display = "Tamil"
    elif lang_key == "hi":
        lang_code = "hin"
        lang_display = "Hindi"
    else:
        lang_code = "eng"
        lang_display = "English"

    if audio_duration < video_duration:
        filter_complex_parts.append(f"[1:a]apad=whole_dur={video_duration:.3f}[a]")
        audio_map = "[a]"
    else:
        audio_map = "1:a:0"

    mux_cmd = [
        "ffmpeg", "-y",
        "-i", str(raw_video_path),
        "-i", str(raw_audio_path)
    ]

    if filter_complex_parts:
        mux_cmd.extend(["-filter_complex", ";".join(filter_complex_parts)])
        mux_cmd.extend(["-map", video_map, "-map", audio_map])
    else:
        mux_cmd.extend(["-map", "0:v:0", "-map", audio_map])

    if reencode_video:
        mux_cmd.extend([
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-pix_fmt", "yuv420p"
        ])
    else:
        mux_cmd.extend(["-c:v", "copy"])

    mux_cmd.extend([
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-metadata", f"title={canonical_id} - {title}",
        "-metadata", f"copyright={BRAND_COPYRIGHT}",
        "-metadata", "comment=NEET UG Video Engine Obsidian-Neon",
        "-metadata:s:a:0", f"language={lang_code}",
        "-metadata:s:a:0", f"title={lang_display} Audio",
        str(output_final_path)
    ])

    res = subprocess.run(mux_cmd, cwd=str(BASE_DIR), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg muxing failed: {res.stderr}")

    final_duration = get_media_duration(output_final_path)
    final_size_mb = output_final_path.stat().st_size / (1024 * 1024)
    elapsed = time.time() - t_start

    print(f"\n✨ COMPLETE SUCCESS: Final Video Ready!")
    print(f"   Output File    : {output_final_path.name}")
    print(f"   Full Path      : {output_final_path}")
    print(f"   Final Duration : {final_duration:.2f}s")
    print(f"   File Size      : {final_size_mb:.2f} MB")
    print(f"   Total Pipeline : {elapsed:.1f}s")
    print("=" * 80)

    return {
        "canonical_id": canonical_id,
        "title": title,
        "language": lang,
        "output_path": str(output_final_path),
        "thumbnail_path": str(thumbnail_path),
        "duration": final_duration,
        "size_mb": final_size_mb,
        "elapsed_sec": elapsed
    }

def main():
    parser = argparse.ArgumentParser(description="One-Command NEET Concept Video Compiler")
    parser.add_argument("--id", type=str, required=True, help="Canonical concept ID (e.g. P11-C02-T03-V02)")
    parser.add_argument("--lang", type=str, default="en-IN", help="Language code ('en-IN', 'ta-IN', etc.)")
    parser.add_argument("--quality", type=str, default="hd", choices=["draft", "hd", "master"], help="Render quality")
    parser.add_argument("--provider", type=str, default="edge_tts", choices=["edge_tts", "google", "elevenlabs"], help="TTS provider")
    parser.add_argument("--voice", type=str, default=None, help="Explicit voice ID override")
    parser.add_argument("--dimension", type=str, default="auto", choices=["auto", "2d", "3d"],
                        help="Dimension mode: 'auto' (respects CSV column), '2d' (force 2D), or '3d' (force 3D cinematic)")
    parser.add_argument("--theme", type=str, default=None,
                        choices=["modern_edtech", "academic_masterclass", "3b1b", "cupertino"],
                        help="Visual typography & color theme")
    parser.add_argument("--skip_cache", action="store_true", help="Force re-rendering without cache")

    args = parser.parse_args()

    render_concept_video(
        canonical_id=args.id,
        lang=args.lang,
        quality=args.quality,
        provider=args.provider,
        voice_id=args.voice,
        dimension=args.dimension,
        theme=args.theme,
        skip_cache=args.skip_cache
    )

if __name__ == "__main__":
    main()
