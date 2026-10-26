import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
runner_path = BASE_DIR / "tools" / "render_multilingual_unit2.py"

with open(runner_path, "r", encoding="utf-8") as f:
    text = f.read()

gate2_scripts = '''    "P11-C02-T02-V01": {
        "en-IN": [
            ("beat_1", "Welcome to 2D Kinematics. In this masterclass, we unlock the foundation of plane motion: the Orthogonal Resolution of Vectors."),
            ("beat_2", "Any two-dimensional vector A can be uniquely decomposed into two mutually perpendicular components: Ax along the x-axis, and Ay along the y-axis, written as A equals Ax i-cap plus Ay j-cap. When the angle theta is measured from the horizontal, Ax equals A cos theta and Ay equals A sin theta, with magnitude root of Ax squared plus Ay squared."),
            ("beat_3", "The central pillar of vector mechanics, emphasized in H C Verma: components along mutually perpendicular axes are completely independent! A force or acceleration along the x-coordinate changes only the x-velocity, exerting zero influence on the y-coordinate."),
            ("beat_4", "Now, beware the fatal NEET Trap: the automatic cosine assumption! When an exam question specifies the angle phi with the vertical axis rather than the horizontal, the components swap: Ay becomes A cos phi and Ax becomes A sin phi. Always attach cosine to the side adjacent to the given angle!")
        ],
        "hi-IN": [
            ("beat_1", "समतल में गति यानी टू-डी किनेमेटिक्स में आपका स्वागत है। इस सत्र में हम सदिशों के समकोणिक वियोजन यानी रेजोल्यूशन ऑफ वेक्टर्स का अध्ययन करेंगे।"),
            ("beat_2", "किसी भी द्विविमीय सदिश ए को दो परस्पर लंबवत घटकों में वियोजित किया जा सकता है: एक्स-अक्ष पर ए-एक्स और वाई-अक्ष पर ए-वाई। जब कोण थीटा क्षैतिज से दिया हो, तो ए-एक्स बराबर ए कॉस थीटा और ए-वाई बराबर ए साइन थीटा होता है।"),
            ("beat_3", "एच सी वर्मा का मूलभूत सिद्धांत याद रखें: परस्पर लंबवत अक्षों के घटक एक-दूसरे से पूर्णतः स्वतंत्र होते हैं! एक्स-दिशा में लगने वाला बल या त्वरण केवल एक्स-घटक को प्रभावित करता है, वाई-घटक पर इसका कोई प्रभाव नहीं पड़ता।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: आँख बंद करके कॉस थीटा लगाने की भूल! यदि परीक्षा में कोण ऊर्ध्वाधर यानी वर्टिकल अक्ष से दिया हो, तो घटक उलट जाते हैं: वाई-घटक कॉस बनता है और एक्स-घटक साइन। हमेशा कोण से सटी संलग्न भुजा के साथ ही कॉस का प्रयोग करें!")
        ],
        "ta-IN": [
            ("beat_1", "தளத்தில் இயக்கத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் இரு பரிமாண இயக்கத்தின் அடித்தளமாக விளங்கும் வெக்டார்களின் செங்குத்து பகுப்பாய்வை ஆராய்கிறோம்."),
            ("beat_2", "எந்தவொரு இரு பரிமாண வெக்டார் ஏ-வையும் இரு செங்குத்து கூறுகளாக பிரிக்கலாம்: எக்ஸ் அச்சு திசையில் ஏ-எக்ஸ் மற்றும் ஒய் அச்சு திசையில் ஏ-ஒய். கோணம் கிடைமட்டத்துடன் இருக்கும் போது, ஏ-எக்ஸ் சமம் ஏ காஸ் தீட்டா, மற்றும் ஏ-ஒய் சமம் ஏ சைன் தீட்டா."),
            ("beat_3", "எச் சி வர்மா குறிப்பிடும் முதன்மை விதியைக் கவனியுங்கள்: செங்குத்து அச்சுகளில் உள்ள கூறுகள் ஒன்றையொன்று பாதிக்காமல் தனித்து இயங்கும்! எக்ஸ் திசையில் உள்ள முடுக்கம் ஒய் திசை இயக்கத்தை எந்த வகையிலும் மாற்றுவதில்லை."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: எப்போதும் கிடைமட்டத்திற்கு காஸ் பயன்படுத்தும் தவறு! கோணம் செங்குத்து அச்சுடன் கொடுக்கப்பட்டால், கூறுகள் மாறும்: ஒய் கூறு காஸ் ஆகவும், எக்ஸ் கூறு சைன் ஆகவும் மாறும். கோணத்தை ஒட்டியுள்ள பக்கத்திற்கே காஸ் பயன்படுத்த வேண்டும்!")
        ]
    },
    "P11-C02-T03-V09": {
        "en-IN": [
            ("beat_1", "Moving deeper into Plane Motion: in this masterclass, we explore Relative Velocity in two dimensions through the classic River-Boat kinematics problem."),
            ("beat_2", "The relative velocity of an object A with respect to B is defined as the vector difference: v-AB equals v-A minus v-B. For a boat steering across a river with water flow velocity v-r, the ground velocity is the vector sum: v-boat equals boat relative to water plus river flow."),
            ("beat_3", "To cross the river along the shortest physical path with zero drift, the boat must steer upstream at an angle sin theta equals v-r divided by v-boat-water. However, to cross the river in minimum time, the boat must steer directly across perpendicular to the banks, resulting in downstream drift."),
            ("beat_4", "Now, heed the fatal NEET Trap: confusing the shortest path with the shortest time! To cross in shortest time, aim directly across; drift will occur. To cross with zero drift, aim upstream; but crossing will take longer. Keep these two distinct conditions crystal clear in NEET Physics!")
        ],
        "hi-IN": [
            ("beat_1", "समतल में गति के महत्वपूर्ण भाग में आपका स्वागत है: इस सत्र में हम नदी और नाव की गति के माध्यम से द्विविमीय आपेक्षिक वेग यानी रिलेटिव वेलोसिटी का अध्ययन करेंगे।"),
            ("beat_2", "वस्तु बी के सापेक्ष वस्तु ए का आपेक्षिक वेग दोनों के सदिश अंतर के बराबर होता है: वी-ए-बी बराबर वी-ए माइनस वी-बी। नदी में बहते जल के सापेक्ष नाव का वेग और नदी के बहाव का सदिश योग ही जमीन के सापेक्ष नाव का कुल वेग निर्धारित करता है।"),
            ("beat_3", "नदी को न्यूनतम दूरी यानी बिना किसी बहाव के सीधे पार करने के लिए नाव को धारा के विपरीत कोण पर चलाना पड़ता है। लेकिन नदी को न्यूनतम समय में पार करने के लिए नाव को ठीक सामने लंबवत दिशा में चलाना होता है, जिससे नाव धारा के साथ आगे बह जाती है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पॉइंट पर: न्यूनतम दूरी और न्यूनतम समय में भ्रम! न्यूनतम समय के लिए सीधे पार करें, जिससे बहाव होगा। न्यूनतम दूरी के लिए धारा के विपरीत चलाएं, जिसमें समय अधिक लगेगा। नीट परीक्षा में प्रश्न की मांग को ध्यान से पढ़कर ही सूत्र का चयन करें!")
        ],
        "ta-IN": [
            ("beat_1", "தளத்தில் இயக்கத்தை தொடர்கிறோம்: இந்த அமர்வில் நாம் ஆற்று-படகு இயக்கத்தின் மூலம் இரு பரிமாண சார்பு திசைவேகத்தை ஆராய்கிறோம்."),
            ("beat_2", "பொருள் பி-யைப் பொறுத்து பொருள் ஏ-வின் சார்பு திசைவேகம் என்பது அவற்றின் வெக்டார் கழித்தலாகும்: வி-ஏ-பி சமம் வி-ஏ மைனஸ் வி-பி. ஆற்றில் செல்லும் படகின் தரைவழி திசைவேகம் என்பது நீரின் திசைவேகம் மற்றும் நீரைப் பொறுத்து படகின் திசைவேகத்தின் வெக்டார் கூடுதலாகும்."),
            ("beat_3", "ஆற்றை மிகக் குறுகிய பாதையில் நேராகக் கடக்க, படகை நீரோட்டத்திற்கு எதிர்திசையில் கோணத்தில் செலுத்த வேண்டும். ஆனால் குறைந்தபட்ச நேரத்தில் ஆற்றைக் கடக்க, படகை கரைகளுக்கு செங்குத்தாக நேரடியாக செலுத்த வேண்டும், இதனால் படகு முன்னோக்கி அடித்துச் செல்லப்படும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: குறைந்தபட்ச பாதை மற்றும் குறைந்தபட்ச நேரக் குழப்பம்! குறைந்த நேரத்தில் கடக்க செங்குத்தாகச் செல்ல வேண்டும், விலகல் ஏற்படும். விலகல் இல்லாமல் நேராகக் கடக்க எதிர்த்திசையில் செலுத்த வேண்டும், நேரம் அதிகமாகும். இந்த இரு நிபந்தனைகளையும் தெளிவாகப் பிரித்தறியுங்கள்!")
        ]
    },'''

