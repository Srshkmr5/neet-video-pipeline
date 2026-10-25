import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
runner_engine_path = BASE_DIR / "tools" / "render_multilingual_unit2.py"

with open(runner_engine_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect where CONCEPT_BEAT_SCRIPTS is defined and inject P11-C02-T03-V08
c2_scripts = '''    "P11-C02-T03-V08": {
        "en-IN": [
            ("beat_1", "Continuing Straight Line Motion: in this masterclass, we explore the geometry of Velocity-Time graphs, where slope represents acceleration and area yields displacement."),
            ("beat_2", "On a velocity-time graph, the instantaneous slope dv by dt defines acceleration: a positive slope means speeding up, a negative slope represents deceleration, and a horizontal line denotes uniform velocity. Simultaneously, the definite integral of velocity over time—the area between the curve and the time axis—equals the particle's displacement."),
            ("beat_3", "Distinguish between signed and unsigned areas: displacement is a vector, calculated as the net algebraic sum of areas, where regions below the time axis are negative. Conversely, total distance traveled is a scalar, found by adding the absolute geometric magnitudes of all areas. For uniform acceleration, the linear graph leads directly to the core kinematic formulas."),
            ("beat_4", "Now, heed the fatal NEET Trap: calculating distance instead of displacement! In NEET exam problems, when asked for distance, students mistakenly subtract the negative area below the time axis. Remember: distance always sums absolute areas and is always positive, while displacement uses signed net area. Master this distinction to secure top marks!")
        ],
        "hi-IN": [
            ("beat_1", "सरल रेखा में गति को आगे बढ़ाते हुए: इस सत्र में हम वेग-समय ग्राफ यानी वी-टी ग्राफ की ज्यामिति का अध्ययन करेंगे, जहाँ प्रवणता त्वरण और क्षेत्रफल विस्थापन देता है।"),
            ("beat_2", "वेग-समय ग्राफ पर तात्क्षणिक प्रवणता डी-वी बटे डी-टी त्वरण को दर्शाती है: धनात्मक ढाल का अर्थ है त्वरित गति, ऋणात्मक ढाल मंदन, और क्षैतिज रेखा एकसमान वेग को दर्शाती है। साथ ही, समय अक्ष और वक्र के बीच का समाकलित क्षेत्रफल कण के कुल विस्थापन को दर्शाता है।"),
            ("beat_3", "चिन्हित और अचिन्हित क्षेत्रफलों का अंतर समझें: विस्थापन एक सदिश राशि है, जो क्षेत्रफलों का बीजीय योग है, जहाँ समय अक्ष के नीचे का क्षेत्रफल ऋणात्मक होता है। इसके विपरीत, तय की गई कुल दूरी एक अदिश राशि है, जो सभी क्षेत्रफलों के परिमाण का योग होती है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पॉइंट पर: कुल दूरी और विस्थापन में भ्रम! नीट परीक्षा में जब दूरी पूछी जाती है, तो छात्र नीचे वाले क्षेत्रफल को घटाने की गलती कर बैठते हैं। याद रखें: दूरी के लिए सभी क्षेत्रफलों का धनात्मक योग लें, जबकि विस्थापन के लिए चिन्ह सहित गणना करें। इसे याद रखें और नीट में पूरे अंक प्राप्त करें।")
        ],
        "ta-IN": [
            ("beat_1", "நேர்க்கோட்டு இயக்கத்தை தொடர்கிறோம்: இந்த அமர்வில் நாம் திசைவேக-கால வரைபடங்களின் வடிவியலை ஆராய்கிறோம், இதில் சாய்வு முடுக்கத்தையும் பரப்பு இடப்பெயர்ச்சியையும் தருகிறது."),
            ("beat_2", "திசைவேக-கால வரைபடத்தில் உடனடி சாய்வு டி-வி பை டி-டி முடுக்கத்தைக் குறிக்கிறது: நேர்மறை சாய்வு முடுக்கத்தையும், எதிர்மறை சாய்வு வேகக்குறைவையும், கிடைமட்டக் கோடு சீரான திசைவேகத்தையும் குறிக்கிறது. அதே நேரத்தில், வளைவரைக்கு கீழுள்ள பரப்பு துகளின் இடப்பெயர்ச்சியைத் தருகிறது."),
            ("beat_3", "குறிக்கப்பட்ட பரப்புகளுக்கு இடையேயான வேறுபாட்டைப் புரிந்து கொள்ளுங்கள்: இடப்பெயர்ச்சி என்பது ஒரு வெக்டார் அளவு, இது கால அச்சுக்கு கீழேயுள்ள பரப்பை கழித்து கணக்கிடப்படும் நிகர பரப்பாகும். ஆனால் பயணித்த மொத்த தொலைவு ஒரு ஸ்கேலார் அளவு, இது அனைத்து பரப்புகளின் கூட்டலாகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: தொலைவு மற்றும் இடப்பெயர்ச்சி கணக்கீட்டுப் பிழை! நீட் தேர்வில் தொலைவு கேட்கப்படும் போது, மாணவர்கள் கீழ் பரப்பைக் கழித்து தவறிழைக்கிறார்கள். நினைவில் கொள்ளுங்கள்: தொலைவுக்கு அனைத்து பரப்புகளையும் கூட்ட வேண்டும், இடப்பெயர்ச்சிக்கு மட்டுமே குறியீட்டுடன் கழிக்க வேண்டும். இந்த விதியை சரியாகப் பின்பற்றுங்கள்.")
        ]
    },'''

# Replace CONCEPT_BEAT_SCRIPTS closing bracket with c2_scripts
if '"P11-C02-T03-V08"' not in content:
    content = content.replace('CONCEPT_BEAT_SCRIPTS = {\n', 'CONCEPT_BEAT_SCRIPTS = {\n' + c2_scripts + '\n')

archetype_map_code = '''
ARCHETYPE_SCENE_MAP = {
    "P11-C02-T01-V01": "PositionTimeGraphsScene",
    "P11-C02-T03-V08": "VelocityTimeGraphsScene",
}
'''
if 'ARCHETYPE_SCENE_MAP' not in content:
    content = content.replace('def load_concept_row', archetype_map_code + '\ndef load_concept_row')

# Update runner class generation to use ARCHETYPE_SCENE_MAP
old_runner_def = 'class {runner_scene_class}(u2.PositionTimeGraphsScene):'
new_runner_def = '''base_class = ARCHETYPE_SCENE_MAP.get(canonical_id, "ModularUnit2Scene")
        runner_code = f\'\'\'import sys
from pathlib import Path
BASE_DIR = Path({repr(str(BASE_DIR))})
sys.path.insert(0, str(BASE_DIR))

from manim import *
import manimpango
from config import FONTS_DIR
import render.templates.unit_02_archetypes as u2
from render.templates.base import (
    FONT_HEADER, FONT_CARD, FONT_BODY,
    BG_COLOR, ACCENT_BLUE, ACCENT_GOLD, ACCENT_RED, ACCENT_GREEN,
    TEXT_WHITE, MUTED_TEXT
)

for font_file in FONTS_DIR.glob("*.[tT][tT][fF]"):
    manimpango.register_font(str(font_file.resolve()))

NODE_DATA = {{
    "videoId": "{canonical_id}_{lang}",
    "canonical_id": "{canonical_id}",
    "serialTitle": "{title}",
    "subject": "{concept.get('subject', 'Physics')}",
    "grade": int({concept.get('grade', 11)}),
    "chapter_no": int({concept.get('chapter_no', 2)}),
    "topic_no": int({concept.get('topic_no', 1)}),
    "video_no": int({concept.get('video_no', 1)}),
    "seq_chapter": int({concept.get('chapter_seq', 1)}),
    "total_chapter_videos": int({concept.get('total_chapter_videos', 14)}),
    "next_video_id": "{concept.get('next_video_id', '')}",
    "next_video_title": "{concept.get('next_video_title', '')}",
    "parameters": {{
        "pyqBadge": "HIGH-YIELD CORE",
        "conceptTitle": "{title} — {concept.get('topic_name', 'Straight Line Motion')}"
    }}
}}

class {runner_scene_class}(u2.{base_class}):'''

if old_runner_def in content:
    # replace runner_code = f''' ... class {runner_scene_class}(u2.PositionTimeGraphsScene):
    idx1 = content.find("runner_code = f'''import sys")
    idx2 = content.find("class {runner_scene_class}(u2.PositionTimeGraphsScene):")
    if idx1 != -1 and idx2 != -1:
        content = content[:idx1] + new_runner_def + content[idx2 + len(old_runner_def):]

with open(runner_engine_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated render_multilingual_unit2.py for P11-C02-T03-V08 and dynamic archetype mapping!")
