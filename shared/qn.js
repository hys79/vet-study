// 모든 퀴즈가 같이 쓰는 "문제 수" 슬라이더. 값은 기기에 저장되어 퀴즈끼리 공유됩니다.
// 사용법(퀴즈 html): <script src="../../shared/qn.js"></script>
//   QNum.get()        → 현재 문제 수 (기본 20)
//   QNum.mount(el)    → el 앞에 슬라이더를 끼워 넣음 (모드 선택 화면을 그릴 때마다 호출)
window.QNum = {
  KEY: "quizN", MIN: 5, MAX: 50, STEP: 1, DEF: 20,
  get() {
    try { const v = +localStorage.getItem(this.KEY); if (v >= this.MIN && v <= this.MAX) return v; } catch (e) {}
    return this.DEF;
  },
  set(v) { try { localStorage.setItem(this.KEY, v); } catch (e) {} },
  mount(before) {
    const box = document.createElement("div");
    box.style.cssText = "background:var(--card,#fff);border:1.5px solid var(--line,#d5dede);border-radius:14px;padding:12px 16px;margin-bottom:10px";
    box.innerHTML = '<label style="display:block;font-size:15px;margin-bottom:6px;color:var(--ink,#14202b)">문제 수 <b id="qn-v" style="color:var(--acc,#0f766e);font-size:18px">' + this.get() + '</b>문제</label>' +
      '<input id="qn-r" type="range" min="' + this.MIN + '" max="' + this.MAX + '" step="' + this.STEP + '" value="' + this.get() + '" style="width:100%;height:28px;accent-color:var(--acc,#0f766e)">';
    before.parentNode.insertBefore(box, before);
    const r = box.querySelector("#qn-r"), v = box.querySelector("#qn-v");
    r.oninput = () => { v.textContent = r.value; this.set(r.value); };
  }
};
