# 약물 정보 (AI 작성, 개조식) 2/3 — 순환계, 호흡기, 이뇨제, 소화기, 내분비
INFO_2 = {
"ondansetron": [
    "분류: 5-HT3 길항제 항구토제",
    "용도: 화학요법·장염·췌장염에 의한 구토(개·고양이)",
    "주의: QT 연장 가능, 변비",
],
"cisapride": [
    "분류: 5-HT4 효현제 prokinetic(ACh 유리 촉진)",
    "용도: 개·고양이 거대결장·위 배출 지연·역류성 식도염",
    "금기: 기계적 장 폐색",
    "주의: 사람에서 QT 연장으로 시판 중단 → 수의학은 조제약 사용",
],
"metoclopramide": [
    "분류: D2 길항 + 5-HT4 효현",
    "용도: 구토 억제(CTZ), 위 배출 촉진",
    "금기: 기계적 장 폐색, 위장관 출혈·천공",
    "주의: 중추 부작용(불안·진전·흥분), 말에서 특히 심함",
],
"captopril": [
    "분류: 최초의 ACE 억제제(sulfhydryl기 함유)",
    "특징: 활성형, 작용 시간 짧음(1일 2~3회)",
    "주의: 저혈압, 고칼륨혈증, 신기능 악화(탈수 시), 임신 금기",
],
"enalapril": [
    "분류: ACE 억제제(전구약물 → enalaprilat)",
    "용도: 개 심부전·고혈압·단백뇨 신증",
    "주의: 저혈압, 고칼륨혈증, 탈수·신부전 시 급성 신손상",
],
"lisinopril": [
    "분류: 활성형 ACE 억제제",
    "특징: 작용 시간 김, 신장 배설",
],
"benazepril": [
    "분류: ACE 억제제(전구약물)",
    "용도: 고양이 만성 신부전 단백뇨·고혈압, 개 심부전",
    "특징: 담즙·신장 이중 배설 → 신부전 시 용량 조절 부담 적음",
],
"losartan": [
    "분류: AT1 수용체 차단제(ARB)",
    "특징: ACE 억제제와 달리 bradykinin 축적 없음(기침 적음)",
    "주의: 고칼륨혈증, 임신 금기",
],
"valsartan": [
    "분류: AT1 수용체 차단제(ARB)",
],
"candesartan": [
    "분류: 작용이 긴 AT1 수용체 차단제(ARB)",
],
"aliskiren": [
    "분류: renin 직접 억제제",
    "기전: RAS 최상단(angiotensinogen → Ang I) 차단",
],
"cortisol": [
    "분류: 내인성 글루코코르티코이드(= hydrocortisone)",
    "작용: 당 신생 촉진, 단백 분해, 항염증·면역 억제, 스트레스 반응",
    "특징: 분비는 ACTH가 조절(음성 되먹임)",
],
"cortisone": [
    "분류: 전구형 글루코코르티코이드",
    "특징: 간에서 cortisol로 전환되어야 활성",
],
"hydrocortisone": [
    "분류: 글루코코르티코이드(= cortisol)",
    "특징: 단시간 작용(8~12시간), 항염증 효력 낮고 무기질코르티코이드 작용 있음",
    "용도: 부신 위기·쇼크 응급, 국소 도포",
],
"betamethasone": [
    "분류: 합성 글루코코르티코이드(장시간 작용)",
    "특징: 항염증 효력 cortisol의 약 25~30배, 무기질코르티코이드 작용 없음",
],
"dexamethasone": [
    "분류: 합성 글루코코르티코이드(장시간 작용, 48시간 이상)",
    "특징: 항염증 효력 cortisol의 약 25~30배, 무기질코르티코이드 작용 없음",
    "용도: 쇼크·뇌부종, 소 분만 유도(태아 코르티솔 상승 모방), 부신 기능 검사(저용량 억제 시험)",
    "주의: 임신 동물 조기 분만·유산, 위궤양, 고혈당, 의인성 Cushing",
],
"prednisolone": [
    "분류: 중간 작용 시간 합성 글루코코르티코이드(12~36시간)",
    "용도: 항염증·면역 억제(알레르기, IMHA, 염증성 장질환), 고양이·말에서 prednisone보다 선호",
    "주의: 다음·다뇨·다식, 의인성 Cushing, 위궤양, 감염 취약, 상처 치유 지연",
    "금기: 장기 투여 후 갑작스러운 중단(부신 억제) — 서서히 감량",
],
"prednisone": [
    "분류: 합성 글루코코르티코이드(전구약물)",
    "특징: 간에서 prednisolone으로 전환 — 고양이·말은 전환 효율이 낮음",
],
"aspirin": [
    "분류: 비선택적 COX 억제 NSAID",
    "기전: COX 비가역적 아세틸화 → 혈소판 TXA2 합성 억제(혈소판 수명 동안 지속)",
    "용도: 항혈소판(고양이 대동맥 혈전색전증 예방, 저용량·72시간 간격), 진통·해열",
    "주의: 위궤양·출혈, 고양이는 glucuronide 포합 약해 반감기 길고 독성",
    "중독: 호흡성 알칼리증 후 대사성 산증, 소변 알칼리화로 배설 촉진",
],
"flunixin_meglumine": [
    "분류: 강력한 NSAID",
    "용도: 말 산통(내장통) 진통, 소·말 내독소혈증, 발열·염증",
    "주의: 위궤양·신독성, 개에서는 사용 제한",
    "특징: 식용동물 휴약기간 적용",
],
"naproxen": [
    "분류: NSAID",
    "중독: 개에서 반감기가 매우 길어(약 74시간) 위궤양·신독성 위험 → 사용 금지",
],
"ibuprofen": [
    "분류: NSAID",
    "중독: 개·고양이에서 위궤양·신부전 위험이 큼 → 사용 금지",
],
"indomethacin": [
    "분류: 강력한 NSAID",
    "주의: 위장관 부작용 많아 소동물에서 거의 사용 안 함",
],
"ketoprofen": [
    "분류: NSAID(진통·해열·소염)",
    "용도: 말·소·개·고양이",
    "주의: 위장관·신독성",
],
"acetanilide": [
    "분류: aniline계 해열진통제",
    "특징: acetaminophen의 전신, 독성 때문에 사용 중단",
],
"phenacetin": [
    "분류: aniline계 해열진통제",
    "주의: 신독성(진통제 신병증)·methemoglobinemia로 퇴출",
],
"acetaminophen": [
    "분류: aniline계 해열진통제(항염증 작용 약함)",
    "금기: 고양이 — methemoglobinemia, Heinz body 빈혈, 간괴사 → 절대 금기",
    "주의: 개 — 과량 시 간독성, 건성 각결막염(KCS)",
    "해독: N-acetylcysteine(글루타티온 전구체)",
],
"phenylbutazone": [
    "분류: COX-2 선호 NSAID(= 'bute')",
    "용도: 말 근골격계 통증·파행",
    "주의: 위궤양·우측 배측 결장염, 신독성(유두 괴사), 개에서 골수 억제(재생불량성 빈혈)",
    "금기: 사람 식용 말·식용동물 사용 금지",
],
"meloxicam": [
    "분류: COX-2 선호 NSAID",
    "용도: 개 골관절염·수술 후 통증(1일 1회), 고양이 단회 투여",
    "주의: 고양이 반복 투여 시 신부전, 위장관 부작용",
],
"etodolac": [
    "분류: COX-2 선호 NSAID",
    "용도: 개 골관절염",
    "주의: 건성 각결막염(KCS) 보고",
],
"carprofen": [
    "분류: COX-2 선호 NSAID",
    "용도: 개 골관절염·수술 후 통증",
    "주의: 간독성(특이체질, Labrador), 고양이는 반감기가 길어 비권장",
],
"piroxicam": [
    "분류: NSAID(비선택적 COX 억제에 가까움)",
    "용도: 개 방광 이행상피암 — COX-2 활성·혈관신생 억제",
    "주의: 위궤양",
],
"deracoxib": [
    "분류: 선택적 COX-2 억제제(개 전용)",
    "특징: 위장관 부작용 적음",
],
"firocoxib": [
    "분류: 선택적 COX-2 억제제",
    "용도: 개·말 골관절염",
],
"tepoxalin": [
    "분류: COX와 5-LOX 이중 억제 NSAID",
    "특징: 개 골관절염, 위장관 부작용 감소 기대",
],
"dimethyl_sulfoxide": [
    "분류: 자유 라디칼 소거 항염증제·삼투성 이뇨제",
    "특징: 약물 흡수 촉진(운반체), 마늘 냄새",
    "용도: 부종·뇌압 감소, 국소 항염",
],
"polysulfated_glycosaminoglycan": [
    "분류: 관절 연골 보호제(PSGAG)",
    "용도: 개·말 골관절염",
],
"hyaluronate_sodium": [
    "분류: 관절 윤활액 성분",
    "용도: 말·개 관절염 — 관절 내 주사",
],
"digoxin": [
    "분류: 강심배당체",
    "기전: Na⁺/K⁺-ATPase 억제 → 세포 내 Ca²⁺ 증가 → 수축력↑, 미주 긴장 증가 → 방실 전도 지연",
    "용도: 개 심방세동 심박수 조절, 심부전",
    "주의: 치료 범위 좁음(구토·부정맥), 저칼륨혈증·신부전 시 독성 증가, 신장 배설",
],
"pimobendan": [
    "분류: PDE3 억제 + Ca²⁺ 감수성 증가 inodilator",
    "용도: 개 심부전(MVD·DCM) — 수명 연장",
    "특징: 산소 소모를 크게 늘리지 않고 수축력 증가 + 혈관 확장",
],
"dopamine": [
    "분류: 용량 의존성 카테콜아민",
    "기전: 저용량 D1(신혈관 확장) → 중용량 β1(수축력) → 고용량 α(혈관 수축)",
    "용도: 급성 저혈압·쇼크 — 정맥 지속 주입",
    "주의: 혈관 외 유출 시 조직 괴사, 빈맥·부정맥",
],
"amrinone": [
    "분류: bipyridine계 PDE3 억제제",
    "기전: 수축력 증가 + 혈관 확장",
    "주의: 혈소판 감소",
],
"milrinone": [
    "분류: bipyridine계 PDE3 억제제",
    "특징: amrinone보다 부작용 적음",
],
"furosemide": [
    "분류: loop 이뇨제(Na⁺-K⁺-2Cl⁻ 공동수송체 억제)",
    "용도: 급성 폐부종·울혈성 심부전 1차 선택, 소 유방 부종, 말 운동 유발성 폐출혈(EIPH) 예방",
    "주의: 저칼륨·저나트륨·저마그네슘혈증, 탈수, 대사성 알칼리증, 고용량·aminoglycoside 병용 시 이독성",
],
"spironolactone": [
    "분류: aldosterone 길항 칼륨 보존성 이뇨제",
    "용도: 심부전(리모델링 억제), 복수·간 질환",
    "주의: 고칼륨혈증(ACE 억제제 병용 시), 작용 발현 느림",
],
"ramipril": [
    "분류: ACE 억제제",
],
"quinapril": [
    "분류: ACE 억제제",
],
"hydralazine": [
    "분류: 동맥 직접 이완 혈관 확장제",
    "용도: 개 승모판 역류·심부전의 후부하 감소",
    "주의: 저혈압, 반사성 빈맥·RAAS 활성화 → ACE 억제제 병용",
],
"amlodipine": [
    "분류: 혈관 선택적 Ca²⁺ 채널 차단제(dihydropyridine)",
    "용도: 고양이 고혈압 1차 선택(만성 신부전·갑상선 기능 항진증 속발), 개 고혈압",
    "특징: 작용 시간 김, 심 억제 적음",
],
"nitroprusside": [
    "분류: NO 공여 혈관 확장제",
    "기전: 동맥·정맥 모두 확장",
    "용도: 급성 폐부종·고혈압 위기 — 정맥 지속 주입(작용 즉시)",
    "주의: 시안화물 독성(장기·고용량), 혈압 연속 감시",
],
"nitroglycerin": [
    "분류: NO 공여 nitrate",
    "기전: cGMP↑ → 정맥 확장 위주(전부하 감소)",
    "용도: 개·고양이 폐부종 보조(연고 경피 투여)",
    "주의: 내성(연속 사용 시 휴지 기간 필요), 저혈압",
],
"disopyramide": [
    "분류: Class IA 항부정맥제",
    "주의: 항콜린 작용, 심근 억제",
],
"flecainide": [
    "분류: Class IC 항부정맥제",
    "주의: 심근경색 후 사망률 증가(CAST), 구조적 심질환 금기",
],
"quinidine": [
    "분류: Class IA 항부정맥제(Na⁺ + K⁺ 채널 차단)",
    "용도: 말 심방세동 약물 전환",
    "주의: 말에서 부작용 — QRS·QT 연장, 저혈압, 빈맥, 비강 부종",
],
"procainamide": [
    "분류: Class IA 항부정맥제",
    "용도: 개 심실성 부정맥",
    "주의: 저혈압, QT 연장",
],
"mexiletine": [
    "분류: Class IB 항부정맥제(경구)",
    "용도: 개 심실성 부정맥 — lidocaine의 경구 대안",
],
"tocainide": [
    "분류: Class IB 항부정맥제",
    "주의: 혈액 이상",
],
"propafenone": [
    "분류: Class IC 항부정맥제",
],
"encainide": [
    "분류: Class IC 항부정맥제",
    "특징: 현재 거의 사용 안 함",
],
"indecainide": [
    "분류: Class IC 항부정맥제",
],
"lorcainide": [
    "분류: Class IC 항부정맥제",
],
"amiodarone": [
    "분류: Class III 항부정맥제(다중 채널 + β 차단)",
    "용도: 개 심실성 부정맥·심방세동",
    "주의: 요오드 함유 → 갑상선 기능 이상, 폐섬유화, 간독성, 반감기 매우 김",
],
"diltiazem": [
    "분류: 비-dihydropyridine Ca²⁺ 채널 차단제(Class IV)",
    "용도: 개 상심실성 빈맥, 고양이 비대성 심근증 심박수 조절",
    "주의: 서맥·방실차단, β 차단제 병용 시 심 억제 가중",
],
"verapamil": [
    "분류: 비-dihydropyridine Ca²⁺ 채널 차단제(Class IV)",
    "용도: 상심실성 빈맥",
    "주의: 심 억제 강함, P-gp 억제 → ivermectin 등 P-gp 기질 약물 독성 증가",
],
"nifedipine": [
    "분류: dihydropyridine계 Ca²⁺ 채널 차단제",
    "특징: 혈관 평활근에 선택적 → 혈관 확장, 항부정맥 효과는 약함",
],
"adenosine": [
    "분류: A1 수용체 효현 항부정맥제",
    "용도: 발작성 상심실성 빈맥 — 방실결절 일시 차단",
    "특징: 반감기 약 10초, 급속 정맥 주사",
],
"isosorbide_dinitrate": [
    "분류: 작용 시간이 긴 nitrate",
    "기전: NO 공여 → 정맥·관상동맥 확장",
],
"amyl_nitrite": [
    "분류: 흡입용 단시간 작용 nitrate",
    "특징: 시안화물 중독 해독 시 methemoglobin 생성 목적으로도 이용",
],
"minoxidil": [
    "분류: K⁺ 채널 개방제(강력한 동맥 확장제)",
    "기전: 평활근 과분극 → 이완",
    "주의: 반사성 빈맥, 수분 저류",
],
"prenylamine": [
    "분류: Ca²⁺ 채널 차단 작용 협심증 약물",
    "특징: 부정맥 위험으로 퇴출",
],
"veratridine": [
    "분류: Na⁺ 채널 개방 유지 veratrum alkaloid",
    "기전: Bezold-Jarisch 반사 → 서맥·저혈압",
    "특징: 독성 식물(Veratrum) 성분",
],
"heparin": [
    "분류: 항응고제(점액다당류)",
    "기전: antithrombin III 활성화 → thrombin(IIa)·Xa 억제",
    "특징: 즉시 작용, 정맥·피하 투여, 경구 불가",
    "용도: DIC·혈전색전증 예방·치료, 체외 항응고(채혈)",
    "해독: protamine sulfate",
    "주의: 출혈, 혈소판 감소",
],
"dicumarol": [
    "분류: coumarin계 경구 항응고제",
    "특징: 곰팡이 핀 sweet clover(스위트클로버)에서 생성 → 소 'sweet clover disease'(출혈성 질환)",
    "해독: vitamin K1",
],
"warfarin": [
    "분류: 비타민 K 의존 응고인자(II, VII, IX, X) 합성 억제 경구 항응고제",
    "기전: 비타민 K epoxide reductase(VKORC1) 억제",
    "특징: 효과 발현 2~3일(factor VII 가장 먼저 감소), PT/INR로 모니터링, 단백 결합률 높아 상호작용 다수",
    "중독: 쥐약(살서제) 중독 — 해독 vitamin K1",
    "주의: 임신 시 기형",
],
"sodium_citrate_solution": [
    "분류: 채혈용 항응고제(Ca²⁺ 킬레이트)",
    "용도: 응고 검사용 채혈(혈액:citrate = 9:1), 수혈",
],
"acid_citrate_dextrose": [
    "분류: ACD 용액(혈액 보존·항응고)",
    "용도: 수혈용 혈액 보존",
],
"sodium_oxalate": [
    "분류: 채혈용 항응고제(Ca²⁺ 침전)",
    "특징: 일반적으로 fluoride와 함께 혈당 채혈에 사용",
],
"fluoride": [
    "분류: 해당 과정 억제제",
    "용도: 혈당 보존용 채혈 첨가제(NaF + oxalate)",
],
"silicone": [
    "분류: 용기 표면 도포제",
    "기전: 접촉 활성화 방지 → 응고 지연",
],
"liquid_paraffin": [
    "분류: 용기 표면 도포제(체외 항응고)",
],
"edetate_disodium": [
    "분류: EDTA — Ca²⁺ 킬레이트제",
    "용도: 혈구 검사(CBC)용 채혈관, 금속 중독 킬레이트",
    "주의: 정맥 투여 시 저칼슘혈증",
],
"hirudin": [
    "분류: 거머리 유래 thrombin 직접 억제 단백질",
],
"glutethimide": [
    "분류: 진정·최면제",
    "특징: 간 효소 유도 → warfarin 효과 감소",
],
"rifampin": [
    "분류: RNA polymerase 억제 항결핵·항균제",
    "특징: 간 효소 유도로 warfarin 효과 감소, 체액 주황색 착색",
    "용도: 말 Rhodococcus equi(erythromycin과 병용)",
],
"cholestyramine": [
    "분류: 담즙산 결합 수지",
    "기전: 장에서 warfarin 등 약물 흡수 방해",
],
"oxyphenbutazone": [
    "분류: phenylbutazone의 대사산물 NSAID",
    "특징: 단백 결합 경쟁 → 항응고제 효과 증가",
],
"disulfiram": [
    "분류: aldehyde dehydrogenase 억제제",
    "특징: warfarin 대사 억제 → 효과 증가",
],
"sulfinpyrazone": [
    "분류: 요산 배설 촉진제(항혈소판 작용)",
    "특징: warfarin 효과 증가",
],
"metronidazole": [
    "분류: 항균·항원충제(혐기성균·Giardia)",
    "기전: 환원 활성화 후 DNA 손상",
    "주의: 고용량 중추 신경 독성(운동실조·안진), 항응고제 대사 억제",
],
"trimethoprim_sulfamethoxazole": [
    "분류: 엽산 대사 순차 차단 복합 항균제",
    "주의: warfarin 효과 증가, 개 KCS·과민반응, Doberman 감수성",
],
"clofibrate": [
    "분류: 지질 강하제",
    "특징: warfarin 효과 증가",
],
"streptokinase": [
    "분류: 혈전 용해제(섬유소 용해제)",
    "기전: plasminogen과 복합체 형성 → plasmin 활성화 → fibrin 분해",
    "주의: 항원성(세균 단백) → 알레르기, 출혈",
],
"clopidogrel": [
    "분류: P2Y12 ADP 수용체 비가역 차단 항혈소판제",
    "특징: 전구약물(간 활성화)",
    "용도: 고양이 동맥 혈전색전증 예방",
],
"vitamin_k": [
    "분류: 응고인자 II·VII·IX·X 합성의 보조인자(phytonadione = K1)",
    "용도: 쥐약(coumarin) 중독, sweet clover 중독 해독",
    "특징: 효과 발현 6~12시간(합성 필요), 지방 식이와 함께 경구 투여 시 흡수 증가",
    "주의: 제2세대 살서제는 3~4주 장기 치료",
],
"bromhexine": [
    "분류: 점액 용해제",
    "기전: 점액 분비 세포 자극, 묽은 점액 분비 증가",
],
"n_acetylcysteine": [
    "분류: 점액 용해제",
    "기전: 점액 당단백 이황화(S–S) 결합 절단",
    "용도: 호흡기 점액 용해, acetaminophen 중독 해독(글루타티온 전구체)",
],
"dembrexine": [
    "분류: 말 호흡기 질환용 점액 용해제",
],
"ipecac": [
    "분류: 토근 — 저용량 거담, 고용량 구토 유발",
    "특징: emetine 함유",
],
"cocillana": [
    "분류: 식물 유래 거담제",
],
"tolu_balsam": [
    "분류: 식물 수지 거담·향미제",
],
"ammonium_bicarbonate": [
    "분류: 거담제",
    "기전: 기도 분비 증가",
],
"potassium_iodide": [
    "분류: 거담제",
    "기전: 기도 분비 증가",
    "주의: 장기 투여 시 요오드중독(iodism) — 눈물·콧물·기침·피부 각질",
],
"sodium_iodide": [
    "분류: 요오드 제제",
    "용도: 소 나무혀병(Actinobacillus lignieresii) 치료 — 정맥 투여",
    "주의: 요오드중독, 임신 동물 주의",
],
"dimenhydrinate": [
    "분류: 1세대 항히스타민제(diphenhydramine의 염)",
    "용도: 멀미·구토 억제",
    "주의: 진정",
],
"chlorpheniramine": [
    "분류: 1세대 H1 길항제",
    "용도: 알레르기·가려움",
],
"hydroxyzine": [
    "분류: 진정·항불안 작용 H1 길항제",
],
"pseudoephedrine": [
    "분류: α 효현 충혈 제거제",
    "중독: 개·고양이에서 진전·빈맥·고체온·경련 → 사람용 감기약 오식 주의",
],
"benzonatate": [
    "분류: 말초성 진해제",
    "기전: 폐 신장 수용체 둔감화",
],
"pholcodine": [
    "분류: 중추성 opioid계 진해제",
],
"noscapine": [
    "분류: 비진통성 아편 alkaloid 진해제",
],
"hydrocodone": [
    "분류: opioid 진해·진통제",
    "용도: 개 기관지염·기관허탈에 의한 기침",
    "주의: 진정, 변비",
],
"butorphanol": [
    "분류: opioid 혼합 효현-길항제(κ 효현, μ 길항)",
    "용도: 개 진해, 진정·경도 진통, 말 산통 진통",
    "특징: 천장 효과(ceiling effect) — 호흡 억제 적음",
    "특징: 길항제로 μ-opioid 효과 되돌림",
],
"maropitant": [
    "분류: NK1 수용체(substance P) 길항제",
    "용도: 개·고양이 광범위 항구토(중추·말초), 멀미",
    "특징: 24시간 작용, 주사 시 통증",
],
"aminophylline": [
    "분류: theophylline의 수용성 염(ethylenediamine)",
    "용도: 기관지 확장제 — 정맥 투여 가능",
    "주의: 치료 범위 좁음, 빈맥·경련",
],
"ibmx": [
    "분류: 비선택적 PDE 억제 methylxanthine",
    "특징: 연구용",
],
"paraxanthine": [
    "분류: caffeine의 주 대사산물 methylxanthine",
],
"pentoxifylline": [
    "분류: PDE 억제제",
    "기전: 혈액 유동성 개선, TNF-α 억제",
    "용도: 말 족부 질환·내독소혈증, 개 면역 매개 피부 질환",
],
"eucatropine": [
    "분류: 항무스카린제(산동제)",
],
"sildenafil": [
    "분류: PDE5 억제제",
    "기전: cGMP↑ → 폐혈관 평활근 이완",
    "용도: 개 폐동맥 고혈압",
],
"digitoxin": [
    "분류: 강심배당체(간 대사)",
    "특징: 작용 시간 김",
],
"gitoxin": [
    "분류: digitalis계 강심배당체",
],
"gitalin": [
    "분류: digitalis계 강심배당체 혼합물",
],
"ouabain": [
    "분류: 빠르게 작용하는 강심배당체",
    "특징: Na⁺/K⁺-ATPase 억제 연구 도구",
],
"mannitol": [
    "분류: 삼투성 이뇨제",
    "기전: 사구체 여과 후 재흡수 안 됨 → 삼투압으로 물 배설",
    "용도: 뇌압·안압 감소, 급성 신부전 예방, 일부 중독 시 배설 촉진",
    "금기: 울혈성 심부전(혈관 내 용적 증가)",
],
"acetazolamide": [
    "분류: 탄산탈수효소 억제제",
    "기전: HCO₃⁻ 재흡수 억제 → 알칼리뇨, 대사성 산증",
    "용도: 녹내장, 말 고칼륨성 주기성 마비(HYPP)",
],
"dichlorphenamide": [
    "분류: 탄산탈수효소 억제제",
    "용도: 녹내장, 말 HYPP",
],
"ethoxzolamide": [
    "분류: 탄산탈수효소 억제제",
],
"methazolamide": [
    "분류: 탄산탈수효소 억제제",
    "용도: 녹내장",
],
"chlorothiazide": [
    "분류: thiazide 이뇨제(최초)",
    "특징: 정맥 투여 가능",
],
"hydrochlorothiazide": [
    "분류: thiazide 이뇨제",
    "기전: 원위세뇨관 Na⁺-Cl⁻ 공동수송체 억제, Ca²⁺ 재흡수 증가",
    "용도: 부종·고혈압, 칼슘 결석 예방, 요붕증(역설적 항이뇨)",
    "주의: 저칼륨혈증, 고칼슘혈증, 고혈당",
],
"hydroflumethiazide": [
    "분류: thiazide 이뇨제",
],
"bendroflumethiazide": [
    "분류: 작용이 긴 thiazide 이뇨제",
],
"benzthiazide": [
    "분류: thiazide 이뇨제",
],
"trichlormethiazide": [
    "분류: thiazide 이뇨제",
],
"methyclothiazide": [
    "분류: thiazide 이뇨제",
],
"polythiazide": [
    "분류: thiazide 이뇨제",
],
"cyclothiazide": [
    "분류: thiazide 이뇨제",
],
"chlorthalidone": [
    "분류: thiazide계 이뇨제(작용 시간 김)",
],
"metolazone": [
    "분류: thiazide계 이뇨제",
    "특징: 신기능 저하 시에도 효과 → loop 이뇨제와 병용",
],
"quinethazone": [
    "분류: thiazide계 이뇨제",
],
"indapamide": [
    "분류: thiazide계 이뇨제 + 혈관 확장 작용",
],
"triamterene": [
    "분류: 칼륨 보존성 이뇨제",
    "기전: 집합관 Na⁺ 채널(ENaC) 차단",
    "주의: 고칼륨혈증",
],
"amiloride": [
    "분류: 칼륨 보존성 이뇨제",
    "기전: 집합관 Na⁺ 채널(ENaC) 차단",
    "주의: 고칼륨혈증",
],
"ethacrynic_acid": [
    "분류: loop 이뇨제(sulfa 구조 없음)",
    "주의: 이독성 큼",
],
"bumetanide": [
    "분류: loop 이뇨제",
    "특징: furosemide보다 강력(약 40배)",
],
"muzolimine": [
    "분류: loop 이뇨제 계열",
],
"torsemide": [
    "분류: 작용 시간이 긴 loop 이뇨제",
    "용도: furosemide 저항성 심부전 개",
],
"ammonium_chloride": [
    "분류: 요 산성화제",
    "용도: 스트루바이트 결석 예방·용해(고양이·소·양)",
    "주의: 대사성 산증",
],
"calcium_chloride": [
    "분류: 요 산성화 염",
    "용도: 저칼슘혈증 응급(정맥, 심장 청진하며 서서히)",
    "주의: 혈관 외 유출 시 조직 괴사",
],
"sodium_phosphate": [
    "분류: 요 산성화 염",
    "특징: 완하 효과도 있음",
],
"ascorbic_acid": [
    "분류: 비타민 C(요 산성화 보조)",
],
"methionine": [
    "분류: 황 함유 아미노산(요 산성화)",
    "용도: 스트루바이트 결석 예방",
],
"sodium_bicarbonate": [
    "분류: 중탄산나트륨(알칼리화제·제산제)",
    "용도: 대사성 산증 교정, 요 알칼리화(산성 약물·독물 배설 촉진), 위산 중화",
    "주의: 반동성 산 분비, Na⁺ 부하, 알칼리증",
],
"citrate": [
    "분류: 구연산염(요 알칼리화제)",
    "용도: 요산·칼슘 결석 예방",
],
"oxazepam": [
    "분류: benzodiazepine",
    "용도: 식욕 촉진(고양이)",
],
"mirtazapine": [
    "분류: α2·5-HT3 길항제",
    "용도: 식욕 촉진, 항구토 — 고양이 경피 제제도 사용",
    "주의: 신장·간 배설(신부전 시 감량)",
],
"dirlotapide": [
    "분류: 장 상피 MTP(microsomal triglyceride transfer protein) 억제제",
    "기전: 지방 흡수·킬로미크론 형성 감소 + 포만감",
    "용도: 개 비만 치료",
],
"homatropine": [
    "분류: 항무스카린제(atropine 유사)",
],
"methylatropine_nitrate": [
    "분류: 4차 암모늄 항무스카린제",
],
"methantheline_bromide": [
    "분류: 4차 암모늄 항무스카린제(위장관 진경)",
],
"burimamide": [
    "분류: 초기 H2 길항제",
    "특징: 연구용, 임상 사용 안 함",
],
"metiamide": [
    "분류: 초기 H2 길항제",
    "특징: 독성(과립구 감소)으로 cimetidine으로 대체",
],
"nizatidine": [
    "분류: H2 길항제",
],
"omeprazole": [
    "분류: 양성자 펌프 억제제(PPI)",
    "기전: H⁺/K⁺-ATPase 비가역 억제 → 위산 분비 억제 가장 강함",
    "용도: 말 위궤양(EGUS), 개·고양이 위식도 역류·위궤양",
],
"pantoprazole": [
    "분류: 양성자 펌프 억제제(PPI)",
    "특징: 정맥 투여 가능",
],
"calcium_carbonate": [
    "분류: 제산제(위산 중화)",
    "주의: 반동성 산 분비, 고칼슘혈증",
],
"aluminum_hydroxide": [
    "분류: 제산제(위산 중화)",
    "특징: 변비, 인산 결합제로 신부전 고인산혈증에도 사용",
],
"magnesium_trisilicate": [
    "분류: 제산제",
],
"misoprostol": [
    "분류: PGE1 유도체",
    "기전: 위산 분비 억제 + 점액·HCO₃⁻ 분비 증가(점막 보호)",
    "용도: NSAID 위궤양 예방·치료",
    "금기: 임신(유산 유발)",
],
"sucralfate": [
    "분류: 점막 보호제",
    "기전: 산성 환경에서 궤양 부위 단백질에 결합해 보호막 형성",
    "주의: 다른 약물 흡수 방해 → 투여 간격 필요, 산성 환경 필요(PPI·H2 병용 효과 감소)",
],
"isopropamide": [
    "분류: 항무스카린 진경·항구토제",
],
"prochlorperazine": [
    "분류: phenothiazine계 항구토제(D2 길항)",
    "주의: 저혈압, 진정",
],
"haloperidol": [
    "분류: butyrophenone계 D2 길항제",
    "용도: 항구토, 신경이완",
],
"dolasetron": [
    "분류: 5-HT3 길항 항구토제",
],
"lactulose": [
    "분류: 비흡수성 이당류 삼투성 완화제",
    "용도: 변비, 간성 뇌증(대장 산성화로 NH₃를 NH₄⁺로 포집)",
    "주의: 가스 발생·설사",
],
"polyethylene_glycol": [
    "분류: 삼투성 완화제",
    "용도: 장 세척, 변비",
],
"sodium_sulfate": [
    "분류: 염류 설사제",
    "용도: 반추동물 소화관 내용물 이동·독물 배설",
],
"magnesium_sulfate": [
    "분류: 염류 설사제(Epsom salt)",
    "용도: 소·말 변비·장 내용물 이동",
    "주의: 탈수, 고마그네슘혈증",
],
"magnesium_hydroxide": [
    "분류: 제산제·삼투성 완화제",
    "용도: 반추위 산증(제산), 변비",
],
"erythromycin": [
    "분류: macrolide 항생제",
    "특징: 저용량에서 motilin 수용체 효현으로 위·장 운동 촉진",
    "용도: 망아지 Rhodococcus equi 폐렴(rifampin 병용), 개·고양이 위 배출 촉진",
    "주의: 성체 말에서 항생제 관련 장염(대장염) 위험",
],
"vasopressin": [
    "분류: ADH(arginine vasopressin)",
    "작용: 신장 수분 재흡수(V2), 혈관 수축(V1), 평활근 수축",
    "용도: 요붕증(desmopressin), 쇼크 시 승압",
],
"tetrodotoxin": [
    "분류: Na⁺ 채널 차단 신경독(복어독)",
    "기전: 채널 외측 구멍을 막아 활동전위 차단",
    "중독: 마비·호흡 정지",
],
"phlorhizin": [
    "분류: SGLT(Na⁺-포도당 공동수송체) 억제제",
    "기전: 신장 포도당 재흡수 억제 → 당뇨(glucosuria)",
    "특징: SGLT2 억제제의 원형",
],
"tetraethylammonium": [
    "분류: K⁺ 채널·신경절 차단제",
    "특징: 연구용",
],
"edta": [
    "분류: Ca²⁺·금속 킬레이트제",
    "용도: 금속 중독 킬레이트 요법(Ca-EDTA), 혈구 검사용 채혈관",
    "주의: 정맥 투여 시 저칼슘혈증",
],
"sometribove": [
    "분류: 재조합 소 성장호르몬(rBST)",
    "용도: 젖소 비유량 증가",
    "특징: 효과는 IGF-1 매개",
],
"pmsg": [
    "분류: 임마혈청성 성선자극호르몬(eCG)",
    "기전: FSH·LH 활성 → 난포 발달·과배란 유도",
    "특징: 반감기 길고 임신한 말 혈청에서 추출",
],
"hcg": [
    "분류: 사람 융모성 성선자극호르몬",
    "기전: LH 유사 작용 → 배란 유도·황체 형성",
],
"domperidone": [
    "분류: 말초 D2 길항제",
    "기전: 프롤락틴 분비 증가 → 비유 촉진",
    "용도: 말 fescue 중독 암말의 비유 부전·태반 비후, 개 비유 촉진",
],
"oxytocin": [
    "분류: 뇌하수체 후엽 호르몬",
    "작용: 자궁 수축, 유선 근상피세포 수축(유즙 배출)",
    "용도: 분만 유도·분만 촉진, 후산 정체, 산후 출혈, 유즙 배출 촉진",
    "금기: 산도 폐쇄(기계적 난산)",
    "특징: 자궁 민감성은 estrogen이 증가, progesterone이 억제",
],
"melatonin": [
    "분류: 송과체 호르몬",
    "특징: 어두울 때 분비 — 계절 번식·수면 조절",
],
"thyroid": [
    "분류: 건조 갑상선 추출물",
    "용도: 갑상선 호르몬 보충",
],
"levothyroxine_sodium": [
    "분류: 합성 T4",
    "용도: 개 갑상선 기능 저하증 1차 치료제",
    "주의: 과량 시 갑상선 기능 항진 증상",
],
"liothyronine_sodium": [
    "분류: 합성 T3",
    "특징: 작용 빠르고 짧음",
],
"liotrix": [
    "분류: T4와 T3 복합 제제",
],
"iodine_casein": [
    "분류: 요오드화 카제인",
    "특징: 갑상선 호르몬 보충제로 쓰이던 약물",
],
"thiouracil": [
    "분류: 항갑상선 약물",
    "기전: 갑상선 peroxidase 억제 → 호르몬 합성 억제",
],
"methylthiouracil": [
    "분류: 항갑상선 약물(thiouracil계)",
    "용도: 갑상선 기능 항진증 치료",
],
"propylthiouracil": [
    "분류: 항갑상선 약물",
    "기전: 호르몬 합성 억제 + 말초 T4 → T3 전환 억제",
    "주의: 고양이에서 용혈성 빈혈·혈소판 감소",
],
"methimazole": [
    "분류: 항갑상선 약물(thioamide)",
    "용도: 고양이 갑상선 기능 항진증 치료",
    "주의: 소양증·안면 긁기, 구토, 호산구 증가, 혈구 감소, 간독성",
],
"sulfaguanidine": [
    "분류: sulfonamide",
    "특징: 갑상선 호르몬 합성 억제 작용 있음(항갑상선 작용)",
],
"phenylthiourea": [
    "분류: thiourea계 항갑상선 물질",
],
"ipodate": [
    "분류: 요오드 조영제",
    "기전: 말초 T4 → T3 전환 억제",
],
"radioactive_iodine_na131i": [
    "분류: 방사성 요오드(¹³¹I)",
    "기전: 갑상선에 집적되어 β선으로 조직 파괴",
    "용도: 고양이 갑상선 기능 항진증 근치 치료",
],
"calcitonin": [
    "분류: 갑상선 C세포 호르몬",
    "기전: 뼈 흡수 억제 → 혈중 Ca²⁺ 감소",
],
"parathyroid_hormone": [
    "분류: 부갑상선 호르몬(PTH)",
    "기전: 뼈 흡수↑, 신장 Ca²⁺ 재흡수↑·인 배설↑, 비타민 D 활성화 → 혈중 Ca²⁺ 증가",
    "특징: 저칼슘혈증에 의해 분비 증가",
],
"calcium_gluconate": [
    "분류: 칼슘 보충제",
    "용도: 저칼슘혈증 응급(개 eclampsia, 젖소 산욕열), 고칼륨혈증 심독성 길항",
    "주의: 정맥 투여 시 서서히 + 심장 청진(서맥·부정맥), 혈관 외 유출 시 조직 괴사",
    "금기: digitalis 병용",
],
"calcium_borogluconate": [
    "분류: 칼슘 보충제",
    "용도: 젖소 산욕열(milk fever) 등 저칼슘혈증",
    "주의: 정맥 투여 시 서서히 + 심장 청진",
],
"dihydrotachysterol": [
    "분류: 비타민 D 유사체",
    "용도: 부갑상선 기능 저하증의 저칼슘혈증",
],
"calcitriol": [
    "분류: 활성형 비타민 D(1,25-(OH)₂D₃)",
    "기전: 장의 Ca²⁺·인 흡수 증가",
    "용도: 만성 신부전 이차성 부갑상선 기능 항진증",
],
"insulin": [
    "분류: 췌장 β세포 호르몬",
    "기전: GLUT4 이동 → 포도당 흡수, 글리코겐·지방·단백 합성 촉진, K⁺ 세포 내 이동",
    "용도: 당뇨병(개·고양이), 고칼륨혈증 보조 치료",
    "주의: 저혈당(과량·식이 불규칙) — 포도당·glucagon 투여",
],
"glipizide": [
    "분류: sulfonylurea",
    "기전: β세포 K-ATP 채널 차단 → 인슐린 분비 촉진(β세포 기능이 남아 있어야 함)",
    "용도: 고양이 NIDDM 일부",
],
"glyburide": [
    "분류: sulfonylurea",
    "기전: 인슐린 분비 촉진",
],
"glimepiride": [
    "분류: 작용 시간이 긴 sulfonylurea",
],
"metformin": [
    "분류: 경구 혈당강하제(biguanide)",
    "기전: 간 포도당 신생 억제, 인슐린 감수성 개선",
    "특징: 수의학 사용 제한적, 젖산증 주의",
],
"glucagon": [
    "분류: 췌장 α세포 호르몬",
    "기전: 간 글리코겐 분해·포도당 신생 → 혈당 상승",
    "용도: 저혈당 응급, insulinoma 진단·치료 보조",
],
"corticosterone": [
    "분류: 내인성 글루코코르티코이드",
    "특징: 설치류·조류에서 주된 형태",
],
"deoxycorticosterone": [
    "분류: 내인성 무기질코르티코이드",
    "용도: Addison병 대치(DOCP, 장기 작용 pivalate 제제)",
],
"aldosterone": [
    "분류: 주된 무기질코르티코이드",
    "기전: 신장 Na⁺ 재흡수·K⁺ 배설 촉진 → 수분 저류",
    "특징: 분비는 angiotensin II·혈중 K⁺ 증가가 자극",
],
"fludrocortisone": [
    "분류: 합성 무기질코르티코이드(글루코코르티코이드 작용도 있음)",
    "용도: 개 Addison병 대치",
    "주의: 다뇨·다음, 저칼륨혈증",
],
"methylprednisolone": [
    "분류: 합성 글루코코르티코이드(중간 작용)",
    "특징: methylprednisolone acetate는 장시간 작용 주사제(고양이 등)",
],
"triamcinolone": [
    "분류: 합성 글루코코르티코이드(중간 작용, 무기질코르티코이드 작용 없음)",
    "용도: 관절 내·병변 내 주사",
    "주의: 말에서 편자병(laminitis) 위험 보고",
],
"flumethasone": [
    "분류: 강력한 합성 글루코코르티코이드",
],
"ddt": [
    "분류: 유기염소계 살충제(o,p'-DDD가 mitotane)",
    "특징: 부신 피질 억제 작용 연구",
],
"amphenone_b": [
    "분류: 부신 스테로이드 합성 억제 약물",
    "특징: 연구용",
],
}
