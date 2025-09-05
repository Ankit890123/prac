# Service data matching frontend servicesData.js
SERVICES = {
    1: {
        "emoji": "🧺",
        "name": {"en": "Steam Pressing", "hi": "स्टीम प्रेसिंग", "mr": "स्टीम प्रेसिंग"},
        "tagline": {"en": "Wrinkle-free, confidence-ready clothes.", "hi": "झुर्रियों-रहित, आत्मविश्वास से तैयार कपड़े।", "mr": "सुरकसार, आत्मविश्वासासाठी तयार कपडे।"},
        "before": {"en": "😵‍💫  Wrinkled & crumpled", "hi": "😵‍💫  सिकुड़े और झुर्रियों वाले", "mr": "😵‍💫  शिकटले आणि ताणलेले"},
        "after": {"en": "😌  Sharp & polished", "hi": "😌  ताजगी और प्रेस किया हुआ", "mr": "😌  ताजे आणि प्रेस केलेले"},
        "steps": {
            "en": ["Pickup", "Steam Press", "Quality Check", "Deliver"],
            "hi": ["पिकअप", "स्टीम प्रेस", "गुणवत्ता जांच", "डिलिवर"],
            "mr": ["पिकअप", "स्टीम प्रेस", "गुणवत्ता तपासणी", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Eco-safe steam", "No shine marks", "Same-day option", "Affordable"],
            "hi": ["ईको-सेफ स्टीम", "कोई चमक नहीं", "समान दिन विकल्प", "किफायती"],
            "mr": ["इको-सुरक्षित स्टीम", "कुणतीही चमक नाही", "त्याच दिवशी पर्याय", "परवडणारे"]
        },
        "options": [
            {"id": "press-shirt", "emoji": "👔", "price": 15, "label": {"en": "Shirt", "hi": "शर्ट", "mr": "शर्ट"}},
            {"id": "press-tshirt", "emoji": "👕", "price": 12, "label": {"en": "T-Shirt", "hi": "टी-शर्ट", "mr": "टी-शर्ट"}},
            {"id": "press-kurta", "emoji": "🧕", "price": 18, "label": {"en": "Kurta", "hi": "कुर्ता", "mr": "कुर्ता"}},
            {"id": "press-jeans", "emoji": "👖", "price": 20, "label": {"en": "Jeans", "hi": "जीन्स", "mr": "जीन्स"}},
        ],
    },
    2: {
        "emoji": "👔",
        "name": {"en": "Dry Cleaning", "hi": "ड्राई क्लीनिंग", "mr": "ड्राय क्लिनिंग"},
        "tagline": {"en": "From casual wear to couture — we clean it all.", "hi": "कैजुअल से क्यूटोर तक — हम सब साफ करते हैं।", "mr": "कॅज्युअलपासून क्युटूर पर्यंत — आम्ही सर्व साफ करतो."},
        "before": {"en": "🫤  Dull & stained", "hi": "🫤  फीके और दागदार", "mr": "🫤  म्लान आणि डागदार"},
        "after": {"en": "✨  Crisp & revival finish", "hi": "✨  ताजा और पुनर्जीवित फिनिश", "mr": "✨  ताजेतवाने आणि नूतनीकरण फिनिश"},
        "steps": {
            "en": ["Pickup", "Spotting", "Dry Clean", "Deliver"],
            "hi": ["पिकअप", "स्पॉटिंग", "ड्राई क्लीन", "डिलिवर"],
            "mr": ["पिकअप", "स्पॉटिंग", "ड्राय क्लिन", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Delicate-safe", "Color guard", "Odor removal", "Expert care"],
            "hi": ["नाजुक-सुरक्षित", "रंग की सुरक्षा", "गंध हटाएं", "विशेषज्ञ देखभाल"],
            "mr": ["नाजूक-सुरक्षित", "रंगाची सुरक्षा", "सुवास हटवणे", "तज्ञ देखभाल"]
        },
        "options": [
            {"id": "dry-saree", "emoji": "🧣", "price": 120, "label": {"en": "Saree", "hi": "साड़ी", "mr": "साडी"}},
            {"id": "dry-suit", "emoji": "🤵", "price": 150, "label": {"en": "Suit / Blazer", "hi": "सूट / ब्लेज़र", "mr": "सूट / ब्लेझर"}},
            {"id": "dry-dress", "emoji": "👗", "price": 140, "label": {"en": "Dress / Gown", "hi": "ड्रेस / गाउन", "mr": "ड्रेस / गाऊन"}},
            {"id": "dry-sherwani", "emoji": "👘", "price": 160, "label": {"en": "Sherwani", "hi": "शेरवानी", "mr": "शेरवाणी"}},
        ],
    },
    3: {
        "emoji": "🛏️",
        "name": {"en": "Bedsheet Care", "hi": "बेडशीट देखभाल", "mr": "बेडशीट काळजी"},
        "tagline": {"en": "Single, Double & King — refreshed like new.", "hi": "सिंगल, डबल और किंग — नए जैसा ताजा।", "mr": "सिंगल, डबल आणि किंग — नवीनासारखे ताजेतवाने."},
        "before": {"en": "😶‍🌫️  Dusty & dull", "hi": "😶‍🌫️  धूल भरा और फीका", "mr": "😶‍🌫️  धूळकट आणि म्लान"},
        "after": {"en": "🌸  Fresh & soft", "hi": "🌸  ताजा और मुलायम", "mr": "🌸  ताजेतवाने आणि मऊ"},
        "steps": {
            "en": ["Pickup", "Wash", "Steam Press", "Deliver"],
            "hi": ["पिकअप", "धोना", "स्टीम प्रेस", "डिलिवर"],
            "mr": ["पिकअप", "धुणे", "स्टीम प्रेस", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Skin-safe detergents", "Hygienic care", "Soft finish", "Neatly folded"],
            "hi": ["त्वचा सुरक्षित डिटर्जेंट", "सफाई देखभाल", "मुलायम फिनिश", "साफ-सुथरा मोड़ा हुआ"],
            "mr": ["त्वचे-सुरक्षित डिटर्जंट", "स्वच्छता काळजी", "मऊ फिनिश", "सुसंगतपणे फोल्ड केलेले"]
        },
        "options": [
            {"id": "bed-single", "emoji": "🛏️", "price": 80, "label": {"en": "Single Bedsheet", "hi": "सिंगल बेडशीट", "mr": "सिंगल बेडशीट"}},
            {"id": "bed-double", "emoji": "🛏️🛏️", "price": 150, "label": {"en": "Double Bedsheet", "hi": "डबल बेडशीट", "mr": "डबल बेडशीट"}},
            {"id": "bed-king", "emoji": "👑🛏️", "price": 200, "label": {"en": "King Size Bedsheet", "hi": "किंग साइज बेडशीट", "mr": "किंग साईझ बेडशीट"}},
        ],
    },
    4: {
        "emoji": "🪄",
        "name": {"en": "Carpet & Linen Care", "hi": "कारपेट और लिनेन देखभाल", "mr": "कार्पेट व लिनेन काळजी"},
        "tagline": {"en": "Rugs, Carpets & Duvets cleaned with care.", "hi": "रग्स, कारपेट्स और डुवेट्स को देखभाल से साफ किया गया।", "mr": "रग, कार्पेट व डुवेट काळजीपूर्वक साफ केले."},
        "before": {"en": "🤧  Allergens & dust", "hi": "🤧  एलर्जी और धूल", "mr": "🤧  अलर्जन आणि धूळ"},
        "after": {"en": "💨  Deep-clean & deodorized", "hi": "💨  गहरी सफाई और डिओडराइज्ड", "mr": "💨  खोल स्वच्छता व दुर्गंध मुक्त"},
        "steps": {
            "en": ["Pickup", "Dusting", "Deep Clean", "Dry & Deliver"],
            "hi": ["पिकअप", "धूल हटाना", "गहरी सफाई", "सूखा और डिलिवर"],
            "mr": ["पिकअप", "धूळ काढणे", "गंभीर साफसफाई", "सुकवून डिलिव्हर"]
        },
        "perks": {
            "en": ["Dust mite control", "Deodorized", "Color-safe", "Quick dry"],
            "hi": ["धूल कण नियंत्रण", "गंध हटाएं", "रंग सुरक्षित", "जल्दी सूखना"],
            "mr": ["धूळ कण नियंत्रण", "दुर्गंध मुक्त", "रंग सुरक्षित", "जलद सुकणे"]
        },
        "options": [
            {"id": "carpet-small", "emoji": "🧶", "price": 250, "label": {"en": "Rug / Carpet (Small)", "hi": "रग / कारपेट (छोटा)", "mr": "रग / कार्पेट (लहान)"}},
            {"id": "carpet-large", "emoji": "🧵", "price": 450, "label": {"en": "Rug / Carpet (Large)", "hi": "रग / कारपेट (बड़ा)", "mr": "रग / कार्पेट (मोठा)"}},
            {"id": "duvet", "emoji": "🛌", "price": 300, "label": {"en": "Duvet / Quilt", "hi": "डुवेट / कंबल", "mr": "डुवेट / ब्लँकेट"}},
        ],
    },
    5: {
        "emoji": "🪟",
        "name": {"en": "Curtain Cleaning", "hi": "परदे की सफाई", "mr": "परदेस साफसफाई"},
        "tagline": {"en": "Drapes, Curtains & Blinds deep cleaned.", "hi": "ड्रेप्स, पर्दे और ब्लाइंड्स को गहराई से साफ किया गया।", "mr": "ड्रेप, परदे व ब्लाइंड्स खोलून साफ केले."},
        "before": {"en": "😪  Musty & dusty", "hi": "😪  बासी और धूल भरा", "mr": "😪  जुनाट व धूळकट"},
        "after": {"en": "😊  Airy & fresh", "hi": "😊  हवादार और ताजा", "mr": "😊  हवादार व ताजेतवाने"},
        "steps": {
            "en": ["Pickup", "Vacuum & Wash", "Steam Press", "Deliver"],
            "hi": ["पिकअप", "वैक्यूम और धोना", "स्टीम प्रेस", "डिलिवर"],
            "mr": ["पिकअप", "व्हॅक्यूम व धुणे", "स्टीम प्रेस", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Shrink-safe", "Ironed pleats", "Odor-free", "Color care"],
            "hi": ["संकुचन सुरक्षित", "इस्त्री की गई सिलवटें", "गंध रहित", "रंग की देखभाल"],
            "mr": ["संकुचन सुरक्षित", "इस्त्री केलेले तुकडे", "सुवास मुक्त", "रंगाची काळजी"]
        },
        "options": [
            {"id": "curtain-light", "emoji": "🪟", "price": 120, "label": {"en": "Light Curtain (per panel)", "hi": "हल्का परदा (प्रति पैनल)", "mr": "हलका पडदा (प्रति पॅनेल)"}},
            {"id": "curtain-heavy", "emoji": "🪟🧵", "price": 180, "label": {"en": "Heavy Curtain (per panel)", "hi": "भारी परदा (प्रति पैनल)", "mr": "जड पडदा (प्रति पॅनेल)"}},
            {"id": "blinds", "emoji": "🪟🧼", "price": 200, "label": {"en": "Blinds (per unit)", "hi": "ब्लाइंड्स (प्रति यूनिट)", "mr": "ब्लाइंड्स (प्रति युनिट)"}},
        ],
    },
    6: {
        "emoji": "👟",
        "name": {"en": "Shoe Cleaning", "hi": "जूते की सफाई", "mr": "बूट्स साफसफाई"},
        "tagline": {"en": "Sneakers, Heels, Boots & Slippers renewed.", "hi": "स्नीकर्स, हील्स, बूट्स और चप्पल पुनर्नवीनीकृत।", "mr": "स्नीकर्स, हील्स, बूट्स व स्लिपर्स नूतनीकरण."},
        "before": {"en": "🥴  Scuffed & dirty", "hi": "🥴  खरोंच और गंदे", "mr": "🥴  खरचले व घाणेरडे"},
        "after": {"en": "😎  Clean & bright", "hi": "😎  साफ और चमकदार", "mr": "😎  स्वच्छ व तेजस्वी"},
        "steps": {
            "en": ["Pickup", "Spot Clean", "Deep Clean", "Deliver"],
            "hi": ["पिकअप", "स्पॉट क्लीन", "गहरी सफाई", "डिलिवर"],
            "mr": ["पिकअप", "स्पॉट क्लिन", "गंभीर साफसफाई", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Sole whitening", "Color care", "Deodorized", "Moisture-safe"],
            "hi": ["सोल को व्हाइट करना", "रंग की देखभाल", "गंध रहित", "नमी सुरक्षित"],
            "mr": ["सोल पांढरे करणे", "रंगाची काळजी", "दुर्गंध मुक्त", "आर्द्रता सुरक्षित"]
        },
        "options": [
            {"id": "shoe-sneaker", "emoji": "👟", "price": 180, "label": {"en": "Sneakers", "hi": "स्नीकर्स", "mr": "स्नीकर्स"}},
            {"id": "shoe-heel", "emoji": "👠", "price": 160, "label": {"en": "Heels", "hi": "हील्स", "mr": "हील्स"}},
            {"id": "shoe-boot", "emoji": "🥾", "price": 220, "label": {"en": "Boots", "hi": "बूट्स", "mr": "बूट्स"}},
            {"id": "shoe-slipper", "emoji": "🩴", "price": 120, "label": {"en": "Slippers", "hi": "चप्पल", "mr": "स्लिपर्स"}},
        ],
    },
    7: {
        "emoji": "👜",
        "name": {"en": "Handbag Spa", "hi": "हैंडबैग स्पा", "mr": "हँडबॅग स्पा"},
        "tagline": {"en": "Handbags, Clutches, Purses & Totes revived.", "hi": "हैंडबैग्स, क्लचेस, पर्स और टोट्स का नवीनीकरण।", "mr": "हँडबॅग, क्लच, पर्स व टोट्स नूतनीकरण."},
        "before": {"en": "😓  Stains & marks", "hi": "😓  दाग और निशान", "mr": "😓  डाग व ठसे"},
        "after": {"en": "💅  Luxe finish", "hi": "💅  शानदार फिनिश", "mr": "💅  लक्झरी फिनिश"},
        "steps": {
            "en": ["Pickup", "Cleanse", "Condition", "Deliver"],
            "hi": ["पिकअप", "साफ करना", "कंडीशनिंग", "डिलिवर"],
            "mr": ["पिकअप", "स्वच्छता", "कंडीशन", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Leather-safe", "Stain removal", "Color revive", "Finishing"],
            "hi": ["लेदर सुरक्षित", "दाग हटाना", "रंग पुनर्जीवित", "फिनिशिंग"],
            "mr": ["लेदर सुरक्षित", "डाग काढणे", "रंग पुनर्जीवित", "फिनिशिंग"]
        },
        "options": [
            {"id": "bag-clutch", "emoji": "👝", "price": 180, "label": {"en": "Clutch / Wallet", "hi": "क्लच / वॉलेट", "mr": "क्लच / वॉलेट"}},
            {"id": "bag-handbag", "emoji": "👜", "price": 260, "label": {"en": "Handbag", "hi": "हैंडबैग", "mr": "हँडबॅग"}},
            {"id": "bag-tote", "emoji": "🧳", "price": 300, "label": {"en": "Tote", "hi": "टोट", "mr": "टोट"}},
        ],
    },
    8: {
        "emoji": "👗",
        "name": {"en": "Indian & Couture", "hi": "इंडियन और क्यूटोर", "mr": "इंडियन व क्युटूर"},
        "tagline": {"en": "Lehenga, Sherwani, Gowns with expert care.", "hi": "लेहंगा, शेरवानी, गाउन विशेषज्ञ देखभाल के साथ।", "mr": "लेहेंगा, शेरवाणी, गाऊन तज्ञ काळजीसह."},
        "before": {"en": "😬  Delicate & tricky", "hi": "😬  नाजुक और जटिल", "mr": "😬  नाजूक व अवघड"},
        "after": {"en": "👑  Handled by experts", "hi": "👑  विशेषज्ञों द्वारा संभाला गया", "mr": "👑  तज्ज्ञांनी हाताळले"},
        "steps": {
            "en": ["Pickup", "Delicate Care", "Steam / Dry Clean", "Deliver"],
            "hi": ["पिकअप", "नाजुक देखभाल", "स्टीम / ड्राई क्लीन", "डिलिवर"],
            "mr": ["पिकअप", "नाजूक काळजी", "स्टीम / ड्राय क्लिन", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Beadwork-safe", "Fabric matched", "No shrinkage", "Stylist finish"],
            "hi": ["बीडकॉर्क सुरक्षित", "कपड़ा मेल खाता है", "संकोचन नहीं", "स्टाइलिस्ट फिनिश"],
            "mr": ["बीडकॉर्क सुरक्षित", "कापड जुळलेले", "संकुचन नाही", "स्टाइलिश फिनिश"]
        },
        "options": [
            {"id": "couture-lehenga", "emoji": "👗", "price": 350, "label": {"en": "Lehenga", "hi": "लेहंगा", "mr": "लेहेंगा"}},
            {"id": "couture-sherwani", "emoji": "🥻", "price": 320, "label": {"en": "Sherwani", "hi": "शेरवानी", "mr": "शेरवाणी"}},
            {"id": "couture-gown", "emoji": "👗✨", "price": 340, "label": {"en": "Gown", "hi": "गाउन", "mr": "गाऊन"}},
        ],
    },
    9: {
        "emoji": "🧥",
        "name": {"en": "Leather & Suede Care", "hi": "लेदर और स्वेड देखभाल", "mr": "लेदर व स्वेड काळजी"},
        "tagline": {"en": "Coats, Jackets & Accessories pampered.", "hi": "कोट्स, जैकेट्स और एक्सेसरीज की देखभाल।", "mr": "कोट, जॅकेट व अ‍ॅक्सेसरीजची काळजी."},
        "before": {"en": "😟  Dry & dull", "hi": "😟  सूखा और फीका", "mr": "😟  कोरडा व म्लान"},
        "after": {"en": "😌  Restored & conditioned", "hi": "😌  पुनर्स्थापित और कंडीशन किया हुआ", "mr": "😌  पुनर्संचित व कंडीशन केलेले"},
        "steps": {
            "en": ["Pickup", "Cleanse", "Condition", "Deliver"],
            "hi": ["पिकअप", "साफ करना", "कंडीशनिंग", "डिलिवर"],
            "mr": ["पिकअप", "स्वच्छता", "कंडीशन", "डिलिव्हर"]
        },
        "perks": {
            "en": ["Oil-based care", "Crack-safe", "Odor removal", "Soft feel"],
            "hi": ["तेल आधारित देखभाल", "दरार सुरक्षित", "गंध हटाएं", "मुलायम अनुभव"],
            "mr": ["तेल-आधारित काळजी", "सुरक्षित तुटलेले नाही", "सुवास हटवणे", "मऊ अनुभव"]
        },
        "options": [
            {"id": "leather-jacket", "emoji": "🧥", "price": 400, "label": {"en": "Leather Jacket", "hi": "लेदर जैकेट", "mr": "लेदर जॅकेट"}},
            {"id": "leather-coat", "emoji": "🧥🧴", "price": 450, "label": {"en": "Leather Coat", "hi": "लेदर कोट", "mr": "लेदर कोट"}},
            {"id": "suede-accessory", "emoji": "🧤", "price": 260, "label": {"en": "Suede Accessory", "hi": "स्वेड एक्सेसरी", "mr": "स्वेड अ‍ॅक्सेसरी"}},
        ],
    },
}