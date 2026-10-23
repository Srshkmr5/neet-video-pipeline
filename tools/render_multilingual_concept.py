"""
Master Multilingual Synchronized Concept Video Engine
Codified from IMPLEMENTATION_RULES_v1.0.md (Pillars 11, 12, 13) and .antigravity/rules.md (Rules 8-12).

Executes the complete, verified 6-step production pipeline:
1. Script & Pedagogical Beat Breakdown (en-IN, hi-IN, ta-IN)
2. Discrete Beat Audio Synthesis & Empirical Duration Measurement
3. Dynamic Timeline Calculation & 3.0s NEET Trap Silent Consolidation Hold
4. Mobile-First High-DPI Obsidian-Neon Manim Video Rendering
5. Timed SRT/VTT Generation & Soft MP4 Subtitle Multiplexing (mov_text)
6. Stream Verification & Multi-Beat Proof Frame Extraction
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
OUTPUT_DIR = BASE_DIR / "output" / "unit_01_physics_and_measurement"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Language configurations
VOICES = {
    "en-IN": {"voice": "en-IN-NeerjaExpressiveNeural", "iso639": "eng", "name": "English"},
    "hi-IN": {"voice": "hi-IN-MadhurNeural", "iso639": "hin", "name": "Hindi"},
    "ta-IN": {"voice": "ta-IN-ValluvarNeural", "iso639": "tam", "name": "Tamil"}
}

# Curated 4-Beat Scripts Registry
CONCEPT_BEAT_SCRIPTS = {
    "P11-C01-T01-V01": {
        "en-IN": [
            ("beat_1", "Welcome to Physics and Measurement. In this masterclass, we establish the foundations of physical science: the International System of Units."),
            ("beat_2", "The SI framework defines exactly seven fundamental base quantities: Length in metres, Mass in kilograms, Time in seconds, Electric Current in amperes, Thermodynamic Temperature in kelvins, Amount of Substance in moles, and Luminous Intensity in candelas. In addition, there are two supplementary units: the radian for plane angles, and the steradian for solid angles."),
            ("beat_3", "These seven standards are mutually independent, forming the irreducible foundation of all physical science. Every derived unit in mechanics, electromagnetism, and thermodynamics is formed by combining these dimensions. Remember, plane and solid angles are pure geometric ratios: arc over radius, and area over radius squared."),
            ("beat_4", "Now, heed the crucial NEET Trap: students frequently assume that all quantities possessing units must possess physical dimensions. This is a fatal misconception! Both radian and steradian have well-defined units, yet both are strictly dimensionless with M-zero L-zero T-zero. Master this fundamental principle to secure your foundation for NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम भौतिक विज्ञान की नींव यानी अंतर्राष्ट्रीय मात्रक प्रणाली, एस आई मात्रकों का अध्ययन करेंगे।"),
            ("beat_2", "एस आई प्रणाली में ठीक सात मूल राशियाँ हैं: लंबाई मीटर में, द्रव्यमान किलोग्राम में, समय सेकंड में, विद्युत धारा एम्पीयर में, ताप केल्विन में, पदार्थ की मात्रा मोल में, और ज्योति तीव्रता कैंडेला में। इसके अतिरिक्त दो पूरक मात्रक हैं: समतल कोण के लिए रेडियन और ठोस कोण के लिए स्टेरेडियन।"),
            ("beat_3", "ये सातों मूल राशियाँ एक-दूसरे से पूर्णतः स्वतंत्र हैं। भौतिकी की अन्य सभी व्युत्पन्न राशियाँ इन्हीं सात मूल मात्रकों के संयोजन से बनती हैं। याद रखें, समतल कोण और ठोस कोण विशुद्ध ज्यामितीय अनुपात हैं, जो चाप बटे त्रिज्या और क्षेत्रफल बटे त्रिज्या वर्ग से परिभाषित होते हैं।"),
            ("beat_4", "अब ध्यान दें सबसे महत्वपूर्ण नीट ट्रैप पॉइंट पर: छात्र अक्सर यह मान लेते हैं कि जिस भौतिक राशि का मात्रक होता है, उसकी विमाएँ भी अवश्य होनी चाहिए। यह एक घातक भूल है! रेडियन और स्टेरेडियन के प्रामाणिक मात्रक तो हैं, परंतु ये दोनों पूर्णतः विमाहीन हैं, यानी एम शून्य एल शून्य टी शून्य। नीट परीक्षा में सफलता के लिए इस सुनहरे नियम को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் சர்வதேச அலகு முறையான எஸ் ஐ அலகுகளின் அடித்தளத்தை ஆராய்கிறோம்."),
            ("beat_2", "எஸ் ஐ முறையில் ஏழு அடிப்படை அளவுகள் உள்ளன: நீளம் மீட்டரிலும், நிறை கிலோகிராமிலும், காலம் வினாடியிலும், மின்னோட்டம் ஆம்பியரிலும், வெப்பநிலை கெல்வின் அளவிலும், பொருளின் அளவு மோலிலும், ஒளிச்செறிவு கேண்டிலாவிலும் அளவிடப்படுகின்றன. இவற்றுடன் தளக் கோணத்திற்கு ரேடியன் மற்றும் திண்மக் கோணத்திற்கு ஸ்டெரேடியன் ஆகிய இரு துணை அலகுகள் உள்ளன."),
            ("beat_3", "இந்த ஏழு அடிப்படை அளவுகளும் ஒன்றையொன்று சார்ந்திருக்காத தனித்துவமானவை. இயற்பியலின் அனைத்து வருவிக்கப்பட்ட அலகுகளும் இந்த ஏழின் சேர்க்கையாலேயே உருவாக்கப்படுகின்றன. தளக் கோணம் மற்றும் திண்மக் கோணம் ஆகியவை தூய வடிவியல் விகிதங்கள் என்பதை நினைவில் கொள்ளுங்கள்."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: அலகுகள் உள்ள அனைத்து அளவுகளுக்கும் கட்டாயம் பரிமாணங்கள் இருக்கும் என்று மாணவர்கள் தவறாகக் கருதுகிறார்கள். இது ஒரு பெரும் தவறு! ரேடியன் மற்றும் ஸ்டெரேடியன் ஆகிய இரண்டும் முறையான அலகுகளைக் கொண்டுள்ளன, ஆனால் அவை பரிமாணமற்றவை, அதாவது எம் ஜீரோ எல் ஜீரோ டி ஜீரோ ஆகும். நீட் இயற்பியலில் முழு மதிப்பெண் பெற இந்த விதியை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C01-T01-V02": {
        "en-IN": [
            ("beat_1", "Welcome to Physics and Measurement. In this session, we investigate Derived Units and Standard Metric Prefixes."),
            ("beat_2", "All physical quantities other than the seven base standards are derived quantities, built through an algebraic ladder. For example, velocity is metres per second, acceleration is metres per second squared, and Force is measured in Newtons, where one Newton equals one kilogram metre per second squared. Similarly, Energy in Joules is one kilogram metre squared per second squared, and Pressure in Pascals is force per unit area."),
            ("beat_3", "Standard metric prefixes express decimal multiples and submultiples from ten to the minus fifteen, femto, up to ten to the eighteen, exa. These prefixes eliminate bulky scientific notation in physical calculations."),
            ("beat_4", "Now pay close attention to the high-yield NEET Trap: SI conventions strictly forbid double prefixes! Writing micro-microfarad is an exam error; you must write picofarad. Furthermore, because kilogram already contains the prefix kilo, all mass prefixes must attach to the gram. One milligram is ten to the minus six kilograms, never one micro-kilogram. Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम व्युत्पन्न मात्रक और मानक मीट्रिक उपसर्गों का विस्तृत अध्ययन करेंगे।"),
            ("beat_2", "सात मूल मात्रकों के अतिरिक्त सभी भौतिक राशियाँ व्युत्पन्न राशियाँ हैं, जो बीजीय सीढ़ी से बनती हैं। जैसे, वेग मीटर प्रति सेकंड है, त्वरण मीटर प्रति सेकंड वर्ग है, और बल का मात्रक न्यूटन है, जहाँ एक न्यूटन बराबर एक किलोग्राम मीटर प्रति सेकंड वर्ग होता है। इसी प्रकार कार्य और ऊर्जा का मात्रक जूल है, तथा दाब का मात्रक पास्कल है।"),
            ("beat_3", "मानक एस आई उपसर्ग दस की घातों को व्यक्त करते हैं, जैसे दस की घात ऋण पंद्रह फेम्टो से लेकर दस की घात अठारह एक्सा तक। ये उपसर्ग वैज्ञानिक गणनाओं को सरल बनाते हैं।"),
            ("beat_4", "अब ध्यान दें नीट परीक्षा के सबसे बड़े ट्रैप पॉइंट पर: एस आई नियमों में दोहरे उपसर्गों का प्रयोग पूर्णतः वर्जित है! कभी भी माइक्रो-माइक्रो-फैराड न लिखें, बल्कि पिको-फैराड लिखें। साथ ही, क्योंकि किलोग्राम में पहले से किलो उपसर्ग जुड़ा है, इसलिए द्रव्यमान के सभी उपसर्ग हमेशा ग्राम के साथ जोड़े जाते हैं। दस की घात ऋण छह किलोग्राम को एक मिलीग्राम लिखें, कभी माइक्रो-किलोग्राम नहीं। नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் வழி அலகுகள் மற்றும் நிலையான மெட்ரிக் முன்னொட்டுகளை ஆராய்கிறோம்."),
            ("beat_2", "ஏழு அடிப்படை அலகுகளைத் தவிர மற்ற அனைத்து இயற்பியல் அளவுகளும் வழி அலகுகள் ஆகும். உதாரணமாக, திசைவேகம் மீட்டர் பர் வினாடி, முடுக்கம் மீட்டர் பர் வினாடி ஸ்கொயர், மற்றும் விசையின் அலகு நியூட்டன், அதாவது ஒரு கிலோகிராம் மீட்டர் பர் வினாடி ஸ்கொயர் ஆகும். ஆற்றலின் அலகு ஜூல் மற்றும் அழுத்தத்தின் அலகு பாஸ்கல் ஆகும்."),
            ("beat_3", "நிலையான எஸ் ஐ முன்னொட்டுகள் பத்தின் அடுக்குகளைக் குறிக்கின்றன, அதாவது பத்து அடுக்கு மைனஸ் பதினைந்து ஃபெம்டோ முதல் பத்து அடுக்கு பதினெட்டு எக்ஸா வரை பயன்படுகின்றன. இவை அறிவியல் கணக்கீடுகளை எளிதாக்குகின்றன."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: எஸ் ஐ விதிகளின்படி இரட்டை முன்னொட்டுகளைப் பயன்படுத்துவது முற்றிலும் தடைசெய்யப்பட்டுள்ளது! மைக்ரோ-மைக்ரோ-ஃபாரட் என்று எழுதக் கூடாது, பிகோ-ஃபாரட் என்றே எழுத வேண்டும். மேலும், கிலோகிராமில் ஏற்கனவே கிலோ உள்ளதால், நிறையின் முன்னொட்டுகள் கிராமிற்கு மட்டுமே சேர்க்கப்பட வேண்டும். பத்து அடுக்கு மைனஸ் ஆறு கிலோகிராமை மில்லிகிராம் என்றே எழுத வேண்டும், மைக்ரோ-கிலோகிராம் அல்ல. நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C01-T02-V03": {
        "en-IN": [
            ("beat_1", "Welcome to Physics and Measurement. In this masterclass, we analyze Dimensions of Physical Quantities and Common Equivalences."),
            ("beat_2", "The dimensions of any physical quantity are the powers to which base units are raised. In NEET, questions frequently test pairs sharing identical dimensions. For example, Planck's constant and Angular Momentum share M L-squared T-minus-one; Stress, Pressure, and Energy Density share M L-minus-one T-minus-two; while Work, Kinetic Energy, and Torque all share M L-squared T-minus-two."),
            ("beat_3", "Pay close attention: identical dimensions do not mean identical physical nature! Consider Work and Torque: both possess dimensions M L-squared T-minus-two. But Work is a scalar dot-product measured in Joules, whereas Torque is a rotational vector cross-product measured in Newton-metres. Never express Torque in Joules!"),
            ("beat_4", "Now heed the high-yield NEET Trap: you can never add two quantities merely because their dimensions match! Adding Work to Torque is physically invalid. Furthermore, pure ratios like refractive index and strain are dimensionless with M-zero L-zero T-zero. Master this to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम भौतिक राशियों की विमाओं और समान विमीय सूत्रों का अध्ययन करेंगे।"),
            ("beat_2", "किसी भौतिक राशि की विमाएँ वे घातें हैं जो मूल मात्रकों पर चढ़ाई जाती हैं। नीट परीक्षा में समान विमाओं वाले युग्म अक्सर पूछे जाते हैं। जैसे, प्लांक नियतांक और कोणीय संवेग दोनों की विमा M L square T minus 1 होती है; दाब, प्रतिबल और ऊर्जा घनत्व की विमा M L minus 1 T minus 2 होती है; तथा कार्य, गतिज ऊर्जा और बल आघूर्ण की विमा M L square T minus 2 होती है।"),
            ("beat_3", "विशेष ध्यान दें: समान विमा होने का अर्थ यह नहीं कि राशियाँ भी भौतिक रूप से समान हैं! कार्य और बल आघूर्ण दोनों की विमा समान है, परंतु कार्य एक अदिश राशि है जिसका मात्रक जूल है, जबकि बल आघूर्ण एक सदिश राशि है जिसका मात्रक न्यूटन-मीटर है। बल आघूर्ण को कभी जूल में न लिखें!"),
            ("beat_4", "अब ध्यान दें नीट परीक्षा के सबसे बड़े ट्रैप पर: केवल विमा समान होने पर दो राशियों को कभी जोड़ा नहीं जा सकता! कार्य और बल आघूर्ण का योग भौतिक रूप से असंभव है। साथ ही अपवर्तनांक और विकृति विमाहीन राशियाँ हैं। नीट परीक्षा में पूरे अंक सुनिश्चित करने के लिए इन नियमों को कंठस्थ कर लें।")
        ],
        "ta-IN": [
            ("beat_1", "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் இயற்பியல் அளவுகளின் பரிமாணங்கள் மற்றும் பொதுவான சமன்பாடுகளை ஆராய்கிறோம்."),
            ("beat_2", "ஒரு இயற்பியல் அளவின் பரிமாணங்கள் என்பது அடிப்படை அளவுகளின் அடுக்குகளாகும். நீட் தேர்வில் ஒரே பரிமாணம் கொண்ட ஜோடிகள் அடிக்கடி கேட்கப்படுகின்றன. உதாரணமாக, பிளாங்க் மாறிலி மற்றும் கோண உந்தம் M L squared T minus 1 பரிமாணத்தைக் கொண்டுள்ளன; அழுத்தம், தகைவு மற்றும் ஆற்றல் அடர்த்தி M L minus 1 T minus 2 கொண்டுள்ளன; மற்றும் வேலை, இயக்க ஆற்றல் மற்றும் திருப்புவிசை M L squared T minus 2 கொண்டுள்ளன."),
            ("beat_3", "முக்கிய வேறுபாட்டைக் கவனியுங்கள்: ஒரே பரிமாணம் இருப்பதால் இரு அளவுகளும் ஒன்றல்ல! வேலை மற்றும் திருப்புவிசை இரண்டிற்கும் பரிமாணம் ஒன்றே, ஆனால் வேலை என்பது ஸ்கேலார் அளவாகும் இதன் அலகு ஜூல், திருப்புவிசை என்பது வெக்டார் அளவாகும் இதன் அலகு நியூட்டன்-மீட்டர். திருப்புவிசையை ஒருபோதும் ஜூல் என்று குறிப்பிடாதீர்கள்!"),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: பரிமாணங்கள் ஒன்றாக இருப்பதற்காக இரண்டு வெவ்வேறு அளவுகளை ஒருபோதும் கூட்ட முடியாது! வேலையையும் திருப்புவிசையையும் கூட்டுவது இயற்பியல் விதிகளுக்கு எதிரானது. நீட் தேர்வில் முழு மதிப்பெண் பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C01-T02-V04": {
        "en-IN": [
            ("beat_1", "Welcome to Physics and Measurement. In this masterclass, we explore the Principle of Homogeneity of Dimensions and its high-yield applications in NEET."),
            ("beat_2", "The Principle of Homogeneity states that terms added, subtracted, or equated in any physical equation must possess identical dimensions. Consider the classic NEET example, the van der Waals gas equation: P plus a over V-squared, multiplied by V minus b, equals R T. By homogeneity, a over V-squared must match the dimension of Pressure, revealing that constant a has dimensions M L to the fifth T minus two; while constant b matches volume with dimension L cubed."),
            ("beat_3", "Furthermore, the arguments of all trigonometric, exponential, and logarithmic functions must be strictly dimensionless pure numbers. In the wave equation y equals A sine omega t minus k x, omega t and k x must be dimensionless M zero L zero T zero. This immediately yields the dimensions of angular frequency omega as T minus one, wave number k as L minus one, and amplitude A matching displacement L."),
            ("beat_4", "Now heed the critical NEET Trap: dimensional correctness is a necessary condition, but NEVER a sufficient condition for physical validity! An equation can be dimensionally consistent yet physically incorrect, such as s equals u t plus a t squared. Moreover, dimensional analysis can never determine dimensionless numerical coefficients like one-half or two pi. Remember these boundaries to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम विमाओं की समांगता का सिद्धांत और नीट परीक्षा में इसके महत्वपूर्ण अनुप्रयोगों का अध्ययन करेंगे।"),
            ("beat_2", "समांगता का सिद्धांत कहता है कि किसी भी भौतिक समीकरण में केवल समान विमाओं वाली राशियों को ही जोड़ा, घटाया या बराबर किया जा सकता है। नीट का क्लासिक उदाहरण देखें, वांडर वाल्स समीकरण: P plus a over V square, गुना V minus b, बराबर R T। समांगता के नियम से, a over V square की विमा दाब P के समान होनी चाहिए, जिससे नियतांक a की विमा M L to the power 5 T minus 2 प्राप्त होती है, और नियतांक b की विमा आयतन L cube के बराबर होती है।"),
            ("beat_3", "इसके अतिरिक्त, सभी त्रिकोणमितीय, चरघातांकी और लघुगणकीय फलनों के कोणांक विशुद्ध विमाहीन संख्याएँ होने चाहिए। तरंग समीकरण y equals A sin omega t minus k x में, omega t और k x दोनों विमाहीन M zero L zero T zero हैं। इससे कोणीय आवृत्ति omega की विमा T minus 1, तरंग संख्या k की विमा L minus 1, और आयाम A की विमा विस्थापन L के समान प्राप्त होती है।"),
            ("beat_4", "अब ध्यान दें नीट परीक्षा के सबसे बड़े ट्रैप पॉइंट पर: विमीय सत्यता किसी समीकरण के सही होने की आवश्यक शर्त तो है, परंतु पर्याप्त शर्त कभी नहीं है! कोई समीकरण विमीय रूप से सही होकर भी भौतिक रूप से असत्य हो सकता है, जैसे s equals u t plus a t square। इसके अलावा, विमीय विश्लेषण 1/2 या 2 pi जैसे संख्यात्मक नियतांकों की जाँच कभी नहीं कर सकता। नीट में पूरे अंक पाने के लिए इस नियम को कंठस्थ रखें।")
        ],
        "ta-IN": [
            ("beat_1", "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் பரிமாண ஒருபடித்தான நெறிமுறை மற்றும் நீட் தேர்வில் அதன் பயன்பாடுகளை விரிவாக ஆராய்கிறோம்."),
            ("beat_2", "பரிமாண ஒருபடித்தான நெறிமுறையின்படி, ஒரு சமன்பாட்டில் கூட்டப்படும், கழிக்கப்படும் அல்லது சமப்படுத்தப்படும் அனைத்து உறுப்புகளும் ஒரே பரிமாணத்தைக் கொண்டிருக்க வேண்டும். நீட் தேர்வின் விருப்பமான வான் டெர் வால்ஸ் சமன்பாட்டைக் கவனியுங்கள்: P plus a over V squared பெருக்கல் V minus b சமம் R T. ஒருபடித்தான விதியின்படி, a over V squared அழுத்தத்திற்கு சமமான பரிமாணத்தைக் கொண்டுள்ளது. எனவே மாறிலி a-ன் பரிமாணம் M L to the power 5 T minus 2 ஆகும், மாறிலி b-ன் பரிமாணம் கனஅளவான L cubed ஆகும்."),
            ("beat_3", "மேலும், அனைத்து திரிகோணமிதி, அடுக்கு மற்றும் மடக்கை சார்புகளின் உள்ளடக்கங்கள் முற்றிலும் பரிமாணமற்ற எண்களாக இருக்க வேண்டும். அலை சமன்பாடு y equals A sin omega t minus k x என்பதில், omega t மற்றும் k x ஆகியவை M zero L zero T zero ஆகும். இதிலிருந்து கோண அதிர்வெண் omega-வின் பரிமாணம் T minus 1 ஆகவும், அலை எண் k-ன் பரிமாணம் L minus 1 ஆகவும், வீச்சு A-ன் பரிமாணம் இடப்பெயர்ச்சி L ஆகவும் கிடைக்கின்றன."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: பரிமாண சமநிலை ஒரு சமன்பாடு சரியானது என்பதற்கு இன்றியமையாத நிபந்தனையே தவிர, முழுமையான உத்தரவாதம் அல்ல! ஒரு சமன்பாடு பரிமாண ரீதியாக சரியாக இருந்தாலும் இயற்பியல் ரீதியாக தவறாக இருக்கலாம், உதாரணமாக s equals u t plus a t squared. மேலும், அரை அல்லது இரண்டு பை போன்ற பரிமாணமற்ற எண்களை பரிமாணங்களால் அறிய முடியாது. நீட் தேர்வில் வெற்றி பெற இந்த விதிகளை நினைவில் நிறுத்துங்கள்.")
        ]
    },
    "P11-C01-T03-V05": {
        "en-IN": [
            ("beat_1", "Welcome to Physics and Measurement. In this masterclass, we explore the Classification of Experimental Errors and Mean Absolute Error."),
            ("beat_2", "Experimental errors fall into two primary categories. Systematic errors are unidirectional and reproducible, caused by zero errors or calibration flaws, eliminated by proper recalibration. In contrast, Random errors are Gaussian fluctuations caused by ambient temperature or voltage swings, minimized only by taking the arithmetic mean of repeated measurements."),
            ("beat_3", "Mathematically, the arithmetic mean a-mean represents the best estimate of the true value. The absolute error delta a-i of each reading is strictly the positive magnitude of its deviation from a-mean. Summing these magnitudes over n observations yields the Mean Absolute Error, from which we compute relative fractional error and percentage error."),
            ("beat_4", "Now heed the high-yield NEET Trap: students frequently forget to take absolute value signs! By mathematical definition of the arithmetic mean, the sum of signed deviations is identically zero. If you sum deviations without taking absolute magnitudes, you will get zero! Always sum strictly positive magnitudes delta a-i to secure full marks in NEET Physics.")
        ],
        "hi-IN": [
            ("beat_1", "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम प्रायोगिक त्रुटियों के वर्गीकरण और माध्य निरपेक्ष त्रुटि का विस्तृत अध्ययन करेंगे।"),
            ("beat_2", "प्रायोगिक त्रुटियाँ मुख्यतः दो प्रकार की होती हैं। क्रमबद्ध त्रुटियाँ एक ही दिशा में होती हैं जो उपकरण की शून्य त्रुटि या अंशांकन दोष के कारण आती हैं, और इन्हें पुन: अंशांकन द्वारा दूर किया जाता है। जबकि यादृच्छिक त्रुटियाँ तापमान या वोल्टेज के उतार-चढ़ाव से होती हैं, जिन्हें केवल कई पाठ्यांकों का समांतर माध्य लेकर न्यूनतम किया जा सकता है।"),
            ("beat_3", "गणितीय रूप से, सभी पाठ्यांकों का समांतर माध्य a-mean वास्तविक मान का सर्वोत्तम अनुमान है। प्रत्येक पाठ्यांक की निरपेक्ष त्रुटि डेल्टा a-i माध्य से विचलन का विशुद्ध धनात्मक परिमाण होती है। इन सभी परिमाणों का औसत निकालने पर माध्य निरपेक्ष त्रुटि प्राप्त होती है, जिससे आपेक्षिक त्रुटि और प्रतिशत त्रुटि ज्ञात की जाती है।"),
            ("beat_4", "अब ध्यान दें सबसे बड़े नीट ट्रैप पॉइंट पर: छात्र अक्सर विचलनों का निरपेक्ष मान लेना भूल जाते हैं! समांतर माध्य की परिभाषा से सभी विचलनों का बीजीय योग सदैव शून्य होता है। यदि आप बिना परिमाण लिए विचलनों को जोड़ेंगे तो उत्तर शून्य आएगा! अतः माध्य निरपेक्ष त्रुटि के लिए हमेशा धनात्मक परिमाणों को ही जोड़ें।")
        ],
        "ta-IN": [
            ("beat_1", "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் அளவீட்டுப் பிழைகளின் வகைப்பாடு மற்றும் சராசரி தனிப் பிழையை விரிவாகக் கற்கிறோம்."),
            ("beat_2", "சோதனைப் பிழைகள் இரு முக்கிய வகைகளாகப் பிரிக்கப்படுகின்றன. ஒழுங்கான பிழைகள் ஒரு திசையில் மட்டுமே நிகழும், இவை சுழிப் பிழை அல்லது கருவி குறைபாடுகளால் ஏற்படுகின்றன, கருவிகளை மறுசீரமைப்பதன் மூலம் இவற்றை நீக்கலாம். ஆனால் ஒழுங்கற்ற பிழைகள் தன்னிச்சையான மாறுபாடுகளால் ஏற்படுகின்றன, பல அளவீடுகளின் கூட்டுச் சராசரி எடுப்பதன் மூலம் மட்டுமே இவற்றைக் குறைக்க முடியும்."),
            ("beat_3", "கணித ரீதியாக, n அளவீடுகளின் கூட்டுச் சராசரி a-mean என்பது உண்மை மதிப்பின் சிறந்த தோராயமாகும். ஒவ்வொரு அளவீட்டின் தனிப் பிழை டெல்டா a-i என்பது சராசரியிலிருந்து அதன் விலக்கத்தின் நேர்மறை எண் மதிப்பாகும். இந்த எண் மதிப்புகளின் சராசரியே சராசரி தனிப் பிழை ஆகும், இதிலிருந்து பின்னப் பிழை மற்றும் விழுக்காட்டுப் பிழை கணக்கிடப்படுகின்றன."),
            ("beat_4", "இப்போது முக்கியமான நீட் தேர்வு பொறியைக் கவனியுங்கள்: சராசரி தனிப் பிழை காணும்போது குறியீடுகளை நீக்க மாணவர்கள் மறந்துவிடுகிறார்கள்! கூட்டுச் சராசரியின் கணித விதிப்படி, அனைத்து விலக்கங்களின் இயற்கணிதக் கூடுதல் எப்போதும் பூஜ்ஜியமாகும். மட்டு எண் மதிப்புகளை எடுக்காமல் கூட்டினால் பூஜ்ஜியமே விடையாக வரும்! எனவே எப்போதும் நேர்மறை எண் மதிப்புகளை மட்டுமே கூட்டி நீட் தேர்வில் முழு மதிப்பெண் பெறுங்கள்.")
        ]
    }
}

def load_concept_row(canonical_id: str) -> Dict[str, Any]:
    csv_path = BASE_DIR / "queue" / "curriculum" / "physics" / "unit_01_measurement.csv"
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

def render_concept_multilingual(canonical_id: str, languages: List[str] = None):
    if languages is None:
        languages = ["en-IN", "hi-IN", "ta-IN"]

    concept = load_concept_row(canonical_id)
    title = concept["concept_title"]
    template_name = concept["template_name"]

    print("=" * 80)
    print(f"🎬 MASTER MULTILINGUAL CONCEPT PIPELINE: {canonical_id}")
    print(f"   Title   : {title}")
    print(f"   Template: {template_name}")
    print(f"   Target Languages: {languages}")
    print("=" * 80)

    # Lazy import audio engine
    from audio.engine import AudioEngine
    audio_engine = AudioEngine(default_provider="edge_tts")

    for lang in languages:
        cfg = VOICES[lang]
        voice = cfg["voice"]
        iso639 = cfg["iso639"]
        lang_name = cfg["name"]

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
                audio_engine.generate_narration(
                    text=text,
                    output_path=b_file,
                    provider="edge_tts",
                    voice_id=voice,
                    language=lang,
                    use_cache=True
                )
            # Measure duration
            cmd_probe = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(b_file)]
            res_p = subprocess.run(cmd_probe, capture_output=True, text=True, check=True)
            dur = float(json.loads(res_p.stdout)["format"]["duration"])
            durations[b_name] = dur
            print(f"   {b_name}: {dur:.2f}s | \"{text[:50]}...\"")

        # Save durations
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

        # MANDATORY 3.0s NEET TRAP SILENT FREEZE
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

        # Step 3: Mux Master Audio
        b1_file = (beat_dir / "beat_1.mp3").resolve().as_posix()
        b2_file = (beat_dir / "beat_2.mp3").resolve().as_posix()
        b3_file = (beat_dir / "beat_3.mp3").resolve().as_posix()
        b4_file = (beat_dir / "beat_4.mp3").resolve().as_posix()

        master_audio = beat_dir / f"{canonical_id}_{lang}_master_synced.mp3"

        filter_str = (
            f"[0:a]adelay={int(offset_b1*1000)}|{int(offset_b1*1000)}[a1]; "
            f"[1:a]adelay={int(offset_b2*1000)}|{int(offset_b2*1000)}[a2]; "
            f"[2:a]adelay={int(offset_b3*1000)}|{int(offset_b3*1000)}[a3]; "
            f"[3:a]adelay={int(offset_b4*1000)}|{int(offset_b4*1000)}[a4]; "
            f"[a1][a2][a3][a4]amix=inputs=4:duration=longest:dropout_transition=0[aout]; "
            f"[aout]apad=whole_dur={total_video_time:.3f}[final_a]"
        )

        cmd_audio = [
            "ffmpeg", "-y",
            "-i", b1_file,
            "-i", b2_file,
            "-i", b3_file,
            "-i", b4_file,
            "-filter_complex", filter_str,
            "-map", "[final_a]",
            "-c:a", "libmp3lame",
            "-b:a", "192k",
            str(master_audio)
        ]
        subprocess.run(cmd_audio, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"   [+] Synced Master Audio: {master_audio.name}")

        # Step 4: Generate Manim Runner
        scene_base_class = f"{template_name}Scene" if not template_name.endswith("Scene") else template_name
        runner_scene_class = f"Synced_{canonical_id.replace('-', '_')}_{lang.replace('-', '_')}"

        runner_code = f'''import sys
from pathlib import Path
BASE_DIR = Path({repr(str(BASE_DIR))})
sys.path.insert(0, str(BASE_DIR))

from manim import *
import manimpango
from config import FONTS_DIR
import render.templates.unit_01_archetypes as u1
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
    "chapter_no": int({concept.get('chapter_no', 1)}),
    "topic_no": int({concept.get('topic_no', 1)}),
    "video_no": int({concept.get('video_no', 2)}),
    "seq_chapter": int({concept.get('chapter_seq', 2)}),
    "total_chapter_videos": int({concept.get('total_chapter_videos', 8)}),
    "next_video_id": "{concept.get('next_video_id', '')}",
    "next_video_title": "{concept.get('next_video_title', '')}",
    "parameters": {{}}
}}

class {runner_scene_class}(u1.{scene_base_class}):
    def __init__(self, **kwargs):
        super().__init__(node_data=NODE_DATA, **kwargs)

    def render_concept_beats(self):
        # Beat 1: Intro
        b1 = self.build_beat_1()
        self.play(FadeIn(b1, shift=UP * 0.2), run_time=0.8)
        self.wait({wait_b1:.3f})
        self.play(FadeOut(b1), run_time=0.6)

        # Beat 2: Hero Stage / Table
        b2 = self.build_beat_2()
        self.play(FadeIn(b2), run_time=0.8)
        self.wait({wait_b2:.3f})
        self.play(FadeOut(b2), run_time=0.6)

        # Beat 3: Core Axioms / Metric Prefixes
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
        if not raw_vid_found:
            for f in (beat_dir / "manim_media").rglob("*.mp4"):
                raw_vid_found = f
                break

        print(f"   [+] Raw visual rendered: {raw_vid_found.name}")

        # Step 6: Generate Subtitles
        # Segment each beat text into clean sentence cues
        beat_start_offsets = {
            "beat_1": offset_b1,
            "beat_2": offset_b2,
            "beat_3": offset_b3,
            "beat_4": offset_b4
        }
        cues = []
        for b_name, full_text in scripts:
            b_offset = beat_start_offsets[b_name]
            b_dur = durations[b_name]
            
            # Split by period or commas into natural cues
            raw_sentences = [s.strip() for s in full_text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
            if not raw_sentences:
                raw_sentences = [full_text]
            
            total_chars = sum(len(s) for s in raw_sentences)
            curr_t = b_offset
            for s in raw_sentences:
                prop = len(s) / total_chars
                s_dur = prop * b_dur
                c_start = curr_t
                c_end = curr_t + s_dur - 0.08
                cues.append((c_start, c_end, s))
                curr_t += s_dur

        srt_lines = []
        for idx, (c_start, c_end, text) in enumerate(cues, 1):
            srt_lines.append(f"{idx}")
            srt_lines.append(f"{format_timestamp_srt(c_start)} --> {format_timestamp_srt(c_end)}")
            srt_lines.append(text)
            srt_lines.append("")
        srt_content = "\n".join(srt_lines)

        vtt_lines = ["WEBVTT", ""]
        for idx, (c_start, c_end, text) in enumerate(cues, 1):
            vtt_lines.append(f"{idx}")
            vtt_lines.append(f"{format_timestamp_vtt(c_start)} --> {format_timestamp_vtt(c_end)}")
            vtt_lines.append(text)
            vtt_lines.append("")
        vtt_content = "\n".join(vtt_lines)

        srt_file = OUTPUT_DIR / f"{canonical_id}_{lang}.srt"
        vtt_file = OUTPUT_DIR / f"{canonical_id}_{lang}.vtt"
        srt_file.write_text(srt_content, encoding="utf-8")
        vtt_file.write_text(vtt_content, encoding="utf-8")
        print(f"   [+] Subtitles Generated: {srt_file.name}, {vtt_file.name}")

        # Step 7: Final Mux with Soft Subtitles
        final_out = OUTPUT_DIR / f"{canonical_id}_{lang}.mp4"
        temp_out = OUTPUT_DIR / f"{canonical_id}_{lang}_temp.mp4"

        cmd_mux = [
            "ffmpeg", "-y",
            "-i", str(raw_vid_found),
            "-i", str(master_audio),
            "-i", str(srt_file),
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-c:s", "mov_text",
            "-metadata:s:s:0", f"language={iso639}",
            "-metadata:s:s:0", f"title={lang_name}",
            str(temp_out)
        ]
        res_mux = subprocess.run(cmd_mux, capture_output=True, text=True)
        if res_mux.returncode != 0:
            print("Mux error:", res_mux.stderr[-400:])
            raise RuntimeError(f"Multiplexing failed for {canonical_id} {lang}")

        time.sleep(0.5)
        if final_out.exists():
            os.remove(final_out)
        shutil.move(str(temp_out), str(final_out))

        file_size_mb = final_out.stat().st_size / 1024 / 1024
        print(f"🎉 [SUCCESS] Master Production Video Ready: {final_out.name} ({total_video_time:.2f}s | {file_size_mb:.2f} MB)")

        # Step 8: Proof Keyframe Extraction
        proof_dir = BASE_DIR / "brain" / f"keyframes_{canonical_id}_{lang}"
        proof_dir.mkdir(parents=True, exist_ok=True)
        proofs = [
            ("beat1_intro", 4.0),
            ("beat2_hero", total_b1 + 6.0),
            ("beat3_principles", total_b1 + total_b2 + 6.0),
            ("beat4_trap", total_b1 + total_b2 + total_b3 + 6.0),
            ("beat4_trap_freeze", total_b1 + total_b2 + total_b3 + dur_b4 + 1.5),
            ("beat5_revision", total_video_time - 1.5)
        ]
        for tag, t in proofs:
            out_img = proof_dir / f"{tag}.png"
            subprocess.run([
                "ffmpeg", "-y", "-ss", f"{t:.2f}",
                "-i", str(final_out),
                "-vframes", "1", "-q:v", "2",
                str(out_img)
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"   [+] Proof frames saved to {proof_dir.name}/")

if __name__ == "__main__":
    cid = sys.argv[1] if len(sys.argv) > 1 else "P11-C01-T01-V02"
    langs = sys.argv[2:] if len(sys.argv) > 2 else ["en-IN", "hi-IN", "ta-IN"]
    render_concept_multilingual(cid, langs)
