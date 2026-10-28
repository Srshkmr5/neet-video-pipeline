"""
Master Multilingual Synchronized Concept Video Engine for Unit 3: Laws of Motion
Codified from IMPLEMENTATION_RULES_v1.0.md (Pillars 11, 12, 13, 14) and .antigravity/rules.md (Rules 8-20).

Enforces:
1. Evergreen NCERT Citation (Zero Page Numbers)
2. Minimalist Ash Telemetry HUD ('HIGH-YIELD CORE', 55% opacity, mono font)
3. Dynamic Audio-Visual Beat Synchronization (Zero hardcoded timers)
4. Mandatory 3.0s NEET Trap Silent Consolidation Hold on Beat 4
5. Pedagogical Punchline & Beat 5 Next Concept End Card
6. Soft Subtitle Multiplexing (mov_text) without -shortest truncation
7. Per-Language Manim Timelines (en-IN, hi-IN, ta-IN)
8. Lossless Audio Padding (apad) to Prevent Player Stalling
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
OUTPUT_DIR = BASE_DIR / "output" / "unit_03_laws_of_motion"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
FINAL_VIDEOS_DIR = BASE_DIR / "output" / "final_videos"
FINAL_VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
SUBTITLES_DIR = BASE_DIR / "output" / "subtitles"
SUBTITLES_DIR.mkdir(parents=True, exist_ok=True)

VOICES = {
    "en-IN": {"voice": "en-IN-NeerjaExpressiveNeural", "iso639": "eng", "name": "English"},
    "hi-IN": {"voice": "hi-IN-MadhurNeural", "iso639": "hin", "name": "Hindi"},
    "ta-IN": {"voice": "ta-IN-ValluvarNeural", "iso639": "tam", "name": "Tamil"}
}

# Curated 4-Beat Scripts Registry for Unit 3 (Laws of Motion)
CONCEPT_BEAT_SCRIPTS = {
    "P11-C03-T01-V01": {
        "en-IN": [
            ("beat_1", "Welcome to Laws of Motion. In this masterclass, we explore Newton's First Law of Motion, Galileo's Principle of Inertia, and Free-Body Diagrams."),
            ("beat_2", "Newton's First Law states that every body continues in its state of rest or uniform rectilinear motion unless acted upon by a non-zero net external force. In translational equilibrium, vector sum of external forces is strictly zero."),
            ("beat_3", "A Free-Body Diagram isolates the body and resolves all external forces along orthogonal axes. When a block is pulled at angle theta, normal reaction N becomes mg minus F sin theta, directly altering the contact pressure with the floor."),
            ("beat_4", "Now heed the fatal NEET Trap: including internal forces or reaction forces exerted BY the body on other objects in its own FBD! Only forces acting ON the isolated body count. Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "गति के नियम में आपका स्वागत है। इस सत्र में हम न्यूटन के गति के प्रथम नियम, जड़त्व के सिद्धांत और मुक्त पिंड आरेख यानी फ्री-बॉडी डायग्राम का अध्ययन करेंगे।"),
            ("beat_2", "न्यूटन का प्रथम नियम कहता है कि प्रत्येक पिंड अपनी विरामावस्था या सरल रेखा में एकसमान गति की अवस्था में तब तक बना रहता है जब तक कि उस पर कोई बाह्य बल न लगाया जाए। संतुलन में सभी बाह्य बलों का सदिश योग शून्य होता है।"),
            ("beat_3", "फ्री-बॉडी डायग्राम में वस्तु को अलग करके उस पर लगने वाले सभी बाह्य बलों को लंबवत अक्षों पर वियोजित करते हैं। जब किसी गुटके को थीटा कोण पर खींचा जाता है, तो अभिलंब बल एन बराबर एम जी माइनस एफ साइन थीटा हो जाता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: वस्तु के स्वयं के फ्री-बॉडी डायग्राम में आंतरिक बलों या वस्तु द्वारा दूसरों पर लगाए गए बलों को शामिल करना! केवल वस्तु पर लगने वाले बाह्य बल ही गिने जाते हैं। नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "இயக்க விதிகள் பகுதிக்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் நியூட்டனின் முதல் இயக்க விதி, நிலைமக் கொள்கை மற்றும் விசைப் படங்களை ஆராய்கிறோம்."),
            ("beat_2", "புறவிசை செயல்படாதவரை ஒவ்வொரு பொருளும் தனது ஓய்வு நிலையையோ அல்லது சீரான நேர்க்கோட்டு இயக்க நிலையையோ தொடர்ந்து பராமரிக்கும். சமநிலையில் அனைத்து புறவிசைகளின் கூடுதல் பூஜ்ஜியமாகும்."),
            ("beat_3", "விசைப் படத்தில் பொருளை தனிமைப்படுத்தி அதன் மீது செயல்படும் விசைகள் செங்குத்து கூறுகளாகப் பிரிக்கப்படுகின்றன. தீட்டா கோணத்தில் இழுக்கப்படும் போது செங்குத்து விசை என் சமம் எம் ஜி மைனஸ் எஃப் சைன் தீட்டா என மாறுகிறது."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: பொருள் பிற பொருட்கள் மீது செலுத்தும் விசைகளை அதன் சொந்த விசைப் படத்தில் சேர்ப்பது பெரும் பிழையாகும்! பொருள் மீது செயல்படும் விசைகள் மட்டுமே கணக்கிடப்பட வேண்டும். நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T01-V02": {
        "en-IN": [
            ("beat_1", "Continuing Newton's Dynamics: in this masterclass, we explore the Second Law of Motion, Apparent Weight in Elevators, and Pseudo Forces."),
            ("beat_2", "Newton's Second Law establishes that net external force equals mass times acceleration: F equals m a. Inside an accelerating elevator, the normal force on a scale reflects apparent weight: N equals m into g plus a when accelerating upwards, and m into g minus a when accelerating downwards."),
            ("beat_3", "In non-inertial accelerating reference frames, an observer must introduce a fictitious pseudo force F-pseudo equals minus m a-zero opposite to the frame acceleration. In free fall where downward acceleration equals g, apparent weight drops to zero, producing weightlessness."),
            ("beat_4", "Now heed the fatal NEET Trap: confusing upward velocity with upward acceleration! An elevator ascending while slowing down has acceleration directed downwards, so normal force is m into g minus a, NOT g plus a! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "न्यूटन की गतिशीलता को आगे बढ़ाते हुए: इस सत्र में हम गति के द्वितीय नियम, लिफ्ट में आभासी भार और छद्म बल यानी स्यूडो फोर्स का विश्लेषण करेंगे।"),
            ("beat_2", "न्यूटन का द्वितीय नियम बताता है कि कुल बाह्य बल द्रव्यमान गुणा त्वरण के बराबर होता है: एफ बराबर एम ए। त्वरित लिफ्ट में आभासी भार एन ऊपर की ओर त्वरण पर एम गुणा जी प्लस ए और नीचे की ओर त्वरण पर एम गुणा जी माइनस ए होता है।"),
            ("beat_3", "अजड़त्वीय निर्देश तंत्र में फ्रेम के त्वरण के विपरीत दिशा में एक छद्म बल एफ-स्यूडो बराबर माइनस एम ए-शून्य लगाना अनिवार्य होता है। स्वतंत्र रूप से गिरती लिफ्ट में आभासी भार शून्य हो जाता है, जिससे भारहीनता उत्पन्न होती है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: ऊपर की दिशा में वेग को ऊपर की दिशा में त्वरण समझ लेना! ऊपर जाती हुई धीमी होती लिफ्ट में त्वरण नीचे की ओर होता है, इसलिए अभिलंब बल एम गुणा जी माइनस ए होता है! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "நியூட்டனின் இயக்கவியலை தொடர்கிறோம்: இந்த அமர்வில் நாம் இரண்டாம் இயக்க விதி, மின்தூக்கியில் தோற்ற எடை மற்றும் போலி விசைகளை ஆராய்கிறோம்."),
            ("beat_2", "தொகுபயன் புறவிசை முடுக்கத்திற்கு நேர்விகிதத்தில் இருக்கும்: எஃப் சமம் எம் ஏ. மின்தூக்கி மேலே முடுக்கமடையும் போது தோற்ற எடை எம் இன்டு ஜி பிளஸ் ஏ ஆகவும், கீழே முடுக்கமடையும் போது எம் இன்டு ஜி மைனஸ் ஏ ஆகவும் மாறும்."),
            ("beat_3", "முடுக்கமடையும் அமைப்பில் அமைப்பின் முடுக்கத்திற்கு எதிர் திசையில் போலி விசை மைனஸ் எம் ஏ-0 செயல்படுகிறது. தடையின்றி கீழே விழும் மின்தூக்கியில் முடுக்கம் ஜி ஆக இருப்பதால் தோற்ற எடை பூஜ்ஜியமாகி எடையற்ற நிலை உண்டாகிறது."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: திசைவேக திசையையும் முடுக்க திசையையும் குழப்பிக் கொள்வது! மேலே சென்று வேகம் குறையும் மின்தூக்கியின் முடுக்கம் கீழ்நோக்கியது, எனவே எடை எம் இன்டு ஜி மைனஸ் ஏ ஆகும்! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T01-V03": {
        "en-IN": [
            ("beat_1", "Mastering Third Law Dynamics: in this masterclass, we explore Action-Reaction pairs and String Tension in Atwood Machines."),
            ("beat_2", "Newton's Third Law states that every action has an equal and opposite reaction. Crucially, action and reaction act simultaneously on two completely different bodies, meaning they can NEVER cancel each other out on a single object."),
            ("beat_3", "In an Atwood Machine with masses m1 greater than m2 over an ideal frictionless pulley, common acceleration is m1 minus m2 divided by m1 plus m2 into g, while uniform string tension is 2 m1 m2 g divided by m1 plus m2."),
            ("beat_4", "Now heed the fatal NEET Trap: claiming Normal force and gravity on a table block are an action-reaction pair! Both act on the SAME block and cancel by the First Law. The true reaction to Earth's gravity is the block's gravitational pull on Earth! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "तृतीय नियम की गतिशीलता: इस सत्र में हम क्रिया-प्रतिक्रिया युग्म और एटवुड मशीन में डोरी के तनाव का अध्ययन करेंगे।"),
            ("beat_2", "न्यूटन का तृतीय नियम कहता है कि प्रत्येक क्रिया के बराबर और विपरीत प्रतिक्रिया होती है। महत्वपूर्ण बात यह है कि क्रिया और प्रतिक्रिया दो अलग-अलग पिंडों पर एक साथ लगती हैं, इसलिए वे कभी एक पिंड पर निरस्त नहीं हो सकतीं।"),
            ("beat_3", "घर्षणरहित घिरनी पर दो द्रव्यमानों वाली एटवुड मशीन में साझा त्वरण एम-1 माइनस एम-2 बटे एम-1 प्लस एम-2 गुणा जी होता है, और डोरी का तनाव 2 एम-1 एम-2 जी बटे एम-1 प्लस एम-2 होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: मेज पर रखे गुटके पर अभिलंब बल और गुरुत्वाकर्षण को क्रिया-प्रतिक्रिया युग्म मान लेना! ये दोनों एक ही गुटके पर लगते हैं और प्रथम नियम से संतुलित होते हैं। गुरुत्वाकर्षण की वास्तविक प्रतिक्रिया गुटके द्वारा पृथ्वी पर लगाया गया खिंचाव है! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "மூன்றாம் விதி இயக்கவியல்: இந்த அமர்வில் நாம் செயல்-எதிர்செயல் இணைகள் மற்றும் கப்பி அமைப்பில் கயிற்றின் இழுவிசையை ஆராய்கிறோம்."),
            ("beat_2", "ஒவ்வொரு செயலுக்கும் சமமான எதிர்செயல் உண்டு. மிக முக்கியமாக செயலும் எதிர்செயலும் இரண்டு வெவ்வேறு பொருட்களின் மீது ஒரே நேரத்தில் செயல்படுவதால் அவை ஒருபோதும் தம்முள் சமன் செய்யாது."),
            ("beat_3", "கப்பியுடன் இணைக்கப்பட்ட இரண்டு நிறைகளின் பொதுவான முடுக்கம் எம்-1 மைனஸ் எம்-2 பை எம்-1 பிளஸ் எம்-2 இன்டு ஜி ஆகும். கயிற்றின் இழுவிசை 2 எம்-1 எம்-2 ஜி பை எம்-1 பிளஸ் எம்-2 ஆகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: மேஜை மீதான செங்குத்து விசையையும் புவியீர்ப்பையும் செயல்-எதிர்செயல் ஜோடி எனக் கருதுவது! இரண்டும் ஒரே பொருளின் மீது செயல்படுகின்றன. புவியீர்ப்பின் உண்மையான எதிர்செயல் பொருள் பூமி மீது செலுத்தும் ஈர்ப்பு விசையே! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T02-V04": {
        "en-IN": [
            ("beat_1", "Welcome to Momentum Dynamics. In this masterclass, we explore Linear Momentum, Impulse, and the Area under the Force-Time Curve."),
            ("beat_2", "Linear momentum is mass times velocity vector. By the Impulse-Momentum Theorem, total impulse J equals the change in linear momentum Delta p, which is represented geometrically by the area under the Force-Time graph: J equals integral F dt."),
            ("beat_3", "In elastic wall collisions where a ball of mass m strikes perpendicularly at speed v and rebounds at speed v, the vector change in momentum is minus m v minus m v, producing total impulse magnitude of 2 m v. At incidence angle theta with the normal, impulse is 2 m v cos theta."),
            ("beat_4", "Now heed the fatal NEET Trap: forgetting the negative sign of rebound velocity and calculating Delta p as mv minus mv equals zero! Momentum is a strict vector; reversing direction doubles the impulse to 2 m v! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "संवेग गतिशीलता में आपका स्वागत है। इस सत्र में हम रैखिक संवेग, आवेग यानी इम्पल्स और बल-समय वक्र के क्षेत्रफल का अध्ययन करेंगे।"),
            ("beat_2", "रैखिक संवेग द्रव्यमान और वेग सदिश का गुणनफल होता है। आवेग-संवेग प्रमेय के अनुसार कुल आवेग जे संवेग में परिवर्तन डेल्टा पी के बराबर होता है, जो बल-समय ग्राफ के अंतर्गत आने वाले क्षेत्रफल से प्राप्त होता है।"),
            ("beat_3", "दीवार से प्रत्यास्थ टक्कर में जब एम द्रव्यमान की गेंद वी चाल से टकराकर वापस लौटती है, तो संवेग में सदिश परिवर्तन माइनस एम वी माइनस एम वी होता है, जिससे कुल आवेग 2 एम वी बनता है। थीटा कोण पर यह 2 एम वी कॉस थीटा होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: प्रत्यावर्ती वेग के ऋण चिह्न को भूलकर संवेग परिवर्तन को शून्य मान लेना! संवेग एक सदिश राशि है; दिशा उलटने से आवेग दोगुना होकर 2 एम वी हो जाता है! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "உந்த இயக்கவியலுக்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் நேர்க்கோட்டு உந்தம், கணத்தாக்கு விசை மற்றும் விசை-கால வரைபடப் பரப்பை ஆராய்கிறோம்."),
            ("beat_2", "நேர்க்கோட்டு உந்தம் நிறை மற்றும் திசைவேகத்தின் பெருக்கற்பலனாகும். கணத்தாக்கு விசை உந்த மாறுபாட்டிற்குச் சமமாகும், இது விசை-கால வரைபடத்தின் பரப்பளவினால் குறிக்கப்படுகிறது: ஜே சமம் இன்டெக்ரல் எஃப் டி-டி."),
            ("beat_3", "சுவரில் மோதி மீளும் பந்தின் உந்த மாறுபாடு மைனஸ் எம் வி மைனஸ் எம் வி என அமைவதால் மொத்த கணத்தாக்கு 2 எம் வி ஆகிறது. செங்குத்துடன் தீட்டா கோணத்தில் மோதினால் கணத்தாக்கு 2 எம் வி காஸ் தீட்டா ஆகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: திசை மாறிய திசைவேகத்தின் எதிர் குறியை மறந்து உந்த மாறுபாட்டை பூஜ்ஜியம் என தவறாகக் கணக்கிடுவது! திசைவேகம் தலைகீழாக மாறுவதால் உந்த மாறுபாடு இரட்டிப்பாகி 2 எம் வி ஆகும்! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T02-V05": {
        "en-IN": [
            ("beat_1", "Continuing Momentum Principles: in this masterclass, we analyze the Law of Conservation of Linear Momentum and Variable Mass Rocket Propulsion."),
            ("beat_2", "When the net external force on a system is zero, total linear momentum remains strictly invariant. For a rifle of mass M firing a bullet of mass m with velocity v, recoil velocity is V equals minus m divided by M into v."),
            ("beat_3", "In variable-mass rocket propulsion, ejecting fuel at relative exhaust speed u creates upward thrust force F-thrust equals u into dm by dt. The net upward acceleration is u by m into dm by dt minus g."),
            ("beat_4", "Now heed the fatal NEET Trap: neglecting the mass of the bullet or using scalar speeds instead of signed vectors in recoil problems! Momentum conservation requires strict directional signs. Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "संवेग सिद्धांतों को आगे बढ़ाते हुए: इस सत्र में हम रैखिक संवेग संरक्षण के नियम और रॉकेट नोदन यानी रॉकेट प्रोपल्शन का विश्लेषण करेंगे।"),
            ("beat_2", "जब किसी निकाय पर कुल बाह्य बल शून्य होता है, तो उसका कुल रैखिक संवेग सदैव संरक्षित रहता है। द्रव्यमान एम की बंदूक से द्रव्यमान छोटे एम की गोली वी वेग से दागने पर बंदूक का प्रतिक्षेप वेग वी बराबर माइनस छोटा एम बटे बड़ा एम गुणा वी होता है।"),
            ("beat_3", "परिवर्ती द्रव्यमान वाले रॉकेट में सापेक्ष निकास चाल यू से गैस बाहर निकलने पर ऊपर की ओर थ्रस्ट बल यू गुणा डी-एम बटे डी-टी उत्पन्न होता है। कुल त्वरण यू बटे एम गुणा डी-एम बटे डी-टी माइनस जी होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: बंदूक के प्रतिक्षेप में दिशा के चिह्न की उपेक्षा करना या गोली के द्रव्यमान को भूल जाना! संवेग संरक्षण में सदिश चिह्नों का पालन अनिवार्य है। नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "உந்தக் கொள்கைகளை தொடர்கிறோம்: இந்த அமர்வில் நாம் நேர்க்கோட்டு உந்த மாறா விதி மற்றும் ராக்கெட் உந்துவிசையை ஆராய்கிறோம்."),
            ("beat_2", "புறவிசை செயல்படாத அமைப்பில் மொத்த நேர்க்கோட்டு உந்தம் மாறாமல் இருக்கும். துப்பாக்கியிலிருந்து குண்டு பாயும் போது துப்பாக்கியின் பின்னியக்க திசைவேகம் வி சமம் மைனஸ் எம் பை கேபிடல் எம் இன்டு வி ஆகும்."),
            ("beat_3", "மாறும் நிறை கொண்ட ராக்கெட்டில் வாயுக்கள் வெளியேற்றப்படும் போது மேல்நோக்கிய உந்துவிசை யு இன்டு டி-எம் பை டி-டி உருவாகிறது. ராக்கெட்டின் நிகர முடுக்கம் யு பை எம் இன்டு டி-எம் பை டி-டி மைனஸ் ஜி ஆகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: துப்பாக்கி பின்னியக்கத்தில் திசைக் குறியீட்டைப் புறக்கணிப்பது பெரும் தவறாகும்! உந்த மாறா விதியில் வெக்டார் குறியீடுகள் மிக அவசியமானவை. நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T02-V06": {
        "en-IN": [
            ("beat_1", "Mastering Concurrent Equilibrium: in this masterclass, we explore Equilibrium of Concurrent Forces and Lami's Theorem."),
            ("beat_2", "When three coplanar concurrent forces act on a body in static equilibrium, each force magnitude is directly proportional to the sine of the angle between the remaining two forces: F1 by sin alpha equals F2 by sin beta equals F3 by sin gamma."),
            ("beat_3", "Lami's Theorem is the mathematical embodiment of the closed triangle of vectors: the three force vectors placed tip-to-tail form a closed loop with zero resultant, solving tension in hanging cables with incredible speed."),
            ("beat_4", "Now heed the fatal NEET Trap: measuring the angle between a force and a coordinate axis instead of the INTERIOR ANGLE between the other two forces! Always take the angle opposite the force being evaluated. Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "संगाती बलों के संतुलन का अध्ययन: इस सत्र में हम एकबिंदुगामी बलों के संतुलन और लामी की प्रमेय यानी लामीस थ्योरम का अध्ययन करेंगे।"),
            ("beat_2", "जब किसी संतुलन में स्थित पिंड पर तीन समतलीय संगाती बल कार्य करते हैं, तो प्रत्येक बल शेष दो बलों के बीच के कोण की ज्या यानी साइन के समानुपाती होता है: एफ-1 बटे साइन अल्फा बराबर एफ-2 बटे साइन बीटा बराबर एफ-3 बटे साइन गामा।"),
            ("beat_3", "लामी की प्रमेय सदिशों के बंद त्रिभुज नियम का गणितीय रूप है: तीनों बल सदिश मिलकर एक बंद त्रिभुज बनाते हैं जिसका परिणामी शून्य होता है। यह लटके हुए तारों में तनाव तुरंत ज्ञात करने की सबसे तेज विधि है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: कोण को अक्ष से माप लेना, जबकि नियम के अनुसार कोण शेष दो बलों के बीच का होना चाहिए! हमेशा जिस बल का मान निकाल रहे हैं उसके सम्मुख कोण की ज्या लें। नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "ஒருபுள்ளி விசைகளின் சமநிலை: இந்த அமர்வில் நாம் ஒருபுள்ளி விசைகளின் சமநிலை மற்றும் லாமியின் தேற்றத்தை ஆராய்கிறோம்."),
            ("beat_2", "சமநிலையில் உள்ள ஒரு பொருளின் மீது செயல்படும் மூன்று விசைகளில், ஒவ்வொரு விசையின் மதிப்பும் மற்ற இரு விசைகளுக்கு இடைப்பட்ட கோணத்தின் சைன் மதிப்பிற்கு நேர்விகிதத்தில் இருக்கும்: எஃப்-1 பை சைன் ஆல்ஃபா சமம் எஃப்-2 பை சைன் பீட்டா சமம் எஃப்-3 பை சைன் காமா."),
            ("beat_3", "லாமியின் தேற்றம் முக்கோண விசை விதியின் வடிவமாகும்: மூன்று விசைகளும் ஒன்றன்பின் ஒன்றாக இணைந்து மூடிய முக்கோணத்தை உருவாக்குகின்றன, இதன் தொகுபயன் பூஜ்ஜியமாகும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: மற்ற இரு விசைகளுக்கு இடைப்பட்ட கோணத்திற்குப் பதிலாக ஆய அச்சுகளுடன் உள்ள கோணத்தைப் பயன்படுத்துவது! எப்போதும் கணக்கிடும் விசைக்கு எதிரே உள்ள கோணத்தின் சைன் மதிப்பையே எடுக்க வேண்டும். நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T03-V07": {
        "en-IN": [
            ("beat_1", "Welcome to Friction Dynamics. In this masterclass, we analyze Static Friction, Kinetic Friction, and the Classical Friction Graph."),
            ("beat_2", "Static friction is a self-adjusting contact force: it exactly balances applied force up to the limiting threshold: f-s-max equals mu-s into N. Once relative motion initiates, friction drops slightly to kinetic friction f-k equals mu-k into N, remaining virtually constant."),
            ("beat_3", "On the friction-versus-applied-force graph, the static regime exhibits a linear 45-degree slope where friction equals applied force, reaching a sharp peak at limiting friction, followed by a slight drop to a horizontal kinetic plateau."),
            ("beat_4", "Now heed the fatal NEET Trap: blindly computing static friction as mu-s into N when applied force is small! If limiting friction is 20 Newtons and you push with 5 Newtons, actual static friction is exactly 5 Newtons, NOT 20 Newtons! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "घर्षण गतिशीलता में आपका स्वागत है। इस सत्र में हम स्थैतिक घर्षण, गतिक घर्षण और घर्षण ग्राफ का विश्लेषण करेंगे।"),
            ("beat_2", "स्थैतिक घर्षण एक स्वतः-समायोज्य बल है: यह सीमांत मान एफ-एस-मैक्स बराबर म्यू-एस गुणा एन तक लगाए गए बल को ठीक संतुलित करता है। गति आरंभ होते ही घर्षण थोड़ा घटकर गतिक घर्षण म्यू-के गुणा एन पर स्थिर हो जाता है।"),
            ("beat_3", "घर्षण बनाम प्रयुक्त बल के ग्राफ में स्थैतिक क्षेत्र 45 अंश की सीधी रेखा दिखाता है जहाँ घर्षण लगाए गए बल के बराबर होता है, फिर सीमांत मान पर शीर्ष छूकर गतिक घर्षण के क्षैतिज स्तर पर आ जाता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: कम बल लगाने पर भी स्थैतिक घर्षण को सीधे म्यू-एस गुणा एन लिख देना! यदि सीमांत घर्षण 20 न्यूटन है और प्रयुक्त बल 5 न्यूटन है, तो वास्तविक घर्षण ठीक 5 न्यूटन होगा, 20 न्यूटन नहीं! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "உராய்வு இயக்கவியலுக்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் நிலை உராய்வு, இயக்க உராய்வு மற்றும் உராய்வு வரைபடத்தை ஆராய்கிறோம்."),
            ("beat_2", "நிலை உராய்வு தன்னைத்தானே சரிசெய்து கொள்ளும் விசையாகும்: இது வரம்பு உராய்வு எஃப்-எஸ் சமம் மியூ-எஸ் இன்டு என் வரை செலுத்தப்படும் விசைக்கு சமமாக இருக்கும். இயக்கம் தொடங்கியவுடன் இது இயக்க உராய்வு மியூ-கே இன்டு என் என்ற மாறாத மதிப்பிற்கு சற்று குறைகிறது."),
            ("beat_3", "உராய்வு வரைபடத்தில் நிலை உராய்வுப் பகுதி 45 டிகிரி நேர்க்கோடாக உயர்ந்து உச்ச வரம்பை அடைந்து, பின்னர் இயக்க உராய்வின் கிடைமட்டக் கோடாகத் தொடர்கிறது."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: குறைந்த விசை செயல்படும் போதும் நிலை உராய்வை மியூ-எஸ் இன்டு என் என தவறாகக் கணக்கிடுவது! வரம்பு உராய்வு 20 நியூட்டனாக இருந்து நீங்கள் 5 நியூட்டன் செலுத்தினால், உண்மையான நிலை உராய்வு 5 நியூட்டன் மட்டுமே! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T03-V08": {
        "en-IN": [
            ("beat_1", "Continuing Friction Principles: in this masterclass, we explore the Rough Inclined Plane, Angle of Repose, and Asymmetric Accelerations."),
            ("beat_2", "On an incline of angle theta, gravity resolves into mg sin theta down the slope and mg cos theta normal to the slope. The Angle of Repose theta-R is the critical tilt where sliding just begins, defined by tan theta-R equals mu-s."),
            ("beat_3", "Because friction always opposes relative velocity, accelerations are asymmetric: sliding DOWN, acceleration is g into sin theta minus mu-k cos theta. Projected UP, friction and gravity both oppose motion, producing a greater retardation of g into sin theta plus mu-k cos theta."),
            ("beat_4", "Now heed the fatal NEET Trap: using the identical acceleration formula for upward and downward motion on a rough incline! Going up, friction acts downward; going down, friction acts upward. Time of ascent is strictly less than time of descent! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "घर्षण सिद्धांतों को आगे बढ़ाते हुए: इस सत्र में हम खुरदुरे नत समतल, विश्राम कोण यानी एंगल ऑफ रिपोज और असममित त्वरण का अध्ययन करेंगे।"),
            ("beat_2", "थीटा कोण के नत समतल पर गुरुत्वाकर्षण नत के अनुदिश एम जी साइन थीटा और लंबवत एम जी कॉस थीटा में वियोजित होता है। विश्राम कोण वह न्यूनतम झुकाव है जिस पर गुटका स्वतः फिसलने लगता है: टेन थीटा बराबर म्यू-एस।"),
            ("beat_3", "चूंकि घर्षण सदैव गति का विरोध करता है, इसलिए त्वरण असममित होता है: नीचे फिसलते समय त्वरण जी गुणा साइन थीटा माइनस म्यू कॉस थीटा होता है, जबकि ऊपर जाते समय मंदन जी गुणा साइन थीटा प्लस म्यू कॉस थीटा होता है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: ऊपर और नीचे की गति के लिए समान त्वरण का उपयोग करना! ऊपर जाते समय घर्षण नीचे लगता है और नीचे आते समय ऊपर। ऊपर जाने का समय नीचे आने के समय से हमेशा कम होता है! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "உராய்வுக் கொள்கைகளை தொடர்கிறோம்: இந்த அமர்வில் நாம் சொரசொரப்பான சாய்தளம், சறுக்குக் கோணம் மற்றும் சமச்சீரற்ற முடுக்கங்களை ஆராய்கிறோம்."),
            ("beat_2", "சாய்தளத்தில் புவியீர்ப்பு விசை தளம் வழியே எம் ஜி சைன் தீட்டாவாகவும், தளத்திற்கு செங்குத்தாக எம் ஜி காஸ் தீட்டாவாகவும் பிரிகிறது. பொருள் தானாக சரியத் தொடங்கும் சறுக்குக் கோணம் டேன் தீட்டா சமம் மியூ-எஸ் ஆகும்."),
            ("beat_3", "உராய்வு எப்போதும் இயக்கத்தை எதிர்ப்பதால் கீழ்நோக்கி சரியும் போது முடுக்கம் ஜி இன்டு சைன் தீட்டா மைனஸ் மியூ காஸ் தீட்டா ஆகவும், மேல்நோக்கி எறியப்படும் போது எதிர்முடுக்கம் ஜி இன்டு சைன் தீட்டா பிளஸ் மியூ காஸ் தீட்டா ஆகவும் இருக்கும்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: சாய்தளத்தில் மேல்நோக்கிய மற்றும் கீழ்நோக்கிய இயக்கத்திற்கு ஒரே முடுக்கத்தைப் பயன்படுத்துவது! மேலே செல்லும் நேரம் கீழே இறங்கும் நேரத்தை விட எப்போதும் குறைவாகவே இருக்கும்! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T03-V09": {
        "en-IN": [
            ("beat_1", "Advanced Friction Dynamics: in this masterclass, we explore Two-Block Friction Systems and Relative Motion Thresholds."),
            ("beat_2", "For a block m1 placed atop block m2 on a frictionless floor, the only horizontal force accelerating m1 is the static friction between the two blocks. Therefore, the maximum acceleration m1 can experience without slipping is a-max equals mu-s into g."),
            ("beat_3", "When pulling bottom block m2, both blocks accelerate together up to threshold force F-max equals m1 plus m2 into mu-s into g. When applied force exceeds F-max, relative slipping occurs and the friction drops to kinetic friction mu-k into m1 into g."),
            ("beat_4", "Now heed the fatal NEET Trap: using the total composite mass m1 plus m2 when computing normal force at the contact interface between the blocks! Normal reaction between blocks depends exclusively on the top block weight: N equals m1 into g! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "उन्नत घर्षण गतिशीलता: इस सत्र में हम द्वि-गुटका प्रणाली यानी टू-ब्लॉक सिस्टम और सापेक्ष गति की देहली का विश्लेषण करेंगे।"),
            ("beat_2", "घर्षणरहित सतह पर रखे गुटके एम-2 के ऊपर स्थित गुटके एम-1 को त्वरित करने वाला एकमात्र क्षैतिज बल दोनों के बीच का स्थैतिक घर्षण है। इसलिए बिना फिसले एम-1 का अधिकतम त्वरण ए-मैक्स बराबर म्यू-एस गुणा जी होता है।"),
            ("beat_3", "नीचे वाले गुटके एम-2 को खींचने पर दोनों गुटके अधिकतम बल एफ-मैक्स बराबर एम-1 प्लस एम-2 गुणा म्यू-एस गुणा जी तक एक साथ चलते हैं। इससे अधिक बल लगाने पर दोनों में सापेक्ष फिसलन शुरू हो जाती है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: दोनों गुटकों के बीच अभिलंब बल निकालते समय कुल द्रव्यमान एम-1 प्लस एम-2 का उपयोग कर लेना! संपर्क सतह पर अभिलंब बल केवल ऊपरी गुटके के भार एम-1 गुणा जी पर निर्भर करता है! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "மேம்பட்ட உராய்வு இயக்கவியல்: இந்த அமர்வில் நாம் இரட்டைப் பொருள் உராய்வு அமைப்பு மற்றும் சார்பு இயக்க வரம்பை ஆராய்கிறோம்."),
            ("beat_2", "வழுவழுப்பான தரையில் உள்ள எம்-2 நிறையின் மீதிருக்கும் எம்-1 நிறையை முடுக்கும் ஒரே விசை அவற்றுக்கு இடையேயான நிலை உராய்வே ஆகும். எனவே சறுக்கல் இல்லாமல் எம்-1 அடையும் உச்ச முடுக்கம் ஏ-மேக்ஸ் சமம் மியூ-எஸ் இன்டு ஜி ஆகும்."),
            ("beat_3", "கீழ் நிறையை இழுக்கும் போது இரண்டும் இணைந்து செல்லும் பெரும விசை எஃப்-மேக்ஸ் சமம் எம்-1 பிளஸ் எம்-2 இன்டு மியூ-எஸ் இன்டு ஜி ஆகும். விசை இதை விட அதிகரிக்கும் போது சார்பு சறுக்கல் ஏற்படுகிறது."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: பொருட்களுக்கு இடையிலான செங்குத்து விசையைக் கணக்கிடும் போது மொத்த நிறையைப் பயன்படுத்துவது! இடைமுக செங்குத்து விசை மேல் பொருளின் எடை எம்-1 ஜி-யை மட்டுமே சார்ந்தது! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T04-V10": {
        "en-IN": [
            ("beat_1", "Welcome to Circular Dynamics. In this masterclass, we explore Centripetal Force and Skidding Limits on Level Curved Roads."),
            ("beat_2", "When a vehicle negotiates a flat, unbanked circular turn of radius r at speed v, the indispensable inward centripetal acceleration v squared divided by r is supplied exclusively by the static friction between the tires and the asphalt."),
            ("beat_3", "Equating centripetal requirement m v squared by r to maximum available friction mu-s into m into g yields the maximum safe velocity: v-max equals square root of mu-s into r into g. Vehicle mass cancels out entirely!"),
            ("beat_4", "Now heed the fatal NEET Trap: believing heavier vehicles have higher safe turning speeds on flat roads! Mass cancels completely in v-max equals square root of mu-s into r into g. A 10-ton truck and a 100-kilogram motorcycle share the exact same skidding speed! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "वृत्तीय गतिशीलता में आपका स्वागत है। इस सत्र में हम अभिकेंद्रीय बल और समतल वृत्ताकार मोड़ पर फिसलने की सीमा का अध्ययन करेंगे।"),
            ("beat_2", "जब कोई वाहन त्रिज्या आर के समतल मोड़ पर चाल वी से मुड़ता है, तो आवश्यक अभिकेंद्रीय त्वरण वी वर्ग बटे आर पूरी तरह से टायरों और सड़क के बीच के स्थैतिक घर्षण द्वारा प्रदान किया जाता है।"),
            ("beat_3", "अभिकेंद्रीय बल एम वी वर्ग बटे आर को अधिकतम घर्षण म्यू-एस गुणा एम गुणा जी के बराबर रखने पर अधिकतम सुरक्षित चाल प्राप्त होती है: वी-मैक्स बराबर रूट में म्यू-एस गुणा आर गुणा जी। इसमें वाहन का द्रव्यमान पूरी तरह कट जाता है!"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: यह सोचना कि भारी वाहन समतल मोड़ पर अधिक गति से मुड़ सकते हैं! द्रव्यमान पूरी तरह निरस्त हो जाता है। एक भारी ट्रक और एक हल्की बाइक दोनों के फिसलने की अधिकतम सीमा चाल बिल्कुल समान होती है! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "வட்ட இயக்கவியலுக்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் மையநோக்கு விசை மற்றும் மட்டமான வளைவுச் சாலையில் சறுக்கல் வரம்பை ஆராய்கிறோம்."),
            ("beat_2", "மட்டமான வளைவுச் சாலையில் வாகனம் திரும்பும் போது தேவையான மையநோக்கு முடுக்கம் வி ஸ்கொயர் பை ஆர் முழுமையாக டயர்களுக்கும் சாலைக்கும் இடையிலான நிலை உராய்வினால் மட்டுமே வழங்கப்படுகிறது."),
            ("beat_3", "மையநோக்கு விசையை பெரும உராய்விற்கு சமன் செய்யும் போது பாதுகாப்பான உச்ச வேகம் வி-மேக்ஸ் சமம் ரூட் ஆஃப் மியூ-எஸ் இன்டு ஆர் இன்டு ஜி என கிடைக்கிறது. இதில் வாகனத்தின் நிறை முற்றிலும் நீங்கிவிடுகிறது!"),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: அதிக எடையுள்ள வாகனங்கள் வளைவில் வேகமாக திரும்ப முடியும் என்ற தவறான கணிப்பு! வி-மேக்ஸ் சமன்பாட்டில் நிறை இல்லை. கனரக லாரிக்கும் இருசக்கர வாகனத்திற்கும் சறுக்கல் வேக வரம்பு ஒன்றே! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C03-T04-V11": {
        "en-IN": [
            ("beat_1", "Mastering Advanced Circular Dynamics: in this masterclass, we explore Engineered Banking of Roads and Vertical Circle Thresholds."),
            ("beat_2", "By banking a road at angle theta, the horizontal component of normal force N sin theta supplies centripetal acceleration, enabling an optimum speed v-opt equals square root of r g tan theta with zero tire wear and zero friction dependence."),
            ("beat_3", "In vertical circular motion with a mass tied to a light string, tension must remain non-negative at the apex, dictating minimum apex speed square root of g r and minimum bottom launch speed square root of 5 g r. For a light rigid rod that can support compression, apex speed can drop to zero, requiring bottom speed square root of 4 g r equals 2 square root of g r."),
            ("beat_4", "Now heed the fatal NEET Trap: using the string threshold square root of 5 g r for a sphere fixed to a light rigid rod! A rigid rod supports compression and never goes slack; minimum bottom speed is square root of 4 g r, NOT 5 g r! Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "उन्नत वृत्तीय गतिशीलता: इस सत्र में हम सड़कों की बंकिंग यानी झुकाव और ऊर्ध्वाधर वृत्त में गति के क्रांतिक वेगों का अध्ययन करेंगे।"),
            ("beat_2", "सड़क को थीटा कोण पर झुका देने से अभिलंब बल का क्षैतिज घटक एन साइन थीटा अभिकेंद्रीय बल प्रदान करता है, जिससे अनुकूलतम चाल वी-ऑप्ट बराबर रूट में आर जी टेन थीटा मिलती है जहाँ टायरों में कोई घिसाव नहीं होता।"),
            ("beat_3", "डोरी से बंधे पिंड के ऊर्ध्वाधर वृत्त में शीर्ष पर न्यूनतम चाल रूट जी आर और तल पर न्यूनतम चाल रूट 5 जी आर होना आवश्यक है। लेकिन दृढ़ छड़ के लिए शीर्ष पर चाल शून्य हो सकती है, इसलिए तल पर न्यूनतम चाल रूट 4 जी आर यानी 2 रूट जी आर होती है।"),
            ("beat_4", "अब ध्यान दें सबसे घातक नीट ट्रैप पर: हल्की दृढ़ छड़ के लिए भी डोरी वाला सूत्र रूट 5 जी आर लगा देना! छड़ कभी ढीली नहीं पड़ती; तल पर न्यूनतम आवश्यक चाल रूट 4 जी आर होती है, रूट 5 जी आर नहीं! नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "மேம்பட்ட வட்ட இயக்கவியல்: இந்த அமர்வில் நாம் சாலைகளின் வெளிவிளிம்பு உயர்த்துதல் மற்றும் செங்குத்து வட்ட இயக்க வரம்புகளை ஆராய்கிறோம்."),
            ("beat_2", "சாலையை தீட்டா கோணத்தில் உயர்த்துவதன் மூலம் செங்குத்து விசையின் கிடைமட்டக் கூறு என் சைன் தீட்டா மையநோக்கு விசையை வழங்குகிறது. இதனால் உராய்வின்றி செல்லும் உகந்த வேகம் வி-ஆப்ட் சமம் ரூட் ஆஃப் ஆர் ஜி டேன் தீட்டா ஆகும்."),
            ("beat_3", "கயிற்றில் சுழலும் துகள் செங்குத்து வட்டத்தில் முழுமையாகச் சுழல உச்சிப் புள்ளியில் வேகம் ரூட் ஜி ஆர் ஆகவும், அடிப்புள்ளியில் வேகம் ரூட் 5 ஜி ஆர் ஆகவும் இருக்க வேண்டும். ஆனால் திடமான கம்பியில் சுழலும் போது அடிப்புள்ளியில் குறைந்தபட்ச வேகம் ரூட் 4 ஜி ஆர் போதுமானது."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: திடமான கம்பியில் சுழலும் பொருளுக்கும் கயிற்றின் விதியான ரூட் 5 ஜி ஆர்-ஐப் பயன்படுத்துவது! கம்பி சுருங்குவதை தாங்கக்கூடியது என்பதால் அடிப்புள்ளியின் குறைந்தபட்ச வேகம் ரூட் 4 ஜி ஆர் மட்டுமே! நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    }
}

ARCHETYPE_SCENE_MAP = {
    "P11-C03-T01-V01": "FirstLawFbdScene",
    "P11-C03-T01-V02": "SecondLawElevatorScene",
    "P11-C03-T01-V03": "ThirdLawAtwoodScene",
    "P11-C03-T02-V04": "ImpulseFtCurveScene",
    "P11-C03-T02-V05": "RocketMomentumScene",
    "P11-C03-T02-V06": "LamiTheoremScene",
    "P11-C03-T03-V07": "FrictionGraphScene",
    "P11-C03-T03-V08": "RoughInclineReposeScene",
    "P11-C03-T03-V09": "TwoBlockFrictionScene",
    "P11-C03-T04-V10": "LevelCurveSkiddingScene",
    "P11-C03-T04-V11": "BankedRoadVerticalCircleScene"
}

def load_concept_row(canonical_id: str) -> Dict[str, Any]:
    csv_path = BASE_DIR / "queue" / "curriculum" / "physics" / "unit_03_laws_of_motion.csv"
    if csv_path.exists():
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if r.get("canonical_id") == canonical_id:
                    return r

    manifest_path = BASE_DIR / "apps" / "curriculum_manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    for c in manifest["concepts"]:
        if c.get("canonical_id") == canonical_id:
            return {
                "canonical_id": canonical_id,
                "concept_title": c.get("title", ""),
                "subject": c.get("subject", "Physics"),
                "grade": c.get("grade", 11),
                "chapter_no": c.get("chapter_no", 3),
                "topic_no": c.get("topic_no", 1),
                "video_no": c.get("video_no", 1),
                "chapter_seq": 1,
                "total_chapter_videos": 11,
                "next_video_id": "",
                "next_video_title": "",
                "topic_name": c.get("topic_name", "Laws of Motion")
            }
    raise ValueError(f"Concept {canonical_id} not found in manifest or CSV")

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

def extract_storyboard_proofs(video_path: Path, canonical_id: str):
    proof_dir = BASE_DIR / "brain" / "d9fc2045-37b2-4535-b18a-d8358d69714d" / "storyboards_unit3" / canonical_id
    proof_dir.mkdir(parents=True, exist_ok=True)
    if not video_path.exists():
        return

    cmd_p = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(video_path)]
    r = subprocess.run(cmd_p, capture_output=True, text=True)
    dur = float(json.loads(r.stdout)["format"]["duration"])

    samples = [
        ("beat_1_intro.png", min(3.5, dur * 0.08)),
        ("beat_2_hero.png", dur * 0.25),
        ("beat_3_scenarios.png", dur * 0.55),
        ("beat_4_trap.png", dur * 0.82),
        ("beat_5_teaser.png", max(dur - 1.5, dur * 0.95))
    ]

    for name, ts in samples:
        out_f = proof_dir / name
        if not out_f.exists() or out_f.stat().st_size == 0:
            cmd = ["ffmpeg", "-y", "-ss", f"{ts:.2f}", "-i", str(video_path), "-vframes", "1", "-q:v", "2", str(out_f)]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"   [📸 Storyboard Proofs Captured -> {proof_dir.name}]")

def render_concept_multilingual_unit3(canonical_id: str, languages: List[str] = None):
    if languages is None:
        languages = ["en-IN", "hi-IN", "ta-IN"]

    concept = load_concept_row(canonical_id)
    title = concept["concept_title"]

    print("=" * 80)
    print(f"🎬 MASTER MULTILINGUAL CONCEPT PIPELINE (UNIT 3): {canonical_id}")
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
        cached = final_mp4.exists() and final_mp4.stat().st_size > 500000

        if cached:
            print(f"\n-------------------------------------------------------------")
            print(f"⚡ [CACHED] {final_mp4.name} already exists ({final_mp4.stat().st_size / (1024*1024):.2f} MB). Skipping render.")
            print(f"-------------------------------------------------------------")
            # Ensure final_videos has copy
            target_f = FINAL_VIDEOS_DIR / final_mp4.name
            if not target_f.exists():
                shutil.copy2(final_mp4, target_f)
            if lang == "en-IN":
                extract_storyboard_proofs(final_mp4, canonical_id)
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

        # Step 2: Dynamic Timeline Architecture
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

        # Step 3: Stitch Master Audio Track with apad for lossless alignment
        master_audio = beat_dir / f"{canonical_id}_{lang}_synced_master.wav"
        filter_str = (
            f"[0:a]adelay={int(offset_b1*1000)}|{int(offset_b1*1000)}[a1]; "
            f"[1:a]adelay={int(offset_b2*1000)}|{int(offset_b2*1000)}[a2]; "
            f"[2:a]adelay={int(offset_b3*1000)}|{int(offset_b3*1000)}[a3]; "
            f"[3:a]adelay={int(offset_b4*1000)}|{int(offset_b4*1000)}[a4]; "
            f"[a1][a2][a3][a4][4:a]amix=inputs=5:duration=longest:dropout_transition=0,volume=1.0[outa]"
        )
        cmd_audio = [
            "ffmpeg", "-y",
            "-i", str(beat_dir / "beat_1.mp3"),
            "-i", str(beat_dir / "beat_2.mp3"),
            "-i", str(beat_dir / "beat_3.mp3"),
            "-i", str(beat_dir / "beat_4.mp3"),
            "-f", "lavfi", "-t", f"{total_video_time:.3f}", "-i", "anullsrc=r=44100:cl=stereo",
            "-filter_complex", filter_str,
            "-map", "[outa]",
            "-t", f"{total_video_time:.3f}",
            str(master_audio)
        ]
        subprocess.run(cmd_audio, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"   [+] Synced Master Audio: {master_audio.name}")

        # Step 4: Generate Manim Runner Script
        runner_scene_class = f"Synced_{canonical_id.replace('-', '_')}_{lang.replace('-', '_')}"
        base_class = ARCHETYPE_SCENE_MAP.get(canonical_id, "ModularUnit3Scene")
        runner_code = f'''import sys
from pathlib import Path
BASE_DIR = Path({repr(str(BASE_DIR))})
sys.path.insert(0, str(BASE_DIR))

from manim import *
import manimpango
from config import FONTS_DIR
import render.templates.unit_03_archetypes as u3
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
    "chapter_no": int({concept.get('chapter_no', 3)}),
    "topic_no": int({concept.get('topic_no', 1)}),
    "video_no": int({concept.get('video_no', 1)}),
    "seq_chapter": int({concept.get('chapter_seq', 1)}),
    "total_chapter_videos": int({concept.get('total_chapter_videos', 11)}),
    "next_video_id": "{concept.get('next_video_id', '')}",
    "next_video_title": "{concept.get('next_video_title', '')}",
    "parameters": {{
        "pyqBadge": "HIGH-YIELD CORE",
        "conceptTitle": "{title} — {concept.get('topic_name', 'Laws of Motion')}"
    }}
}}

class {runner_scene_class}(u3.{base_class}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)

    def render_concept_beats(self):
        # Beat 1: Intro (Evergreen citation, Zero Page Numbers)
        b1 = self.build_beat_1()
        self.play(FadeIn(b1, shift=UP * 0.2), run_time=0.8)
        self.wait({wait_b1:.3f})
        self.play(FadeOut(b1), run_time=0.6)

        # Beat 2: Hero Stage / Formulas / Diagrams
        b2 = self.build_beat_2()
        self.play(FadeIn(b2), run_time=0.8)
        self.wait({wait_b2:.3f})
        self.play(FadeOut(b2), run_time=0.6)

        # Beat 3: Core Scenarios & Nuance
        b3 = self.build_beat_3()
        self.play(FadeIn(b3), run_time=0.8)
        self.wait({wait_b3:.3f})
        self.play(FadeOut(b3), run_time=0.6)

        # Beat 4: NEET Trap Card (Includes 3.0s Silent Hold)
        b4 = self.build_beat_4()
        self.play(FadeIn(b4), run_time=0.8)
        self.wait({wait_b4:.3f})
        self.play(FadeOut(b4), run_time=0.6)

        # Beat 5: Next Video End Card
        b5 = self.build_beat_5()
        self.play(FadeIn(b5), run_time=0.8)
        self.wait(1.9)
        self.play(FadeOut(b5), run_time=0.8)
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

        # Copy VTT to global subtitles directory for direct EdApp player access
        shutil.copy2(vtt_file, SUBTITLES_DIR / f"{canonical_id}_{lang}.vtt")

        # Step 7: Lossless Final Muxing with Rule 15 apad audio protection
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
            "-af", "apad",
            "-c:s", "mov_text",
            "-metadata:s:s:0", f"language={iso639}",
            "-metadata:s:s:0", f"title={lang_name}",
            str(final_mp4)
        ]
        subprocess.run(cmd_mux, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        f_size_mb = final_mp4.stat().st_size / (1024 * 1024)
        print(f"   ✨ FINAL BROADCAST PRODUCTION VIDEO: {final_mp4.name} ({f_size_mb:.2f} MB)")

        # Sync to FINAL_VIDEOS_DIR
        shutil.copy2(final_mp4, FINAL_VIDEOS_DIR / final_mp4.name)

        if lang == "en-IN":
            extract_storyboard_proofs(final_mp4, canonical_id)

if __name__ == "__main__":
    cid = sys.argv[1] if len(sys.argv) > 1 else "P11-C03-T01-V01"
    target_langs = sys.argv[2].split(",") if len(sys.argv) > 2 else ["en-IN", "hi-IN", "ta-IN"]
    render_concept_multilingual_unit3(cid, target_langs)
