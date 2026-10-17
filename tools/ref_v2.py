"""핵심 정리(AI 작성): 약물군마다 하나의 '📎 핵심 정리' 상자, 계열마다 필요한 경우만 하나.
형식: 항목 목록 — 문자열(글머리표) / {"h": 소제목, "i": [...]} / {"p": 문단} / {"table": [[머리글...], [행...], ...]}
시험에 자주 나오는 비교·기전·주의점만 남기고 기초 설명은 줄였다(교재 원문은 약물 정보 창에서 확인)."""

REF_FAM = {
    "auto": [
        {"h": "자율신경계 지도", "i": [
            "**교감**: 신경절 전 ACh(Nn) → 신경절 후 **NE**(α·β). 예외: 땀샘은 교감이지만 ACh(무스카린), 부신 수질은 epinephrine을 혈중으로 분비",
            "**부교감**: 신경절 전·후 모두 **ACh**(신경절 Nn, 효과기 M)",
            {"table": [["기관", "교감 (수용체)", "부교감 (무스카린)"],
                       ["심장", "심박수·수축력↑ (β1)", "서맥 (M2)"],
                       ["혈관", "수축 (α1), 골격근 혈관 이완 (β2)", "대부분 직접 지배 없음"],
                       ["기관지", "이완 (β2)", "수축·분비↑ (M3)"],
                       ["홍채", "산동 (α1)", "축동 (M3)"],
                       ["위장관 · 방광", "운동 감소 · 배뇨근 이완/괄약근 수축", "운동·분비↑ · 배뇨근 수축"]]},
        ]},
    ],
    "cns": [
        {"h": "수용체 ↔ 대표 약물", "i": [
            {"table": [["수용체", "약물 예", "효과"],
                       ["GABA_A", "benzodiazepine, barbiturate, propofol, alfaxalone / 길항: picrotoxin, bemegride", "진정·마취·항경련 / 경련"],
                       ["NMDA", "ketamine (길항)", "해리성 마취·진통"],
                       ["glycine", "strychnine (길항)", "척수 경련"],
                       ["μ-opioid", "morphine, fentanyl / 길항: naloxone", "진통·진정·호흡 억제"],
                       ["D2", "phenothiazine, butyrophenone, metoclopramide (길항) / apomorphine (효현)", "정온·항구토 / 구토 유발"],
                       ["α2", "xylazine, medetomidine (효현) / yohimbine, atipamezole (길항)", "진정·진통 / 해독"],
                       ["Nm · M", "신경근 차단제 · atropine(길항), bethanechol(효현)", "근이완 · 부교감 차단/자극"]]},
        ]},
    ],
    "circ": [
        {"h": "혈압 조절과 약물 작용점", "i": [
            "**혈압 = 심박출량 × 말초 혈관 저항**. 심박출량 = 심박수 × 1회 박출량(전부하·수축력·후부하)",
            {"table": [["조절 요소", "낮추는 약물"],
                       ["심박수·수축력", "β 차단제, Ca²⁺ 채널 차단제(verapamil, diltiazem)"],
                       ["후부하(혈관 수축)", "α1 차단제, 혈관 확장제(hydralazine, amlodipine, nitroprusside), ACE 억제제"],
                       ["전부하(혈액량)", "이뇨제, 정맥 확장제(nitroglycerin), ACE 억제제"],
                       ["RAAS", "ACE 억제제, ARB, aliskiren, spironolactone"]]},
        ]},
    ],
    "endo": [
        {"h": "호르몬 조절 지도", "i": [
            "시상하부 방출호르몬 → 뇌하수체 전엽 → 표적 샘(갑상선·부신·생식샘) → **음성 되먹임**. 외인성 호르몬을 쓰면 내인성 분비가 억제되어 표적 샘이 위축(예: 장기 glucocorticoid → 부신 위축)",
            {"table": [["기관", "장애"],
                       ["뇌하수체 전엽", "저하증, GH 과다(말단 거대증), ACTH 과다(Cushing), prolactin 과다"],
                       ["뇌하수체 후엽", "vasopressin 결핍 → **요붕증**"],
                       ["갑상선", "개·말: 저하증 흔함 / 고양이: 항진증 흔함"],
                       ["부갑상선", "저하증 → 저칼슘혈증·경련 / 항진증 → 고칼슘혈증"],
                       ["부신", "저하증(**Addison병**) / 항진증(**Cushing병**, 뇌하수체 의존 80~85 %) / 크롬친화성세포종"],
                       ["췌장", "당뇨병(저인슐린혈증) / 저혈당(insulinoma, 인슐린 과다)"]]},
        ]},
    ],
    "infect": [
        {"h": "항생제 계열별 주의사항", "i": [
            {"table": [["계열", "표적", "대표 주의점"],
                       ["β-lactam", "세포벽(PBP)", "과민반응(교차), 내성(β-lactamase, MRSA)"],
                       ["aminoglycoside", "30S", "신독성·이독성·신경근 차단, 혐기균 무효"],
                       ["tetracycline", "30S", "치아·뼈 침착(어린 동물·임신), 고양이 식도 협착"],
                       ["macrolide", "50S", "tilmicosin 심독성, erythromycin 장 운동 촉진"],
                       ["lincosamide", "50S", "초식동물 치명적 대장염"],
                       ["chloramphenicol", "50S", "식용동물 금지, 골수 억제"],
                       ["fluoroquinolone", "DNA gyrase", "어린 동물 연골 손상, 고양이 망막 변성"],
                       ["sulfonamide + trimethoprim", "엽산 합성 순차 차단", "결정뇨, 개 KCS"],
                       ["metronidazole", "DNA 손상", "고용량 신경독성"]]},
        ]},
    ],
    "parasite": [
        {"h": "기생충별 대표 약물", "i": [
            {"table": [["기생충", "대표 약물"],
                       ["선충", "benzimidazole, levamisole·pyrantel·morantel, ivermectin 등 거대고리 락톤, piperazine, emodepside"],
                       ["조충", "praziquantel, niclosamide, arecoline, bunamidine"],
                       ["흡충", "praziquantel(일부), bithionol, oxyclozanide, nitroxynil, albendazole"],
                       ["심장사상충", "예방: ivermectin·milbemycin·moxidectin·selamectin / 성충: melarsomine"],
                       ["콕시듐", "amprolium, sulfaquinoxaline, monensin·salinomycin·lasalocid, clopidol, nicarbazine"],
                       ["외부 기생충", "유기인, carbamate, pyrethroid, ivermectin, selamectin, 유황, benzyl benzoate"]]},
            "**안전성**: 유기인·carbamate는 숙주 콜린에스터라제도 억제(atropine) / ivermectin은 **collie·Australian shepherd(MDR1 변이)** 독성 / monensin·salinomycin은 **말·개 독성** / permethrin은 **고양이 독성**",
        ]},
    ],
    "onco": [
        {"h": "치료 원칙", "i": [
            "**항암**: 작용점이 다른 약물 병용, 골수 억제 **nadir는 투여 후 5~10일**, 항구토제·수액 지지요법, doxorubicin·vincristine은 **혈관 외 유출 시 괴사**",
            "**면역억제**: glucocorticoid가 기본 → 반응 부족·부작용 시 cyclosporine, azathioprine, mycophenolate 병용·교체, 반응하면 **서서히 감량**. 공통 위험: 감염·종양·골수 억제",
        ]},
    ],
}

