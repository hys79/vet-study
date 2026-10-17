"""추가 약물(2차)과 별칭. 형식은 drug_extra.py 와 같음.
ALIAS: 이미 있는 약물의 다른 이름 — albuterol은 salbutamol(미국식 이름), meperidine은 pethidine(별칭으로 이미 등록)."""
ALIAS = {
    "salbutamol": ["albuterol"],
}

EXTRA_MORE = {
    "histamine": {
        "n": "histamine",
        "info": [
            "분류: 내인성 아민(autacoid), H1 · H2 수용체 효현제",
            "기전: 비만세포·호염기구에 저장되며 항원(IgE) 자극 시 탈과립으로 방출",
            "특징: H1은 평활근 수축·혈관 투과성↑·가려움, H2는 위산 분비↑·심장 자극을 매개하고, 알레르기·아나필락시스의 핵심 매개물질",
            "용도: 치료약이 아님 — 피내 알레르기 반응의 양성 대조, 위산 분비 검사(역사적 용도)",
            "주의: 투여 시 저혈압·기관지 수축·홍조·위산 분비 증가",
        ],
    },
    "oxymorphone": {
        "n": "oxymorphone", "a": ["oxymorphine"],
        "info": [
            "분류: opioid 완전 μ 효현제(morphine 유도체)",
            "특징: morphine보다 효력이 약 5~10배 강하고, 히스타민 유리·구토가 적음. 진정 작용이 강함",
            "용도: 개·고양이 중등도~중증 통증, 마취 전 투약, neuroleptanalgesia",
            "주의: 호흡 억제·서맥, 개는 헐떡임(panting), 고양이·말은 고용량에서 흥분 가능",
        ],
    },
    "carfentanil": {
        "n": "carfentanil",
        "info": [
            "분류: opioid 완전 μ 효현제(fentanyl 유도체, 극강 효력)",
            "특징: morphine의 약 10,000배 효력. 대형·야생동물 불동화에 쓰며 일반 동물병원 약이 아님",
            "주의: 사람 노출(피부·흡입)은 치명적이므로 취급자 안전(보호 장비, naloxone 상비) 필수",
            "주의: 호흡 억제·근경직·체온 상승, 길항제 naloxone·diprenorphine",
        ],
    },
    "mezlocillin": {
        "n": "mezlocillin",
        "info": [
            "분류: ureidopenicillin(광범위 항녹농균 penicillin)",
            "기전: PBP 결합 → 세포벽 합성 억제(살균)",
            "용도: Pseudomonas·Klebsiella 등 그람음성균 감염(주사). 수의에서는 사용이 드묾",
            "특징: β-lactamase에 분해되므로 β-lactamase 억제제와의 병용이 의미 있음",
            "주의: penicillin 교차 과민반응, 고용량에서 혈소판 기능 저하·출혈 경향",
        ],
    },
}
