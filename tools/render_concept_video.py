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
import re
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
    "P11-C01-T01-V01": {
        "en": (
            "Welcome to Physics and Measurement. In this masterclass, we establish the foundations of physical science: the International System of Units. "
            "The SI framework defines exactly seven fundamental base quantities: Length in metres, Mass in kilograms, Time in seconds, Electric Current in amperes, "
            "Thermodynamic Temperature in kelvins, Amount of Substance in moles, and Luminous Intensity in candelas. In addition, there are two supplementary units: "
            "the radian for plane angles, and the steradian for solid angles. Now, heed the crucial NEET Trap: students frequently assume that all quantities possessing "
            "units must possess physical dimensions. This is a fatal misconception! Both radian and steradian have well-defined units, yet both are strictly dimensionless "
            "with M-zero L-zero T-zero. Master this fundamental principle to secure your foundation for NEET Physics."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் சர்வதேச அலகு முறையான எஸ் ஐ அலகுகளை ஆராய்கிறோம். "
            "எஸ் ஐ முறையில் ஏழு அடிப்படை அளவுகள் உள்ளன: நீளம் மீட்டரிலும், நிறை கிலோகிராமிலும், காலம் வினாடியிலும், மின்னோட்டம் ஆம்பியரிலும், "
            "வெப்பநிலை கெல்வின் அளவிலும், பொருளின் அளவு மோலிலும், ஒளிச்செறிவு கேண்டிலாவிலும் அளவிடப்படுகின்றன. இவற்றுடன் தளக் கோணத்திற்கு ரேடியன் மற்றும் "
            "திண்மக் கோணத்திற்கு ஸ்டெரேடியன் ஆகிய இரு துணை அலகுகள் உள்ளன. நீட் தேர்வு பொறி எச்சரிக்கை: அலகுகள் உள்ள அனைத்து அளவுகளுக்கும் பரிமாணங்கள் "
            "இருக்கும் என்று மாணவர்கள் தவறாக நினைக்கிறார்கள். ரேடியன் மற்றும் ஸ்டெரேடியன் ஆகிய இரண்டும் அலகுகள் கொண்டவை, ஆனால் பரிமாணமற்றவை ஆகும்!"
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम अंतर्राष्ट्रीय मात्रक प्रणाली यानी एस आई मात्रकों का अध्ययन करेंगे। "
            "एस आई प्रणाली में ठीक सात मूल राशियाँ हैं: लंबाई मीटर में, द्रव्यमान किलोग्राम में, समय सेकंड में, विद्युत धारा एम्पीयर में, "
            "ताप केल्विन में, पदार्थ की मात्रा मोल में, और ज्योति तीव्रता कैंडेला में। इसके अतिरिक्त दो पूरक मात्रक हैं: समतल कोण के लिए रेडियन "
            "और ठोस कोण के लिए स्टेरेडियन। अब ध्यान दें महत्वपूर्ण नीट ट्रैप पॉइंट पर: छात्र अक्सर यह मान लेते हैं कि जिस राशि का मात्रक है, उसकी विमाएँ भी होंगी। "
            "यह गलत है! रेडियन और स्टेरेडियन के मात्रक तो हैं, परंतु ये दोनों पूर्णतः विमाहीन राशियाँ हैं।"
        )
    },
    "P11-C01-T01-V02": {
        "en": (
            "Welcome to Physics and Measurement. In this session, we investigate Derived Units and Metric Prefixes. All physical quantities other than the seven "
            "base units are derived quantities, expressed through algebraic combinations. For example, Force is measured in Newtons, where one Newton equals one "
            "kilogram metre per second squared; while Energy is measured in Joules, where one Joule equals one kilogram metre squared per second squared. "
            "Metric prefixes express powers of ten, from femto at ten to the minus fifteen to tera at ten to the twelve. Now pay close attention to the high-yield "
            "NEET Trap: SI conventions strictly forbid double prefixes! Writing micromicro-farad is incorrect; you must write picofarad. Furthermore, because kilogram "
            "already contains the prefix kilo, all mass prefixes attach to the gram. One milligram is ten to the minus six kilograms, never one microkilogram. "
            "Remember these SI conventions to avoid negative marks in NEET."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் வழி அலகுகள் மற்றும் முன்னொட்டுகளை ஆராய்கிறோம். "
            "ஏழு அடிப்படை அலகுகளைத் தவிர மற்ற அனைத்து அலகுகளும் வழி அலகுகள் ஆகும். உதாரணமாக, விசையின் அலகு நியூட்டன், ஒரு நியூட்டன் என்பது ஒரு கிலோகிராம் "
            "மீட்டர் பர் வினாடி ஸ்கொயர் ஆகும். ஆற்றலின் அலகு ஜூல், இது ஒரு கிலோகிராம் மீட்டர் ஸ்கொயர் பர் வினாடி ஸ்கொயர் ஆகும். நீட் தேர்வு பொறி எச்சரிக்கை: "
            "எஸ் ஐ விதிகளின்படி இரட்டை முன்னொட்டுகளைப் பயன்படுத்தக் கூடாது! மைக்ரோ-மைக்ரோ-ஃபாரட் என்று எழுதக் கூடாது, பிகோ-ஃபாரட் என்றே எழுத வேண்டும். "
            "மேலும், நிறையின் முன்னொட்டுகள் கிராமிற்கு மட்டுமே சேர்க்கப்பட வேண்டும்!"
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम व्युत्पन्न मात्रक और मानक उपसर्गों का अध्ययन करेंगे। सात मूल मात्रकों के अतिरिक्त सभी भौतिक "
            "राशियाँ व्युत्पन्न राशियाँ हैं। उदाहरण के लिए, बल का मात्रक न्यूटन है, जहाँ एक न्यूटन बराबर एक किलोग्राम मीटर प्रति सेकंड वर्ग होता है। "
            "ऊर्जा का मात्रक जूल है, जो एक किलोग्राम मीटर वर्ग प्रति सेकंड वर्ग के बराबर है। अब नीट परीक्षा का मुख्य ट्रैप पॉइंट: एस आई नियमों में दोहरे "
            "उपसर्गों का उपयोग पूर्णतः वर्जित है! कभी भी माइक्रो-माइक्रो-फैराड न लिखें, बल्कि पिकोफैराड लिखें। साथ ही, द्रव्यमान के उपसर्ग हमेशा ग्राम के साथ जोड़े जाते हैं।"
        )
    },
    "P11-C01-T02-V03": {
        "en": (
            "Welcome to Physics and Measurement. In this masterclass, we master Dimensional Analysis. The dimensions of any physical quantity are the powers to which "
            "base quantities are raised. In NEET, questions frequently test pairs of quantities having identical dimensional formulas. For instance, Work, Kinetic Energy, "
            "and Torque all share the dimension M L-squared T-minus-two. Impulse and Linear Momentum share M L T-minus-one. Planck's constant and Angular Momentum share "
            "M L-squared T-minus-one. And Stress, Pressure, and Energy Density all share M L-minus-one T-minus-two. Now heed the crucial NEET Trap: identical dimensions "
            "do NOT mean identical physical quantities! Torque is a rotational vector cross-product, whereas Work is a scalar dot-product. Never assume two quantities "
            "are identical simply because their dimensional formulas match. Master these equivalences to solve dimensional questions in under thirty seconds."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் பரிமாண பகுப்பாய்வைக் கற்கிறோம். ஒரு இயற்பியல் அளவின் பரிமாணங்கள் "
            "என்பது அடிப்படை அளவுகளின் அடுக்குகளாகும். நீட் தேர்வில் ஒரே பரிமாணத்தைக் கொண்ட ஜோடிகள் அடிக்கடி கேட்கப்படுகின்றன. வேலை, இயக்க ஆற்றல் மற்றும் "
            "திருப்புவிசை ஆகியவை M L squared T minus 2 என்ற ஒரே பரிமாணத்தைக் கொண்டுள்ளன. கணத்தாக்கு மற்றும் நேர்க்கோட்டு உந்தம் ஆகியவை M L T minus 1 கொண்டுள்ளன. "
            "பிளாங்க் மாறிலி மற்றும் கோண உந்தம் ஆகியவை M L squared T minus 1 கொண்டுள்ளன. நீட் தேர்வு பொறி எச்சரிக்கை: ஒரே பரிமாணம் இருப்பதால் இரு அளவுகளும் ஒன்றல்ல! "
            "திருப்புவிசை ஒரு வெக்டார், ஆனால் வேலை ஒரு ஸ்கேலார் ஆகும். இந்த வேறுபாட்டை நினைவில் வையுங்கள்."
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम विमीय विश्लेषण और समान विमाओं वाली राशियों का अध्ययन करेंगे। किसी भौतिक राशि की विमाएँ वे घातें हैं "
            "जो मूल मात्रकों पर चढ़ाई जाती हैं। नीट परीक्षा में समान विमाओं वाले युग्म बहुत पूछे जाते हैं। कार्य, गतिज ऊर्जा और बल आघूर्ण तीनों की विमा M L square T minus 2 "
            "होती है। आवेग और संवेग की विमा M L T minus 1 होती है। प्लांक नियतांक और कोणीय संवेग की विमा M L square T minus 1 होती है। अब नीट परीक्षा का मुख्य ट्रैप: "
            "समान विमा होने का अर्थ यह नहीं कि राशियाँ भी समान हैं! बल आघूर्ण एक सदिश राशि है, जबकि कार्य एक अदिश राशि है।"
        )
    },
    "P11-C01-T02-V04": {
        "en": (
            "Welcome to Physics and Measurement. In this session, we investigate the Principle of Homogeneity. This fundamental physical law states that an equation is "
            "dimensionally correct if and only if every term added, subtracted, or equated on both sides has identical dimensions. In addition, arguments of trigonometric, "
            "exponential, and logarithmic functions must be strictly dimensionless. A classic NEET favorite is the van der Waals gas equation: P plus a over V-squared, "
            "multiplied by V minus b, equals R T. By homogeneity, a over V-squared must have the same dimension as Pressure, which proves that the constant a has "
            "dimensions M L-to-the-fifth T-minus-two; while constant b has the dimension of volume, L-cubed. Now pay attention to the NEET Trap: dimensional consistency "
            "is a necessary condition, but never a sufficient condition for physical correctness! Dimensionless numerical constants like one-half or two-pi cannot be "
            "verified by dimensions. Keep this limitation clear to excel in NEET."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் பரிமாண ஒருபடித்தான நெறிமுறையை ஆராய்கிறோம். ஒரு சமன்பாட்டில் கூட்டப்படும், "
            "கழிக்கப்படும் அல்லது சமப்படுத்தப்படும் ஒவ்வொரு உறுப்பும் ஒரே பரிமாணத்தைக் கொண்டிருக்க வேண்டும் என்பதே இந்த விதியாகும். மேலும், திரிகோணமிதி, அடுக்கு மற்றும் "
            "மடக்கை சார்புகளின் உள்ளடக்கங்கள் பரிமாணமற்றதாக இருக்க வேண்டும். வான் டெர் வால்ஸ் சமன்பாட்டில், P plus a over V squared என்பதில், a over V squared-ன் பரிமாணம் "
            "அழுத்தத்தின் பரிமாணத்திற்கு சமம். இதனால் மாறிலி a-ன் பரிமாணம் M L to the power 5 T minus 2 ஆகிறது, மற்றும் b-ன் பரிமாணம் L cubed ஆகும். நீட் தேர்வு பொறி "
            "எச்சரிக்கை: பரிமாண சமநிலை ஒரு சமன்பாடு சரியானது என்பதற்கு முழு உத்தரவாதம் அல்ல, ஏனெனில் எண்களின் மதிப்பை பரிமாணங்களால் சரிபார்க்க முடியாது!"
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम विमाओं की समांगता का सिद्धांत समझेंगे। यह नियम कहता है कि किसी भी समीकरण के दोनों पक्षों में जोड़े या "
            "घटाए जाने वाले प्रत्येक पद की विमाएँ समान होनी चाहिए। साथ ही, त्रिकोणमितीय, चरघातांकी और लघुगणकीय फलनों के कोणांक विमाहीन होने चाहिए। वांडर वाल्स गैस समीकरण में "
            "P plus a over V square में a over V square की विमा दाब के बराबर होती है, जिससे स्थिरांक a की विमा M L to the power 5 T minus 2 और b की विमा L cube प्राप्त होती है। "
            "नीट परीक्षा का मुख्य ट्रैप: विमीय सत्यता भौतिक सत्यता की पूर्ण गारंटी नहीं है, क्योंकि संख्यात्मक स्थिरांकों जैसे 1/2 या 2 pi की जाँच विमाओं द्वारा नहीं की जा सकती।"
        )
    },
    "P11-C01-T03-V05": {
        "en": (
            "Welcome to Physics and Measurement. In this masterclass, we explore Error Analysis. Experimental errors fall into two primary categories: Systematic errors, "
            "which are unidirectional and eliminated by proper instrument calibration; and Random errors, which fluctuate unpredictably and are minimized by taking "
            "the arithmetic mean of repeated measurements. The absolute error of any observation is the magnitude of difference between the mean value and that "
            "measurement. Summing these magnitudes gives the Mean Absolute Error. Now heed the critical NEET Trap: absolute errors are strictly non-negative! When "
            "calculating the mean absolute error, you MUST take the sum of absolute magnitudes. If you take the signed deviations without absolute value signs, the sum "
            "is mathematically zero by definition of the arithmetic mean! Always remember that percentage error equals mean absolute error divided by mean value, multiplied by one hundred percent."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் பிழைப் பகுப்பாய்வைக் கற்கிறோம். பிழைகள் இரு வகைப்படும்: ஒழுங்கான பிழைகள், "
            "இவை ஒரு திசையில் மட்டுமே நிகழும் மற்றும் கருவிகளை சரிசெய்வதன் மூலம் நீக்கப்படும். ஒழுங்கற்ற பிழைகள், இவை தன்னிச்சையாக நிகழும் மற்றும் பல அளவீடுகளின் கூட்டுச் "
            "சராசரி எடுப்பதன் மூலம் குறைக்கப்படும். சராசரி தனிப் பிழை என்பது அனைத்து தனிப் பிழைகளின் எண் மதிப்புகளின் சராசரி ஆகும். நீட் தேர்வு பொறி எச்சரிக்கை: "
            "தனிப் பிழைகள் எப்போதும் நேர்மறை எண்களாகும்! சராசரி தனிப் பிழை காணும்போது, எண் மதிப்புகளை மட்டுமே கூட்ட வேண்டும். குறியீடுகளுடன் கூட்டினால் கூட்டுத்தொகை பூஜ்ஜியமாகிவிடும்!"
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम त्रुटि विश्लेषण का अध्ययन करेंगे। प्रायोगिक त्रुटियाँ मुख्यतः दो प्रकार की होती हैं: क्रमबद्ध त्रुटियाँ, "
            "जो एक ही दिशा में होती हैं और उपकरण के अंशांकन से दूर की जा सकती हैं; और यादृच्छिक त्रुटियाँ, जो अनिश्चित होती हैं और कई पाठ्यांकों का समांतर माध्य लेकर "
            "न्यूनतम की जाती हैं। माध्य निरपेक्ष त्रुटि सभी निरपेक्ष त्रुटियों के परिमाणों का औसत होती है। अब नीट परीक्षा का मुख्य ट्रैप: निरपेक्ष त्रुटि हमेशा धनात्मक होती है! "
            "यदि आप बिना परिमाण लिए विचलनों को जोड़ेंगे तो समांतर माध्य की परिभाषा से योग शून्य हो जाएगा! अतः हमेशा निरपेक्ष मानों का ही योग करें।"
        )
    },
    "P11-C01-T03-V06": {
        "en": (
            "Welcome to Physics and Measurement. In this high-yield session, we master Error Propagation. When combining physical quantities, errors accumulate. In sum "
            "or difference, maximum absolute errors simply add: delta Z equals delta A plus delta B. In products, quotients, and power relations of the form Z equals "
            "A to the power p, times B to the power q, divided by C to the power r, the maximum fractional error is p times delta A over A, plus q times delta B over B, "
            "plus r times delta C over C. Now heed the single most tested NEET Trap in this unit: students frequently subtract the error of the denominator quantity C! "
            "In worst-case uncertainty analysis, errors NEVER cancel out; they ALWAYS reinforce each other. The power coefficient of C is strictly plus r, never minus r! "
            "Multiply by one hundred to obtain maximum percentage error. Master this power rule to guarantee four marks in your NEET exam."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். நீட் தேர்வில் அதிக மதிப்பெண் பெற்றுத்தரும் பிழைகளின் கூட்டல் மற்றும் பெருக்கல் விதியை நாம் இங்கு கற்கிறோம். "
            "இரு அளவுகளைக் கூட்டும் போதோ கழிக்கும் போதோ, அதிகபட்ச தனிப் பிழைகள் எப்போதும் கூட்டப்படும். Z equals A power p times B power q divided by C power r என்ற வடிவில் "
            "இருக்கும் போது, அதிகபட்ச பின்னப் பிழை p delta A by A plus q delta B by B plus r delta C by C ஆகும். நீட் தேர்வு பொறி எச்சரிக்கை: வகுத்தலில் உள்ள C அளவின் "
            "பிழையைக் கழிக்க வேண்டும் என்று மாணவர்கள் அடிக்கடி தவறு செய்கிறார்கள்! பிழைகள் எப்போதும் கூடும், ஒருபோதும் கழியாது. எனவே C-யின் அடுக்கு பிளஸ் r ஆகவே கூட்டப்பட வேண்டும்."
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम त्रुटियों के संयोजन और घात नियम का अध्ययन करेंगे। जब भौतिक राशियों का संयोजन होता है, तो त्रुटियाँ हमेशा जुड़ती हैं। "
            "योग या अंतर में अधिकतम निरपेक्ष त्रुटि सीधे जुड़ती है: डेल्टा Z बराबर डेल्टा A प्लस डेल्टा B। जब संबंध Z बराबर A की घात p, गुणा B की घात q, भागे C की घात r के "
            "रूप में हो, तो अधिकतम आपेक्षित त्रुटि p delta A by A plus q delta B by B plus r delta C by C होती है। अब नीट परीक्षा का सबसे बड़ा ट्रैप: छात्र अक्सर हर में "
            "स्थित C की त्रुटि को घटा देते हैं! अधिकतम अनिश्चितता में त्रुटियाँ कभी नहीं कटतीं, वे हमेशा जुड़ती हैं। अतः C का गुणांक हमेशा धनात्मक r होगा।"
        )
    },
    "P11-C01-T04-V07": {
        "en": (
            "Welcome to Physics and Measurement. In this session, we investigate precision measuring instruments: the Vernier Callipers and Screw Gauge. For a vernier "
            "calliper, least count equals one main scale division minus one vernier scale division, which simplifies to one main scale division divided by n. For a "
            "screw gauge, least count equals pitch divided by total circular scale divisions. Total reading equals main scale reading plus coinciding division times "
            "least count, minus the zero error. Now pay very close attention to the legendary NEET Zero Error Sign Trap: True reading always equals Observed reading "
            "minus the Zero Error! When zero error is positive, the instrument over-reads, so the positive value MUST BE SUBTRACTED. When zero error is negative, "
            "the instrument under-reads, so subtracting a negative value ADDS it to the reading! Master this sign rule to solve experimental physics questions flawlessly."
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் வெர்னியர் அளவி மற்றும் திருகு அளவி ஆகிய நுட்ப அளவீட்டுக் கருவிகளை ஆராய்கிறோம். "
            "வெர்னியர் அளவியின் மீச்சிற்றளவு என்பது ஒரு முதன்மை கோல் பிரிவு மைனஸ் ஒரு வெர்னியர் பிரிவு ஆகும். திருகு அளவியின் மீச்சிற்றளவு என்பது புரிகோல் அளவு divided by "
            "தலைக்கோல் பிரிவுகளின் எண்ணிக்கை ஆகும். மொத்த அளவு என்பது முதன்மை கோல் அளவு பிளஸ் பொருந்தும் பிரிவு பெருக்கல் மீச்சிற்றளவு மைனஸ் சுழிப்பிழை ஆகும். "
            "நீட் தேர்வு பொறி எச்சரிக்கை: உண்மையான அளவு என்பது கண்டறிந்த அளவு மைனஸ் சுழிப்பிழை! நேர் சுழிப்பிழையைக் கழிக்க வேண்டும், எதிர் சுழிப்பிழையைக் கூட்ட வேண்டும்!"
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। इस सत्र में हम वर्नियर कैलिपर्स और स्क्रू गेज का अध्ययन करेंगे। वर्नियर कैलिपर्स का अल्पतमांक मुख्य पैमाने के एक भाग और "
            "वर्नियर पैमाने के एक भाग के अंतर के बराबर होता है। स्क्रू गेज का अल्पतमांक चूड़ी अंतराल भागे वृत्तीय पैमाने के कुल भागों की संख्या होता है। कुल पाठ्यांक "
            "बराबर मुख्य पैमाना पाठ्यांक प्लस संपाती भाग गुणा अल्पतमांक, माइनस शून्यांक त्रुटि। अब नीट परीक्षा का मुख्य ट्रैप: वास्तविक पाठ्यांक बराबर प्रेक्षित पाठ्यांक "
            "माइनस शून्यांक त्रुटि! धनात्मक शून्यांक त्रुटि को हमेशा घटाया जाता है, और ऋणात्मक शून्यांक त्रुटि को हमेशा जोड़ा जाता है!"
        )
    },
    "P11-C01-T04-V08": {
        "en": (
            "Welcome to Physics and Measurement. In this concluding masterclass of Unit One, we master Significant Figures. Significant figures reflect the precision "
            "of experimental measurement. The key counting rules are: all non-zero digits are significant; zeros between non-zeros are significant; leading zeros are "
            "NEVER significant; while trailing zeros with a decimal point ARE significant. Now heed the high-frequency NEET Trap concerning arithmetic operations: "
            "In addition and subtraction, the final result must retain only as many decimal places as the number with the LEAST DECIMAL PLACES! In contrast, in multiplication "
            "and division, the result retains only as many significant figures as the term with the LEAST SIGNIFICANT FIGURES. Students often mix up these rules! "
            "Adding one hundred point one and zero point zero zero three yields one hundred point one, retaining one decimal place regardless of significant figure counts. "
            "Master both rules to complete Unit One with zero errors!"
        ),
        "ta": (
            "இயற்பியல் மற்றும் அளவீட்டியல் பாடத்திற்கு வரவேற்கிறோம். முதல் அலகின் இந்த இறுதி அமர்வில் நாம் முக்கிய எண்ணுருக்களைக் கற்கிறோம். முக்கிய எண்ணுருக்கள் ஒரு "
            "அளவீட்டின் துல்லியத்தைக் காட்டுகின்றன. பூஜ்ஜியமற்ற அனைத்து எண்களும் முக்கிய எண்ணுருக்கள்; இடதுபுறம் வரும் பூஜ்ஜியங்கள் முக்கிய எண்ணுருக்கள் அல்ல; "
            "தசமப் புள்ளிக்குப் பின் வரும் இறுதிப் பூஜ்ஜியங்கள் முக்கிய எண்ணுருக்கள் ஆகும். நீட் தேர்வு பொறி எச்சரிக்கை: கூட்டல் மற்றும் கழித்தலில், குறைவான தசம "
            "இலக்கங்களைக் கொண்ட எண்ணின் அடிப்படையிலேயே விடை அமைய வேண்டும்! ஆனால் பெருக்கல் மற்றும் வகுத்தலில், குறைவான முக்கிய எண்ணுருக்களின் அடிப்படையில் விடை அமைய வேண்டும்."
        ),
        "hi": (
            "भौतिकी और मापन में आपका स्वागत है। प्रथम इकाई के इस अंतिम सत्र में हम सार्थक अंकों और उनके नियमों का अध्ययन करेंगे। सार्थक अंक मापन की यथार्थता को दर्शाते हैं। "
            "सभी अशून्य अंक सार्थक होते हैं; अशून्य अंकों के बीच के शून्य सार्थक होते हैं; अग्रणी शून्य कभी सार्थक नहीं होते; और दशमलव वाले अनुगामी शून्य सार्थक होते हैं। "
            "अब नीट परीक्षा का मुख्य ट्रैप: जोड़ और घटाव में अंतिम परिणाम में केवल उतने ही दशमलव स्थान होने चाहिए जितने कि न्यूनतम दशमलव स्थान वाली संख्या में हैं! "
            "जबकि गुणा और भाग में परिणाम में न्यूनतम सार्थक अंक होने चाहिए। छात्र अक्सर दोनों नियमों को मिला देते हैं! जोड़ में केवल दशमलव स्थानों पर ध्यान दें।"
        )
    },

    "P11-C02-T01-V01": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we analyze Position-Time Graphs. The slope of a position-time curve represents instantaneous velocity, governed by the differential relationship v equals dx divided by dt. "
            "A horizontal line indicates the particle is at rest with zero velocity. A constant positive slope shows uniform forward velocity, while a negative slope indicates motion in the opposite direction. "
            "Now heed the crucial NEET Trap: students frequently confuse the slope of an x-t graph, which gives velocity, with the slope of a v-t graph, which gives acceleration. "
            "Remember that curvature on an x-t graph indicates acceleration, while the tangent slope gives velocity. Master this distinction to secure your NEET physics score!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் நிலை-நேர வரைபடங்களை ஆராய்கிறோம். ஒரு நிலை-நேர வரைபடத்தின் சாய்வு, துகளின் கணநேர திசைவேகத்தைக் குறிக்கிறது. "
            "இதன் முதன்மை சமன்பாடு v equals dx divided by dt ஆகும். வரைபடம் கிடைமட்டமாக இருந்தால், திசைவேகம் பூஜ்ஜியம், அதாவது பொருள் ஓய்வு நிலையில் உள்ளது. "
            "நேர்க்குறி சாய்வு நேர் திசை இயக்கத்தையும், எதிர்க்குறி சாய்வு எதிர் திசை இயக்கத்தையும் குறிக்கிறது. இப்போது முக்கியமான நீட் தேர்வு பொறி எச்சரிக்கை: "
            "மாணவர்கள் நிலை-நேர வரைபடத்தின் சாய்வான திசைவேகத்தை, திசைவேக-நேர வரைபடத்தின் சாய்வான முடுக்கத்துடன் அடிக்கடி குழப்பிக் கொள்கிறார்கள். "
            "x-t வரைபடத்தின் சாய்வு எப்போதும் திசைவேகம் மட்டுமே என்பதை நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम स्थिति-समय यानी x-t ग्राफ का विश्लेषण करेंगे। स्थिति-समय वक्र की ढाल यानी स्लोप तात्क्षणिक वेग को दर्शाती है, "
            "जिसका सूत्र है v equals dx divided by dt। यदि ग्राफ क्षैतिज रेखा है, तो वेग शून्य है और वस्तु विरामावस्था में है। "
            "धनात्मक ढाल आगे की गति और ऋणात्मक ढाल विपरीत दिशा में गति दर्शाती है। अब ध्यान दें महत्वपूर्ण नीट ट्रैप पॉइंट पर: "
            "छात्र अक्सर x-t ग्राफ की ढाल को v-t ग्राफ की ढाल यानी त्वरण समझकर भ्रमित हो जाते हैं। "
            "याद रखें, स्थिति-समय ग्राफ की ढाल हमेशा केवल वेग देती है, त्वरण नहीं!"
        )
    },
    "P11-C02-T03-V08": {
        "en": (
            "Welcome to Kinematics. In this session, we investigate Velocity-Time Graphs and Displacement. The fundamental physical principle states that the geometric area bounded between a velocity-time curve and the time axis represents net displacement, given by s equals integral v dt. "
            "While the slope of a v-t graph yields acceleration, its area integral yields displacement. Now pay close attention to the high-frequency NEET Trap: area above the time axis represents positive displacement, whereas area below the axis represents negative displacement. "
            "If an exam question asks for total distance, add the absolute magnitudes of both areas. But for net displacement, subtract the area below the axis! Master this sign convention to solve NEET kinematics problems instantly."
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் திசைவேக-நேர வரைபடங்கள் மற்றும் இடப்பெயர்ச்சியை ஆராய்கிறோம். "
            "ஒரு திசைவேக-நேர வரைபடத்திற்கும் கால அச்சுக்கும் இடைப்பட்ட பரப்பளவு, துகள் கடந்த மொத்த இடப்பெயர்ச்சியைக் குறிக்கிறது. இதன் சமன்பாடு s equals integral v dt ஆகும். "
            "வரைபடத்தின் சாய்வு முடுக்கத்தைத் தரும் அதே வேளையில், அதன் பரப்பளவு இடப்பெயர்ச்சியைத் தருகிறது. நீட் தேர்வு பொறி எச்சரிக்கை: "
            "கால அச்சுக்கு மேலே உள்ள பரப்பு நேர் இடப்பெயர்ச்சி, கீழே உள்ள பரப்பு எதிர் இடப்பெயர்ச்சி. மொத்த தூரம் கேட்டால் இரண்டையும் கூட்ட வேண்டும், "
            "ஆனால் நிகர இடப்பெயர்ச்சிக்கு கீழ் பரப்பைக் கழிக்க வேண்டும்! இந்த விதியை நினைவில் நிறுத்துங்கள்."
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम वेग-समय ग्राफ और विस्थापन का अध्ययन करेंगे। मूलभूत सिद्धांत यह है कि v-t ग्राफ और समय अक्ष के बीच घिरा क्षेत्रफल कण के कुल विस्थापन को दर्शाता है, जिसका सूत्र है s equals integral v dt। "
            "जहाँ v-t ग्राफ की ढाल त्वरण देती है, वहीं इसका क्षेत्रफल विस्थापन देता है। नीट परीक्षा का मुख्य ट्रैप पॉइंट: समय अक्ष के ऊपर का क्षेत्रफल धनात्मक और नीचे का क्षेत्रफल ऋणात्मक विस्थापन होता है। "
            "यदि कुल दूरी पूछी जाए तो दोनों क्षेत्रफलों को जोड़ें, लेकिन कुल विस्थापन के लिए नीचे के क्षेत्रफल को घटाना होगा! इस नियम को हमेशा याद रखें।"
        )
    },
    "P11-C02-T02-V01": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we explore the Resolution of Vectors. Any two-dimensional vector A can be decomposed into two mutually perpendicular orthogonal components along the x and y axes, expressed as vector A equals Ax i-hat plus Ay j-hat. "
            "When the angle theta is measured relative to the horizontal axis, the horizontal component is Ax equals A cosine theta, and the vertical component is Ay equals A sine theta. "
            "Now heed the high-yield NEET Trap: students frequently memorize that x is always cosine and y is always sine. This is a fatal mistake! "
            "The component adjacent to the given angle always takes the cosine, while the opposite component takes the sine. If an exam question gives the angle relative to the vertical axis, then Ay becomes A cosine alpha and Ax becomes A sine alpha! Master this golden rule to conquer vector mechanics in NEET."
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் வெக்டார்களின் கூறுகளைப் பிரித்தல் பற்றி கற்கிறோம். இரு பரிமாணத்தில் உள்ள எந்தவொரு வெக்டார் A-வையும் செங்குத்தான இரு கூறுகளாக பிரிக்க முடியும். "
            "இதன் சமன்பாடு வெக்டார் A equals Ax i-cap plus Ay j-cap ஆகும். கோணம் theta கிடைமட்ட அச்சுடன் அமைந்தால், கிடைமட்ட கூறு Ax equals A cosine theta மற்றும் செங்குத்து கூறு Ay equals A sine theta ஆகும். "
            "இப்போது மிக முக்கிய நீட் தேர்வு பொறி எச்சரிக்கை: x எப்போதும் cosine, y எப்போதும் sine என்று குருட்டு மனப்பாடம் செய்யாதீர்கள்! "
            "கோணம் எந்த அச்சுடன் தொடுகிறதோ, அந்த அச்சுக்கு cosine வரும், அதற்கு செங்குத்தான அச்சுக்கு sine வரும். வினாவில் கோணம் செங்குத்து அச்சுடன் கொடுக்கப்பட்டால், Ay equals A cosine alpha மற்றும் Ax equals A sine alpha என மாறும்! இந்த பொன் விதியை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम सदिशों का वियोजन यानी रेजोल्यूशन ऑफ वेक्टर्स समझेंगे। किसी भी द्विविमीय सदिश A को दो परस्पर लंबवत घटकों में वियोजित किया जा सकता है, "
            "जिसे वेक्टर A equals Ax i-cap plus Ay j-cap के रूप में लिखा जाता है। जब कोण theta क्षैतिज अक्ष के साथ हो, तो क्षैतिज घटक Ax equals A cosine theta और ऊर्ध्वाधर घटक Ay equals A sine theta होता है। "
            "अब ध्यान दें महत्वपूर्ण नीट ट्रैप पॉइंट पर: कभी यह रट्टा न मारें कि x हमेशा cosine होगा और y हमेशा sine! "
            "नियम यह है कि जिस अक्ष के साथ कोण बनता है, वह घटक हमेशा cosine लेता है, और दूसरा घटक sine लेता है। यदि कोण ऊर्ध्वाधर अक्ष के साथ दिया जाए, तो Ay equals A cosine alpha और Ax equals A sine alpha होगा! इस नियम को हमेशा याद रखें।"
        )
    },
    "P11-C02-T03-V09": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we explore Relative Velocity and River-Boat Problems. The relative velocity of an object A with respect to B is defined as the vector difference: vector v AB equals vector v A minus vector v B. For a boat crossing a river flowing with velocity v r, the net velocity observed from the riverbank is the vector sum of the boat's velocity in still water and the river's velocity. "
            "Now heed the classic NEET Trap: students frequently confuse the condition for the shortest time with the condition for the shortest path. To cross a river in the shortest time, the swimmer must always head directly perpendicular to the riverbank at 90 degrees, resulting in a downstream drift equal to v r times t min. "
            "Conversely, to cross via the shortest path with zero drift, the swimmer must head upstream at an angle where sine theta equals v r divided by v b. Master this vital distinction to ace your NEET kinematics questions!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் சார்பு திசைவேகம் மற்றும் படகு-ஆறு கணக்குகளை ஆராய்கிறோம். பொருள் B-யைப் பொருத்து பொருள் A-வின் சார்பு திசைவேகம், வெக்டார் v AB equals வெக்டார் v A minus வெக்டார் v B என வரையறுக்கப்படுகிறது. "
            "v r திசைவேகத்தில் பாயும் ஆற்றில் படகு செல்லும்போது, கரையில் இருந்து பார்க்கும் மொத்த திசைவேகம், இவ்விரு வெக்டார்களின் கூடுதலாகும். "
            "இப்போது முக்கியமான நீட் தேர்வு பொறி எச்சரிக்கை: குறைந்தபட்ச நேரத்தில் ஆற்றைக் கடப்பதற்கும், குறைந்தபட்ச தூரத்தில் கடப்பதற்கும் உள்ள வேறுபாட்டை கவனியுங்கள்! "
            "குறைந்தபட்ச நேரத்தில் கடக்க, படகோட்டி எப்போதும் நீரோட்டத்திற்கு செங்குத்தாக 90 டிகிரி கோணத்தில் செலுத்த வேண்டும்; இதனால் படகு சற்று முன்னோக்கி நகரும். "
            "மாறாக, விலகல் இன்றி குறைந்தபட்ச பாதையில் நேராக எதிர் கரையை அடைய, நீரோட்டத்திற்கு எதிரே எதிர் கோணத்தில் செலுத்த வேண்டும். இந்த முக்கிய விதியை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम आपेक्षिक वेग यानी रिलेटिव वेलोसिटी और नदी-नाव समस्याओं का अध्ययन करेंगे। वस्तु B के सापेक्ष वस्तु A का आपेक्षिक वेग दोनों के सदिश अंतर से दिया जाता है: वेक्टर v AB equals वेक्टर v A minus वेक्टर v B। "
            "जब कोई नाव v r वेग से बहती नदी को पार करती है, तो किनारे से देखने पर कुल वेग शांत जल में नाव के वेग और नदी के वेग का सदिश योग होता है। "
            "अब ध्यान दें प्रमुख नीट ट्रैप पॉइंट पर: छात्र अक्सर न्यूनतम समय और न्यूनतम पथ यानी शॉर्टेस्ट पाथ की शर्तों में भ्रमित हो जाते हैं। "
            "न्यूनतम समय में नदी पार करने के लिए तैराक को हमेशा धारा के ठीक लंबवत यानी 90 डिग्री पर तैरना चाहिए, जिससे वह धारा के साथ थोड़ा आगे बह जाता है। "
            "वहीं दूसरी ओर, न्यूनतम पथ से सीधे सामने वाले बिंदु पर पहुँचने के लिए तैराक को धारा की विपरीत दिशा में एक निश्चित कोण पर तैरना होगा। इस अंतर को पक्का याद रखें!"
        )
    },
    "P11-C02-T04-V10": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we examine Horizontal Projection from a Height h. When a particle is projected horizontally with an initial speed v-naught from a tower of height h, its initial vertical velocity is exactly zero. "
            "The time taken to reach the ground is determined purely by free fall under gravity: t equals square root of 2h divided by g. Because there is no horizontal acceleration, the horizontal range covered before impact is R equals v-naught times square root of 2h divided by g. "
            "Now pay attention to the classic NEET Trap: students frequently imagine that a ball fired at high speed stays airborne longer than one simply dropped from the same height. This is entirely incorrect! "
            "Both projectiles accelerate downward at g with zero initial vertical velocity, so both strike the ground at the exact same instant. Horizontal velocity expands the range, but does not alter the flight duration. Master this core principle for NEET physics!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் h உயரத்திலிருந்து கிடைமட்டமாக எறியப்படும் பொருளின் இயக்கத்தை ஆராய்கிறோம். h உயர கோபுரத்திலிருந்து v-naught என்ற ஆரம்ப கிடைமட்ட திசைவேகத்துடன் ஒரு பொருள் எறியப்படும்போது, அதன் ஆரம்ப செங்குத்து திசைவேகம் பூஜ்ஜியமாகும். "
            "பொருள் தரையை அடைய எடுக்கும் நேரம், முழுமையாக புவியீர்ப்பு முடுக்கத்தை மட்டுமே சார்ந்துள்ளது: t equals square root of 2h divided by g. கிடைமட்ட முடுக்கம் இல்லாததால், பொருள் அடையும் கிடைமட்ட வீச்சு R equals v-naught times square root of 2h divided by g ஆகும். "
            "இப்போது நீட் தேர்வின் மிக முக்கிய பொறி எச்சரிக்கை: கிடைமட்டமாக அதிக வேகத்தில் எறியப்படும் பந்து, சாதாரணமாக கீழே விடப்படும் பந்தை விட அதிக நேரம் காற்றில் இருக்கும் என்று பல மாணவர்கள் தவறாக எண்ணுகிறார்கள். இது முற்றிலும் தவறு! "
            "இரண்டு பந்துகளும் ஒரே நேரத்தில் தான் தரையைத் தொடும். கிடைமட்ட திசைவேகம் வீச்சை மட்டுமே அதிகரிக்குமே தவிர, பறக்கும் நேரத்தை மாற்றாது! இந்த பொன் விதியை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम ऊँचाई h से क्षैतिज प्रक्षेपण यानी हॉरिजॉन्टल प्रोजेक्शन का अध्ययन करेंगे। जब किसी वस्तु को h ऊँचाई के टॉवर से v-naught क्षैतिज वेग से फेंका जाता है, तो उसका प्रारंभिक ऊर्ध्वाधर वेग शून्य होता है। "
            "जमीन तक पहुँचने में लगा समय केवल गुरुत्वाकर्षण के अंतर्गत मुक्त पतन से निर्धारित होता है: t equals square root of 2h divided by g। चूंकि क्षैतिज दिशा में कोई त्वरण नहीं है, इसलिए क्षैतिज परास यानी रेंज का सूत्र R equals v-naught times square root of 2h divided by g होता है। "
            "अब ध्यान दें प्रमुख नीट ट्रैप पॉइंट पर: छात्र अक्सर यह सोचते हैं कि तेज गति से फेंकी गई गेंद नीचे गिराई गई गेंद की तुलना में अधिक समय तक हवा में रहेगी। यह बिल्कुल गलत धारणा है! "
            "दोनों गेंदें बिल्कुल एक ही समय पर जमीन पर गिरेंगी। क्षैतिज वेग केवल रेंज को बढ़ाता है, उड्डयन काल को नहीं! इस स्वर्णिम नियम को हमेशा याद रखें।"
        )
    },
    "P11-C02-T04-V11": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we analyze Projectile Motion on an Inclined Plane. When a projectile is launched at an angle alpha onto an incline inclined at angle beta, the standard coordinate axes must be rotated to align with the inclined surface. "
            "The effective gravity decomposes into two components: g cosine beta acting perpendicular to the incline, and g sine beta opposing the projectile's motion along the incline. "
            "The time of flight is given by T equals 2 v-naught sine of alpha minus beta, divided by g cosine beta. "
            "Now heed the critical NEET Trap: students often forget that the acceleration along the incline is not zero! Because g sine beta decelerates the particle along the surface, standard ground range formulas completely fail. "
            "Always use rotated coordinates and remember that range depends on whether you project up or down the incline! Master this method to secure full marks."
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் சாய்வுதளத்தில் எறிபொருள் இயக்கத்தை ஆராய்கிறோம். beta கோணமுடைய சாய்வுதளத்தின் மீது, கிடைமட்டத்துடன் alpha கோணத்தில் ஒரு பொருள் எறியப்படும்போது, நாம் ஆய அச்சுகளை சாய்வுதளத்திற்கு ஏற்ப சுழற்ற வேண்டும். "
            "புவியீர்ப்பு முடுக்கம் இரண்டு கூறுகளாகப் பிரிகிறது: சாய்வுதளத்திற்கு செங்குத்தாக g cosine beta, மற்றும் சாய்வுதளத்திற்கு இணையாக g sine beta செயல்படுகிறது. "
            "பறக்கும் நேரம் T equals 2 v-naught sine of alpha minus beta divided by g cosine beta ஆகும். "
            "இப்போது நீட் தேர்வின் மிக முக்கிய பொறி எச்சரிக்கை: சாய்வுதளத்தின் திசையில் முடுக்கம் பூஜ்ஜியம் அல்ல என்பதை மாணவர்கள் மறந்து விடுகிறார்கள்! g sine beta துகளின் வேகத்தைக் குறைப்பதால், சாதாரண வீச்சு சமன்பாடுகள் இங்கு பொருந்தாது. "
            "எப்போதும் சாய்வுதள அச்சுகளைப் பயன்படுத்தி கணக்கிடுங்கள்! இந்த முக்கிய விதியை நினைவில் நிறுத்துங்கள்."
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम आनत तल यानी इन्क्लाइंड प्लेन पर प्रक्षेप्य गति का विश्लेषण करेंगे। जब किसी वस्तु को beta कोण वाले आनत तल पर alpha प्रक्षेपण कोण से फेंका जाता है, तो हमें निर्देशांक अक्षों को आनत तल के अनुदिश घुमाना पड़ता है। "
            "गुरुत्वीय त्वरण दो घटकों में टूटता है: तल के लंबवत g cosine beta, और तल के अनुदिश नीचे की ओर g sine beta। "
            "उड्डयन काल का सूत्र है: T equals 2 v-naught sine of alpha minus beta divided by g cosine beta। "
            "अब ध्यान दें प्रमुख नीट ट्रैप पॉइंट पर: छात्र अक्सर यह भूल जाते हैं कि आनत तल के अनुदिश त्वरण शून्य नहीं होता! g sine beta तल पर कण की गति को मंदित करता है, इसलिए सामान्य समतल वाले सूत्र यहाँ लागू नहीं होते। "
            "हमेशा आनत तल के घटक g sine beta और g cosine beta को ध्यान में रखकर ही प्रश्न हल करें! इस नियम को हमेशा याद रखें।"
        )
    },
    "P11-C02-T04-V12": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we determine the Radius of Curvature at the Apex of a projectile's trajectory. The radius of curvature rho defines the radius of an osculating circle that matches the path curvature at any point, given by speed squared divided by normal acceleration: rho equals v squared divided by a-normal. "
            "At the apex, the vertical velocity is zero, meaning the particle moves with purely horizontal speed: v equals v-naught cosine theta. Simultaneously, gravity g acts entirely perpendicular to this instantaneous velocity, so a-normal equals g. "
            "Therefore, the radius of curvature at the apex is rho equals v-naught squared cosine squared theta divided by g. "
            "Now heed the classic NEET Trap: students frequently plug the full launch speed v-naught into the numerator instead of v-naught cosine theta! "
            "Remember, at the peak, speed drops to v-naught cosine theta. Applying this exact speed prevents the most common mistake in NEET advanced kinematics!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் எறிபொருள் உச்சியில் இருக்கும்போது அதன் வளைவு ஆரத்தை கணக்கிடுகிறோம். வளைவு ஆரம் rho என்பது பாதையின் வளைவுக்குப் பொருந்தும் வட்டத்தின் ஆரமாகும்; இதன் பொதுவான சமன்பாடு rho equals v squared divided by a-normal ஆகும். "
            "உச்சியில், செங்குத்து திசைவேகம் பூஜ்ஜியமாகி, துகளுக்கு கிடைமட்ட திசைவேகம் மட்டுமே இருக்கும்: v equals v-naught cosine theta. அதே வேளையில், புவியீர்ப்பு முடுக்கம் g இந்த திசைவேகத்திற்கு முழுமையாக செங்குத்தாக செயல்படுவதால், a-normal equals g ஆகிறது. "
            "எனவே, உச்சியில் வளைவு ஆரம் rho equals v-naught squared cosine squared theta divided by g ஆகும். "
            "இப்போது நீட் தேர்வின் முக்கிய பொறி எச்சரிக்கை: மாணவர்கள் தொடக்க திசைவேகமான v-naught-ஐ நேரடியாக சமன்பாட்டில் பிரதியிட்டு தவறான விடையைப் பெறுகிறார்கள்! "
            "உச்சியில் திசைவேகம் v-naught cosine theta மட்டுமே என்பதை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम प्रक्षेप्य पथ के उच्चतम बिंदु शीर्ष पर वक्रता त्रिज्या यानी रेडियस ऑफ कर्वेचर ज्ञात करेंगे। वक्रता त्रिज्या rho उस स्पर्श वृत की त्रिज्या होती है जो वक्र से मेल खाती है, जिसका सूत्र है rho equals v squared divided by a-normal। "
            "शीर्ष पर ऊर्ध्वाधर वेग शून्य होता है, अतः कण केवल क्षैतिज वेग v equals v-naught cosine theta से गति करता है। साथ ही, गुरुत्वाकर्षण त्वरण g इस वेग के पूर्णतः लंबवत होता है, इसलिए a-normal equals g होगा। "
            "अतः शीर्ष पर वक्रता त्रिज्या का सूत्र बनता है: rho equals v-naught squared cosine squared theta divided by g। "
            "अब नीट परीक्षा का मुख्य ट्रैप पॉइंट: छात्र अक्सर अंश में v-naught cosine theta के स्थान पर पूरा प्रारंभिक वेग v-naught रख देते हैं! "
            "याद रखें, शीर्ष पर केवल क्षैतिज वेग v-naught cosine theta ही शेष रहता है। इस नियम से आपके पूरे अंक सुरक्षित होंगे!"
        )
    },
    "P11-C02-T04-V01": {
        "en": (
            "Welcome to Kinematics. In this masterclass, we explore Centripetal Acceleration in Uniform Circular Motion. Even when a particle traverses a circular path of radius r at a perfectly constant speed v, its direction of motion changes at every single infinitesimal instant. "
            "Because velocity is a vector, this continuous directional change creates an acceleration directed radially inward toward the circle's center, called centripetal acceleration. "
            "The magnitude is governed by a-sub-c equals v squared divided by r, or equivalently, omega squared times r. "
            "Now heed the classic NEET Trap: students frequently assume that because speed is constant, the acceleration must be zero. This is a fatal misconception! "
            "Speed is constant, but velocity is definitely not constant. Furthermore, because centripetal acceleration is strictly perpendicular to the velocity vector, the centripetal force does zero work on the particle! Master this foundational distinction for NEET physics."
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். இந்த அமர்வில் நாம் சீரான வட்ட இயக்கத்தில் மையநோக்கு முடுக்கத்தை ஆராய்கிறோம். ஒரு துகள் r ஆரம் கொண்ட வட்டப்பாதையில் v என்ற மாறா வேகத்தில் சென்றாலும், அதன் திசைவேகத்தின் திசை ஒவ்வொரு கணமும் தொடர்ந்து மாறிக் கொண்டே இருக்கிறது. "
            "திசைவேகம் ஒரு வெக்டார் என்பதால், இந்த திசை மாற்றம் வட்டத்தின் மையத்தை நோக்கி ஒரு முடுக்கத்தை உருவாக்குகிறது; இதுவே மையநோக்கு முடுக்கம் எனப்படும். "
            "இதன் சமன்பாடு: a-sub-c equals v squared divided by r, அல்லது omega squared times r ஆகும். "
            "இப்போது நீட் தேர்வின் மிக முக்கிய பொறி எச்சரிக்கை: வேகம் மாறாமல் இருப்பதால் முடுக்கம் பூஜ்ஜியம் என்று பல மாணவர்கள் தவறாக எண்ணுகிறார்கள்! "
            "வேகம் மாறவில்லை என்றாலும், திசை மாறுவதால் முடுக்கம் உண்டு. மேலும், மையநோக்கு முடுக்கம் திசைவேகத்திற்கு செங்குத்தாக இருப்பதால், மையநோக்கு விசை செய்யும் வேலை எப்போதும் பூஜ்ஜியமாகும்! இந்த பொன் விதியை எப்போதும் நினைவில் நிறுத்துங்கள்."
        ),
        "hi": (
            "गतिकी में आपका स्वागत है। इस सत्र में हम एकसमान वृत्तीय गति में अभिकेंद्रीय त्वरण यानी सेंट्रिपेटल एक्सेलेरेशन का अध्ययन करेंगे। जब कोई कण r त्रिज्या के वृत्ताकार पथ पर नियत चाल v से गति करता है, तो भी प्रत्येक क्षण उसकी गति की दिशा निरंतर बदलती रहती है। "
            "चूंकि वेग एक सदिश राशि है, अतः दिशा में यह निरंतर परिवर्तन वृत्त के केंद्र की ओर एक त्वरण उत्पन्न करता है जिसे अभिकेंद्रीय त्वरण कहते हैं। "
            "इसका सूत्र है: a-sub-c equals v squared divided by r, अथवा omega squared times r। "
            "अब ध्यान दें प्रमुख नीट ट्रैप पॉइंट पर: छात्र अक्सर यह मान लेते हैं कि चाल नियत होने के कारण त्वरण शून्य होगा। यह एक गंभीर भूल है! "
            "चाल नियत है परंतु वेग की दिशा निरंतर बदल रही है। इसके अतिरिक्त, अभिकेंद्रीय त्वरण हमेशा वेग के लंबवत होता है, अतः अभिकेंद्रीय बल द्वारा किया गया कार्य हमेशा शून्य होता है! इस महत्वपूर्ण नियम को हमेशा याद रखें।"
        )
    },
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
    },
    "P11-C02-T05-V13": {
        "en": (
            "Welcome to Kinematics. In circular motion, linear speed v and angular velocity omega are directly related through the radial distance r. "
            "The governing formula is v equals omega times r. When a rigid body rotates about a fixed axis, all particles sweep equal angles in equal time intervals, "
            "so angular velocity omega is strictly identical for every point! However, particles farther from the center travel a larger circumference, "
            "meaning linear velocity v increases directly with radius r. Now here is the crucial NEET Trap: students often think points closer to the center move faster, "
            "or that angular velocity changes with radius. This is false! Angular velocity omega is constant everywhere on the body, while the outermost rim moves "
            "with the greatest linear speed. Remember v equals omega times r to score full marks in NEET!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். வட்ட இயக்கத்தில், நேரியல் வேகம் v மற்றும் கோணத் திசைவேகம் omega ஆகியவை ஆரம் r மூலமாக ஒன்றோடொன்று தொடர்புடையவை. "
            "இதன் முதன்மை சமன்பாடு: v equals omega times r. ஒரு திடப்பொருள் சுழலும் போது, அதிலுள்ள அனைத்து புள்ளிகளும் ஒரே நேரத்தில் சமமான கோண இடப்பெயர்ச்சியைக் கடப்பதால், "
            "கோணத் திசைவேகம் omega அனைவருக்கும் சமமாக இருக்கும்! ஆனால் மையத்திலிருந்து அதிக தூரத்தில் உள்ள புள்ளிகள் அதிக சுற்றளவைக் கடப்பதால், "
            "நேரியல் வேகம் v ஆரத்திற்கு நேர்விகிதத்தில் அதிகரிக்கும். நீட் தேர்வு பொறி எச்சரிக்கை: மையத்திற்கு அருகில் உள்ள புள்ளிகள் அதிக வேகத்தில் சுழலும் என ஒருபோதும் தவறாக நினைக்காதீர்கள்! "
            "omega அனைவருக்கும் பொதுவானது; விளிம்பில் இருக்கும் புள்ளியே அதிகபட்ச நேரியல் வேகம் v-ஐக் கொண்டிருக்கும். இந்த விதியை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "किनेमैटिक्स में आपका स्वागत है। वृत्तीय गति में रेखीय चाल v और कोणीय वेग omega त्रिज्या r द्वारा संबंधित होते हैं। "
            "इसका मूलभूत सूत्र है: v equals omega times r। जब कोई दृढ़ पिंड घूर्णन करता है, तो उसके सभी कण समान समय में समान कोण घूमते हैं, "
            "इसलिए कोणीय वेग omega सभी बिंदुओं के लिए बिल्कुल समान रहता है! परंतु केंद्र से अधिक दूरी वाले कण बड़ी परिधि तय करते हैं, "
            "इसलिए रेखीय चाल v त्रिज्या r के साथ बढ़ती है। अब नीट परीक्षा का मुख्य ट्रैप पॉइंट: छात्र अक्सर सोचते हैं कि केंद्र के पास वाले बिंदु तेज़ चलते हैं "
            "या omega बदलता है। यह गलत है! पूरे पिंड का omega समान रहता है, जबकि बाहरी रिम पर रेखीय चाल v सबसे अधिक होती है। इस सूत्र को हमेशा याद रखें!"
        )
    },
    "P11-C02-T05-V14": {
        "en": (
            "Welcome to Kinematics. In non-uniform circular motion, a particle experiences two simultaneous, mutually perpendicular accelerations. "
            "The first is radial centripetal acceleration, a-c equals v squared over r, which continuously changes the direction of velocity toward the center. "
            "The second is tangential acceleration, a-t equals dv over dt, which directly changes the speed along the path. "
            "Because these components are orthogonal, the net acceleration magnitude is given by the Pythagorean relation: a-net equals square root of a-c squared plus a-t squared. "
            "Now heed the high-frequency NEET Trap: when speed varies in circular motion, students frequently calculate only centripetal acceleration and forget tangential acceleration entirely! "
            "In uniform circular motion, only a-c exists; but in non-uniform circular motion, both a-c and a-t are present. Never omit the tangential component!"
        ),
        "ta": (
            "இயக்கவியல் பாடத்திற்கு வரவேற்கிறோம். சீரற்ற வட்ட இயக்கத்தில், ஒரு பொருள் ஒன்றுக்கொன்று செங்குத்தான இரண்டு முடுக்கங்களை ஒரே நேரத்தில் எதிர்கொள்கிறது. "
            "முதலாவது மையநோக்கு முடுக்கம் a-c equals v squared by r, இது திசைவேகத்தின் திசையை மட்டுமே மாற்றுகிறது. "
            "இரண்டாவது தொடுகோட்டு முடுக்கம் a-t equals dv by dt, இது பொருளின் வேகத்தை மட்டுமே மாற்றுகிறது. "
            "இந்த இரண்டு கூறுகளும் செங்குத்தாக அமைவதால், மொத்த நிகர முடுக்கத்தின் அளவு: a-net equals square root of a-c squared plus a-t squared ஆகும். "
            "நீட் தேர்வு பொறி எச்சரிக்கை: வேகம் மாறும் போது, மையநோக்கு முடுக்கத்தை மட்டும் கணக்கிட்டு விட்டு, தொடுகோட்டு முடுக்கத்தை மாணவர்கள் மறந்து விடுகிறார்கள்! "
            "சீரான வட்ட இயக்கத்திற்கு a-c மட்டுமே; சீரற்ற இயக்கத்திற்கு a-c மற்றும் a-t இரண்டும் தேவை. இந்த வேறுபாட்டை எப்போதும் நினைவில் நிறுத்துங்கள்!"
        ),
        "hi": (
            "किनेमैटिक्स में आपका स्वागत है। असमान वृत्तीय गति में कण पर एक साथ दो परस्पर लंबवत त्वरण कार्य करते हैं। "
            "पहला है अभिकेंद्रीय त्वरण a-c equals v squared over r, जो लगातार वेग की दिशा को केंद्र की ओर मोड़ता है। "
            "दूसरा है स्पर्शरेखीय त्वरण a-t equals dv by dt, जो चाल के परिमाण को बदलता है। "
            "चूँकि ये दोनों लंबवत हैं, कुल परिणामी त्वरण है: a-net equals square root of a-c squared plus a-t squared। "
            "अब नीट परीक्षा का मुख्य ट्रैप: जब चाल बदल रही हो, तब छात्र केवल अभिकेंद्रीय त्वरण निकालते हैं और स्पर्शरेखीय त्वरण को भूल जाते हैं! "
            "एकसमान गति में केवल a-c होता है, परंतु असमान गति में a-c और a-t दोनों होते हैं। इस अंतर को हमेशा याद रखें!"
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
