import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
TARGET_FILE = BASE_DIR / "tools" / "render_concept_video.py"

UNIT_1_SCRIPTS_CODE = '''    "P11-C01-T01-V01": {
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
'''

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Insert before "FLAGSHIP_SCRIPTS = {"
target = "FLAGSHIP_SCRIPTS = {"
if target in content and "P11-C01-T01-V01" not in content:
    replacement = target + "\n" + UNIT_1_SCRIPTS_CODE
    new_content = content.replace(target, replacement, 1)
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✓ Successfully injected Unit 1 scripts into render_concept_video.py")
else:
    print("Scripts already present or target not found.")
