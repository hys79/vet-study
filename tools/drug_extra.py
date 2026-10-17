"""교재 DB(pharmacology_data)에 없어서 직접 추가한 약물. 형식: id → {"n": 표시 이름, "a": [별칭], "info": [개조식 항목]}
분류는 pharma_cats_a.py, 용도는 pharma_uses.py 에서 연결한다."""
EXTRA = {
    "atipamezole": {
        "n": "atipamezole",
        "a": ["Antisedan"],
        "info": [
            "분류: 선택적 α2 길항제(합성 imidazole 유도체)",
            "기전: α2 수용체를 경쟁적으로 차단해 α2 효현제의 진정·진통·서맥 작용을 빠르게 되돌림",
            "용도: medetomidine·dexmedetomidine(개·고양이) 해독, xylazine·detomidine 등 α2 효현제 진정 길항, 야생동물 마취 회복",
            "특징: yohimbine·tolazoline보다 α2 선택성이 높고 작용 발현이 빠름(근육 주사 후 수 분)",
            "주의: 진정과 함께 진통 효과도 사라지므로 통증이 있는 시술 후에는 진통제 필요",
            "주의: 너무 빨리 투여하면 흥분·떨림·빈맥·일시적 저혈압, α2 효현제 투여 직후(약 30~40분 이내) 길항은 피함",
        ],
    },
}

from drug_extra_vet import EXTRA_VET   # 수의 임상 추가 약물
EXTRA.update(EXTRA_VET)
