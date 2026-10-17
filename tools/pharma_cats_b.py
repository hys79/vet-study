"""약물군(탭) 정의 B: 소화기계 · 대사/내분비 · 항감염제 · 항기생충/살충제 · 항암/면역 (형식은 pharma_cats_a.py 설명 참조)"""
from pharma_cats_a import S

CATS_B = [
    # ═════════ 소화기계 ═════════
    {
        "id": "gi_acid", "n": "위산 분비 억제제 · 점막 보호제", "unit": "소화기계", "fam": "gi", "b": "작용 기전", "old": ["gi_acid"],
        "sections": [
            S("항콜린제", ["homatropine", "methylatropine_nitrate", "methantheline_bromide"], x=["atropine", "glycopyrrolate", "propantheline"]),
            S("H2 길항제", [], x=["cimetidine", "ranitidine", "famotidine", "burimamide", "metiamide", "nizatidine"]),
            S("양성자 펌프 억제제(PPI)", ["omeprazole", "pantoprazole"]),
            S("제산제", ["sodium_bicarbonate", "calcium_carbonate", "aluminum_hydroxide", "magnesium_trisilicate"]),
            S("점막 보호제", ["sucralfate"], x=["misoprostol"]),
        ],
    },
    {
        "id": "antiemetic", "n": "항구토제", "unit": "소화기계", "fam": "gi", "b": "작용 기전(수용체)", "old": ["antiemetic"],
        "sections": [
            S("D2 길항제", [], x=["chlorpromazine", "acepromazine", "promazine", "prochlorperazine", "haloperidol", "metoclopramide"]),
            S("5-HT3 길항제", [], x=["ondansetron", "dolasetron"]),
            S("NK1 길항제", ["maropitant"], sb="중추 · 말초 경로를 모두 차단하는 광범위 항구토제, 멀미에도 사용"),
            S("항히스타민제 · 항콜린제(전정성 구토)", [], x=["diphenhydramine", "dimenhydrinate", "promethazine", "scopolamine", "aminopentamide", "propantheline", "isopropamide"]),
            S("진정제", [], x=["phenobarbital"]),
        ],
    },
    {
        "id": "gi_motility", "n": "장관운동 · 식욕 조절 약물", "unit": "소화기계", "fam": "gi", "b": "작용 목적", "old": ["gi_motility", "gi_appetite"],
        "sections": [
            S("완화제", ["lactulose", "polyethylene_glycol", "sodium_sulfate", "magnesium_sulfate", "magnesium_hydroxide"]),
            S("장관운동 촉진제(prokinetic)", [], x=["cisapride", "metoclopramide", "ranitidine", "erythromycin", "bethanechol", "neostigmine", "vasopressin"], sb="기계적 장 폐색에는 금기"),
            S("식욕 촉진제", ["oxazepam"], x=["diazepam", "cyproheptadine", "mirtazapine"]),
            S("Ghrelin 수용체 효현제(식욕 촉진)", ["capromorelin"]),
            S("항비만제", ["dirlotapide"]),
        ],
    },

    # ═════════ 대사 · 내분비 ═════════
    {
        "id": "pituitary", "n": "시상하부 · 뇌하수체 · 송과체 호르몬", "unit": "대사 · 내분비", "fam": "endo", "b": "분비 기관", "old": ["pituitary_pineal"],
        "sections": [
            S("성장호르몬(GH) 제제", ["sometribove"]),
            S("태반성 성선자극호르몬(Gonadotropin)", ["pmsg", "hcg"]),
            S("프로락틴 관련", ["domperidone", "bromocriptine", "cabergoline"]),
            S("뇌하수체 후엽 호르몬", ["oxytocin", "vasopressin", "desmopressin"]),
            S("송과체 호르몬", ["melatonin"]),
        ],
    },
    {
        "id": "thyroid_calcium", "n": "갑상선 · 칼슘 조절 약물", "unit": "대사 · 내분비", "fam": "endo", "b": "분비 기관 · 작용", "old": ["thyroid_drugs", "calcium_regulation_drugs"],
        "sections": [
            S("갑상선 호르몬제", ["thyroid", "levothyroxine_sodium", "liothyronine_sodium", "liotrix", "iodine_casein"], h="갑상선"),
            S("항갑상선제", ["thiouracil", "methylthiouracil", "propylthiouracil", "methimazole", "sulfaguanidine", "phenylthiourea"], h="갑상선"),
            S("T4→T3 전환 억제제", ["ipodate"], h="갑상선"),
            S("방사성 요오드", ["radioactive_iodine_na131i"], h="갑상선"),
            S("칼슘 조절 호르몬", ["calcitonin", "parathyroid_hormone"], h="칼슘 조절"),
            S("저칼슘혈증 치료제", ["calcium_gluconate", "calcium_borogluconate", "dihydrotachysterol", "calcitriol"], h="칼슘 조절"),
        ],
    },
    {
        "id": "pancreas", "n": "췌장 호르몬 · 항당뇨제", "unit": "대사 · 내분비", "fam": "endo", "b": "작용 기전", "old": ["pancreas_drugs"],
        "sections": [
            S("인슐린", ["insulin"]),
            S("설폰요소제(Sulfonylurea)", ["glipizide", "glyburide", "glimepiride"]),
            S("경구 혈당강하제", ["metformin"]),
            S("글루카곤", ["glucagon"]),
        ],
    },
    {
        "id": "sex_hormone", "n": "성호르몬 · 자궁 수축제", "unit": "대사 · 내분비", "fam": "endo", "b": "호르몬 종류", "old": ["sex_hormone_drugs", "prostaglandin_other"],
        "sections": [
            S("남성 호르몬(Androgen)", ["testosterone", "stanozolol", "boldenone", "trenbolone", "danazol", "fluoxymesterone", "19_nortestosterone", "methandrostenolone"]),
            S("항남성호르몬(Antiandrogen)", ["finasteride"]),
            S("여성 호르몬(Estrogen)", ["estradiol", "estrone", "estriol", "zeranol", "diethylstilbestrol"]),
            S("항여성호르몬(Estrogen 수용체 길항제)", ["tamoxifen"]),
            S("프로게스테론 수용체 길항제", ["aglepristone"], sb="임신 중절 · 자궁축농증 내과적 치료"),
            S("황체호르몬(Progestin)", ["progesterone", "altrenogest", "melengestrol", "megestrol_acetate", "medroxyprogesterone_acetate"]),
            S("자궁 수축제 · 황체융해 유도제", ["ergonovine"], x=["oxytocin", "bromocriptine", "cabergoline", "pgf2alpha", "cloprostenol", "dexamethasone"]),
        ],
    },
    {
        "id": "ion_misc", "n": "이온 채널 · 기타 제제", "unit": "대사 · 내분비", "fam": "endo", "b": "표적 이온 · 제제 종류", "old": ["ion_inhibitors"],
        "sections": [
            S("Na⁺ 억제제", ["tetrodotoxin", "phlorhizin"]),
            S("K⁺ 억제제", ["tetraethylammonium"]),
            S("Ca²⁺ 억제제 · 킬레이트제", ["edta"], x=["verapamil", "nifedipine", "diltiazem"]),
            S("Na⁺/K⁺-ATPase 억제제", [], x=["ouabain"]),
            S("재조합 적혈구 생성인자", ["erythropoietin"]),
        ],
    },

    # ═════════ 항감염제 ═════════
    {
        "id": "antibiotic", "n": "항생제", "unit": "항감염제", "fam": "infect", "b": "작용 기전 › 화학 계열", "old": ["antibiotic_mechanism", "antibiotic_spectrum"],
        "sections": [
            S("Penicillin계", ["penicillin_g", "penicillin_v", "ampicillin", "amoxicillin", "hetacillin", "carbenicillin", "ticarcillin", "mezlocillin", "piperacillin"], h="세포벽 합성 억제", o="천연 → 아미노 → 항녹농균 penicillin 순"),
            S("Penicillin계 - penicillinase 저항성", ["methicillin", "oxacillin", "cloxacillin", "nafcillin"], h="세포벽 합성 억제"),
            S("Penicillin계 - β-lactamase 억제제(병용)", ["clavulanic_acid", "sulbactam", "tazobactam"], h="세포벽 합성 억제"),
            S("Cephalosporin 1세대", ["cephalexin", "cephalothin", "cefazolin"], h="세포벽 합성 억제"),
            S("Cephalosporin 2세대", ["cefaclor", "cefoxitin"], h="세포벽 합성 억제"),
            S("Cephalosporin 3세대", ["ceftiofur", "cefotaxime", "cefpodoxime", "cefovecin"], h="세포벽 합성 억제"),
            S("Cephalosporin 4세대", ["cefepime"], h="세포벽 합성 억제"),
            S("Carbapenem계", ["imipenem", "meropenem"], h="세포벽 합성 억제"),
            S("기타 세포벽 합성 억제제", ["vancomycin", "bacitracin", "cycloserine"], h="세포벽 합성 억제"),
            S("Aminoglycoside · aminocyclitol계(30S)", ["streptomycin", "neomycin", "kanamycin", "gentamicin", "tobramycin", "amikacin", "spectinomycin"], h="단백질 합성 억제", o="개발 순"),
            S("Tetracycline계(30S)", ["tetracycline", "oxytetracycline", "doxycycline", "minocycline"], h="단백질 합성 억제", o="작용 시간 짧은 → 긴"),
            S("Macrolide계(50S)", ["erythromycin", "tylosin", "tilmicosin", "azithromycin", "tulathromycin"], h="단백질 합성 억제"),
            S("Phenicol계(50S)", ["chloramphenicol", "florfenicol"], h="단백질 합성 억제"),
            S("Lincosamide계(50S)", ["clindamycin", "lincomycin", "pirlimycin"], h="단백질 합성 억제"),
            S("Pleuromutilin계(50S)", ["tiamulin"], h="단백질 합성 억제"),
            S("Quinolone계", ["nalidixic_acid", "ciprofloxacin", "enrofloxacin", "marbofloxacin"], h="핵산 합성 억제", o="세대 순"),
            S("Rifamycin계", ["rifampin"], h="핵산 합성 억제"),
            S("Novobiocin", ["novobiocin"], h="핵산 합성 억제"),
            S("Nitroimidazole계", ["metronidazole"], h="핵산 합성 억제"),
            S("Sulfonamide계", ["sulfamethazine", "sulfasalazine"], h="대사(엽산) 억제"),
            S("Trimethoprim", ["trimethoprim"], h="대사(엽산) 억제"),
            S("결핵 치료제", ["isoniazid", "ethambutol"], x=["rifampin"], h="대사(엽산) 억제"),
            S("Polymyxin계", ["polymyxin_b", "colistin"], h="세포막 작용"),
        ],
    },
    {
        "id": "antifungal", "n": "항진균제", "unit": "항감염제", "fam": "infect", "b": "작용 기전", "old": ["antifungal"],
        "sections": [
            S("Polyene계(ergosterol 결합)", ["amphotericin_b", "nystatin"]),
            S("Azole계(ergosterol 합성 억제)", ["miconazole", "ketoconazole", "fluconazole", "itraconazole"]),
            S("Allylamine계(squalene 변환 억제)", ["terbinafine"]),
            S("Griseofulvin(유사분열 억제)", ["griseofulvin"]),
            S("Flucytosine(핵산합성 억제)", ["flucytosine"]),
        ],
    },
    {
        "id": "antiviral", "n": "항바이러스제", "unit": "항감염제", "fam": "infect", "b": "바이러스 증식 단계", "old": ["antiviral"],
        "sections": [
            S("조립(Assembly) 억제", ["amantadine"]),
            S("핵산 합성 억제 - 바이러스 TK로 인산화", ["acyclovir", "famciclovir"]),
            S("핵산 합성 억제 - 숙주 효소로 인산화", ["zidovudine"]),
            S("번역 억제", ["idoxuridine"]),
            S("배출 억제(neuraminidase)", ["oseltamivir"]),
        ],
    },

    # ═════════ 항기생충 · 살충제 ═════════
    {
        "id": "anthelmintic", "n": "구충제", "unit": "항기생충 · 살충제", "fam": "parasite", "b": "대상 기생충 › 작용 기전 · 화학 계열", "old": ["anthelmintic_classification", "anthelmintic_mechanism", "antinematode", "anticestode_antitrematode", "heartworm_drugs"],
        "sections": [
            S("Benzimidazole계(β-tubulin 결합)", ["albendazole", "fenbendazole", "mebendazole", "thiabendazole", "prabendazole"], h="선충"),
            S("니코틴 수용체 효현제", ["metyridine"], x=["levamisole", "pyrantel", "morantel", "nicotine"], h="선충"),
            S("거대고리 락톤계 - Avermectin", ["ivermectin", "doramectin", "selamectin"], h="선충"),
            S("거대고리 락톤계 - Milbemycin", ["milbemycin", "moxidectin"], h="선충"),
            S("Piperazine(GABA 효현)", ["piperazine"], h="선충"),
            S("유기인계(AChE 억제)", ["dichlorvos", "trichlorfon"], h="선충"),
            S("SLO-1 K⁺ 채널 개방제", ["emodepside"], h="선충"),
            S("Salicylanilide · Phenol계(산화적 인산화 탈공역)", ["niclosamide", "bithionol", "hexachlorophene", "dichlorophen", "nitroxynil", "niclofolan", "oxyclozanide", "bunamidine", "dithiazine", "closantel"], h="조충 · 흡충"),
            S("Isoquinoline계(Ca²⁺ 투과성 증가)", ["praziquantel", "diamphenethide"], h="조충 · 흡충"),
            S("콜린 효현제", [], x=["arecoline"], h="조충 · 흡충"),
            S("살성충제", ["melarsomine"], h="심장사상충"),
            S("살성충제 부작용 완화제", ["dimercaprol"], h="심장사상충"),
            S("살미세사상충제 · 예방용 살유충제(거대고리 락톤계)", [], x=["ivermectin", "milbemycin", "moxidectin", "selamectin"], h="심장사상충"),
        ],
    },
    {
        "id": "antiprotozoal", "n": "항원충제", "unit": "항기생충 · 살충제", "fam": "parasite", "b": "대상 원충 › 작용 기전", "old": ["antiprotozoal"],
        "sections": [
            S("합성 약물", ["clopidol", "robenidine", "dinitolmide", "nicarbazine"], h="항콕시듐제"),
            S("Polyether 항생물질(ionophore)", ["monensin", "salinomycin", "lasalocid"], h="항콕시듐제"),
            S("Thiamine · 엽산 길항제", ["amprolium", "ethopabate", "sulfaquinoxaline", "diaveridine", "sulfadimethoxine", "ormethoprim"], x=["trimethoprim"], h="항콕시듐제"),
            S("Triazinetrione계", ["toltrazuril"], h="항콕시듐제"),
            S("Diminazene(항바베시아제)", ["diminazene"], h="항피로플라즈마제"),
            S("항타일레리아제", ["pamaquine", "primaquine"], h="항피로플라즈마제"),
            S("항톡소플라스마제", ["pyrimethamine", "sulfamonomethoxine"]),
            S("기타", ["acrinamine"], x=["metronidazole"]),
        ],
    },
    {
        "id": "insecticide", "n": "살충제", "unit": "항기생충 · 살충제", "fam": "parasite", "b": "화학 계열", "old": ["insecticide"],
        "sections": [
            S("유기인산계", ["fenitrothion", "coumaphos", "fenchlorphos"], x=["dichlorvos", "malathion"]),
            S("Carbamate계", ["carbaryl"]),
            S("Pyrethrin계", ["pyrethrin", "decamethrin", "allethrin", "permethrin"]),
            S("Isoxazoline계(GABA · glutamate Cl⁻ 채널 차단)", ["afoxolaner", "fluralaner"]),
            S("Phenylpyrazole계", ["fipronil"]),
            S("Neonicotinoid계", ["imidacloprid"]),
            S("Formamidine계", ["amitraz"]),
            S("곤충 성장 조절제(IGR)", ["lufenuron"]),
            S("기타", ["rotenone", "benzyl_benzoate", "sulfur"], x=["nicotine", "ivermectin"]),
        ],
    },

    # ═════════ 항암 · 면역 ═════════
    {
        "id": "antineoplastic", "n": "항암제", "unit": "항암 · 면역", "fam": "onco", "b": "작용 기전 › 화학 계열", "old": ["antineoplastic"],
        "sections": [
            S("Nitrogen mustard계", ["cyclophosphamide", "chlorambucil", "melphalan", "mechlorethamine", "ifosfamide"], h="알킬화제 · 백금 제제"),
            S("Nitrosourea계", ["lomustine", "carmustine", "streptozocin"], h="알킬화제 · 백금 제제"),
            S("Methylhydrazine계", ["procarbazine"], h="알킬화제 · 백금 제제"),
            S("Triazene계", ["dacarbazine"], h="알킬화제 · 백금 제제"),
            S("Hydroxyurea", ["hydroxyurea"], h="알킬화제 · 백금 제제"),
            S("백금 제제", ["cisplatin", "carboplatin"], h="알킬화제 · 백금 제제"),
            S("엽산 유사체", ["methotrexate"], h="항대사제"),
            S("피리미딘 유사체", ["5_fluorouracil", "cytarabine", "gemcitabine"], h="항대사제"),
            S("퓨린 유사체", ["6_mercaptopurine", "6_thioguanine"], h="항대사제"),
            S("Vinca alkaloid", ["vincristine", "vinblastine", "vinorelbine"], h="유사분열 방추체 억제제"),
            S("Taxane계", ["paclitaxel"], h="유사분열 방추체 억제제"),
            S("안트라사이클린계 · 기타 세포독성 항생제", ["doxorubicin", "epirubicin", "actinomycin", "mitomycin", "mitoxantrone", "bleomycin", "etoposide"], h="세포독성 항생제"),
            S("Doxorubicin 혈관 외 유출 시 투여", ["dexrazoxane"], h="세포독성 항생제"),
            S("효소", ["l_asparaginase"], h="기타"),
            S("Tyrosine kinase 억제제", ["toceranib", "masitinib"], h="기타"),
            S("기타 약물", [], x=["mitotane", "piroxicam"], h="기타"),
        ],
    },
    {
        "id": "immunosuppressant", "n": "면역억제제", "unit": "항암 · 면역", "fam": "onco", "b": "면역 반응 작용점", "old": ["immunosuppressant"],
        "sections": [
            S("퓨린 합성 억제제", ["azathioprine", "mycophenolic_acid"]),
            S("JAK 억제제", ["oclacitinib"], sb="IL-31 등 소양 사이토카인 신호 차단 — 개 아토피 피부염"),
            S("피리미딘 합성 억제제", ["leflunomide"]),
            S("사이토카인 억제제 - IL-2(cyclophilin/calcineurin)", ["cyclosporine", "tacrolimus"]),
            S("사이토카인 억제제 - TNF-α", [], x=["pentoxifylline"]),
            S("MMP 억제제 - Tetracycline계", [], x=["tetracycline", "oxytetracycline", "doxycycline", "minocycline"]),
            S("기타 면역 조절 - 금 요법", ["aurothioglucose", "aurothiomalate", "auranofin"]),
            S("기타 면역 조절 - Niacinamide", ["niacinamide"]),
        ],
    },
]
