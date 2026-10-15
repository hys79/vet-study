# 약물 정보 (AI 작성, 개조식) 3/3 — 부신·성호르몬, 항우울제, 항생제, 항진균, 구충·살충, 항암, 항바이러스, 면역억제
INFO_3 = {
"metyrapone": [
    "분류: 11β-hydroxylase 억제제",
    "기전: cortisol 합성 차단 → ACTH 증가",
    "용도: Cushing 진단·치료",
],
"mitotane": [
    "분류: 부신 피질 세포 선택적 파괴제(o,p'-DDD)",
    "용도: 개 뇌하수체 의존성 Cushing병·부신 종양",
    "주의: 부신 피질 기능 부전(Addison 위기) — glucocorticoid 보충·모니터링 필요, 구토·무기력",
],
"trilostane": [
    "분류: 3β-hydroxysteroid dehydrogenase 억제제",
    "용도: 개 Cushing병 1차 치료(스테로이드 합성 차단)",
    "주의: 부신 기능 저하, 전해질 이상 — ACTH 자극 시험으로 모니터링",
],
"ketoconazole": [
    "분류: azole 항진균제 + 스테로이드 합성 CYP 억제제",
    "용도: 전신 진균증, 개 Cushing(대안)",
    "주의: 간독성, CYP 억제로 약물 상호작용, 구토·식욕 부진",
],
"selegiline": [
    "분류: MAO-B 억제제",
    "용도: 개 인지기능장애(CDS) 치료",
    "특징: Cushing 치료 효과는 평가가 엇갈림",
    "금기: SSRI·TCA·meperidine·amitraz 병용(세로토닌 증후군)",
],
"testosterone": [
    "분류: 대표 androgen",
    "작용: 부속 생식기 발달, 이차 성징, 단백 동화, 성욕 증진",
    "특징: 표적 조직에서 5α-reductase에 의해 더 강력한 DHT로 전환",
    "주의: 고농도에서 발정 억제",
],
"stanozolol": [
    "분류: 동화 스테로이드",
    "용도: 식욕·체중·근육 증진",
    "주의: 간독성",
],
"boldenone": [
    "분류: 동화 스테로이드",
    "용도: 말 식욕·체중 증진",
    "금기: 경주마 도핑·식용동물 사용 금지",
],
"trenbolone": [
    "분류: 강력한 동화 스테로이드",
    "특징: 육우 성장 촉진제로 쓰이나 잔류 규제 대상",
],
"danazol": [
    "분류: 약한 androgen 작용 + gonadotropin 억제",
    "용도: 면역 매개 혈소판 감소증 등",
],
"fluoxymesterone": [
    "분류: 합성 androgen",
],
"19_nortestosterone": [
    "분류: 동화 스테로이드(nandrolone 계열)",
],
"methandrostenolone": [
    "분류: 합성 동화 스테로이드",
],
"finasteride": [
    "분류: 5α-reductase 억제제",
    "기전: DHT 생성 감소",
    "용도: 개 전립선 비대 완화",
],
"estradiol": [
    "분류: 주된 estrogen",
    "작용: 발정 유도, 생식관 자극, 발정 징후",
    "주의: 개에서 골수 억제(재생불량성 빈혈), 자궁축농증(cystic endometrial hyperplasia 유발)",
    "금기: 임신 중",
],
"estrone": [
    "분류: 천연 estrogen",
],
"estriol": [
    "분류: 약한 천연 estrogen",
    "용도: 개 요실금(요도 괄약근 긴장 증가)",
],
"zeranol": [
    "분류: 곰팡이 독소 zearalenone 유도체 — estrogen 작용 성장 촉진제",
    "특징: 식용동물 잔류 규제",
],
"diethylstilbestrol": [
    "분류: 합성 estrogen(DES)",
    "용도: 개 요실금 등",
    "주의: 발암성·골수 억제로 사용 제한",
],
"tamoxifen": [
    "분류: 선택적 estrogen 수용체 조절제(SERM)",
    "특징: 유방 조직에서 estrogen 길항",
],
"progesterone": [
    "분류: 황체호르몬",
    "작용: 임신 유지, 자궁 수축 억제(oxytocin 감수성 제거), 황체기 연장, 유선 발달",
],
"altrenogest": [
    "분류: 합성 progestin",
    "용도: 말·돼지 발정 동기화, 암말 임신 유지, 번식기 이행기 발정 억제",
    "주의: 사람 피부 흡수 주의(취급 시 장갑 착용)",
],
"melengestrol": [
    "분류: 합성 progestin(melengestrol acetate, MGA)",
    "용도: 육성 암소 발정 억제 — 사료 첨가",
],
"megestrol_acetate": [
    "분류: 합성 progestin",
    "용도: 개·고양이 발정 억제, 마킹·공격성 등 행동 조절, 피부염",
    "주의: 자궁축농증, 당뇨, 유선 종양, 부신 억제, 식욕 증가",
],
"medroxyprogesterone_acetate": [
    "분류: 합성 progestin",
    "용도: 발정 억제·행동 조절",
    "주의: 자궁축농증, 당뇨, 유선 종양",
],
"pge1": [
    "분류: prostaglandin E1",
    "작용: 혈관 확장, 점막 보호",
    "특징: misoprostol의 모체",
],
"pge2": [
    "분류: prostaglandin E2(dinoprostone)",
    "작용: 염증·발열·통증 매개, 자궁 경부 이완",
],
"pgf2alpha": [
    "분류: prostaglandin F2α(dinoprost)",
    "기전: 황체 퇴행(luteolysis)",
    "용도: 발정 동기화, 유산 유도, 자궁축농증 치료(개·소), 소 지연 분만",
    "주의: 구토·유연·설사·호흡 곤란(개·고양이는 소량부터 점증), 임신 중 금기",
    "특징: 사람 취급 시 기관지 수축 주의(임신부·천식 환자)",
],
"ergonovine": [
    "분류: 맥각 alkaloid",
    "기전: 지속적 자궁 수축",
    "용도: 분만 후 출혈 억제",
    "금기: 분만 중(태아 사망 위험)",
],
"bromocriptine": [
    "분류: D2 효현제",
    "기전: 프롤락틴 분비 억제 → 황체 퇴행",
    "용도: 개 가성임신, 임신 중절",
    "주의: 구토 빈발",
],
"cabergoline": [
    "분류: 작용이 긴 D2 효현제",
    "용도: 개 가성임신·임신 중절, 유즙 분비 억제",
    "주의: bromocriptine보다 구토 적음",
],
"cloprostenol": [
    "분류: PGF2α 합성 유사체",
    "용도: 소·말 발정 동기화, 황체 퇴행, 유산 유도",
],
"erythropoietin": [
    "분류: 적혈구 생성 촉진 호르몬(신장에서 생성)",
    "용도: 만성 신부전 빈혈",
    "주의: 재조합 사람 EPO는 항체 형성 시 순수 적혈구 무형성(PRCA)",
],
"amitriptyline": [
    "분류: 삼환계 항우울제(TCA)",
    "용도: 행동 문제, 신경병증성 통증 보조, 고양이 특발성 방광염",
    "주의: 항무스카린 부작용, 진정, 심 전도 이상",
],
"clomipramine": [
    "분류: 삼환계 항우울제 — 5-HT 재흡수 억제 우세",
    "용도: 개 분리불안·강박 행동",
    "주의: 구강 건조, 진정, 심 전도 이상",
],
"doxepin": [
    "분류: 삼환계 항우울제 — H1 차단 강함",
    "용도: 개 소양증",
],
"fluoxetine": [
    "분류: SSRI",
    "용도: 개 분리불안, 고양이 스프레이·공격성",
    "특징: 활성 대사산물(norfluoxetine) 반감기 김",
    "금기: MAOI·TCA 병용(세로토닌 증후군)",
],
"paroxetine": [
    "분류: SSRI 항우울제",
],
"sertraline": [
    "분류: SSRI 항우울제",
],
"fluvoxamine": [
    "분류: SSRI 항우울제",
],
"cycloserine": [
    "분류: D-alanine 유사체 항결핵제",
    "기전: murein(세포벽) 합성 초기 억제",
],
"bacitracin": [
    "분류: 폴리펩티드 항생제(국소용)",
    "기전: 세포벽 전구체 운반 억제",
    "주의: 전신 투여 시 신독성",
],
"vancomycin": [
    "분류: glycopeptide 항생제",
    "기전: D-Ala-D-Ala에 결합 → 세포벽 합성 차단",
    "용도: MRSA 등 그람양성 다제 내성균, 경구 시 Clostridium difficile 감염",
    "특징: 다제 내성 관리를 위해 사용 제한",
],
"polymyxin_b": [
    "분류: polymyxin계 항생제",
    "기전: 세균 외막 인지질 파괴(양이온성 세제 작용)",
    "주의: 신독성·신경독성 → 전신 사용 제한",
],
"colistin": [
    "분류: polymyxin E",
    "기전: 세균 외막 인지질 파괴",
    "용도: 그람음성균 장염(주로 돼지·가금)",
],
"nystatin": [
    "분류: polyene 항진균제",
    "특징: 장관 흡수 안 됨 → 국소·소화관 칸디다증",
],
"amphotericin_b": [
    "분류: polyene 항진균제",
    "기전: ergosterol에 결합해 막에 구멍 형성",
    "주의: 전신 투여 시 신독성 — liposome 제제로 완화",
],
"streptomycin": [
    "분류: aminoglycoside",
    "특징: 결핵·브루셀라 등 병용, 이독성(전정 장애)",
],
"neomycin": [
    "분류: aminoglycoside(경구 흡수 거의 안 됨)",
    "용도: 장관 감염, 간성 뇌증, 국소",
    "주의: 전신 흡수 시 신독성·이독성",
],
"kanamycin": [
    "분류: aminoglycoside",
],
"gentamicin": [
    "분류: 광범위 aminoglycoside",
    "기전: 30S 리보솜 결합 → 단백 합성 오류, 살균(농도 의존)",
    "용도: 그람음성균·녹농균 감염",
    "주의: 신독성(근위세뇨관), 이독성(전정·와우), 신경근 차단, 탈수·신부전·loop 이뇨제 병용 시 위험↑",
    "특징: 1일 1회 투여, 혐기균 무효(산소 필요)",
],
"tobramycin": [
    "분류: aminoglycoside",
    "특징: 녹농균에 효과적",
],
"amikacin": [
    "분류: aminoglycoside",
    "특징: 효소에 의한 불활성에 안정 → gentamicin 내성균 감염",
],
"spectinomycin": [
    "분류: aminocyclitol계 정균성 항생제",
    "용도: 가금·돼지 호흡기·장 감염",
],
"tylosin": [
    "분류: 수의 전용 macrolide(50S 리보솜 억제)",
    "용도: 돼지 장염(회장염), 가금 마이코플라스마, 개 만성 설사, 소 호흡기",
],
"tilmicosin": [
    "분류: macrolide(소 호흡기 질환용)",
    "금기: 돼지·사람 주사 노출 — 심독성으로 치명적",
],
"chloramphenicol": [
    "분류: 50S 리보솜 억제 정균성 항생제",
    "금기: 식용동물 — 사람에서 비가역적 재생불량성 빈혈 위험",
    "주의: 고양이는 포합이 느려 반감기 김, 골수 억제",
],
"tiamulin": [
    "분류: pleuromutilin계(50S 리보솜 억제)",
    "용도: 돼지 이질·폐렴(Mycoplasma)",
    "금기: ionophore(monensin, salinomycin) 병용 — 독성",
],
"lincomycin": [
    "분류: lincosamide(50S 리보솜 억제)",
    "금기: 말·토끼·기니피그·햄스터 등 초식동물 — 치명적 대장염(Clostridium)",
],
"clindamycin": [
    "분류: lincosamide(50S 리보솜 억제)",
    "용도: 혐기균 감염, 골수염, 개·고양이 toxoplasmosis",
    "금기: 말·토끼 등 초식동물",
],
"pirlimycin": [
    "분류: lincosamide",
    "용도: 소 유방염(유방 내 주입)",
],
"nalidixic_acid": [
    "분류: 1세대 quinolone",
    "용도: 요로 그람음성균 감염",
],
"ciprofloxacin": [
    "분류: fluoroquinolone",
    "기전: DNA gyrase·topoisomerase IV 억제 → 살균(농도 의존)",
    "주의: 어린 동물 연골 손상, 고양이 enrofloxacin 고용량 망막 변성, 제산제·금속 이온과 킬레이트, 경련 역치 저하",
],
"novobiocin": [
    "분류: DNA gyrase B 억제 항생제",
    "용도: 소 건유기 유방염(과거)",
],
"actinomycin": [
    "분류: 세포독성 항생제(actinomycin D)",
    "기전: DNA 전사 억제",
    "용도: 항암제",
],
"mitomycin": [
    "분류: DNA 가교 항암성 항생제",
],
"isoniazid": [
    "분류: 항결핵제",
    "기전: mycolic acid 합성 억제",
    "주의: 간독성, 말초 신경병증(비타민 B6 결핍)",
],
"ethambutol": [
    "분류: 항결핵제",
    "기전: arabinosyl transferase 억제",
    "주의: 시신경염",
],
"trimethoprim": [
    "분류: 엽산 대사 억제 항균제(DHFR 억제)",
    "특징: sulfonamide와 병용 시 순차 차단 → 상승·살균 효과",
],
"penicillin_g": [
    "분류: 천연 penicillin(β-lactam)",
    "기전: PBP 결합 → 세포벽 합성 차단, 시간 의존성 살균",
    "용도: 그람양성균·혐기균(Clostridium) 감염, 가축 주사제(procaine penicillin)",
    "주의: 과민반응(아나필락시스), procaine 제제 정맥 투여 금지",
    "특징: 산에 불안정 — 경구 불가",
],
"penicillin_v": [
    "분류: 경구용 천연 penicillin",
    "특징: 산에 안정",
],
"amoxicillin": [
    "분류: 광범위 penicillin(aminopenicillin)",
    "특징: 경구 흡수 양호",
    "용도: 개·고양이 요로·피부 감염, clavulanic acid와 병용(Clavamox)",
],
"ampicillin": [
    "분류: 광범위 aminopenicillin",
    "특징: 경구 흡수가 amoxicillin보다 낮음",
],
"piperacillin": [
    "분류: 항녹농균 광범위 penicillin",
    "특징: tazobactam과 병용",
],
"hetacillin": [
    "분류: ampicillin 전구약물",
    "용도: 소 유방염",
],
"ticarcillin": [
    "분류: 항녹농균 penicillin",
    "특징: clavulanic acid와 병용",
],
"carbenicillin": [
    "분류: 항녹농균 penicillin",
],
"methicillin": [
    "분류: penicillinase 저항성 penicillin",
    "특징: MRSA(methicillin-resistant S. aureus) 명칭의 기원",
],
"oxacillin": [
    "분류: penicillinase 저항성 penicillin",
    "용도: 포도구균 감염",
],
"cloxacillin": [
    "분류: penicillinase 저항성 penicillin",
    "용도: 소 유방염(건유기 주입)",
],
"nafcillin": [
    "분류: penicillinase 저항성 penicillin",
],
"clavulanic_acid": [
    "분류: β-lactamase 억제제(자살 억제제)",
    "특징: amoxicillin과 병용",
],
"sulbactam": [
    "분류: β-lactamase 억제제",
    "특징: ampicillin과 병용",
],
"tazobactam": [
    "분류: β-lactamase 억제제",
    "특징: piperacillin과 병용",
],
"cephalexin": [
    "분류: 1세대 cephalosporin",
    "용도: 개·고양이 피부·요로 감염(그람양성균 위주)",
],
"cephalothin": [
    "분류: 1세대 cephalosporin(주사용)",
],
"cefaclor": [
    "분류: 2세대 cephalosporin(경구)",
],
"cefoxitin": [
    "분류: 2세대 cephalosporin",
    "특징: 혐기균(B. fragilis)에도 효과",
],
"ceftiofur": [
    "분류: 수의 전용 3세대 cephalosporin",
    "용도: 소·돼지·말 호흡기 감염, 소 급성 유방염·자궁염",
    "특징: 휴약기 매우 짧거나 없는 제제 있음",
],
"cefotaxime": [
    "분류: 3세대 cephalosporin",
    "특징: 그람음성균에 강함, 뇌척수액 투과",
],
"cefepime": [
    "분류: 4세대 cephalosporin",
    "특징: 광범위, AmpC β-lactamase에 안정",
],
"imipenem": [
    "분류: carbapenem",
    "특징: 가장 넓은 항균 범위, cilastatin과 병용(신장 DHP-I 분해 방지)",
    "주의: 경련 유발 가능",
],
"meropenem": [
    "분류: carbapenem",
    "특징: 다제 내성균 감염에 사용 — 최후 수단 항생제",
],
"doxycycline": [
    "분류: tetracycline계 항생제(30S 리보솜 억제, 정균)",
    "용도: 리케차·Ehrlichia·클라미디아·마이코플라스마·Lyme병(Borrelia), 심장사상충 Wolbachia",
    "특징: 담즙 배설 → 신부전 시에도 사용 가능, 지용성",
    "주의: 고양이에서 알약이 식도에 걸려 식도 협착 → 투약 후 물 필수, Ca²⁺·Mg²⁺ 킬레이트, 어린 동물 치아 착색",
],
"sulfamethazine": [
    "분류: sulfonamide",
    "기전: PABA 길항 → 엽산 합성 억제",
    "주의: 결정뇨(충분한 수분)",
],
"sulfasalazine": [
    "분류: 장에서 5-ASA와 sulfapyridine으로 분해되는 sulfonamide",
    "용도: 개 대장염",
    "주의: 건성 각결막염(KCS)",
],
"miconazole": [
    "분류: azole 항진균제(주로 국소)",
],
"fluconazole": [
    "분류: azole 항진균제",
    "특징: 뇌척수액·안구 투과 양호, 신장 배설",
    "용도: 크립토콕쿠스성 수막염",
],
"itraconazole": [
    "분류: azole 항진균제",
    "용도: 스포로트릭스증, 블라스토미세스증, 히스토플라스마증, 아스페르길루스증",
    "주의: 간독성, 혈관염",
],
"terbinafine": [
    "분류: squalene epoxidase 억제 항진균제",
    "용도: 피부사상균증(ringworm)",
],
"griseofulvin": [
    "분류: 미세소관 결합 항진균제(유사분열 억제)",
    "용도: 피부사상균증 — 케라틴 형성 조직에 축적",
    "금기: 임신(기형 유발)",
    "주의: 고양이 FIV 양성 시 골수 억제, 지방 식이와 함께 투여 시 흡수↑",
],
"flucytosine": [
    "분류: 핵산 합성 억제 항진균제",
    "기전: 진균 cytosine deaminase에 의해 5-FU로 전환",
    "특징: 단독 사용 시 내성 빠름 → amphotericin B 병용",
],
"dichlorvos": [
    "분류: 유기인계 구충·살충제",
    "기전: AChE 억제",
    "주의: 숙주 콜린에스터라제 억제 중독 가능 — atropine",
],
"trichlorfon": [
    "분류: 유기인계 구충·살충제",
    "기전: AChE 억제",
],
"ivermectin": [
    "분류: 거대고리 락톤(avermectin)",
    "기전: 무척추동물 글루타메이트 개폐 Cl⁻ 채널 개방 → 이완성 마비",
    "용도: 선충·외부 기생충(옴·이)·심장사상충 예방",
    "금기: collie·Australian shepherd 등 MDR1(ABCB1) 변이 견종 — P-gp 결손으로 중추 독성(운동실조·유연·혼수)·돌발 허탈·폐사",
    "주의: 어린 강아지·고양이 과량, 거북·악어 등 일부 파충류에 독성",
],
"mebendazole": [
    "분류: benzimidazole 구충제",
    "기전: β-tubulin 결합 → 미세소관 형성 억제",
],
"niclosamide": [
    "분류: 조충 구제약",
    "기전: 산화적 인산화 탈공역",
],
"bunamidine": [
    "분류: 개·고양이 조충 구제약",
    "주의: 독성(심장 부정맥) 보고, 안전역 좁음",
],
"dithiazine": [
    "분류: 구충제(dithiazanine)",
    "용도: 과거 선충·심장사상충 미세사상충 구제",
    "주의: 독성 있음",
],
"thiabendazole": [
    "분류: benzimidazole 구충제",
    "기전: fumarate reductase 억제(미토콘드리아)",
],
"prabendazole": [
    "분류: benzimidazole 구충제",
],
"bithionol": [
    "분류: 흡충·조충 구충제",
    "기전: 산화적 인산화 탈공역",
],
"hexachlorophene": [
    "분류: 흡충 구충제",
    "기전: 산화적 인산화 탈공역",
    "주의: 독성 있음(소독제 성분이기도 함)",
],
"dichlorophen": [
    "분류: 조충 구충제",
    "기전: 산화적 인산화 탈공역",
],
"nitroxynil": [
    "분류: 간 흡충(Fasciola) 구충제",
    "기전: 산화적 인산화 탈공역",
],
"niclofolan": [
    "분류: 간 흡충 구충제",
],
"oxyclozanide": [
    "분류: 간 흡충 구충제(탈공역제)",
],
"metyridine": [
    "분류: 선충 구충제",
    "기전: 선충 마비",
],
"piperazine": [
    "분류: 선충 구충제",
    "기전: 선충 근육 GABA_A 수용체 자극 → 이완성 마비",
    "용도: 개·고양이 회충",
],
"albendazole": [
    "분류: 광범위 benzimidazole 구충제",
    "용도: 선충·간 흡충·조충",
    "금기: 임신 초기(기형 유발)",
],
"fenbendazole": [
    "분류: benzimidazole 구충제",
    "용도: 개·가축 선충, 개·고양이 Giardia",
    "특징: 안전역 넓음",
],
"doramectin": [
    "분류: avermectin계 거대고리 락톤",
    "용도: 소·돼지 선충·외부 기생충",
],
"selamectin": [
    "분류: avermectin계 거대고리 락톤(도포제)",
    "용도: 개·고양이 심장사상충 예방, 벼룩·진드기·귀 진드기",
],
"milbemycin": [
    "분류: milbemycin계 거대고리 락톤",
    "용도: 심장사상충 예방, 장내 선충",
],
"moxidectin": [
    "분류: milbemycin계 거대고리 락톤(작용 지속 김)",
    "용도: 심장사상충 예방, 소·말 선충",
    "주의: 어린 동물·MDR1 변이 견종 감수성",
],
"emodepside": [
    "분류: SLO-1 K⁺ 채널 개방제",
    "기전: 선충 과분극 → 마비",
    "용도: 고양이 선충(도포제)",
],
"melarsomine": [
    "분류: 비소 제제 살성충제",
    "용도: 심장사상충 성충 제거(근육 주사)",
    "주의: 성충 사멸로 폐 혈전색전증 → 운동 제한, 주사 부위 통증",
    "해독: dimercaprol(독성 시)",
],
"dimercaprol": [
    "분류: BAL — 비소·중금속 킬레이트 해독제",
    "용도: melarsomine·비소 중독",
],
"diamphenethide": [
    "분류: 간 흡충 구충제",
    "특징: 미성숙충에 효과적",
],
"praziquantel": [
    "분류: 흡충·조충 구충제",
    "기전: 근육 Ca²⁺ 투과성 증가 → 경직 + 외피 손상",
    "용도: 개·고양이 조충, 흡충",
],
"clopidol": [
    "분류: 닭 콕시듐 억제 합성 첨가제",
],
"robenidine": [
    "분류: 닭 콕시듐 억제 합성 첨가제",
],
"dinitolmide": [
    "분류: 닭 콕시듐 억제 합성 첨가제(zoalene)",
],
"nicarbazine": [
    "분류: 닭 콕시듐 억제 합성 첨가제",
    "주의: 고온에서 폐사율 증가",
],
"monensin": [
    "분류: polyether ionophore",
    "용도: 닭·소 콕시듐 억제, 반추위 발효 효율 개선",
    "금기: 말에게 치명적(심근 독성) — 사료 오염 주의, 개·칠면조 독성",
],
"salinomycin": [
    "분류: polyether ionophore 항콕시듐제",
    "금기: 말·개 독성",
],
"lasalocid": [
    "분류: polyether ionophore 항콕시듐제",
    "특징: 말에 독성",
],
"amprolium": [
    "분류: thiamine 유사체 항콕시듐제",
    "기전: 콕시듐의 thiamine 흡수 경쟁적 방해",
    "주의: 과량·장기 투여 시 동물의 thiamine 결핍(소 대뇌피질괴사증)",
],
"ethopabate": [
    "분류: PABA 유사체 — 엽산 합성 방해",
    "특징: amprolium과 병용",
],
"sulfaquinoxaline": [
    "분류: sulfonamide 항콕시듐제",
    "주의: 장기 사용 시 출혈성 소인(비타민 K 결핍)",
],
"diaveridine": [
    "분류: DHFR 억제 항콕시듐 보조제",
],
"sulfadimethoxine": [
    "분류: 장시간 작용 sulfonamide",
    "용도: 개·고양이 콕시듐증",
],
"ormethoprim": [
    "분류: DHFR 억제 항콕시듐 보조제",
    "특징: sulfadimethoxine과 병용",
],
"diminazene": [
    "분류: 항원충제(Babesia·Trypanosoma)",
    "용도: 개·소 Babesia 감염(babesiosis)",
    "주의: 과량 시 중추 신경 독성",
],
"pamaquine": [
    "분류: 8-aminoquinoline계 항원충제",
    "특징: DB상 항 Theileria 약물로 분류",
],
"primaquine": [
    "분류: 8-aminoquinoline계 항원충제",
    "특징: DB상 항 Theileria 약물로 분류",
],
"pyrimethamine": [
    "분류: DHFR 억제 항원충제",
    "용도: sulfonamide와 병용해 Toxoplasma 감염 치료",
],
"sulfamonomethoxine": [
    "분류: sulfonamide",
    "용도: Toxoplasma·콕시듐 감염",
],
"acrinamine": [
    "분류: DB상 항원충제(기타)로 분류된 약물",
    "특징: 교재 정보 제한적",
],
"fenitrothion": [
    "분류: 유기인계 살충제",
],
"coumaphos": [
    "분류: 유기인계 살충제",
    "용도: 소 외부 기생충(진드기·파리)",
],
"fenchlorphos": [
    "분류: 유기인계 살충제(ronnel)",
],
"carbaryl": [
    "분류: carbamate계 살충제",
    "기전: AChE 가역적 억제",
    "해독: atropine",
],
"pyrethrin": [
    "분류: 국화에서 얻는 천연 살충 성분",
    "기전: 곤충 Na⁺ 채널 불활성 지연 → 지속 탈분극·마비",
],
"decamethrin": [
    "분류: 합성 pyrethroid(deltamethrin)",
    "용도: 살충·외부 기생충 구제",
],
"allethrin": [
    "분류: 합성 pyrethroid",
],
"rotenone": [
    "분류: 천연 살충제(식물 유래)",
    "기전: 미토콘드리아 복합체 I 억제",
    "특징: 어류에 독성 강함",
],
"benzyl_benzoate": [
    "분류: 외용 살충제",
    "용도: 옴진드기",
    "주의: 고양이에서 독성 가능 — 피부 자극",
],
"sulfur": [
    "분류: 유황(외용제)",
    "작용: 각질 용해·항진균·항기생충",
],
"cyclophosphamide": [
    "분류: 알킬화제(nitrogen mustard) — 전구약물",
    "기전: 간에서 활성화, DNA 가교",
    "용도: 림프종·육종 병용 화학요법, 면역 매개 질환(면역억제)",
    "주의: 출혈성 방광염(대사산물 acrolein) — 충분한 수분·배뇨, 골수 억제",
],
"chlorambucil": [
    "분류: 알킬화제(nitrogen mustard)",
    "용도: 만성 림프성 백혈병, 고양이 림프종·IMHA",
],
"melphalan": [
    "분류: 알킬화제(nitrogen mustard)",
    "용도: 다발성 골수종",
],
"mechlorethamine": [
    "분류: 알킬화제(nitrogen mustard, 최초의 항암제)",
],
"ifosfamide": [
    "분류: 알킬화제(nitrogen mustard)",
    "용도: 연부조직 육종",
    "주의: 출혈성 방광염·신독성 → mesna 병용",
],
"lomustine": [
    "분류: 지용성 nitrosourea 알킬화제",
    "특징: 혈액-뇌 장벽 통과",
    "용도: 개 림프종(구제), 비만세포종, 뇌종양",
    "주의: 지연성 골수 억제, 간독성",
],
"carmustine": [
    "분류: 지용성 nitrosourea 알킬화제",
    "특징: 뇌 투과",
],
"streptozocin": [
    "분류: nitrosourea 알킬화제",
    "특징: 췌장 β세포 선택적 독성",
    "용도: 개 인슐린종 치료",
    "주의: 신독성, 당뇨 유발",
],
"procarbazine": [
    "분류: methylhydrazine계 알킬화제",
],
"dacarbazine": [
    "분류: triazene계 알킬화제",
    "용도: 흑색종, 림프종 구제 요법(DAV)",
],
"hydroxyurea": [
    "분류: 리보뉴클레오티드 환원효소 억제제",
    "용도: 고양이 진성 적혈구 증가증",
],
"cisplatin": [
    "분류: 백금 제제",
    "기전: DNA 가교(세포주기 비특이적)",
    "용도: 개 골육종·편평상피암",
    "금기: 고양이 — 치명적 폐수종",
    "주의: 신독성(사전 생리식염수 이뇨), 구토 심함, 이독성",
],
"carboplatin": [
    "분류: 백금 제제",
    "특징: cisplatin보다 신독성·구토 적음",
    "주의: 골수 억제(용량 제한 독성), 고양이에도 사용 가능",
],
"methotrexate": [
    "분류: 엽산 유사 항대사제",
    "기전: DHFR 억제 → 티미딜산·퓨린 합성 저하(S기 특이적)",
    "용도: 림프종, 골육종 병용",
    "해독: leucovorin(folinic acid) rescue",
    "주의: 신독성, 골수 억제, 구내염",
],
"5_fluorouracil": [
    "분류: 피리미딘 유사 항대사제",
    "기전: thymidylate synthase 억제",
    "금기: 고양이 — 신경독성(경련·사망)",
    "주의: 개 — 경련, 골수 억제",
],
"cytarabine": [
    "분류: 피리미딘 유사 항대사제",
    "용도: 림프종·중추신경계 종양 — 피하·정맥 지속 주입",
],
"gemcitabine": [
    "분류: 피리미딘 유사 항대사제",
    "용도: 고양이 종양(방사선 감작)",
],
"6_mercaptopurine": [
    "분류: 퓨린 유사 항대사제",
    "특징: azathioprine의 활성 대사산물",
],
"6_thioguanine": [
    "분류: 퓨린 유사 항대사제",
],
"vincristine": [
    "분류: vinca alkaloid(미세소관 중합 억제, M기 특이적)",
    "용도: 림프종, 개 전염성 성 종양(TVT) 1차 치료",
    "주의: 말초 신경독성(변비·장 마비), 혈관 외 유출 시 조직 괴사, collie MDR1 변이 견종 감수성↑",
    "특징: 골수 억제 적음",
],
"vinblastine": [
    "분류: vinca alkaloid",
    "용도: 개 비만세포종·림프종",
    "주의: 골수 억제(vincristine보다 큼), 혈관 외 유출 괴사",
],
"vinorelbine": [
    "분류: 반합성 vinca alkaloid",
    "용도: 폐 종양 등",
],
"paclitaxel": [
    "분류: taxane계(미세소관 안정화)",
    "주의: 과민반응",
],
"doxorubicin": [
    "분류: 안트라사이클린 항암 항생제",
    "기전: DNA 삽입·topoisomerase II 억제, 자유 라디칼",
    "용도: 림프종, 육종, 혈관육종",
    "주의: 누적 용량 심독성(개 DCM), 고양이 신독성, 혈관 외 유출 시 조직 괴사",
    "해독: dexrazoxane(혈관 외 유출·심독성 예방)",
],
"epirubicin": [
    "분류: doxorubicin 유사 안트라사이클린",
    "특징: 심독성 다소 적음",
],
"mitoxantrone": [
    "분류: anthracenedione계 topoisomerase II 억제 항암제",
    "특징: 심독성 적음",
],
"bleomycin": [
    "분류: DNA 절단 항암 항생제",
    "주의: 폐섬유화",
    "특징: 골수 억제 적음",
],
"etoposide": [
    "분류: topoisomerase II 억제 항암제",
],
"dexrazoxane": [
    "분류: 철 킬레이트 보호제",
    "용도: doxorubicin 혈관 외 유출 조직 괴사·심독성 완화",
],
"l_asparaginase": [
    "분류: 효소 항암제",
    "기전: asparagine 분해 → 림프종 세포 단백 합성 저해(정상 세포는 합성 가능)",
    "용도: 개 림프종 유도 요법",
    "주의: 과민반응(아나필락시스), 췌장염",
],
"toceranib": [
    "분류: tyrosine kinase 억제제(KIT·VEGFR 등)",
    "용도: 개 비만세포종(KIT 돌연변이)",
    "주의: 설사·식욕 부진·혈압 상승",
],
"masitinib": [
    "분류: tyrosine kinase 억제제(KIT 선택적)",
    "용도: 개 비만세포종",
    "주의: 단백뇨",
],
"amantadine": [
    "분류: M2 이온 채널 차단 항바이러스제",
    "기전: influenza A 탈각(uncoating) 억제",
    "용도: 개·고양이 만성 통증 보조(NMDA 길항·도파민 효과)",
],
"acyclovir": [
    "분류: guanosine 유사체 항헤르페스제",
    "기전: 바이러스 thymidine kinase로 인산화(감염 세포 선택) → DNA polymerase 억제·사슬 종결",
],
"famciclovir": [
    "분류: penciclovir 전구약물",
    "용도: 고양이 herpesvirus-1(FHV-1) 감염",
],
"zidovudine": [
    "분류: 역전사효소 억제제(AZT)",
    "용도: 고양이 FIV·FeLV 감염 보조",
    "주의: 고양이에서 빈혈·백혈구 감소(조혈 억제)",
],
"idoxuridine": [
    "분류: thymidine 유사체",
    "용도: 헤르페스성 각막염 점안",
    "특징: 주로 국소용(전신 사용 제한)",
],
"oseltamivir": [
    "분류: neuraminidase 억제제",
    "기전: influenza 바이러스 방출 차단",
    "특징: HA는 침입, NA는 방출에 관여",
],
"azathioprine": [
    "분류: 퓨린 유사 면역억제제(6-MP로 전환)",
    "용도: 개 면역 매개 질환(IMHA 등)",
    "금기: 고양이 — TPMT 활성이 낮아 골수 억제 위험",
    "주의: 골수 억제, 췌장염, 간독성",
],
"mycophenolic_acid": [
    "분류: IMPDH 억제 면역억제제",
    "기전: 림프구 de novo 퓨린 합성 차단(림프구 선택적)",
],
"leflunomide": [
    "분류: DHODH 억제 면역억제제",
    "기전: de novo 피리미딘 합성 차단",
],
"cyclosporine": [
    "분류: calcineurin 억제 면역억제제",
    "기전: cyclophilin 결합 → calcineurin 억제 → IL-2 생성↓",
    "용도: 개 아토피 피부염, 항문 주위 누공, 면역 매개 질환",
    "주의: 구토, 잇몸 증식, CYP3A4 상호작용(ketoconazole 병용 시 혈중 농도↑)",
],
"tacrolimus": [
    "분류: calcineurin 억제 면역억제제(FKBP12 결합)",
    "용도: 국소 도포 — 개 항문 주위 누공·건성 각결막염",
],
"tetracycline": [
    "분류: tetracycline계 항생제",
    "특징: MMP 억제·항염 작용 — niacinamide와 병용해 면역 매개 피부 질환",
],
"oxytetracycline": [
    "분류: tetracycline계 항생제",
    "용도: 가축 호흡기·세균 감염(장시간 작용 제제), 소 휴약기 적용",
],
"minocycline": [
    "분류: tetracycline계 항생제",
    "특징: P-gp 길항 작용 보고 — P-gp 기질 약물 독성 증가 가능",
],
"aurothioglucose": [
    "분류: 금 제제 면역 조절제",
    "용도: 천포창 등",
],
"aurothiomalate": [
    "분류: 주사용 금 제제",
    "주의: 신독성(단백뇨)",
],
"auranofin": [
    "분류: 경구 금 제제 면역 조절제",
    "용도: 개·고양이 천포창",
],
"niacinamide": [
    "분류: 비타민 B3",
    "용도: tetracycline과 병용해 개 원반상 홍반성 루푸스 등 면역 매개 피부 질환",
    "기전: 비만세포 탈과립·염증 억제",
],
}
