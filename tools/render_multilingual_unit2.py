"""
Master Multilingual Synchronized Concept Video Engine for Unit 2: Kinematics
Codified from IMPLEMENTATION_RULES_v1.0.md (Pillars 11, 12, 13, 14) and .antigravity/rules.md (Rules 8-14).

Enforces:
1. Evergreen NCERT Citation (Zero Page Numbers)
2. Minimalist Ash Telemetry HUD ('HIGH-YIELD CORE', 55% opacity, mono font)
3. Dynamic Audio-Visual Beat Synchronization (Zero hardcoded timers)
4. Mandatory 3.0s NEET Trap Silent Consolidation Hold on Beat 4
5. Pedagogical Punchline & Beat 5 Next Concept End Card
6. Soft Subtitle Multiplexing (mov_text) without -shortest truncation
7. Per-Language Manim Timelines (en-IN, hi-IN, ta-IN)
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

import os
import csv
import json
import time
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any, List

BASE_DIR = Path(r"C:\Users\DELL\.gemini\antigravity\worktrees\neet-video-pipeline_1\optimize_token_usage")
sys.path.insert(0, str(BASE_DIR))
OUTPUT_DIR = BASE_DIR / "output" / "unit_02_kinematics"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VOICES = {
    "en-IN": {"voice": "en-IN-NeerjaExpressiveNeural", "iso639": "eng", "name": "English"},
    "hi-IN": {"voice": "hi-IN-MadhurNeural", "iso639": "hin", "name": "Hindi"},
    "ta-IN": {"voice": "ta-IN-ValluvarNeural", "iso639": "tam", "name": "Tamil"}
}

# Curated 4-Beat Scripts Registry for Unit 2
CONCEPT_BEAT_SCRIPTS = {
    "P11-C02-T04-V01": {
        "en-IN": [
            ("beat_1", "Welcome to Circular Motion. In this masterclass, we explore the dynamics of Uniform Circular Motion and Centripetal Acceleration."),
            ("beat_2", "A particle moving in a circular path of radius r at constant speed v experiences continuous redirection of its velocity vector, resulting in radial inward acceleration: a-c equals v squared divided by r, or omega squared into r."),
            ("beat_3", "Because the centripetal acceleration vector is strictly perpendicular to the instantaneous velocity vector at all times, no work is performed on the particle: power equals force dot velocity equals zero, keeping kinetic energy strictly invariant."),
            ("beat_4", "Now heed the fatal NEET Trap: assuming acceleration is zero because speed is constant! In circular motion, velocity direction changes continuously every millisecond. Centripetal acceleration is strictly non-zero and always directed towards the center!")
        ],
        "hi-IN": [
            ("beat_1", "वृत्तीय गति यानी सर्कुलर मोशन में आपका स्वागत है। इस सत्र में हम एकसमान वृत्तीय गति और अभिकेंद्रीय त्वरण यानी सेंट्रीपीटल एक्सेलेरेशन का अध्ययन करेंगे।"),
            ("beat_2", "त्रिज्या आर के वृत्ताकार पथ पर नियत चाल वी से गतिमान कण के वेग की दिशा लगातार बदलती रहती है, जिससे केंद्र की ओर त्रिज्या के अनुदिश त्वरण उत्पन्न होता है: ए-सी बराबर वी वर्ग बटे आर या ओमेगा वर्ग गुणा आर।"),
            ("beat_3", "चूंकि अभिकेंद्रीय त्वरण हमेशा वेग के लंबवत होता है, इसलिए अभिकेंद्रीय बल द्वारा किया गया कार्य शून्य होता है: शक्ति बराबर बल डॉट वेग बराबर शून्य, जिससे गतिज ऊर्जा सदैव नियत रहती है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: चाल नियत होने के कारण त्वरण को शून्य मान लेना! वृत्तीय गति में वेग की दिशा हर पल बदलती है। अभिकेंद्रीय त्वरण अशून्य होता है और हमेशा केंद्र की ओर निर्देशित रहता है!")
        ],
        "ta-IN": [
            ("beat_1", "வட்ட இயக்கத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் சீரான வட்ட இயக்கம் மற்றும் மையநோக்கு முடுக்கத்தை ஆராய்கிறோம்."),
            ("beat_2", "ஆரம் ஆர் கொண்ட வட்டப் பாதையில் மாறாத வேகம் வி-யில் செல்லும் துகளின் திசைவேக திசை தொடர்ந்து மாறுவதால், மையத்தை நோக்கி முடுக்கம் உருவாகிறது: ஏ-சி சமம் வி ஸ்கொயர் பை ஆர் அல்லது ஒமேகா ஸ்கொயர் ஆர்."),
            ("beat_3", "மையநோக்கு முடுக்கம் திசைவேகத்திற்கு செங்குத்தாக இருப்பதால், செய்யப்பட்ட வேலை பூஜ்ஜியமாகும்: திறன் சமம் விசை டாட் திசைவேகம் சமம் பூஜ்ஜியம், இதனால் இயக்க ஆற்றல் மாறாமல் இருக்கும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: வேகம் மாறாததால் முடுக்கம் பூஜ்ஜியம் என்ற தவறான கணிப்பு! வட்ட இயக்கத்தில் திசைவேகத்தின் திசை தொடர்ந்து மாறுகிறது. மையநோக்கு முடுக்கம் எப்போதும் செயல்படுகிறது!")
        ]
    },
    "P11-C02-T05-V13": {
        "en-IN": [
            ("beat_1", "Mastering Rotational Relations: in this masterclass, we establish the fundamental link between Angular Velocity omega and Linear Speed v."),
            ("beat_2", "For any particle rotating at radius r, linear speed is directly proportional to angular velocity: v equals omega into r. On a rigid rotating body like a wheel, all particles share the identical angular speed omega regardless of radial position."),
            ("beat_3", "Because linear speed scales linearly with distance from the rotation axis, points located further outward on the perimeter travel along longer circular arcs per second, experiencing higher linear speeds and centripetal accelerations."),
            ("beat_4", "Now heed the fatal NEET Trap: believing points closer to the center move faster! On a rigid rotating body, angular velocity omega is constant, so linear speed increases strictly with radius r. Outer perimeter points always move fastest!")
        ],
        "hi-IN": [
            ("beat_1", "घूर्णन संबंधों का अध्ययन: इस सत्र में हम कोणीय वेग ओमेगा और रैखिक चाल वी के बीच मूलभूत संबंध का अध्ययन करेंगे।"),
            ("beat_2", "त्रिज्या आर पर घूमते कण की रैखिक चाल कोणीय वेग के समानुपाती होती है: वी बराबर ओमेगा गुणा आर। किसी दृढ़ घूर्णन पिंड जैसे पहिए के सभी कणों का कोणीय वेग ओमेगा समान रहता है।"),
            ("beat_3", "चूंकि रैखिक चाल घूर्णन अक्ष से दूरी के साथ बढ़ती है, इसलिए बाहरी परिधि पर स्थित कण प्रति सेकंड अधिक दूरी तय करते हैं और उनकी रैखिक चाल तथा अभिकेंद्रीय त्वरण अधिक होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: यह सोचना कि केंद्र के पास वाले बिंदु तेज गति करते हैं! दृढ़ पिंड पर कोणीय वेग समान होता है, इसलिए बाहरी परिधि के बिंदु सबसे अधिक रैखिक चाल से गति करते हैं!")
        ],
        "ta-IN": [
            ("beat_1", "சுழற்சி இயக்கவியல்: இந்த அமர்வில் நாம் கோணத் திசைவேகம் ஒமேகா மற்றும் நேர்க்கோட்டு வேகம் வி-க்கு இடையிலான தொடர்பை ஆராய்கிறோம்."),
            ("beat_2", "ஆரம் ஆர் தூரத்தில் சுழலும் துகளின் நேர்க்கோட்டு வேகம் கோணத் திசைவேகத்திற்கு நேர்விகிதத்தில் இருக்கும்: வி சமம் ஒமேகா இன்டு ஆர். ஒரு சக்கரத்தில் உள்ள அனைத்து புள்ளிகளுக்கும் கோண வேகம் சமமாகும்."),
            ("beat_3", "நேர்க்கோட்டு வேகம் ஆரத்திற்கு ஏற்ப மாறுவதால், வெளிப்புற விளிம்பில் உள்ள புள்ளிகள் வினாடிக்கு அதிக தூரம் கடக்கின்றன, எனவே அவற்றின் வேகம் அதிகமாக இருக்கும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: மையத்திற்கு அருகிலுள்ள புள்ளிகள் வேகமாக நகரும் என்ற பிழை! கோண வேகம் மாறாததால், வெளிப்புற புள்ளிகளே அதிக வேகத்தில் நகரும்!")
        ]
    },
    "P11-C02-T05-V14": {
        "en-IN": [
            ("beat_1", "Advanced Circular Dynamics: in this masterclass, we calculate Net Acceleration in Non-Uniform Circular Motion."),
            ("beat_2", "When the speed of a particle changes along a circular path, it possesses two orthogonal acceleration components: centripetal acceleration a-c equals v squared by r pointing inward, and tangential acceleration a-t equals dv by dt pointing along the tangent."),
            ("beat_3", "The total resultant acceleration vector is the vector sum: a-net equals square root of a-c squared plus a-t squared, directed at an angle theta equals arctan of a-t divided by a-c with respect to the radius vector."),
            ("beat_4", "Now heed the fatal NEET Trap: forgetting the tangential acceleration component! When an exam problem states that speed increases at rate alpha, never calculate acceleration as just v squared by r. You must compute the vector hypotenuse of both components!")
        ],
        "hi-IN": [
            ("beat_1", "उन्नत वृत्तीय गति: इस सत्र में हम असमान वृत्तीय गति यानी नॉन-यूनिफॉर्म सर्कुलर मोशन में कुल परिणामी त्वरण की गणना करेंगे।"),
            ("beat_2", "जब वृत्ताकार पथ पर कण की चाल बदलती है, तो दो लंबवत त्वरण घटक होते हैं: केंद्र की ओर अभिकेंद्रीय त्वरण ए-सी बराबर वी वर्ग बटे आर, और स्पर्श रेखा के अनुदिश स्पर्शरेखीय त्वरण ए-टी बराबर डी-वी बटे डी-टी।"),
            ("beat_3", "कुल परिणामी त्वरण दोनों घटकों का सदिश योग होता है: ए-नेट बराबर रूट में ए-सी वर्ग प्लस ए-टी वर्ग, जो त्रिज्या से टेन थीटा बराबर ए-टी बटे ए-सी के कोण पर झुका होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: स्पर्शरेखीय त्वरण को भूल जाना! जब प्रश्न में चाल में परिवर्तन की दर दी गई हो, तो कुल त्वरण केवल वी वर्ग बटे आर नहीं होता। दोनों घटकों के परिणामी की गणना अवश्य करें!")
        ],
        "ta-IN": [
            ("beat_1", "மேம்பட்ட வட்ட இயக்கவியல்: இந்த அமர்வில் நாம் சீரற்ற வட்ட இயக்கத்தில் நிகர முடுக்கத்தைக் கணக்கிடுகிறோம்."),
            ("beat_2", "வட்டப் பாதையில் வேகம் மாறும் போது இரண்டு செங்குத்து முடுக்கங்கள் செயல்படுகின்றன: மையத்தை நோக்கி மையநோக்கு முடுக்கம் ஏ-சி சமம் வி ஸ்கொயர் பை ஆர், மற்றும் தொடுகோட்டு முடுக்கம் ஏ-டி சமம் டி-வி பை டி-டி."),
            ("beat_3", "மொத்த நிகர முடுக்கம் இவ்விரண்டின் வெக்டார் கூட்டுத்தொகையாகும்: ஏ-நெட் சமம் ரூட் ஆஃப் ஏ-சி ஸ்கொயர் பிளஸ் ஏ-டி ஸ்கொயர்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: தொடுகோட்டு முடுக்கத்தை மறந்துவிடுவது! வேகம் மாறும் போது முடுக்கம் வி ஸ்கொயர் பை ஆர் மட்டுமே அல்ல. இரண்டு கூறுகளின் விளைவு முடுக்கத்தையே கணக்கிட வேண்டும்!")
        ]
    },
    "P11-C02-T03-V01": {
        "en-IN": [
            ("beat_1", "Welcome to Projectile Motion. In this masterclass, we explore the duration of ballistic flight: the Time of Flight T."),
            ("beat_2", "The total time of flight is governed exclusively by the vertical velocity component: T equals 2 v0 sin theta divided by g. The horizontal velocity v0 cos theta proceeds at constant speed with zero acceleration, exerting no effect on time in the air."),
            ("beat_3", "Due to gravitational symmetry, the time taken to reach the highest point equals the time taken to descend back to ground: t-ascent equals t-descent equals v0 sin theta by g. At launch angle 90 degrees, flight time is maximum."),
            ("beat_4", "Now heed the fatal NEET Trap: when launch angle phi is specified with the VERTICAL axis! In that case, the vertical velocity becomes v0 cos phi, so time of flight is 2 v0 cos phi by g. Never blindly write sine without checking which axis theta is measured from!")
        ],
        "hi-IN": [
            ("beat_1", "प्रक्षेप्य गति यानी प्रोजेक्टाइल मोशन में आपका स्वागत है। इस सत्र में हम उड्डयन काल यानी टाइम ऑफ फ्लाइट टी का अध्ययन करेंगे।"),
            ("beat_2", "कुल उड्डयन काल केवल प्रारंभिक वेग के ऊर्ध्वाधर घटक पर निर्भर करता है: टी बराबर 2 वी-शून्य साइन थीटा बटे जी। क्षैतिज वेग वी-शून्य कॉस थीटा एकसमान रहता है और उड्डयन काल पर इसका कोई प्रभाव नहीं पड़ता।"),
            ("beat_3", "गुरुत्वाकर्षण की सममिति के कारण उच्चतम बिंदु तक पहुँचने का समय और वापस जमीन तक आने का समय ठीक बराबर होता है: टी-आरोहण बराबर टी-अवरोहण बराबर वी-शून्य साइन थीटा बटे जी।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: जब कोण ऊर्ध्वाधर अक्ष से दिया गया हो! ऐसी स्थिति में ऊर्ध्वाधर घटक वी-शून्य कॉस फाई बनता है और उड्डयन काल 2 वी-शून्य कॉस फाई बटे जी हो जाता है। हमेशा कोण के संदर्भ अक्ष की जांच करें!")
        ],
        "ta-IN": [
            ("beat_1", "எறிபொருள் இயக்கத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் எறிபொருளின் பறக்கும் காலத்தை ஆராய்கிறோம்."),
            ("beat_2", "மொத்த பறக்கும் காலம் செங்குத்து திசைவேகக் கூறினால் மட்டுமே தீர்மானிக்கப்படுகிறது: டி சமம் 2 வி-0 சைன் தீட்டா பை ஜி. கிடைமட்ட திசைவேகம் பறக்கும் காலத்தை எந்த வகையிலும் மாற்றுவதில்லை."),
            ("beat_3", "புவியீர்ப்பு சமச்சீர்நிலையின் காரணமாக, உச்சியை அடையும் நேரமும் தரையை வந்தடையும் நேரமும் சமமாகும்: ஏறும் நேரம் சமம் இறங்கும் நேரம் சமம் வி-0 சைன் தீட்டா பை ஜி."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: கோணம் செங்குத்து அச்சுடன் கொடுக்கப்படும் போது! அப்போது பறக்கும் காலம் 2 வி-0 காஸ் பை ஜி ஆக மாறும். எந்த அச்சுடன் கோணம் உள்ளது என்பதை உறுதிப்படுத்தாமல் சைன் பயன்படுத்தாதீர்கள்!")
        ]
    },
    "P11-C02-T03-V02": {
        "en-IN": [
            ("beat_1", "Continuing Projectile Motion: in this masterclass, we analyze the highest point of the parabolic arc: Maximum Height H-max."),
            ("beat_2", "Maximum height is achieved when the vertical velocity component momentarily drops to zero: vy equals zero, yielding H-max equals v0 squared sin squared theta divided by 2g. Crucially, the horizontal velocity vx equals v0 cos theta remains completely intact!"),
            ("beat_3", "At the apex, mechanical energy is conserved: potential energy is maximum, while kinetic energy reaches its minimum non-zero value: K-apex equals half m v0 squared cos squared theta. Furthermore, velocity and gravitational acceleration are strictly perpendicular at the top."),
            ("beat_4", "Now heed the fatal NEET Trap: assuming velocity is zero at the apex! Only the vertical velocity component is zero; the particle continues moving forward at v0 cos theta. Speed and kinetic energy are minimum, never zero!")
        ],
        "hi-IN": [
            ("beat_1", "प्रक्षेप्य गति को आगे बढ़ाते हुए: इस सत्र में हम परवलयाकार पथ के उच्चतम बिंदु यानी महत्तम ऊंचाई एच-मैक्स का विश्लेषण करेंगे।"),
            ("beat_2", "महत्तम ऊंचाई तब प्राप्त होती है जब ऊर्ध्वाधर वेग वी-वाई क्षण भर के लिए शून्य हो जाता है, जिससे एच-मैक्स बराबर वी-शून्य वर्ग साइन वर्ग थीटा बटे 2 जी मिलता है। ध्यान रखें कि क्षैतिज वेग वी-शून्य कॉस थीटा निरंतर बना रहता है!"),
            ("beat_3", "शीर्ष बिंदु पर गतिज ऊर्जा न्यूनतम लेकिन अशून्य होती है: के बराबर आधा एम वी-शून्य वर्ग कॉस वर्ग थीटा। साथ ही उच्चतम बिंदु पर वेग और त्वरण परस्पर लंबवत होते हैं।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: शीर्ष पर कुल वेग को शून्य मान लेना! केवल ऊर्ध्वाधर वेग शून्य होता है, क्षैतिज गति निरंतर जारी रहती है। गतिज ऊर्जा न्यूनतम होती है, शून्य कभी नहीं!")
        ],
        "ta-IN": [
            ("beat_1", "எறிபொருள் இயக்கத்தை தொடர்கிறோம்: இந்த அமர்வில் நாம் பரவளையப் பாதையின் உச்ச உயரத்தை ஆராய்கிறோம்."),
            ("beat_2", "செங்குத்து திசைவேகம் வி-ஒய் பூஜ்ஜியமாகும் போது உச்ச உயரம் எட்டப்படுகிறது: எச்-மேக்ஸ் சமம் வி-0 ஸ்கொயர் சைன் ஸ்கொயர் தீட்டா பை 2 ஜி. ஆனால் கிடைமட்ட திசைவேகம் தொடர்ந்து இயங்குகிறது!"),
            ("beat_3", "உச்சியில் இயக்க ஆற்றல் பூஜ்ஜியம் அல்ல, அது குறைந்தபட்ச மதிப்பை அடைகிறது. மேலும் உச்சிப் புள்ளியில் திசைவேகமும் புவியீர்ப்பு முடுக்கமும் சரியாக செங்குத்தாக இருக்கும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: உச்சியில் திசைவேகம் பூஜ்ஜியம் என்ற தவறான கணிப்பு! செங்குத்து திசைவேகம் மட்டுமே பூஜ்ஜியம்; துகள் தொடர்ந்து முன்னோக்கி நகர்கிறது. இயக்க ஆற்றல் எப்போதும் பூஜ்ஜியமாகாது!")
        ]
    },
    "P11-C02-T03-V03": {
        "en-IN": [
            ("beat_1", "Continuing Projectile Dynamics: in this masterclass, we explore Horizontal Range R and the fascinating symmetry of Complementary Projection Angles."),
            ("beat_2", "Horizontal range is the total horizontal displacement: R equals v0 squared sin 2 theta divided by g. Range achieves its absolute maximum value R-max equals v0 squared by g at launch angle theta equals 45 degrees."),
            ("beat_3", "Remarkably, horizontal range is identical for complementary launch angles theta and 90 minus theta! Furthermore, the product of their flight times T1 into T2 equals 2R by g, and the product of their maximum heights H1 into H2 equals R squared by 16."),
            ("beat_4", "Now heed the fatal NEET Trap: assuming equal heights and flight times for complementary angles! Although the landing range is identical, the larger angle 90 minus theta attains a vastly greater height and spends much longer in the air!")
        ],
        "hi-IN": [
            ("beat_1", "प्रक्षेप्य गति के अगले भाग में: इस सत्र में हम क्षैतिज परास यानी हॉरिजॉन्टल रेंज आर और पूरक कोणों की सममिति का अध्ययन करेंगे।"),
            ("beat_2", "क्षैतिज परास कुल क्षैतिज दूरी होती है: आर बराबर वी-शून्य वर्ग साइन 2 थीटा बटे जी। 45 डिग्री के प्रक्षेपण कोण पर परास अधिकतम प्राप्त होती है: आर-मैक्स बराबर वी-शून्य वर्ग बटे जी।"),
            ("beat_3", "पूरक कोणों थीटा और 90 माइनस थीटा के लिए क्षैतिज परास बिल्कुल एक समान होती है! साथ ही दोनों उड्डयन कालों का गुणनफल 2 आर बटे जी और महत्तम ऊंचाइयों का गुणनफल आर वर्ग बटे 16 होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: पूरक कोणों के लिए ऊंचाई को भी बराबर मान लेना! हालांकि परास समान होती है, लेकिन बड़े कोण के लिए उड्डयन काल और महत्तम ऊंचाई दोनों काफी अधिक होते हैं!")
        ],
        "ta-IN": [
            ("beat_1", "எறிபொருள் இயக்கத்தின் அடுத்த பகுதி: இந்த அமர்வில் நாம் கிடைமட்ட வீச்சு மற்றும் நிரப்புக் கோணங்களின் சமச்சீர்நிலையை ஆராய்கிறோம்."),
            ("beat_2", "கிடைமட்ட வீச்சு என்பது மொத்த கிடைமட்ட இடப்பெயர்ச்சியாகும்: ஆர் சமம் வி-0 ஸ்கொயர் சைன் 2 தீட்டா பை ஜி. 45 டிகிரி கோணத்தில் அதிகபட்ச வீச்சு கிடைக்கிறது."),
            ("beat_3", "தீட்டா மற்றும் 90 மைனஸ் தீட்டா ஆகிய நிரப்புக் கோணங்களுக்கு கிடைமட்ட வீச்சு ஒரே மாதிரியாக இருக்கும்! மேலும் அவற்றின் பறக்கும் காலங்களின் பெருக்கற்பலன் 2 ஆர் பை ஜி ஆகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: நிரப்புக் கோணங்களுக்கு உயரமும் சமம் என்று நினைப்பது! வீச்சு சமமாக இருந்தாலும், அதிக கோணத்தில் செல்லும் எறிபொருளின் உயரமும் பறக்கும் நேரமும் அதிகமாக இருக்கும்!")
        ]
    },
    "P11-C02-T03-V04": {
        "en-IN": [
            ("beat_1", "Mastering Trajectory Geometry: in this masterclass, we derive and apply the Cartesian Equation of Trajectory for projectile flight."),
            ("beat_2", "By eliminating time t from the horizontal and vertical parametric equations, we obtain y equals x tan theta minus g x squared divided by 2 v0 squared cos squared theta, proving the path is a downward-opening parabola."),
            ("beat_3", "H C Verma highlights an invaluable alternative formulation: y equals x tan theta into 1 minus x by R, which relates coordinates directly to horizontal range R and solves complex numericals in seconds."),
            ("beat_4", "Now heed the fatal NEET Trap: misidentifying trajectory coefficients! In given polynomial equations like y equals root 3 x minus 5 x squared, remember that tan theta equals the linear coefficient, while the quadratic denominator strictly contains cos squared theta, never sin squared theta!")
        ],
        "hi-IN": [
            ("beat_1", "प्रक्षेप्य पथ की ज्यामिति: इस सत्र में हम प्रक्षेप्य के परवलयाकार पथ का समीकरण यानी इक्वेशन ऑफ ट्रेजेक्टरी का अध्ययन करेंगे।"),
            ("beat_2", "समय टी को विलोपित करने पर हमें पथ का समीकरण प्राप्त होता है: वाई बराबर एक्स टेन थीटा माइनस जी एक्स वर्ग बटे 2 वी-शून्य वर्ग कॉस वर्ग थीटा, जो यह सिद्ध करता है कि पथ परवलयाकार है।"),
            ("beat_3", "एच सी वर्मा का संक्षिप्त रूप याद रखें: वाई बराबर एक्स टेन थीटा कोष्ठक में 1 माइनस एक्स बटे आर। यह सूत्र नीट के कठिन प्रश्नों को सीधे हल कर देता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: समीकरण के गुणांकों को गलत पहचानना! याद रखें कि रैखिक गुणांक टेन थीटा देता है, जबकि द्विघात पद के हर में हमेशा कॉस वर्ग थीटा होता है!")
        ],
        "ta-IN": [
            ("beat_1", "எறிபாதை வடிவியல்: இந்த அமர்வில் நாம் எறிபொருளின் கார்ட்டீசியன் பாதை சமன்பாட்டை ஆராய்கிறோம்."),
            ("beat_2", "காலம் டி-யை நீக்குவதன் மூலம், ஒய் சமம் எக்ஸ் டான் தீட்டா மைனஸ் ஜி எக்ஸ் ஸ்கொயர் பை 2 வி-0 ஸ்கொயர் காஸ் ஸ்கொயர் தீட்டா என்ற பரவளைய பாதை சமன்பாடு கிடைக்கிறது."),
            ("beat_3", "எச் சி வர்மா குறிப்பிடும் குறுக்கு வழி சூத்திரம்: ஒய் சமம் எக்ஸ் டான் தீட்டா இன்டு 1 மைனஸ் எக்ஸ் பை ஆர். இது வீச்சு கொடுக்கப்பட்ட கணக்குகளை எளிதில் தீர்க்கும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: சமன்பாட்டின் குணகங்களை அடையாளம் காண்பதில் தவறு! பகுதியில் எப்போதும் காஸ் ஸ்கொயர் தீட்டா மட்டுமே வரும் என்பதை நினைவில் கொள்ளுங்கள்!")
        ]
    },
    "P11-C02-T04-V10": {
        "en-IN": [
            ("beat_1", "Extending Ballistics: in this masterclass, we investigate Horizontal Projection from a Cliff of Height h."),
            ("beat_2", "Because the launch is purely horizontal, initial vertical velocity vy is zero. Therefore, the time to strike the ground is t equals root of 2h by g, exactly identical to a body dropped freely from rest!"),
            ("beat_3", "Horizontal motion proceeds independently at constant speed v0, yielding range R equals v0 into root of 2h by g. The resultant impact velocity is root of v0 squared plus 2gh."),
            ("beat_4", "Now heed the fatal NEET Trap: believing a high-speed projectile takes longer to hit the ground! The horizontal velocity has zero impact on vertical acceleration. A dropped bullet and a horizontally fired bullet hit the ground simultaneously!")
        ],
        "hi-IN": [
            ("beat_1", "प्रक्षेप्य गति का महत्वपूर्ण प्रयोग: इस सत्र में हम किसी ऊंचाई एच से क्षैतिज प्रक्षेपण का अध्ययन करेंगे।"),
            ("beat_2", "चूंकि प्रक्षेपण पूरी तरह क्षैतिज है, प्रारंभिक ऊर्ध्वाधर वेग शून्य होता है। इसलिए जमीन तक पहुँचने का समय टी बराबर रूट 2 एच बटे जी होता है, जो मुक्त रूप से गिराई गई वस्तु के समान है!"),
            ("beat_3", "क्षैतिज गति निरंतर वेग वी-शून्य से चलती है, जिससे क्षैतिज परास आर बराबर वी-शून्य गुणा रूट 2 एच बटे जी मिलती है। जमीन पर टकराते समय कुल वेग रूट वी-शून्य वर्ग प्लस 2 जी एच होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: यह सोचना कि तेज गति से दागी गई गोली देर से गिरेगी! क्षैतिज वेग का ऊर्ध्वाधर गति पर कोई प्रभाव नहीं पड़ता। गिराई गई और क्षैतिज दागी गई दोनों वस्तुएं एक साथ जमीन पर टकराती हैं!")
        ],
        "ta-IN": [
            ("beat_1", "எறிபொருளின் அடுத்த பயன்பாடு: இந்த அமர்வில் நாம் ஒரு உயரத்திலிருந்து கிடைமட்டமாக எறியப்படும் பொருளின் இயக்கத்தை ஆராய்கிறோம்."),
            ("beat_2", "தொடக்க செங்குத்து திசைவேகம் பூஜ்ஜியமாக இருப்பதால், தரையை அடையும் நேரம் டி சமம் ரூட் 2 எச் பை ஜி. இது தானாக கீழே விழும் பொருளின் நேரத்திற்கு சமமாகும்!"),
            ("beat_3", "கிடைமட்ட திசைவேகம் மாறாமல் வி-0 ஆக நீடிக்கிறது, எனவே வீச்சு ஆர் சமம் வி-0 இன்டு ரூட் 2 எச் பை ஜி. தரையைத் தாக்கும் இறுதி வேகம் ரூட் வி-0 ஸ்கொயர் பிளஸ் 2 ஜி எச்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: வேகமாக எறியப்பட்ட பொருள் தரையைத் தாமதமாகத் தொடும் என்ற தவறான எண்ணம்! கிடைமட்ட வேகம் செங்குத்து வீழ்ச்சியை மாற்றுவதில்லை. இரண்டும் ஒரே நேரத்தில் தரையைத் தாக்கும்!")
        ]
    },
    "P11-C02-T04-V11": {
        "en-IN": [
            ("beat_1", "Advanced Kinematics: in this masterclass, we solve Projectiles on an Inclined Plane of angle beta."),
            ("beat_2", "We establish a rotated coordinate system: x-prime along the incline, and y-prime perpendicular to the incline. Acceleration due to gravity decomposes into ax-prime equals minus g sin beta and ay-prime equals minus g cos beta."),
            ("beat_3", "The time of flight is T equals 2 v0 sin(alpha minus beta) divided by g cos beta. Maximum range up the incline is achieved at launch angle alpha equals 45 degrees plus beta by 2."),
            ("beat_4", "Now heed the fatal NEET Trap: assuming zero acceleration along the inclined plane! Unlike flat ground, the motion along the incline is retarded by g sin beta. Range calculations must include minus half g sin beta T squared!")
        ],
        "hi-IN": [
            ("beat_1", "उन्नत प्रक्षेप्य गति: इस सत्र में हम आनत तल यानी इंक्लाइंड प्लेन पर प्रक्षेप्य गति का विश्लेषण करेंगे।"),
            ("beat_2", "हम निर्देशांक अक्षों को घुमाते हैं: तल के अनुदिश एक्स-डैश और तल के लंबवत वाई-डैश। गुरुत्वीय त्वरण दो घटकों में टूटता है: तल के अनुदिश माइनस जी साइन बीटा और लंबवत माइनस जी कॉस बीटा।"),
            ("beat_3", "उड्डयन काल टी बराबर 2 वी-शून्य साइन(अल्फा माइनस बीटा) बटे जी कॉस बीटा होता है। आनत तल पर अधिकतम परास के लिए प्रक्षेपण कोण अल्फा बराबर 45 डिग्री प्लस बीटा बटे 2 होना चाहिए।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: आनत तल के अनुदिश त्वरण को शून्य मान लेना! समतल जमीन के विपरीत, यहाँ तल पर मंदन जी साइन बीटा कार्य करता है। परास में माइनस आधा जी साइन बीटा टी वर्ग को कभी न भूलें!")
        ],
        "ta-IN": [
            ("beat_1", "மேம்பட்ட இயக்கவியல்: இந்த அமர்வில் நாம் சாய்வு தளத்தின் மீதான எறிபொருள் இயக்கத்தை ஆராய்கிறோம்."),
            ("beat_2", "நாம் ஆய அச்சுகளை சாய்வு தளத்திற்கு ஏற்ப திருப்புகிறோம்: சாய்வின் திசையில் முடுக்கம் மைனஸ் ஜி சைன் பீட்டா மற்றும் செங்குத்தாக மைனஸ் ஜி காஸ் பீட்டா."),
            ("beat_3", "பறக்கும் காலம் டி சமம் 2 வி-0 சைன்(ஆல்பா மைனஸ் பீட்டா) பை ஜி காஸ் பீட்டா. அதிகபட்ச வீச்சுக்கான கோணம் ஆல்பா சமம் 45 டிகிரி பிளஸ் பீட்டா பை 2."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: சாய்வு தளத்தில் முடுக்கம் பூஜ்ஜியம் என நினைப்பது! சாய்வின் திசையில் ஜி சைன் பீட்டா என்ற எதிர் முடுக்கம் செயல்படுகிறது. இதை கணக்கில் கொள்ள தவறாதீர்கள்!")
        ]
    },
    "P11-C02-T04-V12": {
        "en-IN": [
            ("beat_1", "Curvature Analysis: in this masterclass, we calculate the Radius of Curvature at the apex of a projectile trajectory."),
            ("beat_2", "The radius of curvature rho equals speed squared divided by normal acceleration: rho equals v squared by a-n. At the apex, speed is strictly v0 cos theta, and gravitational acceleration g is purely normal to the velocity!"),
            ("beat_3", "Therefore, the radius of curvature at the apex simplifies to rho-apex equals v0 squared cos squared theta divided by g. This is the sharpest, most curved point along the entire ballistic trajectory."),
            ("beat_4", "Now heed the fatal NEET Trap: substituting total launch speed v0 at the apex! Speed at the apex is only the horizontal component v0 cos theta. Using v0 yields a radius too large by a factor of sec squared theta!")
        ],
        "hi-IN": [
            ("beat_1", "वक्रता विश्लेषण: इस सत्र में हम प्रक्षेप्य पथ के उच्चतम बिंदु पर वक्रता त्रिज्या यानी रेडियस ऑफ कर्वेचर की गणना करेंगे।"),
            ("beat_2", "वक्रता त्रिज्या रो बराबर चाल का वर्ग बटे अभिलंब त्वरण होती है। शीर्ष बिंदु पर चाल केवल वी-शून्य कॉस थीटा होती है, और गुरुत्वीय त्वरण जी पूर्णतः वेग के लंबवत होता है!"),
            ("beat_3", "अतः शीर्ष पर वक्रता त्रिज्या रो-शीर्ष बराबर वी-शून्य वर्ग कॉस वर्ग थीटा बटे जी प्राप्त होती है। यह पूरे प्रक्षेप्य पथ का सबसे तीव्र मोड़ वाला बिंदु होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: शीर्ष पर प्रारंभिक चाल वी-शून्य रख देना! शीर्ष पर चाल केवल क्षैतिज घटक होती है। पूरे वी-शून्य का उपयोग करने से उत्तर गलत हो जाता है!")
        ],
        "ta-IN": [
            ("beat_1", "வளைவு பகுப்பாய்வு: இந்த அமர்வில் நாம் எறிபாதை உச்சியில் வளைவு ஆரத்தை கணக்கிடுகிறோம்."),
            ("beat_2", "வளைவு ஆரம் ரோ சமம் வேகம் ஸ்கொயர் பை செங்குத்து முடுக்கம். உச்சியில் வேகம் வி-0 காஸ் தீட்டா மட்டுமே, மற்றும் புவியீர்ப்பு முடுக்கம் ஜி முழுமையாக திசைவேகத்திற்கு செங்குத்தாக உள்ளது!"),
            ("beat_3", "எனவே உச்சியில் வளைவு ஆரம் ரோ சமம் வி-0 ஸ்கொயர் காஸ் ஸ்கொயர் தீட்டா பை ஜி. இது முழு பாதையிலும் மிகக் கூர்மையான வளைவுப் புள்ளியாகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: உச்சியில் தொடக்க வேகம் வி-0 வைப் பயன்படுத்துவது! உச்சியில் கிடைமட்ட கூறு மட்டுமே உள்ளது, எனவே வி-0 காஸ் தீட்டாவையே பயன்படுத்த வேண்டும்!")
        ]
    },
    "P11-C02-T02-V01": {
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
    },
    "P11-C02-T03-V08": {
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
    },
    "P11-C02-T01-V01": {
        "en-IN": [
            ("beat_1", "Welcome to Kinematics. In this masterclass, we explore motion in a straight line through the geometry of Position-Time graphs."),
            ("beat_2", "The instantaneous velocity of a particle is the time derivative of position, v equals dx by dt, geometrically defined as the tangent slope at any point on the position-time curve. A positive slope indicates forward motion, a negative slope represents backward motion, and a zero slope denotes a state of rest."),
            ("beat_3", "A horizontal flat line indicates zero velocity and zero acceleration. A straight line with constant slope represents uniform velocity with zero acceleration. A curved path represents accelerated motion: concave upwards denotes positive acceleration, while concave downwards denotes retardation. Crucially, as emphasized in H C Verma: negative slope indicates velocity direction, not necessarily deceleration."),
            ("beat_4", "Now, heed the fatal NEET Trap: students frequently confuse the slope of an x-t graph with a v-t graph! On a position-time graph, a flat line means zero velocity, not constant velocity. Furthermore, the slope of an x-t curve yields velocity, never acceleration. Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "किनेमेटिक्स में आपका स्वागत है। इस सत्र में हम स्थिति-समय ग्राफ यानी एक्स-टी ग्राफ की ज्यामिति के माध्यम से सरल रेखा में गति का अध्ययन करेंगे।"),
            ("beat_2", "किसी कण का तात्क्षणिक वेग स्थिति का समय के सापेक्ष अवकलज होता है, यानी वी बराबर डी-एक्स बटे डी-टी, जो स्थिति-समय वक्र के किसी भी बिंदु पर स्पर्श रेखा की प्रवणता या ढाल को दर्शाता है। धनात्मक ढाल आगे की दिशा में गति, ऋणात्मक ढाल विपरीत दिशा में गति, और शून्य ढाल विराम अवस्था को दर्शाता है।"),
            ("beat_3", "समय अक्ष के समांतर सीधी रेखा का अर्थ है वेग शून्य है। नियत ढाल वाली सरल रेखा एकसमान वेग को दर्शाती है जहाँ त्वरण शून्य होता है। वक्राकार पथ त्वरित गति को दर्शाता है: ऊपर की ओर अवतल वक्र धनात्मक त्वरण और नीचे की ओर अवतल वक्र मंदन को दर्शाता है। एच सी वर्मा का महत्वपूर्ण बिंदु याद रखें: ऋणात्मक ढाल गति की दिशा को दर्शाता है, आवश्यक नहीं कि यह मंदन ही हो।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पॉइंट पर: छात्र अक्सर एक्स-टी ग्राफ की ढाल को वी-टी ग्राफ की ढाल समझ बैठते हैं! स्थिति-समय ग्राफ पर क्षैतिज रेखा का अर्थ वेग शून्य यानी विराम है, एकसमान वेग नहीं। साथ ही, एक्स-टी ग्राफ की ढाल हमेशा वेग देती है, त्वरण कभी नहीं। नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் நிலை-கால வரைபடங்களின் வடிவியல் மூலம் நேர்க்கோட்டு இயக்கத்தை ஆராய்கிறோம்."),
            ("beat_2", "ஒரு துகளின் உடனடி திசைவேகம் என்பது காலத்தைப் பொறுத்து நிலையின் வகையீடாகும், அதாவது வி சமம் டி-எக்ஸ் பை டி-டி. இது நிலை-கால வளைவரையின் தொடுகோட்டின் சாய்வைக் குறிக்கிறது. நேர்மறை சாய்வு முன்னோக்கிய இயக்கத்தையும், எதிர்மறை சாய்வு பின்னோக்கிய இயக்கத்தையும், பூஜ்ஜிய சாய்வு ஓய்வு நிலையையும் குறிக்கிறது."),
            ("beat_3", "கால அச்சுக்கு இணையான கிடைமட்டக் கோடு பூஜ்ஜிய திசைவேகத்தைக் குறிக்கிறது. நிலையான சாய்வு கொண்ட நேர்க்கோடு சீரான திசைவேகத்தைக் குறிக்கிறது, இதில் முடுக்கம் பூஜ்ஜியம். வளைந்த பாதை முடுக்கப்பட்ட இயக்கத்தைக் குறிக்கிறது: மேல்நோக்கி குழிந்த வளைவரை நேர்மறை முடுக்கத்தையும், கீழ்நோக்கி குழிந்த வளைவரை எதிர்மறை முடுக்கத்தையும் குறிக்கிறது. எச் சி வர்மா குறிப்பிடுவது போல: எதிர்மறை சாய்வு என்பது திசையைக் குறிக்கிறதே தவிர, அது எப்போதும் வேகக்குறைவு அல்ல."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: மாணவர்கள் எக்ஸ்-டி வரைபடத்தின் சாய்வை வி-டி வரைபடத்தின் சாய்வுடன் அடிக்கடி குழப்பிக் கொள்கிறார்கள்! நிலை-கால வரைபடத்தில் கிடைமட்டக் கோடு என்பது ஓய்வு நிலையைக் குறிக்கும், சீரான திசைவேகத்தை அல்ல. மேலும் எக்ஸ்-டி வரைபடத்தின் சாய்வு திசைவேகத்தை மட்டுமே தரும், முடுக்கத்தை அல்ல. நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    }
}


ARCHETYPE_SCENE_MAP = {
    "P11-C02-T01-V01": "PositionTimeGraphsScene",
    "P11-C02-T03-V08": "VelocityTimeGraphsScene",
    "P11-C02-T02-V01": "ResolutionOfVectorsScene",
    "P11-C02-T03-V09": "RelativeVelocityScene",
    "P11-C02-T03-V01": "TimeOfFlightScene",
    "P11-C02-T03-V02": "MaxHeightArcScene",
    "P11-C02-T03-V03": "HorizontalRangeScene",
    "P11-C02-T03-V04": "TrajectoryEquationScene",
    "P11-C02-T04-V10": "HorizontalProjectionScene",
    "P11-C02-T04-V11": "InclinedPlaneProjectileScene",
    "P11-C02-T04-V12": "RadiusOfCurvatureScene",
    "P11-C02-T04-V01": "CentripetalAccelerationScene",
    "P11-C02-T05-V13": "AngularVelocityScene",
    "P11-C02-T05-V14": "NonUniformCircularScene",
}

def load_concept_row(canonical_id: str) -> Dict[str, Any]:
    csv_path = BASE_DIR / "queue" / "curriculum" / "physics" / "unit_02_kinematics.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r.get("canonical_id") == canonical_id:
                return r
    raise ValueError(f"Concept {canonical_id} not found in {csv_path}")

def format_timestamp_srt(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    s, ms = divmod(millis, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def format_timestamp_vtt(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    s, ms = divmod(millis, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"

def render_concept_multilingual_unit2(canonical_id: str, languages: List[str] = None):
    if languages is None:
        languages = ["en-IN", "hi-IN", "ta-IN"]

    concept = load_concept_row(canonical_id)
    title = concept["concept_title"]

    print("=" * 80)
    print(f"🎬 MASTER MULTILINGUAL CONCEPT PIPELINE (UNIT 2): {canonical_id}")
    print(f"   Title   : {title}")
    print(f"   Target Languages: {languages}")
    print("=" * 80)

    from audio.engine import AudioEngine
    audio_engine = AudioEngine(default_provider="edge_tts")

    for lang in languages:
        cfg = VOICES[lang]
        voice = cfg["voice"]
        iso639 = cfg["iso639"]
        lang_name = cfg["name"]

        final_mp4 = OUTPUT_DIR / f"{canonical_id}_{lang}.mp4"
        if final_mp4.exists() and final_mp4.stat().st_size > 500000:
            print(f"\n-------------------------------------------------------------")
            print(f"⚡ [CACHED] {final_mp4.name} already exists ({final_mp4.stat().st_size / (1024*1024):.2f} MB). Skipping render.")
            print(f"-------------------------------------------------------------")
            continue

        print(f"\n-------------------------------------------------------------")
        print(f"🌍 PROCESSING LANGUAGE: {lang} ({lang_name})")
        print(f"-------------------------------------------------------------")

        beat_dir = BASE_DIR / "output" / "beat_audio" / f"{canonical_id}_{lang}"
        beat_dir.mkdir(parents=True, exist_ok=True)

        # Step 1: Synthesize discrete beat audio files
        scripts = CONCEPT_BEAT_SCRIPTS[canonical_id][lang]
        durations = {}

        print(f"🔊 Synthesizing discrete beat audios with {voice}...")
        for b_name, text in scripts:
            b_file = beat_dir / f"{b_name}.mp3"
            if not b_file.exists() or b_file.stat().st_size == 0:
                if b_file.exists() and b_file.stat().st_size == 0:
                    b_file.unlink()
                for attempt in range(6):
                    try:
                        audio_engine.generate_narration(
                            text=text,
                            output_path=b_file,
                            provider="edge_tts",
                            voice_id=voice,
                            language=lang,
                            use_cache=True
                        )
                        if b_file.exists() and b_file.stat().st_size > 1000:
                            break
                        else:
                            raise RuntimeError(f"Generated 0-byte or tiny file: {b_file}")
                    except Exception as e:
                        if b_file.exists() and b_file.stat().st_size == 0:
                            b_file.unlink()
                        if attempt == 5:
                            raise
                        sleep_s = 3.0 * (attempt + 1)
                        print(f"      [!] TTS retry {attempt+1}/5 after network warning: {e} (waiting {sleep_s:.1f}s)...")
                        time.sleep(sleep_s)
            cmd_probe = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(b_file)]
            res_p = subprocess.run(cmd_probe, capture_output=True, text=True, check=True)
            dur = float(json.loads(res_p.stdout)["format"]["duration"])
            durations[b_name] = dur
            print(f"   {b_name}: {dur:.2f}s | \"{text[:50]}...\"")

        with open(beat_dir / "durations.json", "w", encoding="utf-8") as f:
            json.dump(durations, f, indent=2)

        # Step 2: Timeline Architecture
        dur_b1 = durations["beat_1"]
        dur_b2 = durations["beat_2"]
        dur_b3 = durations["beat_3"]
        dur_b4 = durations["beat_4"]

        wait_b1 = max(1.0, dur_b1 - 0.8 + 0.5)
        total_b1 = 0.8 + wait_b1 + 0.6

        wait_b2 = max(1.0, dur_b2 - 0.8 + 0.5)
        total_b2 = 0.8 + wait_b2 + 0.6

        wait_b3 = max(1.0, dur_b3 - 0.8 + 0.5)
        total_b3 = 0.8 + wait_b3 + 0.6

        TRAP_HOLD = 3.0
        wait_b4 = max(1.0, dur_b4 - 0.8 + TRAP_HOLD)
        total_b4 = 0.8 + wait_b4 + 0.6

        total_b5 = 3.5
        total_video_time = total_b1 + total_b2 + total_b3 + total_b4 + total_b5

        offset_b1 = 0.2
        offset_b2 = total_b1 + 0.2
        offset_b3 = total_b1 + total_b2 + 0.2
        offset_b4 = total_b1 + total_b2 + total_b3 + 0.2

        print(f"\n⏱️ Dynamic Pacing & Silence Windows [{lang}]:")
        print(f"   Beat 1: wait {wait_b1:.2f}s (Total {total_b1:.2f}s)")
        print(f"   Beat 2: wait {wait_b2:.2f}s (Total {total_b2:.2f}s)")
        print(f"   Beat 3: wait {wait_b3:.2f}s (Total {total_b3:.2f}s)")
        print(f"   Beat 4: wait {wait_b4:.2f}s (Total {total_b4:.2f}s, incl. {TRAP_HOLD:.1f}s silent freeze)")
        print(f"   Beat 5: {total_b5:.2f}s")
        print(f"   Total Timeline: {total_video_time:.2f}s")

        # Step 3: Stitch Master Audio Track
        master_audio = beat_dir / f"{canonical_id}_{lang}_synced_master.wav"
        filter_str = (
            f"[0:a]adelay={int(offset_b1*1000)}|{int(offset_b1*1000)}[a1]; "
            f"[1:a]adelay={int(offset_b2*1000)}|{int(offset_b2*1000)}[a2]; "
            f"[2:a]adelay={int(offset_b3*1000)}|{int(offset_b3*1000)}[a3]; "
            f"[3:a]adelay={int(offset_b4*1000)}|{int(offset_b4*1000)}[a4]; "
            f"[a1][a2][a3][a4]amix=inputs=4:duration=longest:dropout_transition=0,volume=1.0[outa]"
        )
        cmd_audio = [
            "ffmpeg", "-y",
            "-i", str(beat_dir / "beat_1.mp3"),
            "-i", str(beat_dir / "beat_2.mp3"),
            "-i", str(beat_dir / "beat_3.mp3"),
            "-i", str(beat_dir / "beat_4.mp3"),
            "-filter_complex", filter_str,
            "-map", "[outa]",
            "-t", f"{total_video_time:.3f}",
            str(master_audio)
        ]
        subprocess.run(cmd_audio, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"   [+] Synced Master Audio: {master_audio.name}")

        # Step 4: Generate Manim Runner Script
        runner_scene_class = f"Synced_{canonical_id.replace('-', '_')}_{lang.replace('-', '_')}"
        base_class = ARCHETYPE_SCENE_MAP.get(canonical_id, "ModularUnit2Scene")
        runner_code = f'''import sys
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

class {runner_scene_class}(u2.{base_class}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)

    def render_concept_beats(self):
        # Beat 1: Intro (Evergreen citation, Zero Page Numbers)
        b1 = self.build_beat_1()
        self.play(FadeIn(b1, shift=UP * 0.2), run_time=0.8)
        self.wait({wait_b1:.3f})
        self.play(FadeOut(b1), run_time=0.6)

        # Beat 2: Hero Stage / Graph
        b2 = self.build_beat_2()
        self.play(FadeIn(b2), run_time=0.8)
        self.wait({wait_b2:.3f})
        self.play(FadeOut(b2), run_time=0.6)

        # Beat 3: Core Scenarios & HCV Nuance
        b3 = self.build_beat_3()
        self.play(FadeIn(b3), run_time=0.8)
        self.wait({wait_b3:.3f})
        self.play(FadeOut(b3), run_time=0.6)

        # Beat 4: NEET Trap Card (Includes 3.0s Silent Hold)
        b4 = self.build_beat_4()
        self.play(FadeIn(b4), run_time=0.8)
        self.wait({wait_b4:.3f})
        self.play(FadeOut(b4), run_time=0.6)

        # Beat 5: Transition Teaser
        self.render_release_teaser(duration=3.5)
'''

        runner_path = beat_dir / f"runner_{lang}.py"
        runner_path.write_text(runner_code, encoding="utf-8")
        print(f"   [+] Manim Runner Script: {runner_path.name}")

        # Step 5: Render Manim Scene
        out_raw_video = beat_dir / f"{canonical_id}_{lang}_synced_raw.mp4"
        cmd_manim = [
            "manim", "render",
            "-r", "1920,1080",
            "--fps", "30",
            "--media_dir", str(beat_dir / "manim_media"),
            "-o", out_raw_video.name,
            str(runner_path),
            runner_scene_class
        ]

        print(f"🎥 Rendering Synchronized Manim Scene ({total_video_time:.2f}s)...")
        res_m = subprocess.run(cmd_manim, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res_m.returncode != 0:
            print(f"Manim error:\n{res_m.stderr[-600:]}")
            raise RuntimeError(f"Manim compilation failed for {canonical_id} {lang}")

        raw_vid_found = None
        for f in (beat_dir / "manim_media").rglob("*.mp4"):
            if f.name == out_raw_video.name:
                raw_vid_found = f
                break

        if not raw_vid_found or not raw_vid_found.exists():
            for f in (beat_dir / "manim_media").rglob("*.mp4"):
                if f.name != "partial_movie_files":
                    raw_vid_found = f
                    break

        print(f"   [+] Raw Manim Video: {raw_vid_found}")

        # Step 6: Generate Subtitles & Mux Final Production MP4
        srt_file = beat_dir / f"{canonical_id}_{lang}.srt"
        vtt_file = beat_dir / f"{canonical_id}_{lang}.vtt"

        beats_timeline = [
            (1, offset_b1, offset_b1 + dur_b1, scripts[0][1]),
            (2, offset_b2, offset_b2 + dur_b2, scripts[1][1]),
            (3, offset_b3, offset_b3 + dur_b3, scripts[2][1]),
            (4, offset_b4, offset_b4 + dur_b4, scripts[3][1])
        ]

        with open(srt_file, "w", encoding="utf-8") as fs, open(vtt_file, "w", encoding="utf-8") as fv:
            fv.write("WEBVTT\n\n")
            for idx, start_t, end_t, text_content in beats_timeline:
                fs.write(f"{idx}\n{format_timestamp_srt(start_t)} --> {format_timestamp_srt(end_t)}\n{text_content}\n\n")
                fv.write(f"{idx}\n{format_timestamp_vtt(start_t)} --> {format_timestamp_vtt(end_t)}\n{text_content}\n\n")

        final_mp4 = OUTPUT_DIR / f"{canonical_id}_{lang}.mp4"
        cmd_mux = [
            "ffmpeg", "-y",
            "-i", str(raw_vid_found),
            "-i", str(master_audio),
            "-i", str(srt_file),
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-map", "2:s:0",
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-c:s", "mov_text",
            "-metadata:s:s:0", f"language={iso639}",
            "-metadata:s:s:0", f"title={lang_name}",
            str(final_mp4)
        ]
        subprocess.run(cmd_mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        f_size_mb = final_mp4.stat().st_size / (1024 * 1024)
        print(f"   ✨ FINAL BROADCAST PRODUCTION VIDEO: {final_mp4.name} ({f_size_mb:.2f} MB)")

if __name__ == "__main__":
    cid = sys.argv[1] if len(sys.argv) > 1 else "P11-C02-T01-V01"
    target_langs = sys.argv[2].split(",") if len(sys.argv) > 2 else ["en-IN", "hi-IN", "ta-IN"]
    render_concept_multilingual_unit2(cid, target_langs)
