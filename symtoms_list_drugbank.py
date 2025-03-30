# Liste complète et organisée de symptômes médicaux

def get_comprehensive_symptoms_list():
    """
    Retourne une liste très complète et organisée de symptômes médicaux

    Returns:
        list: Liste de chaînes de caractères représentant des symptômes
    """
    return [
        # Symptômes généraux
        "fever", "high temperature", "low temperature", "hypothermia", "hyperthermia", "pyrexia", "febrile", "afebrile",
        "chills", "rigors", "sweating", "night sweats", "perspiration", "diaphoresis", "hyperhidrosis",
        "fatigue", "tiredness", "exhaustion", "lethargy", "malaise", "weakness", "asthenia",
        "weight loss", "weight gain", "appetite loss", "anorexia", "increased appetite", "polyphagia",
        "thirst", "polydipsia", "dehydration", "edema", "swelling", "fluid retention",

        # Douleur et sensations
        "pain", "ache", "agony", "discomfort", "distress", "soreness", "tenderness",
        "burning", "stabbing", "throbbing", "shooting", "cramping", "pressure", "heaviness",
        "headache", "migraine", "cephalalgia", "head pain", "facial pain",
        "chest pain", "angina", "precordial pain", "chest tightness", "chest pressure",
        "abdominal pain", "stomach pain", "belly pain", "abdominal cramps", "colic", "gastralgia",
        "back pain", "backache", "lumbago", "sciatica", "neck pain", "cervicalgia",
        "joint pain", "arthralgia", "myalgia", "muscle pain", "fibromyalgia",
        "bone pain", "osteodynia", "neuralgia", "nerve pain", "neuropathic pain",
        "dysmenorrhea", "menstrual cramps", "menstrual pain", "pelvic pain",
        "dyspareunia", "painful intercourse", "rectal pain", "proctalgia", "tenesmus",
        "earache", "otalgia", "ear pain", "toothache", "odontalgia", "dental pain",
        "throat pain", "sore throat", "pharyngalgia", "odynophagia", "painful swallowing",
        "eye pain", "ocular pain", "ophthalmalgia",

        # Systèmes neurologiques et sensoriels
        "dizziness", "vertigo", "lightheadedness", "giddiness", "disequilibrium",
        "fainting", "syncope", "blackout", "collapse", "loss of consciousness",
        "seizure", "convulsion", "epilepsy", "fit", "spasm", "paroxysm", "tetany",
        "numbness", "paresthesia", "tingling", "pins and needles", "prickling", "burning sensation",
        "hypesthesia", "decreased sensation", "anesthesia", "sensory loss",
        "hyperesthesia", "increased sensitivity", "allodynia", "dysesthesia", "abnormal sensation",
        "tremor", "shaking", "trembling", "twitching", "fasciculation", "tic", "myoclonus",
        "paralysis", "paresis", "weakness", "hemiplegia", "paraplegia", "quadriplegia",
        "ataxia", "incoordination", "clumsiness", "dyspraxia", "apraxia",
        "aphasia", "dysphasia", "speech disorder", "articulation disorder", "dysarthria",
        "amnesia", "memory loss", "forgetfulness", "confusion", "disorientation", "delirium",
        "hallucination", "delusion", "illusion", "psychosis", "altered mental status",
        "photophobia", "light sensitivity", "phonophobia", "sound sensitivity", "hyperacusis",
        "tinnitus", "ringing in ears", "ear ringing", "ear buzzing", "hearing loss", "deafness",
        "hypoacusis", "hyperacusis", "vision loss", "blindness", "visual impairment", "amaurosis",
        "blurred vision", "diplopia", "double vision", "scotoma", "visual field defect",
        "nystagmus", "abnormal eye movement", "strabismus", "squinting", "eye deviation",
        "anosmia", "smell loss", "hyposmia", "decreased smell", "dysosmia", "parosmia",
        "ageusia", "taste loss", "dysgeusia", "taste distortion", "parageusia",

        # Système respiratoire
        "cough", "dry cough", "productive cough", "whooping cough", "pertussis", "barking cough", "croup",
        "hemoptysis", "coughing blood", "blood-streaked sputum", "rusty sputum",
        "sputum", "phlegm", "mucus", "secretions", "expectoration",
        "shortness of breath", "dyspnea", "breathlessness", "air hunger", "respiratory distress",
        "orthopnea", "difficulty breathing while lying flat", "paroxysmal nocturnal dyspnea",
        "tachypnea", "rapid breathing", "hyperventilation", "bradypnea", "slow breathing",
        "apnea", "breathing cessation", "sleep apnea", "Cheyne-Stokes respiration",
        "wheezing", "stridor", "rhonchi", "crackles", "rales", "bronchospasm",
        "sneezing", "rhinorrhea", "runny nose", "nasal discharge", "nasal congestion",
        "stuffy nose", "nasal obstruction", "postnasal drip", "rhinitis",
        "sore throat", "pharyngitis", "laryngitis", "hoarseness", "dysphonia", "aphonia",
        "hiccups", "singultus", "hiccoughs", "yawning", "sighing",

        # Système cardiovasculaire
        "chest pain", "angina", "precordial pain", "chest tightness", "chest pressure",
        "palpitations", "heart pounding", "rapid heartbeat", "racing heart",
        "tachycardia", "bradycardia", "arrhythmia", "irregular heartbeat", "heart block",
        "atrial fibrillation", "atrial flutter", "ventricular tachycardia",
        "heart murmur", "extra heart sound", "gallop rhythm", "friction rub",
        "hypertension", "high blood pressure", "hypotension", "low blood pressure",
        "orthostatic hypotension", "postural hypotension", "syncope", "fainting",
        "edema", "swelling", "peripheral edema", "ankle swelling", "leg swelling",
        "cyanosis", "bluish discoloration", "acrocyanosis", "pallor", "paleness",
        "flushing", "redness", "blushing", "hot flashes", "erythema",
        "claudication", "limb pain with exercise", "varicose veins", "phlebitis",

        # Système digestif
        "nausea", "vomiting", "emesis", "retching", "hematemesis", "coffee-ground emesis",
        "regurgitation", "reflux", "heartburn", "pyrosis", "indigestion", "dyspepsia",
        "bloating", "distension", "flatulence", "gas", "belching", "eructation",
        "borborygmi", "stomach gurgling", "abdominal rumbling",
        "abdominal pain", "stomach pain", "belly pain", "abdominal cramps", "colic",
        "diarrhea", "loose stools", "watery stools", "frequent bowel movements",
        "constipation", "hard stools", "infrequent bowel movements", "straining",
        "dysphagia", "difficulty swallowing", "odynophagia", "painful swallowing",
        "dyspepsia", "indigestion", "heartburn", "acid reflux", "waterbrash",
        "anorexia", "loss of appetite", "early satiety", "feeling full quickly",
        "jaundice", "icterus", "yellow skin", "yellow eyes", "yellow sclera",
        "melena", "black stool", "tarry stool", "hematochezia", "bloody stool",
        "rectal bleeding", "tenesmus", "fecal urgency", "fecal incontinence",
        "proctalgia", "rectal pain", "anal pain", "pruritus ani", "anal itching",

        # Système génito-urinaire
        "dysuria", "painful urination", "burning urination", "urinary pain",
        "frequency", "urinary frequency", "pollakiuria", "polyuria", "increased urination",
        "oliguria", "decreased urination", "anuria", "no urination", "urine retention",
        "urgency", "urinary urgency", "urge incontinence", "stress incontinence",
        "nocturia", "nighttime urination", "enuresis", "bed-wetting", "incontinence",
        "hematuria", "bloody urine", "red urine", "hemoglobinuria", "myoglobinuria",
        "pyuria", "cloudy urine", "turbid urine", "pneumaturia", "gas in urine",
        "dyspareunia", "painful intercourse", "vaginismus", "vaginal dryness",
        "menorrhagia", "heavy periods", "hypermenorrhea", "metrorrhagia", "irregular periods",
        "amenorrhea", "absent periods", "oligomenorrhea", "infrequent periods",
        "dysmenorrhea", "painful periods", "menstrual cramps", "menstrual pain",
        "menarche", "first period", "menopause", "climacteric", "hot flashes",
        "impotence", "erectile dysfunction", "priapism", "persistent erection",
        "premature ejaculation", "delayed ejaculation", "retrograde ejaculation",

        # Système musculosquelettique
        "joint pain", "arthralgia", "arthritis", "joint swelling", "joint stiffness",
        "muscle pain", "myalgia", "fibromyalgia", "polymyalgia", "myositis",
        "weakness", "muscle weakness", "paresis", "hemiparesis", "paraparesis",
        "spasm", "muscle spasm", "cramp", "charley horse", "contracture",
        "rigidity", "stiffness", "dystonia", "torticollis", "opisthotonus",
        "bone pain", "osteodynia", "ostealgia", "tenderness", "bony tenderness",
        "back pain", "lumbago", "sciatica", "radiculopathy", "spondylosis",
        "neck pain", "cervicalgia", "whiplash", "torticollis", "cervical strain",
        "limping", "gait disturbance", "antalgic gait", "claudication", "ataxia",

        # Peau et téguments
        "rash", "eruption", "exanthem", "dermatitis", "eczema",
        "urticaria", "hives", "wheals", "angioedema", "swelling",
        "pruritus", "itching", "itchiness", "scratching", "prurigo",
        "erythema", "redness", "flushing", "blushing", "rubor",
        "pallor", "paleness", "blanching", "whiteness", "bleaching",
        "cyanosis", "bluish discoloration", "lividity", "ecchymosis", "bruising",
        "petechiae", "purpura", "purpuric spots", "telangiectasia", "spider veins",
        "jaundice", "icterus", "yellow skin", "yellow sclera", "xanthochromia",
        "vesicles", "blisters", "bullae", "pustules", "papules",
        "nodules", "tumors", "cysts", "macules", "patches",
        "scales", "flaking", "desquamation", "exfoliation", "dandruff",
        "xerosis", "dry skin", "ichthyosis", "lichenification", "hyperkeratosis",
        "hyperhidrosis", "excessive sweating", "anhidrosis", "decreased sweating",
        "alopecia", "hair loss", "baldness", "hirsutism", "hypertrichosis",

        # Système endocrinien
        "polyuria", "polydipsia", "polyphagia", "weight loss", "weight gain",
        "heat intolerance", "cold intolerance", "sweating", "dry skin",
        "tremor", "palpitations", "tachycardia", "bradycardia", "arrhythmia",
        "exophthalmos", "proptosis", "goiter", "neck swelling", "thyromegaly",
        "hirsutism", "alopecia", "gynecomastia", "galactorrhea", "amenorrhea",
        "menstrual irregularity", "erectile dysfunction", "decreased libido", "increased libido",
        "excessive thirst", "frequent urination", "hunger", "fatigue", "weakness",

        # Système hématologique
        "pallor", "jaundice", "cyanosis", "ecchymosis", "petechiae",
        "purpura", "easy bruising", "bleeding gums", "epistaxis", "melena",
        "hematuria", "hematemesis", "hemoptysis", "menorrhagia", "metrorrhagia",
        "lymphadenopathy", "splenomegaly", "hepatomegaly", "fatigue", "weakness",

        # Système immunitaire
        "fever", "fatigue", "malaise", "anorexia", "weight loss",
        "lymphadenopathy", "splenomegaly", "hepatomegaly", "arthralgia", "myalgia",
        "rash", "urticaria", "angioedema", "rhinitis", "conjunctivitis",
        "wheezing", "dyspnea", "cough", "diarrhea", "abdominal pain",

        # Système psychiatrique
        "depression", "anxiety", "panic", "phobia", "obsession",
        "compulsion", "mania", "euphoria", "irritability", "agitation",
        "aggression", "psychosis", "delusion", "hallucination", "paranoia",
        "confusion", "disorientation", "amnesia", "memory loss", "dementia",
        "insomnia", "hypersomnia", "parasomnia", "sleep apnea", "narcolepsy",
        "anorexia", "bulimia", "binge eating", "purging", "pica",
        "attention deficit", "hyperactivity", "impulsivity", "mood swings", "emotional lability",

        # Conditions médicales souvent associées à des symptômes
        "asthma", "bronchitis", "pneumonia", "emphysema", "tuberculosis",
        "hypertension", "hypotension", "coronary artery disease", "heart failure", "arrhythmia",
        "gastritis", "peptic ulcer", "inflammatory bowel disease", "irritable bowel syndrome", "pancreatitis",
        "hepatitis", "cirrhosis", "cholecystitis", "cholelithiasis", "appendicitis",
        "nephritis", "urinary tract infection", "pyelonephritis", "cystitis", "urethritis",
        "arthritis", "osteoarthritis", "rheumatoid arthritis", "gout", "fibromyalgia",
        "migraine", "tension headache", "cluster headache", "neuralgia", "neuropathy",
        "dermatitis", "eczema", "psoriasis", "urticaria", "cellulitis",
        "hypothyroidism", "hyperthyroidism", "diabetes", "adrenal insufficiency", "hypercortisolism",
        "anemia", "leukemia", "lymphoma", "thrombocytopenia", "hemophilia",
        "allergy", "asthma", "anaphylaxis", "autoimmune disorder", "immunodeficiency",
        "depression", "anxiety disorder", "bipolar disorder", "schizophrenia", "dementia",
        "influenza", "common cold", "covid-19", "ebola", "zika",
        "malaria", "dengue", "typhoid", "cholera", "dysentery",
        "hiv", "aids", "hepatitis", "herpes", "syphilis"
    ]
