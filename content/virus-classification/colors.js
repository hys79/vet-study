// 바이러스 핵산 유형별 색상 (정리표·퀴즈 해설 칩이 함께 사용)
// c = 파스텔(칩·머리글 배경), d = 같은 색의 진한 버전(글자색)
// 계열이 비슷하면 색도 비슷하게: DNA = 파랑·보라 · RNA = 장미·주황·노랑 · 역전사 = 초록·청록 (V = 노랑)
window.VTYPES = [
  { r: "I",   n: "dsDNA",      k: "이중가닥 DNA",      c: "#93c5fd", d: "#1d4ed8" },
  { r: "II",  n: "ssDNA",      k: "단일가닥 DNA",      c: "#c4b5fd", d: "#6d28d9" },
  { r: "III", n: "dsRNA",      k: "이중가닥 RNA",      c: "#fda4af", d: "#be123c" },
  { r: "IV",  n: "(+)ssRNA",   k: "단일가닥 RNA 양성", c: "#f5cba7", d: "#b4540f" },
  { r: "V",   n: "(−)ssRNA",   k: "단일가닥 RNA 음성", c: "#f3e0a0", d: "#92700c" },
  { r: "VI",  n: "RNA 역전사", k: "RNA → 역전사",      c: "#86efac", d: "#15803d" },
  { r: "VII", n: "DNA 역전사", k: "DNA → 역전사",      c: "#5eead4", d: "#0f766e" }
];