REF_CAT = {
    # ── 신경계 ──
    "adrenergic": [
        {"h": "수용체별 효과", "i": [
            {"table": [["수용체", "주요 효과 · 약물"],
                       ["α1", "혈관 수축(혈압↑), 점막 수축, 산동, 방광 괄약근 수축 — phenylephrine"],
                       ["α2", "NE 방출 억제(되먹임) + 중추 진정·진통·근이완 — xylazine, medetomidine, clonidine"],
                       ["β1", "심박수·수축력↑, renin 분비 — dobutamine"],
                       ["β2", "기관지·자궁·골격근 혈관 이완 — salbutamol, terbutaline, clenbuterol"],
                       ["β3", "지방 분해"]]},
            "수용체 선택성은 **용량이 올라가면 떨어짐**",
        ]},
        {"h": "핵심 포인트", "i": [
            "**합성·종료**: tyrosine → DOPA → dopamine → NE → epinephrine, 속도 제한 효소 **tyrosine hydroxylase**(metyrosine 억제). 작용 종료는 **재흡수(NET)**가 가장 크고, 분해는 MAO·COMT",
            "**직접 작용**(phenylephrine, isoproterenol, dobutamine) / **간접**(tyramine, amphetamine, cocaine: NE 유리·재흡수 억제) / **혼합**(ephedrine, metaraminol). reserpine으로 NE를 고갈시키면 간접 작용 약물만 효과 소실, 반복 투여 시 **tachyphylaxis**",
            "**α2 효현제**: 서맥·호흡 억제·**고혈당**·반추동물 고창/침 분비, **소**는 매우 민감(자궁 수축↑). 길항제 yohimbine, tolazoline, atipamezole",
            "**α 차단제**: phenoxybenzamine은 α1·α2 **비가역** 차단(크롬친화성세포종 수술 전), prazosin 계열은 α1 선택. **epinephrine reversal**: α 차단 후 epinephrine → β2 혈관 확장만 남아 혈압 하강",
            "**β 차단제**: 비선택(propranolol, nadolol, timolol, pindolol은 ISA), β1 선택(atenolol, metoprolol, esmolol 초단시간), sotalol은 class III 병행. 고양이 비대성 심근증·갑상선 항진, 비선택 약물은 **기관지 수축**·당뇨 동물 **저혈당 은폐** 주의",
            "**신경 말단 약물**: reserpine(저장 고갈), guanethidine류(NET로 흡수되어 유리 억제), bretylium(항부정맥 병행), 6-OHDA(말단 파괴, 연구용)",
        ]},
    ],
    "cholinergic": [
        {"h": "수용체와 증상", "i": [
            "ACh: choline + acetyl-CoA(ChAT) 합성 → **AChE**가 분해. **M1** 신경·위 / **M2** 심장(서맥) / **M3** 평활근 수축·분비·축동 / **Nn** 신경절 / **Nm** 신경근 접합부",
            "부교감 항진 = **SLUDGE**(타액·눈물·배뇨·배변·서맥·기관지 분비·축동·구토) + 근섬유속성 경련",
        ]},
        {"h": "약물군별 포인트", "i": [
            "**콜린 에스터**: **bethanechol**(AChE에 분해 안 됨, 요저류·장 무력증), carbachol(M + N), methacholine / **alkaloid**: pilocarpine(침 분비·녹내장 축동), arecoline(구충·설사 유도)",
            "**AChE 억제제**: 가역(physostigmine, neostigmine, pyridostigmine, **edrophonium: 중증근무력증 진단**, demecarium: 녹내장) / **비가역 유기인**(parathion, malathion, DFP, echothiophate). 유기인 중독 해독 = **atropine + 2-PAM**(시간이 지나면 aging으로 효과 감소)",
            "**항무스카린제**: atropine(3차 아민, 중추 작용), scopolamine(진정·멀미), **glycopyrrolate**(4차 암모늄, 중추 이행 적어 마취 전 서맥·분비 억제), butylscopolamine·propantheline·aminopentamide(진경), ipratropium(기관지), tropicamide(단시간 산동), oxybutynin(방광). 부작용: 구강 건조·빈맥·**장 마비(말)**·안압↑·분비물 점조화",
            "**Nn**: nicotine은 소량 흥분·고용량 지속 탈분극 차단(**이상성**). levamisole·morantel·pyrantel은 선충 Nn을 자극해 **경직성 마비**. 신경절 차단제(hexamethonium 등)는 현재 임상 사용 거의 없음",
        ]},
        {"h": "신경근 차단제 두 가지", "i": [
            {"table": [["구분", "비탈분극성(경쟁적)", "탈분극성"],
                       ["약물", "d-tubocurarine, pancuronium, vecuronium, atracurium …", "succinylcholine, decamethonium"],
                       ["기전", "ACh와 Nm 경쟁 → 이완성 마비", "Nm 지속 탈분극 → 처음 **fasciculation** 후 마비"],
                       ["해독", "**neostigmine·edrophonium** + atropine", "**불가**(AChE 억제는 오히려 악화), 혈장 cholinesterase가 분해"],
                       ["특징", "d-tubocurarine 히스타민 유리·저혈압, gallamine 빈맥, **atracurium은 Hofmann 분해**", "고칼륨혈증, 돼지 악성 고열"]]},
            "마비 순서: 눈·얼굴 → 사지 → 호흡근(마지막), 회복은 반대. **진통·진정 효과가 없으므로** 마취와 인공호흡 하에서 사용",
        ]},
        {"h": "신경 독소", "i": [
            "**botulinum toxin**: SNARE 단백질 분해 → ACh 방출 차단(이완성 마비) / **α-bungarotoxin**: Nm에 비가역 결합 / **β-bungarotoxin**: ACh 유리 억제 / **black widow venom**: ACh 폭발적 유리 후 고갈",
        ]},
    ],
    "cns_stim": [
        "**methylxanthine**(caffeine, theophylline, theobromine): 아데노신 길항 + PDE 억제 → 각성·호흡·심장 자극·이뇨. 초콜릿(theobromine) 중독은 개에서 흔함(구토·빈맥·경련)",
        "**doxapram**: 호흡 중추·말초 화학수용체 자극 → 마취 후 호흡 회복·신생동물 소생",
        "**strychnine**: 척수 **glycine 수용체 길항** → 작은 자극에도 경직성 경련 / **picrotoxin, bemegride, leptazol**: GABA_A Cl⁻ 채널 차단 → 경련(과거 barbiturate 해독, 현재 거의 안 씀)",
        "중추 흥분제는 용량이 높으면 **경련 → 중추 억제(소진)** 순서",
    ],
    "cns_depressant": [
        {"h": "GABA_A 작용 방식", "i": [
            "**benzodiazepine**: Cl⁻ 채널 **열리는 빈도**↑(GABA 필요 → 안전역 넓음, 해독 **flumazenil**) / **barbiturate**: **열려 있는 시간**↑(고용량은 GABA 없이도 개방 → **호흡 억제로 치명적**) / chloral hydrate: 대사산물 trichloroethanol이 GABA_A 증강",
            "**phenothiazine**(acepromazine 등): D2 + α1 차단 → 정온·항구토·**저혈압**·체온 저하, 경련 역치↓, 수컷 말 음경 탈출 / **butyrophenone**: azaperone(돼지 진정), droperidol·fluanisone은 opioid와 neuroleptanalgesia",
        ]},
        {"h": "항경련제", "i": [
            "**phenobarbital**(개 간질 1차), primidone은 phenobarbital로 대사 / **phenytoin**: Na⁺ 채널 불활성 연장, **고양이 대사 느려 독성** / diazepam·midazolam·lorazepam: **중첩 발작 응급** / KBr: 장기 보조(고양이 호흡기 부작용) / gabapentin: Ca²⁺ 채널 α2δ 결합, 신경병증성 통증",
        ]},
        {"h": "근이완제 3종 비교", "i": [
            {"table": [["종류", "작용 부위", "예"],
                       ["신경근 차단제", "신경근 접합부(종판)", "pancuronium, atracurium, succinylcholine"],
                       ["중추성 근이완제", "척수·뇌간 다중 시냅스 반사(중간 신경원) 억제, **횡격막 마비 위험 작음**", "guaifenesin, methocarbamol, mephenesin"],
                       ["직접 작용", "근소포체 ryanodine 수용체 억제", "dantrolene(악성 고열)"]]},
            "guaifenesin은 말 마취 유도에 쓰이며 ketamine + xylazine과 섞은 ‘triple drip’",
        ]},
    ],
    "analgesic": [
        "**μ·κ·δ**는 G단백(Gi/o) 수용체 → cAMP↓, K⁺ 유출↑(과분극), 전시냅스 Ca²⁺↓ → 통증 전달물질 방출↓",
        "주 작용: 진통·진정·**호흡 억제**·서맥·**변비**·진해·구토(개: CTZ). **종 차이**: 개는 축동·진정, **고양이·말·소·돼지는 고용량에서 흥분**. 길항제 **naloxone**은 작용이 짧아 재투여 필요",
        "**morphine** 표준 / **fentanyl** 약 100배(패치·CRI) / **etorphine** 초강력(대동물 불동화, 사람 노출 시 치명적) / **butorphanol** κ 효현·μ 길항(천장 효과, 호흡 억제 적음) / **loperamide·diphenoxylate** 장 μ 수용체 → 지사(loperamide는 P-gp 기질 → **collie 신경독성**) / **apomorphine**은 도파민 효현으로 구토 유도(진통 없음, 구토 유발제 참조)",
        "**다중 양식 진통**: opioid + NSAID + α2 효현제 + 국소마취제 + ketamine(NMDA 길항, wind-up 방지) + gabapentin",
    ],
    "anesthetic": [
        {"h": "마취의 구성", "i": [
            "**전마취**(acepromazine, α2, opioid, benzodiazepine, atropine/glycopyrrolate) → **유도**(propofol, ketamine+diazepam, thiopental, alfaxalone, etomidate) → **유지**(isoflurane, sevoflurane). 여러 약물로 용량을 나눠 부작용 감소",
        ]},
        {"h": "주사 마취제", "i": [
            "**thiopental**: 초단시간 barbiturate, 재분포로 빨리 깸, 알칼리성(혈관 외 유출 시 괴사), 지방이 적은 **sighthound** 회복 지연 / **propofol**: GABA_A, 회복 빠름, 지질 유제(개봉 후 폐기), 고양이 반복 투여 시 Heinz body / **ketamine**: NMDA 길항 **해리성**, 근긴장 유지·진통, 단독 시 경직 → diazepam·xylazine 병용, 고양이 신배설 / **alfaxalone**: 신경 스테로이드 / **etomidate·metomidate**: 심혈관 안정, **부신 억제**",
        ]},
        {"h": "흡입 마취제", "i": [
            "**MAC**이 작을수록 강력. **혈액/가스 분배계수**가 작을수록 유도·회복 빠름: desflurane(0.4) ≈ N₂O(0.5) < sevoflurane(0.7) < isoflurane(1.4) < halothane(2.4) ≪ methoxyflurane(약 12)",
            "**halothane**: catecholamine 예민화 부정맥·간독성 / **methoxyflurane**: 불소 이온 **신독성** / **N₂O**: 약한 마취·진통, 폐쇄 공간(장 가스·기흉) 팽창, 회복 시 **확산 저산소증** → 순산소 / **tricaine(MS-222)**: 어류·양서류",
        ]},
        {"h": "국소마취제", "i": [
            "신경막 **Na⁺ 채널을 안쪽에서 차단**. 차단 순서 **통증 → 온도 → 촉각 → 압각 → 운동**. 염증 조직은 pH가 낮아 효과 감소",
            "**ester형**(procaine, tetracaine, benzocaine): 혈장 cholinesterase 분해, PABA 알레르기 / **amide형**(lidocaine, bupivacaine, mepivacaine, ropivacaine, prilocaine): 간 대사 / **epinephrine 병용**으로 작용 연장(귀·꼬리·발가락 **허혈 괴사로 금지**) / **bupivacaine 심독성** / **benzocaine 고양이 methemoglobinemia**",
        ]},
    ],
    "antidepressant": [
        "**모노아민 가설**: NE·5-HT·도파민을 늘려 작용, 효과는 **2~6주** 후. 수의학에서는 분리불안·강박·공격성·마킹 같은 행동 문제에 사용",
        "**MAOI**: 말단 NE·5-HT·도파민 저장↑ → 방출↑. **selegiline**은 저용량 MAO-B 선택 → 개 인지기능장애. 위험: tyramine 음식 **고혈압 위기**, **세로토닌 증후군**(SSRI·TCA·meperidine·tramadol·dextromethorphan 금기), 휴약기 약 2주, amitraz 주의",
        "**TCA**(NET·SERT 차단): **clomipramine**(5-HT 우세, 개 분리불안), amitriptyline, imipramine(NE 우세), doxepin(H1 차단). 부작용: 항무스카린, α1 차단, 진정, **과량 시 심장 전도 장애**, 경련 역치↓",
        "**SSRI**: SERT만 선택 차단, TCA보다 안전(fluoxetine: 고양이 스프레이·공격성, 활성 대사산물 반감기 길어 교체 시 긴 휴약기). **progestin**(megestrol, medroxyprogesterone): 마킹·공격성, 자궁축농증·당뇨·유선 종양 위험으로 마지막 선택",
    ],
    "emetic": [
        "**중추성**(CTZ): **apomorphine**(D2 효현, 개) / **xylazine**(α2, **고양이**; apomorphine은 고양이에서 약함) / **국소성**(위 점막 자극): 식염수, sodium carbonate, 1 % copper sulfate, emetine(ipecac)",
        "**금기**: 부식성 물질·석유 제품(식도 손상·흡인성 폐렴), 의식 저하·경련·이미 구토 중, 섭취 후 오랜 시간 경과. 독극물 섭취 후 **약 2시간 이내**에만 유효",
    ],
    # ── 오타코이드 · 염증 ──
    "histamine_serotonin": [
        {"h": "히스타민", "i": [
            "비만세포·호염기구의 탈과립(IgE)으로 방출. **H1**: 평활근 수축·투과성↑·가려움·구토(전정) / **H2**: 위산 분비↑·심장 자극 / H3: 신경 말단 되먹임",
            "**생리학적 길항제**: **epinephrine**은 α1 수축 + β2 기관지 이완으로 **아나필락시스 1차 선택**",
            "**H1 길항제**: 1세대(diphenhydramine, promethazine 등)는 중추 이행으로 **진정·항무스카린**(멀미·구토에도 사용), 2세대(astemizole, terfenadine)는 **QT 연장**으로 퇴출 / **H2 길항제**: cimetidine은 **CYP450 억제** / **cromolyn**: 탈과립 억제 **예방약**(이미 시작된 반응에는 무효)",
        ]},
        {"h": "세로토닌(5-HT)", "i": [
            {"table": [["수용체", "약물", "용도"],
                       ["5-HT1A (Gi)", "buspirone (부분 효현)", "항불안"],
                       ["5-HT2 (Gq)", "cyproheptadine, ketanserin (길항)", "식욕 촉진, 세로토닌 증후군 치료"],
                       ["5-HT3 (이온 채널)", "ondansetron, dolasetron (길항)", "항구토"],
                       ["5-HT4 (Gs)", "cisapride, metoclopramide (효현)", "위장관 운동 촉진"]]},
            "**세로토닌 증후군**: SSRI·TCA·MAOI·tramadol·meperidine 병용 시 진전·고열·빈맥·경련 → **cyproheptadine**",
        ]},
    ],
    "prostaglandin": [
        "**아라키돈산 경로**: 인지질 →(**PLA2**, glucocorticoid가 억제)→ 아라키돈산 → **COX**(PGE2, PGF2α, PGI2, **TXA2**; NSAID 억제) / **LOX**(leukotriene)",
        {"table": [["PG", "작용"],
                   ["PGE", "혈관 확장, 위산 분비 억제·점막 보호, 장 운동↑, 기관지 확장, 자궁 수축, 발열·발통"],
                   ["PGF2α", "혈관·기관지 수축, 자궁 수축, **황체 퇴행·배란**(성주기 조절)"],
                   ["PGI2", "혈소판 응집 억제, 혈관 확장"],
                   ["TXA2", "혈소판 응집·혈관 수축(aspirin이 억제)"]]},
        "**PGF2α(dinoprost)·cloprostenol**: 황체 퇴행 → 발정 동기화·유산 유도·자궁축농증 치료 / **misoprostol**: 산 분비 억제 + 점액 증가(NSAID 궤양 예방, **임신 금기**)",
    ],
    "corticosteroid": [
        {"h": "기전", "i": [
            "세포질 수용체 → 핵 → **유전자 발현 조절**(효과가 수 시간 뒤). **lipocortin** 유도 → PLA2 억제 → PG·LT 모두 감소, **NF-κB 억제** → 염증 유전자↓, 백혈구 이동 억제, **림프구 감소(면역 억제)**",
        ]},
        {"h": "합성 corticoid 비교", "i": [
            {"table": [["약물", "항염증(cortisol=1)", "무기질 작용", "작용 시간"],
                       ["hydrocortisone(cortisol)", "1", "있음", "단(8~12h)"],
                       ["prednisone·prednisolone", "약 4", "약함", "중(12~36h)"],
                       ["methylprednisolone·triamcinolone", "약 5", "거의 없음", "중"],
                       ["dexamethasone·betamethasone", "약 25~30", "없음", "장(>48h)"]]},
            "**cortisone·prednisone**은 간에서 활성형으로 전환되는 전구약물 → **고양이·말**은 prednisolone 사용",
        ]},
        {"h": "부작용 · 내분비", "i": [
            "다음·다뇨·다식, **의인성 Cushing**, 상처 치유 지연, 감염 취약, 당뇨 악화, 위궤양(**NSAID 병용 금지**), 말 **laminitis**, 임신 동물 유산(소 분만 유도에 dexamethasone). **장기 투여 후 갑자기 중단하면 부신 위기** → 서서히 감량",
            "**mineralocorticoid**(aldosterone): 신세뇨관 Na⁺·수분 재흡수↑, K⁺ 배설 / Addison병 대치: **fludrocortisone**, deoxycorticosterone",
            "**Cushing 치료(합성 억제)**: **trilostane**(3β-HSD 억제, 개 1차), **mitotane**(부신 피질 세포 파괴), ketoconazole·metyrapone",
        ]},
    ],
    "nsaid": [
        "**COX 억제** → PG·TXA2 감소 = 진통·해열·항염 + 혈소판 응집↓. **COX-1**: 항상성(위점막·혈소판·신 혈류) / **COX-2**: 염증 때 유도 → COX-1 억제가 위장관·신장 부작용의 원인, **deracoxib·firocoxib**(선택적 COX-2)는 위장관 부작용 적음, tepoxalin은 COX + 5-LOX 이중. **aspirin은 비가역**(아세틸화), 나머지는 가역",
        "**부작용**: 위장관 궤양·출혈, **신독성**(탈수·저혈압·마취 중 위험), 간독성. NSAID끼리·corticosteroid와 **병용 금지**, 교체 시 휴약기",
        "**종 특이성**: **고양이**는 glucuronide 포합이 약해 aspirin 반감기↑, **acetaminophen 금기**(methemoglobinemia·Heinz body·간독성; 개도 주의) / **naproxen·ibuprofen**은 개 중독 위험 / meloxicam 고양이 반복 투여 시 신장 위험 / **flunixin** 말·소 / **phenylbutazone** 말",
        "**기타**: DMSO(자유 라디칼 제거·흡수 촉진), PSGAG·hyaluronate(관절 연골 보호·윤활)",
    ],
    # ── 순환 · 신장계 ──
    "inotrope": [
        {"h": "심부전 치료 목표와 약물", "i": [
            {"table": [["목표", "약물"],
                       ["전부하 감소(울혈 해소)", "furosemide, spironolactone, nitroglycerin"],
                       ["후부하 감소", "ACE 억제제, hydralazine, amlodipine, nitroprusside"],
                       ["수축력 증가", "pimobendan, digoxin, dobutamine, dopamine, amrinone·milrinone"],
                       ["신경호르몬 차단", "ACE 억제제, spironolactone"]]},
        ]},
        "**digoxin**: Na⁺/K⁺-ATPase 억제 → 세포 내 Ca²⁺↑ → 수축력↑, 미주 긴장↑(방실 전도 지연). **치료 범위 좁음**: 독성(구토·부정맥), **저칼륨혈증이 독성 증가**, 신 배설(신부전 위험)",
        "**pimobendan**: PDE3 억제 + 수축 단백 **Ca²⁺ 감수성↑**(inodilator, 산소 소모 증가 적음) / **dobutamine**(β1), **dopamine**(저용량 D1 신혈관 확장 → 중간 β1 → 고용량 α 수축): 급성기 정맥 지속 투여",
    ],
    "antiarrhythmic": [
        {"h": "활동전위와 Vaughan-Williams 분류", "i": [
            "**0상** Na⁺ 유입 탈분극 → 1상 → **2상** Ca²⁺ 유입(평탄) → **3상** K⁺ 유출 재분극 → **4상** 자동능",
            {"table": [["Class", "표적", "효과", "예"],
                       ["IA", "Na⁺ + K⁺ 채널", "활동전위 연장, QRS·QT 연장", "quinidine, procainamide, disopyramide"],
                       ["IB", "Na⁺ 채널(불활성 상태)", "활동전위 **단축**, 허혈 조직 선택", "lidocaine, mexiletine, phenytoin"],
                       ["IC", "Na⁺ 채널 강한 차단", "전도 크게 지연", "flecainide, propafenone"],
                       ["II", "β 수용체", "자동능↓, 방실 전도↓", "propranolol, metoprolol, esmolol"],
                       ["III", "K⁺ 채널", "활동전위·불응기 연장", "amiodarone, sotalol, bretylium"],
                       ["IV", "L형 Ca²⁺ 채널", "SA·AV 결절 억제", "verapamil, diltiazem"],
                       ["기타", "—", "—", "digoxin(미주 긴장↑), adenosine(AV 결절 일시 차단)"]]},
        ]},
        "**상심실성 빈맥**: II·IV, digoxin, adenosine / **심실성**: **lidocaine(개 1차, 고양이는 민감)**, mexiletine, procainamide, sotalol. **quinidine**: 말 심방세동 전환",
        "**amiodarone**: 다중 채널 + β 차단, 요오드 포함 → 갑상선·폐·간 독성 / **adenosine**: 반감기 약 10초, 발작성 상심실성 빈맥 / **IC군**은 심근경색 후 사망률↑(CAST) → 구조적 심질환 주의",
    ],
    "vasodilator": [
        "**협심증** = 심근 산소 수요 > 공급. 약물은 전부하·후부하·심박수↓ 또는 관상동맥 혈류↑. 수의학에서는 협심증보다 **심부전·고혈압**에 주로 사용",
        "**nitrate**: NO 공여 → cGMP↑ → **정맥 확장 위주**(전부하↓), 연속 사용 시 **내성** / **nitroprusside**: 동·정맥 모두 확장, 응급 폐부종·고혈압 위기 정맥 지속 투여, **시안화물 독성** / **hydralazine**: 동맥 직접 이완(반사성 빈맥·RAAS 활성) / **minoxidil**: K⁺ 채널 개방 → 강력한 동맥 확장",
        "**Ca²⁺ 채널 차단제**: dihydropyridine(nifedipine, **amlodipine**)은 혈관 선택 → 확장, verapamil은 심장 억제, diltiazem은 중간. verapamil·diltiazem + β 차단제 병용 시 심 억제 증가",
        "**고양이 고혈압**: 만성 신부전·갑상선 항진증에 속발(망막 박리·뇌출혈). **amlodipine 1차**, ACE 억제제·β 차단제(atenolol) 병용",
    ],
    "ras": [
        "신장 **renin**(저혈압·저Na⁺·β1) → angiotensinogen → **Ang I** → **ACE** → **Ang II**(AT1: 혈관 수축, **aldosterone**, ADH, 교감 활성, 리모델링). ACE = kininase II → **bradykinin 분해**",
        "**ACE 억제제**(captopril, enalapril, lisinopril, benazepril): Ang II 생성↓ + bradykinin 분해↓ → 심부전·고혈압·단백뇨 / **ARB**(losartan 등): AT1 직접 차단 / **aliskiren**: renin 직접 억제",
        "부작용: 저혈압, **고칼륨혈증**, 탈수 시 **급성 신손상**(사구체 출구 세동맥 이완), **임신 금기**",
    ],
    "diuretic": [
        {"h": "네프론에서 작용 부위", "i": [
            {"table": [["부위", "약물", "기전"],
                       ["근위세뇨관", "탄산탈수효소 억제제, mannitol", "HCO₃⁻·Na⁺ 재흡수 억제 / 삼투압"],
                       ["헨레고리 상행각", "**loop**(furosemide, bumetanide, torsemide, ethacrynic acid)", "Na⁺-K⁺-2Cl⁻ 억제 — **가장 강력**"],
                       ["원위세뇨관", "**thiazide**", "Na⁺-Cl⁻ 억제, Ca²⁺ 재흡수↑"],
                       ["집합관", "**K⁺ 보존성**(spironolactone, triamterene, amiloride)", "aldosterone 길항 / ENaC 차단"]]},
        ]},
        "**loop**: 급성 폐부종·심부전 1차, 저칼륨혈증·탈수·이독성·Ca²⁺ 배설↑ / **thiazide**: 고혈압·부종, **Ca²⁺ 재흡수↑**(고칼슘혈증, 요붕증 역설적 항이뇨), 고혈당 / **K⁺ 보존성**: 고칼륨혈증(ACE 억제제 병용 주의)",
        "**삼투성**(mannitol, DMSO): 뇌압·안압 감소, **심부전 금기** / **탄산탈수효소 억제제**: 대사성 산증, 녹내장 / **수은 이뇨제**: 독성으로 사용 안 함",
        "**산성화**(NH₄Cl 등): 스트루바이트 결석 예방·용해 / **알칼리화**(citrate, bicarbonate): 산성 약물(aspirin 등) 배설 촉진",
    ],
    "hemostasis": [
        {"h": "응고와 항응고제", "i": [
            "**비타민 K 의존 인자**: II, VII, IX, X. **warfarin·dicumarol**: 비타민 K epoxide reductase 억제, **작용 발현 느림** / dicumarol은 곰팡이 핀 sweet clover(소 출혈), **살서제 중독** 해독 **vitamin K1**(효과 발현 6~12시간, 장기 작용 살서제는 3~4주 치료)",
            "**heparin**: antithrombin III 증강 → thrombin·Xa 불활성화, **즉시 작용**, 해독 **protamine** / 채혈용: citrate·oxalate·EDTA는 Ca²⁺ 킬레이트(citrate: 응고 검사·수혈, EDTA: 혈구 검사), fluoride는 혈당 보존, hirudin은 thrombin 직접 억제",
            "**작용 증가**: 단백 결합 경쟁(aspirin, phenylbutazone, sulfonamide), 대사 억제(cimetidine, metronidazole, disulfiram, TMP-SMX) / **감소**: 간 효소 유도(rifampin, glutethimide), 흡수 방해(cholestyramine) → warfarin은 PT/INR 모니터링",
        ]},
        {"h": "혈소판 · 섬유소 용해", "i": [
            "**aspirin**: COX-1 **비가역** → TXA₂↓, 혈소판 수명(약 1주) 지속, 고양이 **대동맥 혈전색전증** 예방(저용량) / **clopidogrel**: 전구약물, **P2Y12** 비가역 차단 / **streptokinase**: plasminogen → plasmin → fibrin 분해(항원성, 출혈 위험)",
        ]},
    ],
    # ── 호흡기계 ──
    "resp_secretion": [
        "**충혈 제거제**: α1 효현제(phenylephrine, pseudoephedrine)는 비점막 혈관 수축(**pseudoephedrine은 개·고양이 독성 위험**), 1세대 H1 항히스타민은 알레르기성 비염 분비 감소",
        "**거담제**: guaifenesin은 기도 분비를 늘려 점액을 묽게, **ipecac**(구역 반사), **KI·NaI**(기도 분비↑, 장기 시 요오드중독)",
        "**점액 용해제**: **N-acetylcysteine**는 점액 당단백 S–S 결합을 끊어 점도↓(+ 아세트아미노펜 해독, 글루타티온 전구체) / **bromhexine·dembrexine**은 묽은 점액 분비↑",
    ],
    "resp_cough_bronchodilator": [
        {"h": "증상별 선택", "i": [
            {"table": [["증상", "약물 계열", "예"],
                       ["마른 기침", "중추성 진해제", "butorphanol, hydrocodone, codeine, dextromethorphan"],
                       ["습성 기침", "거담제·점액 용해제(진해제는 피함)", "guaifenesin, N-acetylcysteine, bromhexine"],
                       ["기관지 수축(천식·말 RAO)", "기관지 이완제 + 항염증", "salbutamol(흡입), clenbuterol, aminophylline, corticosteroid"],
                       ["폐동맥 고혈압", "PDE5 억제제", "sildenafil"],
                       ["마취 후 호흡 억제", "호흡 자극제", "doxapram"]]},
        ]},
        "**진해**: 중추성 opioid는 기침 중추 억제, **dextromethorphan·noscapine**은 진통·호흡 억제 적은 비마약성, 말초성 benzonatate는 폐 신장 수용체 둔감화. **습성 기침·화농성 폐렴에는 진해제 금지**",
        "**β2 효현제**: Gs → cAMP↑ → 기관지 이완(흡입이 부작용 적음) / **methylxanthine**: PDE 억제 + 아데노신 길항, **치료 범위 좁음**(aminophylline = theophylline 수용성 염) / **항무스카린제**: 분비물이 끈끈해질 수 있음",
        "**sildenafil**: PDE5 억제 → cGMP↑ → 폐혈관 이완 / **surfactant**: 폐포 표면장력 감소, 미숙 신생동물 호흡곤란증후군",
    ],
    # ── 소화기계 ──
    "gi_acid": [
        "위벽세포 **H⁺/K⁺-ATPase(양성자 펌프)**가 산 분비, 자극: **histamine(H2)**, **ACh(M3)**, **gastrin**. 억제력: **PPI(비가역) > H2 길항제 > 항콜린제**",
        "**제산제**: Al은 변비, Mg는 설사 → 혼합제 / CaCO₃·bicarbonate는 반동성 산 분비 가능 / **sucralfate**: 산성에서 중합되어 궤양에 보호막(다른 약과 시간 간격) / **misoprostol**: PGE1 유도체(NSAID 궤양 예방, 임신 금기)",
    ],
    "antiemetic": [
        {"h": "구토 경로와 약물", "i": [
            {"table": [["경로", "수용체", "약물"],
                       ["CTZ(뇌혈관장벽 밖)", "D2, 5-HT3, NK1, μ-opioid, α2", "phenothiazine, metoclopramide, ondansetron, maropitant"],
                       ["전정기관(멀미)", "H1, M", "diphenhydramine, dimenhydrinate, scopolamine"],
                       ["위장관 미주 구심성", "5-HT3", "ondansetron, dolasetron"]]},
            "**종 차이**: 개는 D2(apomorphine 유도), **고양이는 α2**(xylazine 유도)에 민감",
            "**maropitant(NK1 길항)**: 중추·말초 경로를 모두 차단하는 광범위 항구토제 / 구토 원인(이물·폐색·독소)을 먼저 확인, **장 폐색 시 metoclopramide 등 prokinetic 금기**",
        ]},
    ],
    "gi_motility": [
        "**완화제**: 삼투성(**lactulose**: 비흡수 이당류, 대장 세균 발효 → 변 연화, **간성 뇌증**에서 NH₃를 NH₄⁺로 가둠 / PEG / 염류 설사제 Na₂SO₄·MgSO₄: 소에서 반추위·장 내용물 이동), 그 외 팽창성(psyllium)·자극성(bisacodyl, castor oil)·윤활성(mineral oil: 흡인·지용성 비타민 흡수↓)",
        "**prokinetic**: cisapride(5-HT4 효현), metoclopramide(D2 길항 + 5-HT4 효현), erythromycin(저용량 **motilin 효현**), bethanechol·neostigmine(ACh↑) / **기계적 장 폐색에는 금기**",
        "**식욕 촉진**: cyproheptadine(5-HT 길항), mirtazapine(α2 + 5-HT3 길항, 고양이 경피 제제), diazepam·oxazepam / **dirlotapide**: 장 MTP 억제 → 지방 흡수↓·포만감↑(개 비만)",
    ],
    # ── 대사 · 내분비 ──
    "pituitary": [
        "**GH**: IGF-1을 통해 성장·비유량 증가(sometribove = rBST) / **PMSG(eCG)**: FSH·LH 활성(과배란) / **hCG**: LH 유사(배란·황체 형성)",
        "**oxytocin**: 자궁 수축·유즙 배출, 분만 촉진·후산 정체, **산도 폐쇄(기계적 난산)에는 금기** / **ADH(vasopressin)**: 항이뇨, 결핍 시 **요붕증**",
        "**prolactin**: D2 차단(domperidone) → 분비↑(비유 촉진), D2 효현(**bromocriptine, cabergoline**) → 분비↓(개 가성임신·임신 중절) / **melatonin**: 어두울 때 분비, 계절 번식 조절",
    ],
    "thyroid_calcium": [
        "**항갑상선제**(thiouracil, methimazole, propylthiouracil): **peroxidase 억제 → 호르몬 합성 차단**(고양이 항진증), propylthiouracil은 용혈성 빈혈 독성 / **ipodate**: T4→T3 전환 억제 / **¹³¹I**: 갑상선 조직 파괴(고양이 근치) / **levothyroxine**: 개 저하증 1차",
        "**PTH**: 뼈 흡수·신 재흡수↑ + 비타민 D 활성화 → Ca²⁺↑ / **calcitonin**: 뼈 흡수 억제 → Ca²⁺↓ / **calcitriol**: 장 Ca²⁺·인 흡수↑ / **calcium gluconate·borogluconate**: 산욕열(젖소)·개 eclampsia 응급, **천천히 정맥 주사하며 심장 청진**",
    ],
    "pancreas": [
        "**insulin**: GLUT4 이동 → 포도당 흡수↑, 글리코겐·지방·단백 합성↑, K⁺ 세포 내 이동 / **sulfonylurea**: β세포 K-ATP 채널 차단 → **인슐린 분비↑**(β세포 기능 필요) / **metformin**: 간 포도당 신생↓, 인슐린 감수성↑ / **glucagon**: 간 글리코겐 분해 → 저혈당 응급",
    ],
    "sex_hormone": [
        "**androgen**: 표적에서 **5α-DHT**로 활성화(finasteride가 5α-reductase 억제), 동화 스테로이드는 단백 동화 / **estrogen**: 발정·생식관 자극, 개 **골수 억제**·자궁축농증, 골단선 폐쇄 / **progestin**: 임신 유지·발정 억제, 자궁축농증·당뇨·유선 종양",
        "**자궁 수축제**: oxytocin(산도 폐쇄 금기), ergonovine(지속 수축 → 분만 후 출혈 억제), PGF2α·cloprostenol(황체 퇴행), bromocriptine·cabergoline(prolactin↓), dexamethasone(소·양 분만 유도)",
    ],
    "ion_misc": [
        "**tetrodotoxin**: Na⁺ 채널 바깥 구멍 차단(복어독) / **phlorhizin**: SGLT 억제(신장 당 재흡수↓) / **tetraethylammonium**: K⁺ 채널 차단(연구용) / **ouabain**: Na⁺/K⁺-ATPase 억제 / **EDTA**: Ca²⁺ 킬레이트(금속 중독 치료, 저칼슘혈증 주의) / **erythropoietin**: 적혈구 생성(만성 신부전 빈혈), 항체 생성 시 적혈구 무형성 위험",
    ],
    # ── 항감염제 ──
    "antibiotic": [
        {"h": "선택의 기본", "i": [
            "**살균성**: β-lactam, aminoglycoside, fluoroquinolone, polymyxin, metronidazole / **정균성**: tetracycline, macrolide, lincosamide, chloramphenicol, sulfonamide(+trimethoprim은 살균)",
            "**농도 의존성**(aminoglycoside, FQ): 고용량 간헐 투여 / **시간 의존성**(β-lactam): 자주 투여. **정균제 + β-lactam 병용은 길항** 가능",
            "**내성**: β-lactamase, 표적 변화(MRSA의 PBP2a), 유출 펌프, 투과성 감소(plasmid·transposon 전달). 식용동물 **휴약기간** 준수",
        ]},
        {"h": "계열별 핵심", "i": [
            "**β-lactam**: PBP(transpeptidase) 억제 → 용균(성장 중 세균). **clavulanic acid·sulbactam·tazobactam**은 β-lactamase ‘자살 억제제’. **cephalosporin 세대**: 1(그람양성) → 2(혐기균) → 3(그람음성↑, 뇌척수액 투과) → 4(광범위). carbapenem 가장 넓음(보존적 사용)",
            "**aminoglycoside**: 산소 필요(혐기균 무효), 신독성·이독성·**신경근 차단**(Ca²⁺·neostigmine 길항), 1일 1회 / **tetracycline**: Ca²⁺ 킬레이트 → 치아·뼈, 고양이 식도 협착 / **lincosamide**: 초식동물 **치명적 대장염** / **tiamulin**: ionophore 병용 독성 / **tilmicosin**: 심독성",
            "**FQ**: DNA gyrase·topoisomerase IV, 어린 동물 연골 손상, 고양이 **망막 변성**, 금속 이온과 킬레이트 / **sulfonamide**(PABA 유사, DHPS 억제) + **trimethoprim**(DHFR 억제) = 엽산 **순차 차단** / **rifampin**: RNA polymerase, 체액 주황색, 간 효소 유도 / **metronidazole**: 혐기균·원충, 고용량 신경독성",
            "**결핵 치료제**: isoniazid(mycolic acid 합성 억제), ethambutol(arabinosyl transferase), rifampin",
        ]},
    ],
    "antifungal": [
        "진균 막은 **ergosterol**(동물은 cholesterol) → ergosterol 경로가 표적",
        "**polyene**(amphotericin B, nystatin): ergosterol에 결합해 구멍 형성, amphotericin B 전신 시 **신독성**, nystatin은 흡수 안 됨(국소·장관) / **azole**: **CYP51** 억제 → ergosterol↓, ketoconazole은 **CYP 억제·간독성**, fluconazole은 **뇌척수액 투과**(크립토콕쿠스 수막염)",
        "**terbinafine**: squalene epoxidase 억제 / **griseofulvin**: 미세소관 결합(피부사상균), **임신 기형·고양이 골수 억제** / **flucytosine**: cytosine deaminase → 5-FU, 내성 빨라 amphotericin B와 병용",
    ],
    "antiviral": [
        "증식 단계: 흡착·침투 → **탈각** → 핵산 복제·번역 → 조립 → 방출",
        "**amantadine**: influenza A **M2 채널** 차단(탈각 억제), 도파민 방출·NMDA 길항(통증 보조) / **acyclovir**: **바이러스 TK**가 1차 인산화(감염 세포에서만) → DNA polymerase 억제·사슬 종결 / **famciclovir**: penciclovir 전구약물(고양이 헤르페스) / **zidovudine**: 역전사효소 억제(FIV·FeLV) / **idoxuridine**: 헤르페스 각막염 국소",
        "**oseltamivir**: **neuraminidase** 억제 → 바이러스 방출 차단 (인플루엔자 **HA는 침입, NA는 방출**)",
    ],
    # ── 항기생충 · 살충제 ──
    "anthelmintic": [
        {"h": "선택 독성의 표적", "i": [
            "무척추동물 전용 **글루타메이트 개폐 Cl⁻ 채널** / 선충 **니코틴 수용체** / 기생충 **β-tubulin** / 기생충 에너지 대사(fumarate reductase 등)",
        ]},
        {"h": "선충", "i": [
            "**benzimidazole**: β-tubulin 결합 → 포도당 흡수 장애·ATP 고갈, 효과 **서서히**, 임신 초기 기형 / **levamisole·pyrantel·morantel**: nAChR 자극 → **경직성 마비** / **거대고리 락톤**(avermectin: ivermectin·doramectin·selamectin, milbemycin: milbemycin·moxidectin): 글루타메이트 Cl⁻ 채널 → **이완성 마비** / **piperazine**: GABA_A 효현 → 이완성 마비 / **emodepside**: SLO-1 K⁺ 채널 개방 / 유기인: AChE 억제(숙주 독성 주의)",
            "**MDR1(ABCB1) 변이**(collie, Australian shepherd): BBB의 P-gp가 없어 ivermectin 등이 뇌에 축적 → **운동 실조·침 흘림·혼수**. P-gp 억제제(verapamil, 일부 항생제) 병용·loperamide도 주의",
        ]},
        {"h": "조충 · 흡충 · 심장사상충", "i": [
            "**praziquantel**: 근육 Ca²⁺ 투과성↑ → 경직·tegument 손상 / **niclosamide, bithionol, hexachlorophene, dichlorophen, nitroxynil, oxyclozanide, closantel**: **산화적 인산화 탈공역** / arecoline·bunamidine: 조충 마비(구식)",
            "**심장사상충**: 모기 → L3 → 폐동맥 성충 → 미세사상충. **예방**: macrocyclic lactone **월 1회**(지난 한 달 유충 제거) / **성충 치료**: melarsomine(비소, 폐 혈전색전증 위험 → 운동 제한, 부작용 시 **dimercaprol**)",
        ]},
    ],
    "antiprotozoal": [
        "**콕시듐**: polyether ionophore(**monensin, salinomycin, lasalocid**: 이온 이동으로 삼투 파열, **말 독성**), amprolium(thiamine 흡수 경쟁), sulfaquinoxaline·ethopabate(엽산 합성 억제), trimethoprim·diaveridine·ormethoprim(DHFR 억제)",
        "**babesia**: diminazene / **toxoplasma**: pyrimethamine + sulfonamide(엽산 대사 순차 차단)",
    ],
    "insecticide": [
        "**유기인계**(dichlorvos, malathion, coumaphos): AChE **비가역** 억제, 중독 시 **atropine** / **carbamate**(carbaryl): AChE **가역** 억제",
        "**pyrethrin·pyrethroid**: 곤충 Na⁺ 채널 불활성화 지연 → 지속 탈분극·경련·마비, **고양이는 permethrin 고농도 제품에 중독**(진전·경련)",
        "rotenone: 미토콘드리아 복합체 I 억제 / benzyl benzoate: 옴진드기 신경독 / 유황: 각질 용해·항균",
    ],
    # ── 항암 · 면역 ──
    "antineoplastic": [
        "**세포 주기**: 특이적(항대사제 S기, vinca M기, bleomycin G2) vs 비특이적(알킬화제·백금·안트라사이클린). 분열 빠른 정상 세포(골수·장 상피·모낭)도 손상 → **골수 억제·구토·설사·탈모**",
        {"table": [["약물", "기전", "주의할 독성"],
                   ["cyclophosphamide", "DNA 가교(간에서 활성화)", "**출혈성 방광염**(acrolein) → 수분·이뇨"],
                   ["cisplatin", "DNA 가교", "**신독성**(사전 수액), **고양이 금기**(폐수종)"],
                   ["carboplatin", "DNA 가교", "골수 억제(고양이 대안)"],
                   ["doxorubicin", "DNA 삽입·topoisomerase II", "누적 **심근독성**(개), 고양이 신독성, **혈관 외 유출 괴사**(dexrazoxane)"],
                   ["methotrexate", "DHFR 억제", "골수·장 독성, leucovorin 구제"],
                   ["5-FU · cytarabine · gemcitabine", "피리미딘 유사체", "5-FU **고양이 신경독성 금기**"],
                   ["vincristine · vinblastine · vinorelbine", "미세소관 중합 억제(M기)", "신경독성, 혈관 외 유출 괴사, collie MDR1"],
                   ["paclitaxel", "미세소관 안정화", "과민반응"],
                   ["L-asparaginase", "asparagine 고갈(림프종)", "과민반응"],
                   ["toceranib · masitinib", "tyrosine kinase 억제(KIT)", "비만세포종 표적치료"]]},
        "**nitrosourea**(lomustine, carmustine, streptozocin): 지용성으로 뇌 투과, streptozocin은 췌장 β세포 독성 / **bleomycin**: DNA 절단·폐섬유화 / **piroxicam**: 방광 이행상피암 항종양",
    ],
    "immunosuppressant": [
        {"h": "작용점", "i": [
            "항원 제시 → **T 세포**(calcineurin → NFAT → **IL-2**) → 림프구 증식(퓨린·피리미딘 de novo 합성) → 사이토카인·항체",
            {"table": [["작용점", "약물"],
                       ["IL-2 차단(calcineurin 억제)", "cyclosporine(cyclophilin), tacrolimus(FKBP12)"],
                       ["퓨린 합성 억제", "azathioprine(6-MP로 전환), mycophenolic acid(IMPDH)"],
                       ["피리미딘 합성 억제", "leflunomide(DHODH)"],
                       ["TNF-α 억제", "pentoxifylline"],
                       ["MMP 억제", "tetracycline·doxycycline·minocycline"],
                       ["기타", "금 제제, niacinamide"]]},
        ]},
        "**cyclosporine**: 개 아토피 피부염·항문 주위 누공 / **azathioprine**: **고양이는 TPMT 활성이 낮아 골수 억제 위험(주의·금기)** / **tetracycline + niacinamide**: 개 일부 면역 매개 피부질환(원반상 홍반성 루푸스 등) / 금 제제: 천포창, 신독성",
    ],
}
