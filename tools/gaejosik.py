"""교재 원문의 서술형 어미(~한다, ~이다, ~있다 …)를 개조식(~함, ~임, ~있음 …)으로 바꾸는 보수적 변환기.
'과다', '보다'처럼 서술어가 아닌 단어가 바뀌지 않도록, 아래 규칙에 해당하는 어미만 변환한다."""
import re

_S, _V, _T = 0xAC00, 21, 28
_NIEUN, _MIEUM = 4, 16
_ADJ = {"있다": "있음", "없다": "없음", "않다": "않음", "아니다": "아님", "높다": "높음", "낮다": "낮음",
        "좋다": "좋음", "많다": "많음", "적다": "적음", "작다": "작음", "짧다": "짧음", "넓다": "넓음",
        "좁다": "좁음", "같다": "같음", "길다": "긺", "다르다": "다름", "크다": "큼", "빠르다": "빠름", "느리다": "느림"}


def _final(ch):
    return (ord(ch) - _S) % _T


def _with_final(ch, t):
    c = ord(ch) - _S
    return chr(_S + (c // _T) * _T + t)


def _nominalize(w):
    if w in _ADJ:
        return _ADJ[w]
    for k, v in _ADJ.items():                  # '~있다' '~없다' '~않다' 등
        if w.endswith(k) and len(w) > len(k):
            return w[: -len(k)] + v
    if w.endswith("하다") or w.endswith("되다") or w.endswith("이다") or w.endswith("아니다"):
        return w[:-2] + "함" if w.endswith("하다") else (w[:-2] + "됨" if w.endswith("되다") else w[:-2] + "임")
    if w.endswith("는다") and len(w) >= 3:     # 막는다 → 막음
        return w[:-2] + "음"
    if len(w) >= 3 and w[-1] == "다" and _final(w[-2]) == _NIEUN:   # 한다·된다·올린다·쓴다 → 함·됨·올림·씀
        return w[:-2] + _with_final(w[-2], _MIEUM)
    return None


_TOKEN = re.compile(r"([가-힣]+다)(?=[\s.,;:)\]·/→↔]|$)")
_SPACED = re.compile(r"(?<=[가-힣A-Za-z]) 한다(?=[\s.,;:)\]]|$)")   # '킬레이트 한다' → '킬레이트 함'


def convert(text):
    if not isinstance(text, str):
        return text

    def sub(m):
        w = m.group(1)
        r = _nominalize(w)
        return r if r else w

    return _SPACED.sub(" 함", _TOKEN.sub(sub, text))


def convert_obj(o):
    """dict/list 안의 문자열을 모두 변환(dict의 키는 그대로)."""
    if isinstance(o, str):
        return convert(o)
    if isinstance(o, list):
        return [convert_obj(x) for x in o]
    if isinstance(o, dict):
        return {k: convert_obj(v) for k, v in o.items()}
    return o
