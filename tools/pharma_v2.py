"""분류 체계 재구성(통일된 틀) — build_pharma.py 가 호출한다.

원칙
 1) 접는 단계는 '계열 > 약물군(탭)' 2단만. 약물군 안의 세부 분류는 소제목 + 약물 칩. (단원은 접지 않는 작은 머리글)
 2) 약물군마다 분류 기준 하나(b). 수용체형 약물군은 '수용체 × 효현제/길항제' 표(cols)로 통일.
 3) 약물마다 주 분류는 한 곳(d). 다른 약물군에서 보여 줄 약물은 참조(x), 여러 용도는 용도 태그(pharma_uses.py)로 연결.
 4) '참고' 상자는 약물군마다 하나(ref_v2.py)
정의 파일: pharma_cats_a.py · pharma_cats_b.py(약물군) / pharma_uses.py(용도) / ref_v2.py(핵심 정리)
"""
from pharma_cats_a import CATS_A
from pharma_cats_b import CATS_B
from pharma_uses import USES
from ref_v2 import REF_FAM, REF_CAT

FAMILIES_V2 = [
    {"id": "auto", "name": "자율신경계", "icon": "⚡"},
    {"id": "cns", "name": "중추신경계", "icon": "🧠"},
    {"id": "autacoid", "name": "오타코이드 · 염증", "icon": "🔥"},
    {"id": "circ", "name": "순환 · 신장계", "icon": "❤️"},
    {"id": "resp", "name": "호흡기계", "icon": "🫁"},
    {"id": "gi", "name": "소화기계", "icon": "🍽️"},
    {"id": "endo", "name": "대사 · 내분비", "icon": "🧪"},
    {"id": "infect", "name": "항감염제", "icon": "🦠"},
    {"id": "parasite", "name": "항기생충 · 살충제", "icon": "🐛"},
    {"id": "onco", "name": "항암 · 면역", "icon": "🎗️"},
]


def build_v2(drugs, old_cats, old_groups):
    CATS = CATS_A + CATS_B
    old_cat = {c["i"]: c for c in old_cats}
    old_by_cat = {}
    for g in old_groups:
        old_by_cat.setdefault(g["c"], []).append(g)
    old_grp = {(g["c"], g["g"]): g for g in old_groups}
    all_old = {x for g in old_groups for x in g["d"]}

    seen = {}
    cats, groups = [], []
    for c in CATS:
        secs = c["sections"]
        nc = {"i": c["id"], "n": c["n"], "u": c["unit"], "b": c["b"]}
        if c.get("cols"): nc["cols"] = c["cols"]
        det = {}
        for oc in c.get("old", []):
            for k, v in (old_cat[oc].get("d") or {}).items():
                if k in det and isinstance(det[k], dict) and isinstance(v, dict): det[k].update(v)
                else: det.setdefault(k, v)
        if det: nc["d"] = det
        if c["id"] in REF_CAT: nc["ref"] = REF_CAT[c["id"]]
        cats.append(nc)

        infos = [{} for _ in secs]
        for k, s in enumerate(secs):                                  # 명시한 원문 가져오기
            for ref in s["info"]:
                src = old_grp[(ref[1], ref[2])].get("i") if ref[0] == "grp" else old_cat[ref[1]].get("d")
                infos[k].update(src or {})
        for oc in c.get("old", []):                                   # 자동: 원래 분류의 기전·특징을 가장 많이 겹치는 섹션에 붙임
            for og in old_by_cat.get(oc, []):
                if not og.get("i") or not og["d"]: continue
                score = [len(set(og["d"]) & (set(s["d"]) | set(s["x"]))) for s in secs]
                best = max(range(len(secs)), key=lambda k: score[k])
                if score[best] >= max(1, 0.5 * len(og["d"])): infos[best].update(og["i"])

        for k, s in enumerate(secs):
            for x in s["d"]:
                assert x in drugs, "DB에 없는 약물: " + x
                seen.setdefault(x, []).append(c["id"] + ":" + s["g"])
            g2 = {"c": c["id"], "g": s["g"], "d": list(s["d"])}
            if s["t"]: g2["t"] = s["t"]
            if s["a"]: g2["a"] = s["a"]
            if s["h"]: g2["h"] = s["h"]
            if s["sb"]: g2["sb"] = s["sb"]
            if s["x"]: g2["x"] = list(s["x"])
            if infos[k]: g2["i"] = infos[k]
            groups.append(g2)

    dup = {x: v for x, v in seen.items() if len(v) > 1}
    assert not dup, "한 약물이 여러 분류에 주 분류로 들어갔습니다: " + str(dup)
    missing = sorted(all_old - set(seen))
    assert not missing, "새 분류에 빠진 약물: " + str(missing)
    extra = sorted(set(seen) - all_old)
    print("새로 분류에 들어간 약물:", extra)
    for g in groups:
        for x in g.get("x", []):
            assert x in seen, "참조 약물의 주 분류가 없습니다: " + x

    uses = []
    for uid, un, ug, uds in USES:
        for x in uds: assert x in drugs, (uid, x)
        uds = list(dict.fromkeys(uds))
        uses.append({"i": uid, "n": un, "g": ug, "d": uds})
        for x in uds: drugs[x].setdefault("u", []).append(uid)

    units, fam = [], []
    for f in FAMILIES_V2:
        us = list(dict.fromkeys(c["unit"] for c in CATS if c["fam"] == f["id"]))
        assert us, f["id"]
        units += us
        fam.append({"id": f["id"], "name": f["name"], "icon": f["icon"], "units": us, "v2": 1, "ref": REF_FAM.get(f["id"], []),
                    "chunks": [{"n": (u if len(us) > 1 else f["name"]), "units": [u]} for u in us]})
    assert len(set(units)) == len(units), "단원 이름이 겹칩니다"
    ulab = {u: {"g": None, "s": u} for u in units}
    return {"units": units, "fam": fam, "ulab": ulab, "cats": cats, "groups": groups, "uses": uses}
