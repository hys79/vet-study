"""약물 이름 어미(stem) 정리 — content/pharmacology/stems.html 이 사용 (build_pharma.py 가 data.js 에 포함).

ST(어미, 정규식, 묶음, 계열, 한 줄 포인트, 예외=[(약물 id, 설명)])
  정규식: 약물 표시 이름(소문자)에 적용해 예시를 자동으로 모은다.
  예외  : 이름은 비슷하지만 다른 계열인 약물 — ‘함정’으로 따로 보여 준다(정규식에 걸려도 예시에서는 뺀다).
빌드할 때 예시가 하나도 없는 어미가 있으면 오류를 낸다."""


def ST(s, rx, k, m, c, tr=()):
    return {"s": s, "rx": rx, "k": k, "m": m, "c": c, "tr": list(tr)}


STEMS = [
    # ── 항감염제 ──
    ST("-cillin", r"cillin$", "항감염제", "Penicillin계(β-lactam)", "PBP 억제 → 세포벽 합성 억제(살균). β-lactamase에 분해 → clavulanic acid 등 병용"),
    ST("cef- / ceph-", r"^(cef|ceph)", "항감염제", "Cephalosporin계(β-lactam)", "세대가 높을수록 그람음성↑ · 뇌척수액 투과(1세대 cephalexin → 3세대 ceftiofur → 4세대 cefepime)"),
    ST("-penem", r"penem$", "항감염제", "Carbapenem계", "가장 넓은 항균 범위, 보존적 사용"),
    ST("-bactam", r"bactam$", "항감염제", "β-lactamase 억제제", "단독 항균력은 약하고 penicillin과 병용"),
    ST("-cycline", r"cycline$", "항감염제", "Tetracycline계", "30S 리보솜 억제(정균). 치아·뼈 침착(어린 동물·임신 금기), 고양이 식도 협착"),
    ST("-micin / -mycin", r"(streptomycin|neomycin|kanamycin|gentamicin|tobramycin|spectinomycin|erythromycin|lincomycin|clindamycin|pirlimycin|azithromycin|tulathromycin)$", "항감염제",
       "Aminoglycoside(-micin·-mycin), Macrolide·Lincosamide(-mycin)",
       "계열이 섞여 있어 이름만으로 구분 불가: aminoglycoside(30S, 신독성·이독성), macrolide(erythromycin)·lincosamide(clindamycin: 초식동물 대장염)(50S)",
       [("vancomycin", "Glycopeptide — 세포벽 합성 억제"), ("mitomycin", "항암 항생제"), ("bleomycin", "항암 항생제(DNA 절단)"),
        ("milbemycin", "구충제(거대고리 락톤)"), ("salinomycin", "콕시듐 ionophore")]),
    ST("-floxacin", r"floxacin$", "항감염제", "Fluoroquinolone계", "DNA gyrase 억제(살균). 어린 동물 연골 손상, 고양이 망막 변성"),
    ST("sulfa-", r"^sulfa", "항감염제", "Sulfonamide계", "PABA 유사 → 엽산 합성 억제. trimethoprim과 순차 차단(상승 작용), 결정뇨"),
    ST("-azole", r"(ketoconazole|miconazole|fluconazole|itraconazole)$", "항감염제", "Azole계 항진균제", "진균 ergosterol 합성 억제(CYP51). ketoconazole은 CYP 억제 · 간독성",
       [("metronidazole", "-nidazole — 혐기균·원충 항생제"), ("omeprazole", "-prazole — 위산 분비 억제제(PPI)"), ("pantoprazole", "-prazole — PPI"),
        ("albendazole", "-bendazole — 벤지미다졸 구충제"), ("methimazole", "항갑상선제")]),
    ST("-nidazole", r"nidazole$", "항감염제", "Nitroimidazole계", "혐기균·원충(Giardia 등)에서 환원 활성화 → DNA 손상. 고용량 신경독성"),
    ST("-vir", r"vir$", "항감염제", "항바이러스제", "acyclovir·famciclovir: 바이러스 TK로 인산화(DNA polymerase 억제) / oseltamivir: neuraminidase 억제"),
    ST("-vudine", r"vudine$", "항감염제", "역전사효소 억제제(NRTI)", "zidovudine — 고양이 FIV·FeLV"),
    # ── 항기생충 ──
    ST("-bendazole", r"bendazole$", "항기생충", "Benzimidazole계 구충제", "β-tubulin 결합 → 포도당 흡수 장애. 효과 서서히, 임신 초기 기형"),
    ST("-mectin / -ectin", r"(mectin|moxidectin)$", "항기생충", "거대고리 락톤계(avermectin · milbemycin)", "글루타메이트 개폐 Cl⁻ 채널 → 이완성 마비. collie·Australian shepherd MDR1 변이 독성",
       [("milbemycin", "milbemycin — 이름은 -mycin이지만 같은 거대고리 락톤계")]),
    ST("-antel", r"antel$", "항기생충", "니코틴 수용체 효현 구충제", "선충 Nn 자극 → 경직성 마비(pyrantel, morantel). levamisole도 같은 기전",
       [("praziquantel", "-quantel — 조충·흡충 약물(Ca²⁺ 투과성↑), 기전이 다름")]),
    # ── 항암 · 면역 ──
    ST("-platin", r"platin$", "항암·면역", "백금 제제", "DNA 가교. cisplatin 신독성·고양이 금기 / carboplatin 골수 억제"),
    ST("-rubicin", r"rubicin$", "항암·면역", "안트라사이클린계", "DNA 삽입 · topoisomerase II 억제. 누적 심근독성, 혈관 외 유출 시 괴사(dexrazoxane)"),
    ST("-taxel", r"taxel$", "항암·면역", "Taxane계", "미세소관 안정화(M기)"),
    ST("-mustine", r"mustine$", "항암·면역", "Nitrosourea계(알킬화제)", "지용성 → 뇌 투과(lomustine, carmustine)"),
    ST("-citabine / -rabine", r"(citabine|rabine)$", "항암·면역", "피리미딘 유사체(항대사제)", "S기 특이. cytarabine · gemcitabine"),
    ST("-trexate", r"trexate$", "항암·면역", "엽산 유사체", "DHFR 억제. leucovorin으로 구제"),
    ST("-nib", r"nib$", "항암·면역", "Tyrosine kinase 억제제", "KIT 등 표적치료 — toceranib, masitinib(비만세포종)",
       [("oclacitinib", "JAK1 억제제 — -citinib, 개 소양증(항암제가 아님)")]),
    ST("-sporine / -limus", r"(sporine|limus)$", "항암·면역", "Calcineurin 억제제(면역억제)", "IL-2 생성 차단. cyclosporine(cyclophilin) · tacrolimus(FKBP12)"),
    # ── 심혈관 · 신장 ──
    ST("-pril", r"pril$", "심혈관·신장", "ACE 억제제", "angiotensin II↓ · bradykinin 분해↓. 고칼륨혈증, 탈수 시 신손상, 임신 금기"),
    ST("-sartan", r"sartan$", "심혈관·신장", "안지오텐신 수용체 차단제(ARB)", "AT1 직접 차단"),
    ST("-olol", r"olol$", "심혈관·신장", "β 차단제", "심박수·수축력↓. 비선택(propranolol)은 기관지 수축 주의, β1 선택(atenolol, metoprolol, esmolol)",
       [("stanozolol", "동화 스테로이드(-zolol이 아니라 -ol)")]),
    ST("-terol", r"terol$", "심혈관·신장", "β2 효현제", "기관지 확장(clenbuterol, formoterol, procaterol). salbutamol·terbutaline은 예외적 이름",
       [("dihydrotachysterol", "-sterol — 비타민 D 유사체(저칼슘혈증 치료제)")]),
    ST("-zosin", r"zosin$", "심혈관·신장", "α1 차단제", "혈관 확장 · 요도 이완(prazosin, terazosin, doxazosin)"),
    ST("-dipine", r"dipine$", "심혈관·신장", "Dihydropyridine계 Ca²⁺ 채널 차단제", "혈관 선택적 확장(amlodipine: 고양이 고혈압 1차)"),
    ST("-thiazide", r"thiazide$", "심혈관·신장", "Thiazide계 이뇨제", "원위세뇨관 Na⁺-Cl⁻ 억제, Ca²⁺ 재흡수↑"),
    ST("-semide / -tanide", r"(semide|tanide)$", "심혈관·신장", "Loop 이뇨제", "Na⁺-K⁺-2Cl⁻ 억제 — 가장 강력(furosemide, torsemide, bumetanide)"),
    ST("-ainide / -afenone", r"(ainide|afenone)$", "심혈관·신장", "Class I 항부정맥제(Na⁺ 채널 차단)", "IB: lidocaine·mexiletine·tocainide / IC: flecainide·propafenone"),
    ST("-arone", r"arone$", "심혈관·신장", "Class III 항부정맥제", "amiodarone — 다중 채널·β 차단, 갑상선·폐·간 독성"),
    ST("-afil", r"afil$", "심혈관·신장", "PDE5 억제제", "sildenafil — 폐동맥 고혈압"),
    ST("-parin / -farin", r"(parin|farin)$", "심혈관·신장", "항응고제", "heparin: antithrombin III 증강(즉시, 해독 protamine) / warfarin: 비타민 K 의존 인자 억제(느림, 해독 vitamin K1)"),
    ST("-kinase", r"kinase$", "심혈관·신장", "혈전 용해제", "streptokinase — plasminogen 활성화(항원성·출혈 위험)"),
    # ── 신경 · 마취 ──
    ST("-caine", r"caine$", "신경·마취", "국소마취제", "Na⁺ 채널 차단. ester형(procaine, tetracaine, benzocaine) / amide형(lidocaine, bupivacaine, mepivacaine)"),
    ST("-flurane", r"flurane$", "신경·마취", "흡입 마취제", "혈액/가스 분배계수↓ → 빠른 유도·회복(desflurane, sevoflurane, isoflurane)"),
    ST("-barbital / -pental", r"(barbital|pental)$", "신경·마취", "Barbiturate계", "GABA_A Cl⁻ 채널 열림 시간↑. 고용량은 직접 개방 → 호흡 억제"),
    ST("-zepam / -zolam", r"(zepam|zolam)$", "신경·마취", "Benzodiazepine계", "GABA_A Cl⁻ 채널 열림 빈도↑(안전역 넓음). 해독 flumazenil"),
    ST("-azine", r"(chlorpromazine|acepromazine|promazine|prochlorperazine|promethazine)$", "신경·마취", "Phenothiazine계", "D2·α1 차단 → 정온·항구토·저혈압. 경련 역치↓",
       [("xylazine", "α2 효현제 — 진정·진통·근이완"), ("hydralazine", "직접 혈관 확장제"), ("piperazine", "구충제(GABA 효현)"),
        ("procarbazine", "항암제(알킬화제)"), ("dacarbazine", "항암제(알킬화제)"), ("sulfamethazine", "sulfonamide 항균제")]),
    ST("-peridol", r"peridol$", "신경·마취", "Butyrophenone계", "D2 차단. haloperidol(항구토·신경이완), droperidol(opioid와 neuroleptanalgesia)",
       [("domperidone", "-peridone — D2 길항 소화관 운동·prolactin↑(butyrophenone 아님)")]),
    ST("-midine / -fidine", r"(medetomidine|detomidine|romifidine|clonidine)$", "신경·마취", "α2 효현제", "진정·진통·근이완, 서맥. 해독 atipamezole·yohimbine",
       [("bunamidine", "조충 구충제"), ("cimetidine", "-tidine — H2 길항제")]),
    ST("-stigmine", r"stigmine$", "신경·마취", "콜린에스터라제 억제제(가역적)", "ACh 분해 억제. neostigmine·pyridostigmine, physostigmine(중추 이행)"),
    ST("-curium / -curonium", r"(curonium|curium|curarine)$", "신경·마취", "비탈분극성 신경근 차단제", "ACh와 Nm 경쟁. 해독 neostigmine + atropine"),
    ST("-tropine", r"tropine$", "신경·마취", "항무스카린제", "atropine, homatropine, eucatropine — 부교감 차단"),
    ST("-triptyline / -ipramine", r"(triptyline|ipramine)$", "신경·마취", "삼환계 항우울제(TCA)", "NE·5-HT 재흡수 차단. clomipramine: 개 분리불안"),
    ST("-xetine / -traline", r"(oxetine|xetine|traline|fluvoxamine)$", "신경·마취", "SSRI", "SERT 선택 차단, 세로토닌 증후군 주의",
       [("methoxamine", "α1 효현제"), ("butoxamine", "β2 길항제")]),
    ST("-fentanil", r"fentanil$|fentanyl$", "신경·마취", "Fentanyl계 opioid", "μ 효현제 — fentanyl(약 100배), carfentanil(약 10,000배, 대동물 불동화·사람 노출 치명적)"),
    ST("-orphine / -orphan", r"(orphine|orphan|orphanol|orphone)$", "신경·마취", "Opioid(morphinan계)", "μ 수용체 → 진통·호흡 억제. 길항제 naloxone",
       [("apomorphine", "도파민 효현 — 진통 없이 구토 유도"), ("dextromethorphan", "진통 효과 없는 진해제")]),
    # ── 소화기 · 호흡기 ──
    ST("-prazole", r"prazole$", "소화기·호흡기", "양성자 펌프 억제제(PPI)", "H⁺/K⁺-ATPase 비가역 억제 — 위산 억제 가장 강력"),
    ST("-tidine", r"tidine$", "소화기·호흡기", "H2 길항제", "위산 분비 억제. cimetidine은 CYP450 억제"),
    ST("-setron", r"setron$", "소화기·호흡기", "5-HT3 길항제", "항구토 — ondansetron, dolasetron"),
    ST("-laner", r"laner$", "항기생충", "Isoxazoline계 외부 기생충 구제제", "곤충·진드기 GABA 개폐 Cl⁻ 채널 차단 — afoxolaner, fluralaner(개 벼룩·진드기, 경구)"),
    ST("-racetam", r"racetam$", "신경·마취", "항경련제(SV2A 결합)", "levetiracetam — 간 대사 적어 상호작용 적음, 개·고양이 간질 보조"),
    ST("-prant", r"prant$", "항염증", "EP4 수용체 길항제(NSAID 아님)", "grapiprant — COX를 억제하지 않고 개 골관절염 통증 완화"),
    ST("-pitant", r"pitant$", "소화기·호흡기", "NK1 길항제", "maropitant — 중추·말초 모두 차단하는 광범위 항구토제"),
    ST("-phylline", r"(phylline|fylline)$", "소화기·호흡기", "Methylxanthine계", "PDE 억제 + 아데노신 길항 → 기관지 이완. 치료 범위 좁음"),
    # ── 호르몬 · 대사 ──
    ST("-sone / -solone / -olone", r"(cortisone|prednisone|prednisolone|triamcinolone|dexamethasone|betamethasone|flumethasone|hydrocortisone|methylprednisolone|fludrocortisone)$", "호르몬·대사",
       "코르티코스테로이드", "항염증 · 면역 억제. cortisone·prednisone은 전구약물(고양이·말은 prednisolone), dexamethasone이 가장 강력",
       [("fluanisone", "Butyrophenone계 신경이완제"), ("trenbolone", "동화 스테로이드(-olone이지만 성호르몬)"), ("methandrostenolone", "동화 스테로이드")]),
    ST("-sterone", r"sterone$", "호르몬·대사", "스테로이드 호르몬", "testosterone(androgen), progesterone(progestin), aldosterone·deoxycorticosterone(mineralocorticoid)"),
    ST("estr-", r"^estr", "호르몬·대사", "Estrogen", "발정·생식관 자극. 개 골수 억제 · 자궁축농증"),
    ST("-thyroxine / -thyronine", r"(thyroxine|thyronine)", "호르몬·대사", "갑상선 호르몬제", "levothyroxine(T4): 개 저하증 1차 / liothyronine(T3)"),
    ST("-thiouracil", r"thiouracil$", "호르몬·대사", "항갑상선제", "peroxidase 억제 → 호르몬 합성 차단. propylthiouracil은 고양이 독성"),
    ST("-tocin / -pressin", r"(tocin|pressin)$", "호르몬·대사", "뇌하수체 후엽 호르몬", "oxytocin: 자궁 수축·유즙 배출 / vasopressin(ADH): 항이뇨"),
    ST("gli- / gly-", r"^(glip|glim|glyb)", "호르몬·대사", "Sulfonylurea(경구 혈당강하제)", "β세포 K-ATP 채널 차단 → 인슐린 분비↑",
       [("glycopyrrolate", "항무스카린제(4차 암모늄)")]),
    # ── 항염증 ──
    ST("-profen", r"profen$", "항염증", "Propionic acid계 NSAID", "비선택적 COX 억제. ibuprofen은 개 독성, carprofen은 개 사용",
       [("naproxen", "propionic acid계지만 이름은 -oxen")]),
    ST("-coxib", r"coxib$", "항염증", "선택적 COX-2 억제제", "위장관 부작용 적음 — deracoxib, firocoxib"),
    ST("-icam", r"icam$", "항염증", "Oxicam계 NSAID", "COX-2 선호(meloxicam, piroxicam)"),
]
