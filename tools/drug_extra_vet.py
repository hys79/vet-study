"""수의 임상에서 자주 쓰이는데 교재 DB에 없는 약물(추가분). 형식은 drug_extra.py 와 같음."""
EXTRA_VET = {
    "tiletamine": {
        "n": "tiletamine", "a": ["Telazol", "Zoletil(zolazepam 복합)"],
        "info": [
            "분류: 해리성 마취제(NMDA 길항, ketamine 유사체)",
            "기전: NMDA 수용체 길항 → 해리성 마취·진통",
            "용도: zolazepam과 1:1 복합제로 개·고양이·야생동물의 불동화·마취(근육 주사 가능)",
            "특징: ketamine보다 강력하고 작용 시간이 길며, zolazepam이 근경직·경련을 억제",
            "주의: 고양이는 신배설이라 신부전 시 회복 지연, 개는 회복기 흥분 가능",
        ],
    },
    "buprenorphine": {
        "n": "buprenorphine", "a": ["Buprenex"],
        "info": [
            "분류: opioid 부분 μ 효현제(κ 길항)",
            "기전: μ 수용체에 친화력이 높고 내재 활성은 낮음",
            "용도: 고양이 중등도 통증(경구점막 투여가 효과적), 개 진통·마취 전 투약",
            "특징: 천장 효과로 호흡 억제 적음, 작용 지속 6~8시간",
            "주의: 친화력이 높아 naloxone으로 길항이 어렵고, 완전 μ 효현제와 병용하면 효과 감소",
        ],
    },
    "tramadol": {
        "n": "tramadol",
        "info": [
            "분류: 비전형 opioid(약한 μ 효현 + 세로토닌·NE 재흡수 억제)",
            "기전: 활성 대사산물 M1(O-desmethyltramadol)이 μ 수용체에 작용",
            "용도: 개·고양이 만성·신경병증성 통증 보조",
            "특징: 개는 M1 생성이 적어 진통 효과 변동이 크고, 고양이는 M1이 많아 효과가 비교적 일정",
            "주의: 세로토닌 증후군(SSRI·TCA·MAOI 병용), 경련 역치 감소, 진정",
        ],
    },
    "hydromorphone": {
        "n": "hydromorphone",
        "info": [
            "분류: opioid 완전 μ 효현제(morphine 유도체, 효력 약 5~10배)",
            "용도: 개·고양이 중등도~중증 통증, 마취 전 투약",
            "주의: 구토(개), 호흡 억제, 고양이 고체온증 보고",
        ],
    },
    "nalbuphine": {
        "n": "nalbuphine",
        "info": [
            "분류: opioid 혼합 효현-길항제(κ 효현, μ 길항)",
            "용도: 경도~중등도 통증, 진정, μ 효현제 과량 시 호흡 억제 완화",
            "특징: 천장 효과(호흡 억제 적음), 진통 작용은 butorphanol과 유사",
        ],
    },
    "levetiracetam": {
        "n": "levetiracetam", "a": ["Keppra"],
        "info": [
            "분류: 항경련제(SV2A 시냅스 소포 단백 결합)",
            "용도: 개·고양이 간질 보조(phenobarbital 병용), 중첩 발작 정맥 투여",
            "특징: 간 대사가 적어 약물 상호작용·간독성이 적고, 반감기가 짧아 서방정을 쓰기도 함",
            "주의: 진정·운동 실조(경미)",
        ],
    },
    "zonisamide": {
        "n": "zonisamide",
        "info": [
            "분류: sulfonamide계 항경련제(Na⁺ · T형 Ca²⁺ 채널 차단)",
            "용도: 개 간질 단독·보조 요법",
            "주의: sulfonamide 과민반응(KCS, 간독성), 식욕 부진·진정",
        ],
    },
    "trazodone": {
        "n": "trazodone",
        "info": [
            "분류: SARI(5-HT2 길항 + 세로토닌 재흡수 억제) 항불안제",
            "용도: 개 수술 후 안정·병원 방문 불안·분리 불안 보조, 고양이 불안",
            "주의: 진정·운동 실조, 세로토닌 증후군(SSRI·TCA·MAOI 병용 금기)",
        ],
    },
    "flumazenil": {
        "n": "flumazenil",
        "info": [
            "분류: benzodiazepine 수용체 길항제",
            "용도: diazepam·midazolam·zolazepam 과량 해독",
            "특징: 작용 시간이 짧아 재진정(resedation)이 생기면 반복 투여",
            "주의: 장기 benzodiazepine 투여 동물에서 경련 위험",
        ],
    },
    "dantrolene": {
        "n": "dantrolene",
        "info": [
            "분류: 직접 작용 근이완제",
            "기전: 근소포체 ryanodine 수용체 억제 → Ca²⁺ 유리 감소 → 수축력 감소",
            "용도: 악성 고열(돼지 등) 치료·예방",
            "주의: 간독성",
        ],
    },
    "pralidoxime": {
        "n": "pralidoxime", "a": ["2-PAM"],
        "info": [
            "분류: AChE 재활성화제(oxime)",
            "기전: 인산화된 AChE에서 유기인을 분리해 효소를 재활성화",
            "용도: 유기인 중독 해독(atropine과 병용)",
            "주의: 시간이 지나면 aging으로 효과 감소, carbamate 중독에는 불필요",
        ],
    },
    "protamine_sulfate": {
        "n": "protamine sulfate",
        "info": [
            "분류: heparin 해독제(양이온성 단백)",
            "기전: 음전하 heparin과 결합해 중화",
            "용도: heparin 과량 해독",
            "주의: 과민반응·저혈압, 과량 투여 시 자체 항응고 작용",
        ],
    },
    "enrofloxacin": {
        "n": "enrofloxacin", "a": ["Baytril"],
        "info": [
            "분류: fluoroquinolone계(수의 전용으로 개발)",
            "기전: DNA gyrase·topoisomerase IV 억제(농도 의존성 살균)",
            "용도: 개·고양이·가금·소·돼지의 그람음성균·마이코플라스마 감염",
            "주의: 어린 동물 연골 손상, 고양이 고용량 망막 변성, 제산제의 금속 이온과 킬레이트",
            "특징: 개에서 일부가 ciprofloxacin으로 대사",
        ],
    },
    "marbofloxacin": {
        "n": "marbofloxacin",
        "info": [
            "분류: fluoroquinolone계",
            "용도: 개·고양이 요로·피부·호흡기 감염",
            "주의: 어린 동물 연골 손상, 고양이 망막 변성(권장 용량 이내 사용)",
        ],
    },
    "florfenicol": {
        "n": "florfenicol",
        "info": [
            "분류: Phenicol계(chloramphenicol의 불소 유도체)",
            "기전: 50S 리보솜 억제(정균)",
            "용도: 소 호흡기병(BRD)·돼지·어류 감염, 식용동물에 허용",
            "특징: chloramphenicol의 재생불량성 빈혈 위험이 없음",
        ],
    },
    "azithromycin": {
        "n": "azithromycin",
        "info": [
            "분류: macrolide계(azalide)",
            "용도: 개·고양이 호흡기 감염, Mycoplasma·Bartonella 등",
            "특징: 조직 농도가 높고 반감기가 길어 짧은 기간 투여",
            "주의: 구토",
        ],
    },
    "cefazolin": {
        "n": "cefazolin",
        "info": [
            "분류: cephalosporin 1세대(주사)",
            "용도: 수술 전 예방적 항생제",
            "특징: 그람양성균 위주, 혐기균에는 약함",
        ],
    },
    "cefpodoxime": {
        "n": "cefpodoxime",
        "info": [
            "분류: cephalosporin 3세대(경구)",
            "용도: 개 농피증(피부 감염)·요로 감염",
        ],
    },
    "cefovecin": {
        "n": "cefovecin", "a": ["Convenia"],
        "info": [
            "분류: cephalosporin 3세대(장기 지속 주사)",
            "용도: 개·고양이 피부·연조직·요로 감염(1회 주사로 약 14일)",
            "특징: 단백 결합이 높아 반감기가 길다(개 약 5일, 고양이 약 7일)",
            "주의: 이상 반응이 생겨도 약이 오래 남음, 과민반응",
        ],
    },
    "tulathromycin": {
        "n": "tulathromycin",
        "info": [
            "분류: macrolide계(triamilide)",
            "용도: 소·돼지 호흡기병, 1회 피하 주사",
            "주의: 주사 부위 부종, 식용동물 휴약기 준수",
        ],
    },
    "robenacoxib": {
        "n": "robenacoxib",
        "info": [
            "분류: 선택적 COX-2 억제제(NSAID)",
            "용도: 고양이·개 수술 후·급성 근골격계 통증과 염증(단기)",
            "특징: 혈중 반감기는 짧지만 염증 부위에 오래 남음",
        ],
    },
    "grapiprant": {
        "n": "grapiprant",
        "info": [
            "분류: 선택적 EP4(PGE2 수용체) 길항제 — COX 억제제가 아님",
            "용도: 개 골관절염 통증·염증",
            "특징: NSAID보다 위장관·신장 부작용이 적다고 알려짐(구토·설사는 가능)",
        ],
    },
    "afoxolaner": {
        "n": "afoxolaner",
        "info": [
            "분류: isoxazoline계 외부 기생충 구제제",
            "기전: 곤충·진드기의 GABA·glutamate 개폐 Cl⁻ 채널 차단 → 과흥분·사멸(포유류에 선택독성)",
            "용도: 개 벼룩·진드기·모낭충, 경구 월 1회",
            "주의: 경련 병력이 있는 개에서 주의",
        ],
    },
    "fluralaner": {
        "n": "fluralaner",
        "info": [
            "분류: isoxazoline계 외부 기생충 구제제",
            "기전: 곤충·진드기의 GABA 개폐 Cl⁻ 채널 차단",
            "용도: 개·고양이 벼룩·진드기, 경구 투여는 약 12주 지속",
            "주의: 경련 병력이 있는 동물에서 주의",
        ],
    },
    "fipronil": {
        "n": "fipronil",
        "info": [
            "분류: phenylpyrazole계 살충제",
            "기전: 곤충 GABA_A Cl⁻ 채널 차단 → 과흥분",
            "용도: 개·고양이 벼룩·진드기(spot-on, 분무)",
            "주의: 토끼에서 독성이 높아 사용 금지",
        ],
    },
    "imidacloprid": {
        "n": "imidacloprid",
        "info": [
            "분류: neonicotinoid계 살충제",
            "기전: 곤충 nAChR 효현 → 지속 탈분극·마비(포유류 선택독성 높음)",
            "용도: 개·고양이 벼룩 구제(spot-on)",
        ],
    },
    "amitraz": {
        "n": "amitraz",
        "info": [
            "분류: formamidine계 살진드기제",
            "기전: 진드기 octopamine 수용체 효현, 포유류에서는 α2 효현·MAO 억제 작용",
            "용도: 개 모낭충증(약욕), 진드기 목걸이",
            "주의: 진정·서맥·고혈당, MAOI·α2 효현제 병용 주의, 고양이·말 독성",
            "해독: atipamezole, yohimbine",
        ],
    },
    "permethrin": {
        "n": "permethrin",
        "info": [
            "분류: pyrethroid계 살충제",
            "기전: 곤충 Na⁺ 채널 불활성화 지연 → 지속 탈분극·경련·마비",
            "용도: 개 벼룩·진드기 구제",
            "주의: 고양이에서 진전·경련 중독(농축 제품)",
        ],
    },
    "lufenuron": {
        "n": "lufenuron",
        "info": [
            "분류: 곤충 성장 조절제(IGR, chitin 합성 억제)",
            "용도: 개·고양이 벼룩 알·유충 발달 억제(월 1회), 성충에는 효과 없음",
        ],
    },
    "closantel": {
        "n": "closantel",
        "info": [
            "분류: salicylanilide계 구충제",
            "기전: 산화적 인산화 탈공역 → ATP 합성 차단",
            "용도: 반추동물 간질(Fasciola)·Haemonchus 구제",
            "주의: 과량 시 시신경 손상(실명)",
        ],
    },
    "toltrazuril": {
        "n": "toltrazuril",
        "info": [
            "분류: triazinetrione계 항콕시듐제",
            "기전: 콕시듐 세포 분열·핵 분열 억제(모든 생활사 단계에 작용)",
            "용도: 돼지·송아지·가금 콕시듐증, 개 이소스포라",
            "주의: 식용동물 휴약기 준수",
        ],
    },
    "oclacitinib": {
        "n": "oclacitinib", "a": ["Apoquel"],
        "info": [
            "분류: JAK1 억제제",
            "기전: IL-31 등 소양·염증 사이토카인 신호 차단",
            "용도: 개 알레르기·아토피 피부염의 소양증",
            "주의: 면역 억제(감염·모낭충 악화), 12개월 미만 개 금기",
        ],
    },
    "capromorelin": {
        "n": "capromorelin",
        "info": [
            "분류: ghrelin 수용체 효현제",
            "용도: 개 식욕 부진, 고양이 만성 신장병의 체중 유지",
            "주의: 구토·설사·침 흘림",
        ],
    },
    "desmopressin": {
        "n": "desmopressin", "a": ["DDAVP"],
        "info": [
            "분류: ADH(vasopressin) 합성 유사체 — V2 선택, 혈압 작용 적음",
            "용도: 중추성 요붕증, 개 von Willebrand병 지혈",
            "주의: 수분 중독(저나트륨혈증)",
        ],
    },
    "aglepristone": {
        "n": "aglepristone",
        "info": [
            "분류: 프로게스테론 수용체 길항제",
            "용도: 개 임신 중절, 자궁축농증 내과적 치료, 분만 유도",
            "주의: 임신 중기 이후 유산 시 태아 배출",
        ],
    },
    "telmisartan": {
        "n": "telmisartan",
        "info": [
            "분류: 안지오텐신 수용체 차단제(ARB)",
            "용도: 고양이 단백뇨 동반 만성 신장병·고혈압",
            "주의: 고칼륨혈증, 저혈압, 임신 금기",
        ],
    },
    "phenylpropanolamine": {
        "n": "phenylpropanolamine",
        "info": [
            "분류: 간접 + 직접 작용 α 효현제(교감신경 흥분제)",
            "기전: 방광 경부·요도 괄약근 평활근 수축",
            "용도: 개 요도 괄약근 기능부전성 요실금",
            "주의: 고혈압·빈맥·불안, 고혈압·심질환 동물 주의",
        ],
    },
}