# Inject scripts into CONCEPT_BEAT_SCRIPTS
if '"P11-C02-T02-V01"' not in text:
    text = text.replace('CONCEPT_BEAT_SCRIPTS = {\n', 'CONCEPT_BEAT_SCRIPTS = {\n' + gate2_scripts + '\n')

# Update ARCHETYPE_SCENE_MAP
old_map = '''ARCHETYPE_SCENE_MAP = {
    "P11-C02-T01-V01": "PositionTimeGraphsScene",
    "P11-C02-T03-V08": "VelocityTimeGraphsScene",
}'''

new_map = '''ARCHETYPE_SCENE_MAP = {
    "P11-C02-T01-V01": "PositionTimeGraphsScene",
    "P11-C02-T03-V08": "VelocityTimeGraphsScene",
    "P11-C02-T02-V01": "ResolutionOfVectorsScene",
    "P11-C02-T03-V09": "RelativeVelocityScene",
}'''

if old_map in text:
    text = text.replace(old_map, new_map)
elif '"P11-C02-T02-V01"' not in text:
    text = text.replace('"P11-C02-T03-V08": "VelocityTimeGraphsScene",', '"P11-C02-T03-V08": "VelocityTimeGraphsScene",\n    "P11-C02-T02-V01": "ResolutionOfVectorsScene",\n    "P11-C02-T03-V09": "RelativeVelocityScene",')

with open(runner_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Injected Gate 2 scripts & scene mapping successfully!")
