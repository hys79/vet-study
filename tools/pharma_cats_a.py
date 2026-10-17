"""약물군(탭) 정의 A: 신경계 · 오타코이드/염증 · 순환/신장계 · 호흡기계

섹션 S(g, d, t, a, info, sb, x, h)
  g  세부 분류 이름           d  이 약물군이 '주 분류'인 약물 id(한 약물은 전체에서 한 곳에만)
  t/a 수용체 표의 행/열        x  다른 약물군이 주 분류인 약물(참조 칩으로만 표시)
  h  소제목(같은 h가 이어지면 한 번만 표시)   sb 한 줄 설명
  info  ("grp", 원래 카테고리 id, 원래 분류 이름) 또는 ("cat", 원래 카테고리 id): 원문 기전·특징 가져오기
cat: id, n, unit, b(분류 기준), cols(수용체 표 열), old(원문 설명을 자동으로 가져올 원래 카테고리 id)
"""


def S(g, d, t=None, a=None, info=(), sb=None, x=(), h=None):
    return {"g": g, "d": list(d), "t": t, "a": a, "info": list(info), "sb": sb, "x": list(x), "h": h}


OPIOID_COLS = ["효현제", "부분 · 혼합 효현-길항제", "길항제"]

CATS_A = [
    # ═════════ 신경계 · 자율신경계 ═════════
    {
        "id": "adrenergic", "n": "아드레날린성 약물", "unit": "자율신경계", "fam": "auto",
        "b": "수용체 · 신경 말단 작용 기전", "cols": ["효현제", "길항제"],
        "sections": [
            S("α1 효현제", ["methoxamine", "metaraminol", "phenylephrine"], "α1", "효현제"),
            S("α1 길항제", ["prazosin", "terazosin", "doxazosin"], "α1", "길항제"),
            S("α2 효현제", ["clonidine", "xylazine", "guanabenz", "guanfacine", "medetomidine", "dexmedetomidine", "detomidine", "romifidine"], "α2", "효현제"),
            S("α2 길항제", ["yohimbine", "atipamezole"], "α2", "길항제"),
            S("α 비선택적 길항제", ["phenoxybenzamine", "phentolamine", "dibenamine", "tolazoline", "ergotoxine"], "α(비선택)", "길항제"),
            S("α·β 효현제(비선택)", ["epinephrine", "norepinephrine"], "α·β(비선택)", "효현제"),
            S("β1 효현제", ["dobutamine", "dopamine"], "β1", "효현제"),
            S("β1 길항제", ["metoprolol", "betaxolol", "atenolol", "acebutolol", "esmolol"], "β1", "길항제"),
            S("β2 효현제", ["salbutamol", "terbutaline", "procaterol", "metaproterenol", "ritodrine", "bitolterol", "pirbuterol", "formoterol", "clenbuterol"], "β2", "효현제"),
            S("β2 길항제", ["butoxamine"], "β2", "길항제"),
            S("β3 효현제", ["brl_37344"], "β3", "효현제"),
            S("β3 길항제", ["bupranolol"], "β3", "길항제"),
            S("β 비선택적 효현제", ["isoproterenol"], "β(비선택)", "효현제"),
            S("β 비선택적 길항제", ["propranolol", "pindolol", "nadolol", "timolol", "sotalol"], "β(비선택)", "길항제"),
            S("카테콜아민 합성 억제", ["metyrosine"], info=[("grp", "nerve_terminal_actions", "합성 억제")]),
            S("저장 소포 운반 억제", ["reserpine"], info=[("grp", "nerve_terminal_actions", "저장 소포 운반 억제")]),
            S("유리 촉진 · 간접 작용", ["ephedrine", "tyramine", "mephentermine", "pseudoephedrine", "phenylpropanolamine"], info=[("grp", "nerve_terminal_actions", "유리 촉진")],
              sb="amphetamine류는 중추신경 흥분제 참조"),
            S("유리 억제 · 신경 차단", ["guanethidine", "bretylium", "guanadrel", "bethanidine", "debrisoquin", "6_hydroxydopamine"], info=[("grp", "nerve_terminal_actions", "유리 억제")]),
            S("재흡수 억제", ["cocaine"], info=[("grp", "nerve_terminal_actions", "재흡수 억제")], sb="삼환계 항우울제(imipramine 등)는 항우울제 참조"),
            S("COMT 억제", ["catechol", "pyrogallol", "quercetin", "rutin"], info=[("grp", "nerve_terminal_actions", "대사(분해) 억제")], sb="MAO 억제제는 항우울제 참조"),
        ],
    },
    {
        "id": "cholinergic", "n": "콜린성 약물", "unit": "자율신경계", "fam": "auto",
        "b": "수용체 · 효소 · 신경 독소", "cols": ["효현제", "길항제"],
        "sections": [
            S("M 효현제", ["methacholine", "carbachol", "bethanechol", "muscarine", "pilocarpine", "arecoline", "oxotremorine"], "무스카린 수용체(M)", "효현제",
              info=[("grp", "choline_agonists", "콜린 에스터"), ("grp", "choline_agonists", "콜린 유사 alkaloid")]),
            S("M 길항제", ["atropine", "scopolamine", "n_butylscopolammonium", "hyoscyamine", "propantheline", "glycopyrrolate", "ipratropium_bromide", "tropicamide", "aminopentamide", "oxybutynin", "pirenzepine", "isopropamide"],
              "무스카린 수용체(M)", "길항제", info=[("cat", "antimuscarinic")]),
            S("Nn 효현제", ["nicotine", "levamisole", "morantel", "pyrantel"], "신경절 니코틴 수용체(Nn)", "효현제"),
            S("Nn 길항제", ["hexamethonium", "mecamylamine", "trimethaphan"], "신경절 니코틴 수용체(Nn)", "길항제"),
            S("Nm 효현제(탈분극성 근이완제)", ["succinylcholine", "decamethonium", "hexacarbacholine"], "신경근 접합부 니코틴 수용체(Nm)", "효현제", info=[("cat", "muscle_relaxant")]),
            S("Nm 길항제(비탈분극성 근이완제)", ["d_tubocurarine", "gallamine_triethiodide", "metocurine", "pancuronium", "vecuronium", "atracurium", "alcuronium", "doxacurium"],
              "신경근 접합부 니코틴 수용체(Nm)", "길항제", info=[("cat", "muscle_relaxant")]),
            S("콜린에스터라제 억제제 - 가역적", ["physostigmine", "neostigmine", "edrophonium", "pyridostigmine", "ambenonium", "demecarium"], info=[("cat", "anticholinesterase")]),
            S("콜린에스터라제 억제제 - 비가역적(유기인)", ["parathion", "malathion", "dfp", "echothiophate"], info=[("cat", "anticholinesterase")]),
            S("콜린에스터라제 재활성화제(해독제)", ["pralidoxime"], sb="유기인 중독: atropine + 2-PAM"),
            S("콜린성 말단 작용 억제", ["hemicholinium", "botulinum_toxin"], sb="hemicholinium: 콜린 재흡수(합성) 억제, botulinum toxin: ACh 유리 억제"),
            S("콜린성 신경 독소", ["alpha_bungarotoxin", "beta_bungarotoxin", "black_widow_spider_venom"]),
        ],
    },
    # ═════════ 신경계 · 중추신경계 ═════════
    {
        "id": "cns_stim", "n": "중추신경 흥분제", "unit": "중추신경계", "fam": "cns", "b": "작용 부위",
        "sections": [
            S("대뇌 피질 작용", ["caffeine", "theophylline", "theobromine", "amphetamine", "methamphetamine"]),
            S("연수 작용", ["picrotoxin", "doxapram", "leptazol", "nikethamide", "bemegride"]),
            S("척수 작용", ["strychnine"]),
        ],
    },
    {
        "id": "cns_depressant", "n": "중추신경 억제제", "unit": "중추신경계", "fam": "cns", "b": "화학 구조",
        "sections": [
            S("Barbiturate계", ["thiopental", "phenobarbital", "pentobarbital", "primidone"]),
            S("Benzodiazepine계", ["diazepam", "midazolam", "clonazepam", "lorazepam", "zolazepam"]),
            S("기타 진정 · 최면제", ["chloral_hydrate", "glutethimide"]),
            S("Phenothiazine계", ["chlorpromazine", "acepromazine", "promazine", "prochlorperazine"]),
            S("Butyrophenone계", ["droperidol", "fluanisone", "azaperone", "haloperidol"]),
            S("Hydantoin계", ["phenytoin"]),
            S("기타 항경련제", ["potassium_bromide", "ethosuximide", "valproic_acid", "gabapentin", "levetiracetam", "zonisamide"]),
            S("Benzodiazepine 길항제", ["flumazenil"]),
            S("중추성 근이완제", ["guaiacol_glycerol_ether", "methocarbamol", "mephenesin"]),
            S("직접 작용 근이완제", ["dantrolene"], sb="근소포체 ryanodine 수용체 억제 — 악성 고열"),
        ],
    },
    {
        "id": "analgesic", "n": "마약성 진통제", "unit": "중추신경계", "fam": "cns", "b": "수용체(오피오이드)", "cols": OPIOID_COLS,
        "sections": [
            S("오피오이드 효현제", ["morphine", "codeine", "diamorphine", "methadone", "thiambutene", "pethidine", "etorphine", "fentanyl", "levorphanol", "alphaprodine", "anileridine", "propoxyphene", "hydrocodone", "hydromorphone", "tramadol"],
              "오피오이드 수용체", "효현제"),
            S("오피오이드 부분 · 혼합 효현제", ["butorphanol", "buprenorphine", "nalbuphine"], "오피오이드 수용체", "부분 · 혼합 효현-길항제"),
            S("오피오이드 길항제", ["naloxone"], "오피오이드 수용체", "길항제"),
            S("진통 효과가 약한 opioid 유도체", ["dextromethorphan", "diphenoxylate", "loperamide"], sb="진해 · 지사 목적. 비마약성 진통은 용도별 보기의 ‘진통’ 참조"),
        ],
    },
    {
        "id": "anesthetic", "n": "마취제", "unit": "중추신경계", "fam": "cns", "b": "투여 경로 · 화학 구조",
        "sections": [
            S("Propofol(주사)", ["propofol"]),
            S("해리성 마취제(주사)", ["ketamine", "tiletamine"]),
            S("Imidazole계(주사)", ["metomidate", "etomidate", "r8110"]),
            S("Alphaxalone(주사)", ["alphaxalone"]),
            S("흡입 마취제", ["halothane", "nitrous_oxide", "methoxyflurane", "isoflurane", "cyclopropane", "trichloroethylene", "desflurane", "sevoflurane", "tricaine_methanesulfonate"]),
            S("국소마취제 - amide형", ["lidocaine", "bupivacaine", "ropivacaine", "mepivacaine", "prilocaine", "etidocaine", "cinchocaine"]),
            S("국소마취제 - ester형", ["tetracaine", "procaine", "benzocaine", "proparacaine", "butacaine", "butyl_aminobenzoate"]),
        ],
    },
    {
        "id": "antidepressant", "n": "항우울제", "unit": "중추신경계", "fam": "cns", "b": "작용 기전",
        "sections": [
            S("MAO 억제제(MAOI)", ["selegiline", "tranylcypromine", "phenelzine", "isocarboxazid", "iproniazid"], info=[("grp", "antidepressant", "MAO 억제제(MAOI)")]),
            S("삼환계 항우울제(TCA)", ["amitriptyline", "imipramine", "clomipramine", "doxepin"], info=[("grp", "antidepressant", "삼환계 항우울제(TCA)")]),
            S("선택적 세로토닌 재흡수 억제제(SSRI)", ["fluoxetine", "paroxetine", "sertraline", "fluvoxamine"], info=[("grp", "antidepressant", "선택적 세로토닌 재흡수 억제제(SSRI)")]),
            S("SARI(기타 항불안제)", ["trazodone"]),
            S("기타 - 행동 교정용 Progestin계", [], x=["megestrol_acetate", "medroxyprogesterone_acetate"], info=[("grp", "antidepressant", "Progestin계 약물")]),
        ],
    },
    {
        "id": "emetic", "n": "구토 유발제", "unit": "중추신경계", "fam": "cns", "b": "작용 부위",
        "sections": [
            S("중추성(CTZ 자극)", ["apomorphine"]),
            S("국소성(위 점막 자극)", ["saline", "sodium_carbonate", "1_copper_sulfate", "emetine", "ipecac"]),
        ],
    },

    # ═════════ 오타코이드 · 염증 ═════════
    {
        "id": "histamine_serotonin", "n": "히스타민 · 세로토닌 약물", "unit": "오타코이드", "fam": "autacoid",
        "b": "수용체", "cols": ["효현제", "길항제"], "old": ["antihistamine", "serotonin_drugs"],
        "sections": [
            S("H1 길항제", ["diphenhydramine", "mepyramine", "promethazine", "tripelennamine", "chlorpheniramine", "hydroxyzine", "dimenhydrinate", "astemizole", "terfenadine"], "H1", "길항제",
              sb="1세대: 진정·항무스카린 작용(멀미·구토에도 사용) / 2세대(astemizole, terfenadine): 진정 적음, QT 연장"),
            S("H2 길항제", ["cimetidine", "ranitidine", "famotidine", "burimamide", "metiamide", "nizatidine"], "H2", "길항제", sb="위산 분비 억제. cimetidine은 CYP450 억제"),
            S("5-HT1 효현제", ["buspirone"], "5-HT1", "효현제"),
            S("5-HT2 길항제", ["cyproheptadine", "ketanserin"], "5-HT2", "길항제"),
            S("5-HT3 길항제", ["ondansetron", "dolasetron"], "5-HT3", "길항제"),
            S("5-HT4 효현제", ["cisapride", "metoclopramide"], "5-HT4", "효현제"),
            S("비만세포 안정제", ["sodium_cromoglycate"], sb="탈과립을 막는 예방약"),
            S("α2 · 5-HT3 길항제(식욕 · 항구토)", ["mirtazapine"]),
        ],
    },
    {
        "id": "prostaglandin", "n": "프로스타글란딘", "unit": "오타코이드", "fam": "autacoid", "b": "화학 구조(PG 계열)",
        "old": ["prostaglandin_other"],
        "sections": [
            S("PGE 계열", ["pge1", "pge2", "misoprostol"], sb="misoprostol: PGE1 유도체(NSAID 궤양 예방, 임신 금기)"),
            S("PGF2α 계열", ["pgf2alpha", "cloprostenol"], sb="황체 퇴행(luteolysis) → 발정 동기화 · 유산 유도 · 자궁축농증 치료"),
        ],
    },
    {
        "id": "corticosteroid", "n": "코르티코스테로이드", "unit": "항염증 · 호르몬", "fam": "autacoid", "b": "호르몬 종류(내인성 · 합성 · 합성 억제)",
        "old": ["anti_inflammatory", "adrenal_drugs"],
        "sections": [
            S("내인성 글루코코르티코이드", ["cortisol", "corticosterone"]),
            S("내인성 무기질코르티코이드", ["deoxycorticosterone", "aldosterone"]),
            S("무기질코르티코이드 대치요법", ["fludrocortisone"], sb="Addison병 치료"),
            S("합성 글루코코르티코이드", ["cortisone", "hydrocortisone", "prednisone", "prednisolone", "methylprednisolone", "dexamethasone", "triamcinolone", "flumethasone", "betamethasone"]),
            S("합성 부신피질 호르몬 길항제", ["ddt", "amphenone_b", "metyrapone"], x=["spironolactone"]),
            S("부신 스테로이드 합성 억제제", ["mitotane", "trilostane"], x=["ketoconazole", "selegiline"], sb="Cushing병 치료"),
        ],
    },
    {
        "id": "nsaid", "n": "NSAIDs · 해열진통제", "unit": "항염증 · 호르몬", "fam": "autacoid", "b": "작용 기전(COX 선택성)",
        "old": ["nsaid"],
        "sections": [
            S("비선택적 COX 억제제", ["aspirin", "flunixin_meglumine", "naproxen", "ibuprofen", "indomethacin", "ketoprofen"]),
            S("COX-2 선호 억제제", ["phenylbutazone", "meloxicam", "etodolac", "carprofen", "piroxicam"]),
            S("선택적 COX-2 억제제", ["deracoxib", "firocoxib", "robenacoxib"]),
            S("EP4 수용체 길항제(NSAID 아님)", ["grapiprant"], sb="COX를 억제하지 않고 PGE2의 EP4 수용체만 차단"),
            S("COX · 5-LOX 이중 억제제", ["tepoxalin"]),
            S("Aniline계 해열진통제(NSAID 아님)", ["acetanilide", "phenacetin", "acetaminophen"], sb="항염증 작용이 약하고 NSAID와 기전이 다름. 고양이 금기"),
            S("기타 항염증 · 관절 보조제", ["dimethyl_sulfoxide", "polysulfated_glycosaminoglycan", "hyaluronate_sodium"]),
        ],
    },

    # ═════════ 순환 · 신장계 ═════════
    {
        "id": "inotrope", "n": "강심제", "unit": "심장", "fam": "circ", "b": "작용 기전", "old": ["heart_failure"],
        "sections": [
            S("강심배당체(Na⁺/K⁺-ATPase 억제)", ["digoxin", "digitoxin", "gitoxin", "gitalin", "ouabain"]),
            S("PDE3 억제제 · inodilator", ["pimobendan", "amrinone", "milrinone"]),
            S("카테콜아민계 강심제(β1 효현)", [], x=["dobutamine", "dopamine"]),
        ],
    },
    {
        "id": "antiarrhythmic", "n": "항부정맥제", "unit": "심장", "fam": "circ", "b": "활동전위 영향(Vaughan-Williams 분류)", "old": ["antiarrhythmic"],
        "sections": [
            S("Class IA", ["disopyramide", "quinidine", "procainamide"], sb="Na⁺ + K⁺ 채널 차단, 활동전위 연장"),
            S("Class IB", ["mexiletine", "tocainide"], x=["lidocaine", "phenytoin"], sb="Na⁺ 채널 차단, 활동전위 단축"),
            S("Class IC", ["flecainide", "propafenone", "encainide", "indecainide", "lorcainide"], sb="Na⁺ 채널 강한 차단, 전도 지연"),
            S("Class II(β 차단제)", [], x=["metoprolol", "propranolol", "pindolol", "esmolol"]),
            S("Class III(K⁺ 채널 차단제)", ["amiodarone"], x=["bretylium", "sotalol"]),
            S("Class IV(Ca²⁺ 채널 차단제)", [], x=["diltiazem", "verapamil", "nifedipine"]),
            S("기타", ["adenosine"], x=["digoxin"]),
        ],
    },
    {
        "id": "vasodilator", "n": "혈관 확장제 · 항고혈압 · 협심증 약물", "unit": "혈관 · 혈압", "fam": "circ", "b": "작용 기전", "old": ["angina", "hypertension"],
        "sections": [
            S("Ca²⁺ 채널 차단제", ["diltiazem", "verapamil", "nifedipine", "prenylamine", "amlodipine"], sb="dihydropyridine(nifedipine, amlodipine): 혈관 선택 / verapamil·diltiazem: 심장 억제"),
            S("Nitrate계(NO 공여)", ["nitroglycerin", "isosorbide_dinitrate", "amyl_nitrite", "nitroprusside"]),
            S("직접 혈관 확장제", ["hydralazine"]),
            S("K⁺ 채널 개방제", ["minoxidil"]),
            S("기타 혈압 강하제", ["veratridine"], x=["clonidine", "reserpine", "chlorpromazine"]),
        ],
    },
    {
        "id": "ras", "n": "Renin-angiotensin계 약물", "unit": "혈관 · 혈압", "fam": "circ", "b": "작용 기전(RAS 차단 단계)", "old": ["ras_antagonist"],
        "sections": [
            S("ACE 억제제", ["captopril", "enalapril", "lisinopril", "benazepril", "ramipril", "quinapril"]),
            S("안지오텐신 수용체 차단제(ARB)", ["losartan", "valsartan", "candesartan", "telmisartan"]),
            S("Renin 억제제", ["aliskiren"]),
        ],
    },
    {
        "id": "diuretic", "n": "이뇨제", "unit": "신장 · 혈액", "fam": "circ", "b": "작용 부위(네프론) · 요 pH", "old": ["diuretic"],
        "sections": [
            S("Loop 이뇨제(헨레고리)", ["furosemide", "ethacrynic_acid", "bumetanide", "muzolimine", "torsemide"], h="신장에 작용하는 이뇨제"),
            S("Thiazide계 이뇨제", ["chlorothiazide", "hydrochlorothiazide", "hydroflumethiazide", "bendroflumethiazide", "benzthiazide", "trichlormethiazide", "methyclothiazide", "polythiazide", "cyclothiazide", "chlorthalidone", "metolazone", "quinethazone", "indapamide"], h="신장에 작용하는 이뇨제"),
            S("칼륨 보존성 이뇨제", ["spironolactone", "triamterene", "amiloride"], h="신장에 작용하는 이뇨제"),
            S("탄산탈수효소 억제제", ["acetazolamide", "dichlorphenamide", "ethoxzolamide", "methazolamide"], h="신장에 작용하는 이뇨제"),
            S("삼투성 이뇨제", ["mannitol"], x=["dimethyl_sulfoxide"], h="신장에 작용하는 이뇨제"),
            S("심혈관성 이뇨제(강심배당체 · Xanthine계)", [], x=["digoxin", "digitoxin", "gitoxin", "gitalin", "ouabain", "caffeine", "theobromine", "theophylline", "aminophylline"], h="심혈관성 이뇨제"),
            S("산성화 이뇨제", ["ammonium_chloride", "calcium_chloride", "sodium_phosphate", "ascorbic_acid", "methionine"], h="요 pH 조절 이뇨제"),
            S("알칼리화 이뇨제", ["citrate"], x=["sodium_bicarbonate"], h="요 pH 조절 이뇨제"),
        ],
    },
    {
        "id": "hemostasis", "n": "항응고제 · 혈전 · 지혈 약물", "unit": "신장 · 혈액", "fam": "circ", "b": "작용 단계(응고 · 혈소판 · 섬유소 용해)", "old": ["anticoagulant", "hemostasis_drugs"],
        "sections": [
            S("생체 내 항응고제", ["heparin", "dicumarol", "warfarin"]),
            S("체외 항응고제(채혈 · 보존용)", ["sodium_citrate_solution", "acid_citrate_dextrose", "sodium_oxalate", "fluoride", "silicone", "liquid_paraffin", "edetate_disodium", "hirudin"], x=["heparin"]),
            S("항혈소판제", ["clopidogrel"], x=["aspirin"]),
            S("혈전 용해제(섬유소 용해제)", ["streptokinase"]),
            S("지혈제", ["vitamin_k"]),
            S("헤파린 해독제", ["protamine_sulfate"]),
            S("항응고제 작용 증가 약물", ["oxyphenbutazone", "disulfiram", "sulfinpyrazone", "trimethoprim_sulfamethoxazole", "clofibrate"],
              x=["chloral_hydrate", "cimetidine", "aspirin", "phenylbutazone", "metronidazole"]),
            S("항응고제 작용 감소 약물", ["cholestyramine"], x=["glutethimide", "rifampin"]),
        ],
    },

    # ═════════ 호흡기계 ═════════
    {
        "id": "resp_secretion", "n": "거담제 · 점액 용해제 · 충혈 제거제", "unit": "호흡기계", "fam": "resp", "b": "작용 목적(증상별)", "old": ["respiratory_drugs"],
        "sections": [
            S("거담제", ["cocillana", "tolu_balsam", "ammonium_bicarbonate", "potassium_iodide", "sodium_iodide"], x=["guaiacol_glycerol_ether", "ipecac"]),
            S("점액 용해제", ["bromhexine", "n_acetylcysteine", "dembrexine"]),
            S("충혈 제거제 - 교감신경 효현제(α)", [], x=["phenylephrine", "ephedrine", "pseudoephedrine"]),
            S("충혈 제거제 - H1 항히스타민제", [], x=["diphenhydramine", "dimenhydrinate", "chlorpheniramine", "hydroxyzine"]),
        ],
    },
    {
        "id": "resp_cough_bronchodilator", "n": "진해제 · 기관지 이완제 · 폐고혈압 약물", "unit": "호흡기계", "fam": "resp", "b": "작용 목적(증상별)", "old": ["antitussive_bronchodilator"],
        "sections": [
            S("중추성 진해제", ["pholcodine", "noscapine"], x=["morphine", "codeine", "diamorphine", "dextromethorphan", "hydrocodone", "butorphanol"], h="진해제"),
            S("말초성 진해제", ["benzonatate"], h="진해제"),
            S("β2 · 아드레날린성 효현제", [], x=["salbutamol", "terbutaline", "ephedrine", "isoproterenol", "clenbuterol", "epinephrine"], h="기관지 이완제"),
            S("Methylxanthine계", ["aminophylline", "ibmx", "paraxanthine", "pentoxifylline"], x=["caffeine", "theophylline", "theobromine"], h="기관지 이완제"),
            S("항무스카린제(진경제)", ["eucatropine"], x=["atropine", "glycopyrrolate", "ipratropium_bromide"], h="기관지 이완제"),
            S("PDE5 억제제", ["sildenafil"], h="폐성 고혈압 억제제"),
        ],
    },
]
