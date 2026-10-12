// 이미지 확대/축소 뷰어
//   PC: 마우스 휠로 확대·축소(커서 위치 기준), 드래그로 이동, 더블클릭으로 초기화/확대
//   모바일·태블릿: 두 손가락 핀치로 확대·축소, 한 손가락 드래그로 이동, 두 번 탭으로 초기화/확대
// 사용법: ZoomView.attach(박스요소, img요소)  — 박스에는 높이를 지정해 두세요.
window.ZoomView = {
  attach(box, img) {
    const st = { s: 1, x: 0, y: 0 }, ptrs = new Map(), MAX = 8;
    let pinch = null, gestureMax = 0, moved = 0, lastTap = 0;
    Object.assign(box.style, { overflow: "hidden", position: "relative", touchAction: "none", cursor: "grab", userSelect: "none", webkitUserSelect: "none" });
    Object.assign(img.style, { display: "block", width: "100%", height: "auto", maxWidth: "none", transformOrigin: "0 0", willChange: "transform" });
    img.draggable = false;
    if (img.parentNode !== box) box.appendChild(img);

    const dims = () => ({ bw: box.clientWidth, bh: box.clientHeight, iw: img.offsetWidth, ih: img.offsetHeight });
    const minS = () => 1; // 원래 크기(가로 맞춤)보다 더 축소할 수 없음
    function apply() {
      const d = dims();
      st.s = Math.max(minS(), Math.min(MAX, st.s));
      st.x = d.iw * st.s <= d.bw ? (d.bw - d.iw * st.s) / 2 : Math.min(0, Math.max(d.bw - d.iw * st.s, st.x));
      st.y = d.ih * st.s <= d.bh ? (d.bh - d.ih * st.s) / 2 : Math.min(0, Math.max(d.bh - d.ih * st.s, st.y));
      img.style.transform = "translate(" + st.x + "px," + st.y + "px) scale(" + st.s + ")";
    }
    function zoomAt(cx, cy, ns) {
      ns = Math.max(minS(), Math.min(MAX, ns));
      const r = ns / st.s;
      st.x = cx - (cx - st.x) * r; st.y = cy - (cy - st.y) * r; st.s = ns;
      apply();
    }
    function reset() { st.s = 1; st.x = 0; st.y = 0; apply(); }
    const local = e => { const r = box.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; };

    box.addEventListener("wheel", e => {
      e.preventDefault();
      const p = local(e);
      zoomAt(p.x, p.y, st.s * Math.exp(-e.deltaY * (e.deltaMode === 1 ? 0.05 : 0.0015)));
    }, { passive: false });

    const pair = () => { const [a, b] = [...ptrs.values()]; return { d: Math.hypot(a.x - b.x, a.y - b.y) || 1, x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 }; };
    box.addEventListener("pointerdown", e => {
      if (e.target.closest("button")) return;
      const p = local(e); ptrs.set(e.pointerId, p);
      box.setPointerCapture(e.pointerId);
      gestureMax = Math.max(gestureMax, ptrs.size);
      if (ptrs.size === 1) moved = 0;
      if (ptrs.size === 2) pinch = pair();
      box.style.cursor = "grabbing";
    });
    box.addEventListener("pointermove", e => {
      if (!ptrs.has(e.pointerId)) return;
      const old = ptrs.get(e.pointerId), p = local(e);
      ptrs.set(e.pointerId, p);
      if (ptrs.size === 1) {
        st.x += p.x - old.x; st.y += p.y - old.y; moved += Math.abs(p.x - old.x) + Math.abs(p.y - old.y);
        apply();
      } else if (ptrs.size === 2 && pinch) {
        const n = pair();
        zoomAt(n.x, n.y, st.s * n.d / pinch.d);
        st.x += n.x - pinch.x; st.y += n.y - pinch.y; apply();
        pinch = n; moved += 99;
      }
    });
    const end = e => {
      if (!ptrs.has(e.pointerId)) return;
      const p = ptrs.get(e.pointerId);
      ptrs.delete(e.pointerId); pinch = null;
      if (ptrs.size === 1) pinch = null;
      if (ptrs.size === 0) {
        box.style.cursor = "grab";
        // 두 번 탭/클릭: 확대된 상태면 초기화, 아니면 그 지점을 2.5배 확대
        if (e.type === "pointerup" && gestureMax === 1 && moved < 8) {
          const now = Date.now();
          if (now - lastTap < 320) { lastTap = 0; (st.s > 1.01 ? reset() : zoomAt(p.x, p.y, 2.5)); }
          else lastTap = now;
        }
        gestureMax = 0;
      }
    };
    box.addEventListener("pointerup", end);
    box.addEventListener("pointercancel", end);

    img.addEventListener("load", apply);
    addEventListener("resize", apply);
    apply();
    return { reset };
  }
};
