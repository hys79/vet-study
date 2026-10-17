"""약리학 DB(pharmacology_data 폴더)에서 사이트용 데이터 파일(content/pharmacology/data.js)을 생성한다.

사용법:  python tools/build_pharma.py [pharmacology_data 폴더 경로]
원본 DB를 고친 뒤에는 이 스크립트를 다시 실행하면 된다.
"""
import json, os, sys

# 기본값: vet-study 폴더 옆의 pharmacology_data
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "pharmacology_data")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "pharmacology", "data.js")


def load(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return json.load(f)


def strip_source(o):
    """DB 내부용 'source' 표시는 사이트에 필요 없으므로 제거."""
    if isinstance(o, dict):
        return {k: strip_source(v) for k, v in o.items() if k != "source"}
    if isinstance(o, list):
        return [strip_source(v) for v in o]
    return o


db = load("pharmacology_db.json")
drugs_src = load("drugs.json")
groups_src = load("groups.json")

drugs = {}
for d in drugs_src:
    n = d["display_name"]
    rec = {"n": n}
    alias = [x for x in d.get("all_names", []) if x != n]
    if alias: rec["a"] = alias
    if d.get("abbr") and d["abbr"] not in alias and d["abbr"] != n: rec["a"] = rec.get("a", []) + [d["abbr"]]
    if d.get("notes"): rec["no"] = d["notes"]
    if d.get("uses"): rec["us"] = d["uses"]
    if d.get("action"): rec["ac"] = d["action"]
    if d.get("site"): rec["si"] = d["site"]
    drugs[d["id"]] = rec

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drug_extra import EXTRA   # DB에 없는 약물 직접 추가
for _id, _v in EXTRA.items():
    assert _id not in drugs, _id
    drugs[_id] = {"n": _v["n"], **({"a": _v["a"]} if _v.get("a") else {})}

# 약물별 정보(AI 작성, 개조식 항목 목록)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drug_info_1 import INFO_1
from drug_info_2 import INFO_2
from drug_info_3 import INFO_3
DRUG_INFO = {**INFO_1, **INFO_2, **INFO_3}
DRUG_INFO.update({_i: _v["info"] for _i, _v in EXTRA.items()})
_missing = [i for i in drugs if i not in DRUG_INFO]
assert not _missing, "정보가 없는 약물: " + str(_missing[:10])
assert not [i for i in DRUG_INFO if i not in drugs], "DB에 없는 약물 id가 있습니다"
from drug_info_patch import OVERRIDE, APPEND   # 교재 내용과 맞추기 위한 보강
for _id, _v in OVERRIDE.items():
    assert _id in DRUG_INFO, _id
    DRUG_INFO[_id] = _v
for _id, _v in APPEND.items():
    assert _id in DRUG_INFO, _id
    DRUG_INFO[_id] = DRUG_INFO[_id] + [x for x in _v if x not in DRUG_INFO[_id]]
from drug_info_more import MORE   # 정보가 적은 약물 보강
for _id, _v in MORE.items():
    assert _id in DRUG_INFO, _id
    DRUG_INFO[_id] = DRUG_INFO[_id] + [x for x in _v if x not in DRUG_INFO[_id]]
# 항목을 분류 → 기전 → 용도 → 특징 → 주의 → 금기 → 중독 → 해독 순으로 정렬(같은 라벨은 기존 순서 유지)
_LORDER = ["분류", "기전", "용도", "특징", "주의", "금기", "중독", "해독"]
def _lkey(t):
    lab = t.split(":")[0].split("(")[0].strip() if ":" in t else ""
    return _LORDER.index(lab) if lab in _LORDER else len(_LORDER)
for _id, _rec in drugs.items():
    _rec["ds"] = sorted(DRUG_INFO[_id], key=_lkey)

cats = []
for c in db["categories"]:
    rec = {"i": c["id"], "n": c["name"], "u": c["unit"]}
    if c.get("details"): rec["d"] = strip_source(c["details"])
    cats.append(rec)

groups = []
for g in groups_src:
    rec = {"c": g["category_id"], "g": g["group"], "d": g["drug_ids"]}
    if g.get("is_label_only"): rec["l"] = 1
    if g.get("info"): rec["i"] = g["info"]
    groups.append(rec)

# ── 분류 묶음(탭 개수 줄이기) ─────────────────────────────────────
# 분류가 많은 카테고리는 같은 성격의 분류를 큰 덩어리(k)로 묶어 접이식 탭 하나로 보여준다.
# 형식: {카테고리 id: [(덩어리 제목, [분류 이름 앞부분, ...]), ...]}  — 분류 이름이 앞부분으로 시작하면 그 덩어리에 속함
GROUP_CLUSTERS = {
    "antibiotic_mechanism": [
        ("세포벽 합성 억제", ["세포벽 합성 억제"]),
        ("세포막 투과성 변동", ["세포막 투과성 변동"]),
        ("단백질 합성 억제 (30S·50S 리보솜)", ["30S 리보솜 억제", "50S 리보솜 억제"]),
        ("핵산 합성 억제", ["핵산 합성 억제"]),
        ("대사 억제", ["대사 억제"]),
    ],
    "antibiotic_spectrum": [
        ("β-lactam계", ["Penicillin계", "Cephalosporin", "Carbapenem", "Monobactam"]),
        ("단백질 합성 억제 계열", ["Aminoglycoside", "Tetracycline", "Macrolide", "Phenicol", "Lincosamide"]),
        ("핵산·대사 억제 계열", ["Quinolone", "Sulfonamide"]),
        ("그 외 (Polymyxin · 기타 · 결핵 치료제)", ["Polymyxin", "기타", "결핵 치료제"]),
    ],
    "adrenergic_receptor_ligands": [
        ("α 수용체", ["α1", "α 비특이적", "α2"]),
        ("β 수용체", ["β1", "β2", "β3", "β 비특이적"]),
    ],
    "diuretic": [
        ("심혈관성 이뇨제", ["심장혈관성", "Methylxanthines"]),
        ("신장에 작용하는 이뇨제", ["삼투성", "수은", "탄산탈수소", "Thiazide", "칼륨 보존성", "헨레고리"]),
        ("요 pH 조절 이뇨제", ["산성화성", "알칼리성"]),
    ],
    "antitussive_bronchodilator": [
        ("기관지 이완제", ["기관지 이완제"]),
        ("진해제", ["진해제"]),
        ("폐성 고혈압 억제제", ["폐성 고혈압"]),
    ],
    "antineoplastic": [
        ("알킬화제 · 백금 제제", ["알킬화제", "백금"]),
        ("항대사제", ["항대사제"]),
        ("유사분열 방추체 억제제", ["유사분열"]),
        ("세포독성 항생제", ["세포독성"]),
        ("기타 (효소 · glucocorticoid · 표적치료 등)", ["글루코코르티코이드", "효소", "기타 제제"]),
    ],
    "anthelmintic_mechanism": [
        ("A. Energy 생산기구의 장애", ["A."]),
        ("B. 신경근전달기구의 장애", ["B."]),
    ],
    "anesthetic": [
        ("주사 마취제", ["주사용 마취제-chloral", "주사용 마취제-Propofol", "정신해리성", "주사용 마취제-imidazole", "주사용 마취제-alphaxalone"]),
        ("흡입 마취제", ["흡입마취제"]),
        ("Barbiturate 해독제", ["주사용 마취제-Barbiturates"]),
    ],
    "antinematode": [
        ("Benzimidazole계", ["Benzimidazole"]),
        ("니코틴 수용체 효현제", ["Nicotinic"]),
        ("거대고리 락톤계", ["거대고리 락톤계"]),
        ("기타 (유기인계 · GABA_A 효현제 · SLO-1 K⁺ 채널 개방제)", ["유기인제", "GABAA", "Ca2+-dependent"]),
    ],
    "antiprotozoal": [
        ("항콕시듐제", ["항 coccidium"]),
        ("항피로플라즈마제", ["항 piroplasma"]),
        ("항톡소플라스마제", ["항 toxoplasma"]),
        ("기타", ["기타"]),
    ],
}
for g in groups:
    spec = GROUP_CLUSTERS.get(g["c"])
    if not spec: continue
    name = g["g"] or ""
    for title, prefixes in spec:
        if any(name.startswith(x) for x in prefixes):
            g["k"] = title
            break
for cid, spec in GROUP_CLUSTERS.items():
    miss = [g["g"] for g in groups if g["c"] == cid and "k" not in g]
    assert not miss, f"{cid}: 덩어리에 속하지 않은 분류 {miss}"
    # 설정한 덩어리 순서대로 정렬 (같은 덩어리 안에서는 원래 순서 유지)
    pos = [i for i, g in enumerate(groups) if g["c"] == cid]
    order = {title: n for n, (title, _) in enumerate(spec)}
    sorted_groups = sorted((groups[i] for i in pos), key=lambda g: order[g["k"]])
    for i, g in zip(pos, sorted_groups):
        groups[i] = g

# ── 중복 제거 ─────────────────────────────────────────────────
# 카테고리 상세 설명의 group_info는 각 분류의 '기전·특징'(groups[].i)과 같은 내용이다.
# 문장이 모두 분류 쪽에 있으면 카테고리에서는 빼서 화면에 한 번만 나오게 한다.
def _texts(o, acc):
    if isinstance(o, str): acc.add(o.strip())
    elif isinstance(o, list):
        for x in o: _texts(x, acc)
    elif isinstance(o, dict):
        for v in o.values(): _texts(v, acc)
    return acc

for c in cats:
    gi = c.get("d", {}).get("group_info")
    if not gi: continue
    in_groups = set()
    for g in groups:
        if g["c"] == c["i"] and g.get("i"): _texts(g["i"], in_groups)
    if _texts(gi, set()) <= in_groups:
        del c["d"]["group_info"]
        if not c["d"]: del c["d"]

# ── 카테고리 상세 설명 정리 ─────────────────────────────────────
# 상세 설명 안의 '약물 이름만 나열한 목록'은 분류(groups)와 중복이므로 빼고,
# 약물 하나에 대한 정보(수용체, 결합 부위 등)는 그 약물의 주석(an)으로 옮긴다.
# 남은 설명 글은 약물 정보 창의 '분류 설명'에 보여준다.
import re
def _norm(x): return re.sub(r"[^0-9a-z가-힣α-ωΑ-Ω]", "", re.sub(r"\(.*?\)", "", str(x)).lower())
_names = {}
for _id, _rec in drugs.items():
    for _nm in [_rec["n"], _id.replace("_", " ")] + _rec.get("a", []):
        _names[_norm(_nm)] = _id
def _drug_of(item):
    return _names.get(_norm(item)) if isinstance(item, str) else None
def _annotate(drug_id, text):
    drugs[drug_id].setdefault("an", [])
    if text not in drugs[drug_id]["an"]: drugs[drug_id]["an"].append(text)

# (카테고리 id, 키) → 주석 라벨. 값의 경로(하위 키)를 주석으로 붙인다.
ANNOT_RULES = {
    ("alpha_antagonist", "subgroups"): "화학 계열",
    ("muscle_relaxant", "subgroups"): "작용 방식",
    ("cns_stimulant", "subgroups"): "작용 부위",
    ("anticholinesterase", "binding_sites"): "결합 부위",
}
def _collect(o, path, label):
    if isinstance(o, list):
        for it in o:
            d = _drug_of(it)
            shown = [x for x in path if x != "기타"]
            if d and shown and _norm(shown[-1]) != _norm(drugs[d]["n"]):
                _annotate(d, f"{label}: {' › '.join(shown)}")
    elif isinstance(o, dict):
        for k, v in o.items(): _collect(v, path + [k], label)

def _prune(o, cid):
    """약물 이름 목록은 빼고 설명 글만 남긴다. '약물(주석)' 형태는 약물 주석으로 옮긴다."""
    if isinstance(o, list):
        out = []
        for x in o:
            if isinstance(x, str):
                d = _drug_of(x)
                if d:
                    m = re.search(r"\((.+)\)\s*$", x)
                    if m and len(m.group(1)) <= 12 and cid in ("receptor_agonist", "receptor_blocker"):
                        _annotate(d, "수용체: " + m.group(1))
                    continue
                out.append(x)
            else:
                p = _prune(x, cid)
                if p not in (None, [], {}, ""): out.append(p)
        return out
    if isinstance(o, dict):
        out = {}
        for k, v in o.items():
            if (cid, k) in ANNOT_RULES: _collect_top(v, ANNOT_RULES[(cid, k)])
            p = _prune(v, cid)
            if k in ("subgroups", "drugs", "adrenergic", "cholinergic", "natural", "synthetic", "members") and isinstance(p, list):
                continue   # 이름 목록의 찌꺼기(약물이 아닌 항목)는 버림
            if k == "subgroups" and isinstance(p, dict):
                p = {kk: vv for kk, vv in p.items() if not isinstance(vv, list)}   # 이름 목록만 남은 항목은 버림
            if p not in (None, [], {}, ""): out[k] = p
        return out
    return o
def _collect_top(v, label):
    # v가 {하위 이름: 약물 목록 또는 중첩 dict} 형태 → 하위 이름 경로를 주석으로
    if isinstance(v, dict):
        for k, sub in v.items(): _collect(sub, [k], label)

for c in cats:
    if c.get("d"):
        c["d"] = _prune(c["d"], c["i"])
        if not c["d"]: del c["d"]

# ── 분류 체계 정리(합치기·나누기·이름 통일) ───────────────────────────
# 설정은 tools/pharma_structure.py. 분류 이름이 바뀌어도 약물 소속은 그대로다.
from pharma_structure import CAT_PLAN, CAT_RENAME, GROUP_RENAME, GROUP_ORDER

_unused = set(GROUP_RENAME)
for g in groups:                                   # 1) 분류 이름 통일 (카테고리 id + 원래 이름으로 찾음)
    key = (g["c"], g["g"])
    if key in GROUP_RENAME:
        g["g"] = GROUP_RENAME[key]
        _unused.discard(key)
assert not _unused, "이름을 바꾸려는 분류를 찾지 못했습니다: " + str(sorted(_unused)[:5])

_cat_by = {c["i"]: c for c in cats}
_groups_by = {}
for g in groups: _groups_by.setdefault(g["c"], []).append(g)
_merge_first, _merge_src, _split = {}, set(), {}
for _p in CAT_PLAN:
    if "merge" in _p:
        _srcs = [x[0] for x in _p["from"]]
        _merge_first[_srcs[0]] = _p
        _merge_src.update(_srcs)
    else:
        _split[_p["split"]] = _p

new_cats, new_groups = [], []
for c in cats:
    cid = c["i"]
    if cid in _merge_src and cid not in _merge_first:
        continue                                   # 합쳐지는 카테고리(첫 번째가 아닌 것)는 건너뜀
    if cid in _merge_first:
        p = _merge_first[cid]
        nc = {"i": p["merge"], "n": p["n"], "u": c["u"]}
        new_cats.append(nc)
        for src, gname, ql in p["from"]:
            sg = _groups_by.get(src, [])
            if gname is None:                      # 원래 분류를 그대로 가져옴
                for g in sg:
                    g2 = dict(g); g2["c"] = nc["i"]; new_groups.append(g2)
                continue
            ids, info = [], {}
            for g in sg:
                ids += [x for x in g["d"] if x not in ids]
                info.update(g.get("i") or {})
            info.update(_cat_by[src].get("d") or {})   # 원래 카테고리의 설명은 이 분류의 기전·특징으로
            g2 = {"c": nc["i"], "g": gname, "d": ids}
            if info: g2["i"] = info
            if ql and ql != gname: g2["ql"] = ql
            new_groups.append(g2)
    elif cid in _split:
        p = _split[cid]
        nc = dict(c); nc["n"] = p["n"]
        new_cats.append(nc)
        src_ids = [x for g in _groups_by.get(cid, []) for x in g["d"]]
        planned = [x for _, ids, _ in p["groups"] for x in ids]
        assert sorted(src_ids) == sorted(planned), f"{cid}: 나눈 분류의 약물이 원래와 다릅니다 {set(src_ids) ^ set(planned)}"
        for gname, ids, ql in p["groups"]:
            g2 = {"c": cid, "g": gname, "d": ids}
            if ql and ql != gname: g2["ql"] = ql
            new_groups.append(g2)
    else:
        nc = dict(c)
        if cid in CAT_RENAME: nc["n"] = CAT_RENAME[cid]
        new_cats.append(nc)
        new_groups.extend(_groups_by.get(cid, []))
cats, groups = new_cats, new_groups

# 소화기계 약물 단원을 '위산 분비 억제제'와 '식욕·비만'으로 분리 (위산 분비 억제제는 시험에서 중요한 범위)
UNIT_ACID = "소화기계 약물 - 위산 분비 억제제"
UNIT_APPETITE = "소화기계 약물 - 식욕·비만"
_old_gi = next(c for c in cats if c["i"] == "gi_drugs")
assert _old_gi["u"] == "소화기계 약물"
_gi_split = [
    ("gi_acid", "위산 분비 억제제", UNIT_ACID, ["항콜린제", "H2 길항제", "양성자 펌프 억제제(PPI)", "제산제", "점막 보호제"]),
    ("gi_appetite", "식욕 촉진제·항비만제", UNIT_APPETITE, ["식욕 촉진제", "항비만제"]),
]
_pos = cats.index(_old_gi)
cats[_pos:_pos + 1] = [{"i": i, "n": n, "u": u} for i, n, u, _ in _gi_split]
_gi_groups = [g for g in groups if g["c"] == "gi_drugs"]
_rest = [g for g in groups if g["c"] != "gi_drugs"]
_gpos = next(i for i, g in enumerate(groups) if g["c"] == "gi_drugs")
_moved = []
for i, n, u, names in _gi_split:
    for nm in names:
        g = next(x for x in _gi_groups if x["g"] == nm)
        g2 = dict(g); g2["c"] = i; _moved.append(g2)
assert len(_moved) == len(_gi_groups)
groups = _rest[:_gpos] + _moved + _rest[_gpos:]
for _cid, _order in GROUP_ORDER.items():            # 3) 분류 순서 지정
    pos = [i for i, g in enumerate(groups) if g["c"] == _cid]
    _rank = {n: k for k, n in enumerate(_order)}
    _sorted = sorted((groups[i] for i in pos), key=lambda g: _rank.get(g["g"], 99))
    for i, g in zip(pos, _sorted): groups[i] = g


# ── 분류 체계 재구성(통일된 틀): tools/pharma_v2.py · pharma_cats_a/b.py · pharma_uses.py · ref_v2.py ──
from pharma_v2 import build_v2
V2 = build_v2(drugs, cats, groups)
cats, groups, uses = V2["cats"], V2["groups"], V2["uses"]

# ── 교재 원문 문장을 개조식(~함, ~임)으로 통일 ──────────────────────
from gaejosik import convert_obj
for _rec in drugs.values():
    for _k in ("no", "us", "ac", "si"):
        if _rec.get(_k): _rec[_k] = convert_obj(_rec[_k])
for g in groups:
    if g.get("i"): g["i"] = convert_obj(g["i"])
for c in cats:
    if c.get("d"): c["d"] = convert_obj(c["d"])

# ── 계열 · 단원 머리글 ──
fam, ulab = V2["fam"], V2["ulab"]

# ── 표기 다듬기: 괄호 앞 공백 제거, 가운뎃점은 ' · '(앞뒤 공백)로 통일 ──
def _pol(t):
    t = re.sub(r"\s+\(", "(", t)
    t = re.sub(r"\s*·\s*", " · ", t)
    return re.sub(r"\s{2,}", " ", t).strip()
for c in cats:
    c["n"] = _pol(c["n"])
for g in groups:
    for _k in ("g", "ql", "k"):
        if g.get(_k): g[_k] = _pol(g[_k])
for _f in fam:
    _f["name"] = _pol(_f["name"])
    for _ch in _f["chunks"]: _ch["n"] = _pol(_ch["n"])
for _u in ulab.values():
    _u["s"] = _pol(_u["s"])
    if _u["g"]: _u["g"] = _pol(_u["g"])

# ── 약물 이름 어미 정리(tools/pharma_stems.py): 정규식으로 예시를 자동 수집 ──
from pharma_stems import STEMS
stems = []
for _st in STEMS:
    _tr = {t[0] for t in _st["tr"]}
    for _t in _tr: assert _t in drugs, ("어미 함정 약물이 DB에 없음", _st["s"], _t)
    _ex = [i for i, r in drugs.items() if re.search(_st["rx"], r["n"].lower()) and i not in _tr]
    assert _ex, "예시가 없는 어미: " + _st["s"]
    stems.append({"s": _st["s"], "k": _st["k"], "m": _st["m"], "c": _st["c"], "ex": _ex, "tr": _st["tr"]})

# 어미 목록 순서: 약물 분류 순서(신경 → 항염증 → 순환 → 소화·호흡 → 호르몬 → 항감염 → 항기생충 → 항암) 안에서 알파벳순
_KO = ["신경·마취", "항염증", "심혈관·신장", "소화기·호흡기", "호르몬·대사", "항감염제", "항기생충", "항암·면역"]
stems.sort(key=lambda s: (_KO.index(s["k"]), re.sub(r"[^a-z]", "", s["s"].lower().split("/")[0])))

data = {
    "units": V2["units"],
    "fam": fam,
    "ulab": ulab,
    "cats": cats,
    "groups": groups,
    "uses": uses,
    "stems": stems,
    "drugs": drugs,
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("// tools/build_pharma.py 로 생성된 파일입니다. 직접 고치지 마세요.\n")
    f.write("window.PHARMA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")

print("drugs", len(drugs), "cats", len(cats), "groups", len(groups), "bytes", os.path.getsize(OUT))
