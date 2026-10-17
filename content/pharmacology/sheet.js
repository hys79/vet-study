// 약물 정보창(팝업) — 약리학 정리 · 어미 정리 페이지가 함께 사용합니다.
// 사용법: data.js 다음에 <script src="sheet.js"></script>. 약물 칩에 class="chip" data-id="약물id",
//        용도 태그/칩에 data-use="용도id" 를 달면 누를 때 정보창이 열립니다. 쓰는 페이지에는 --card --line --sub --acc --accbg --bg --ink 색 변수가 있어야 합니다.
(function () {
  const P = window.PHARMA, D = P.drugs;
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // ── 스타일과 DOM ──
  const st = document.createElement("style");
  st.textContent = `
#sheetbg{position:fixed;inset:0;background:rgba(0,0,0,.5);display:none;z-index:40;padding:16px}
#sheetbg.on{display:flex;align-items:center;justify-content:center;animation:shfade .15s ease-out}
#sheet{background:var(--card);color:var(--ink);width:min(640px,100%);max-height:min(86vh,820px);display:flex;flex-direction:column;border-radius:18px;box-shadow:0 18px 60px rgba(0,0,0,.45);animation:shpop .18s ease-out;line-height:1.55}
@keyframes shfade{from{opacity:0}to{opacity:1}}
@keyframes shpop{from{transform:translateY(10px) scale(.97);opacity:0}to{transform:none;opacity:1}}
#sh-top{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;padding:14px 18px 10px;border-bottom:1px solid var(--line)}
#sh-body{overflow:auto;padding:0 18px 28px}
#sh-top>div{flex:1;min-width:0}
#sh-top .bk{flex:none;background:none;color:var(--sub);font:inherit;font-size:14px;line-height:1;cursor:pointer;border:1.5px solid var(--line);border-radius:50%;width:26px;height:26px;padding:0}
#sh-top .bk:hover,#sh-top .bk:focus-visible{border-color:var(--acc);color:var(--acc);outline:none}
#sheet .xr{border-left-style:dashed}
#sh-top h2{margin:0;font-size:22px;letter-spacing:-.01em;word-break:break-word}
#sh-top .x{background:none;color:inherit;font:inherit;cursor:pointer;border:1.5px solid var(--line);border-radius:50%;width:36px;height:36px;flex:none;font-size:16px}
#sh-top .nm{display:flex;align-items:center;gap:6px;min-width:0}
#sheet .star{background:none;border:0;padding:0 3px;font:inherit;font-size:19px;line-height:1;cursor:pointer;color:var(--sub);opacity:.75;flex:none}
#sheet .star:hover{opacity:1}
#sheet .star.on{color:#f59e0b;opacity:1}
#sheet .star:focus-visible{outline:2px solid var(--acc);border-radius:6px}
#sheet .sr{display:inline-flex;align-items:center;gap:1px;margin:0 6px 6px 0;transition:opacity .15s}
#sheet .sr.off{opacity:.45}
#sheet .sr .chip{padding-right:6px}
#sheet .sr .star{font-size:17px}
#sheet .stdel{margin-top:16px;background:none;color:var(--sub);font:inherit;font-size:13px;border:1px solid var(--line);border-radius:8px;padding:5px 12px;cursor:pointer}
#sheet .none{color:var(--sub);padding:14px 0}
#sheet h4{margin:14px 0 4px;font-size:13px;color:var(--sub)}
#sheet h5{margin:10px 0 4px;font-size:14.5px}
#sheet .alias{color:var(--sub);font-size:14px;margin-top:2px}
#sheet ul.lead{margin:14px 0 4px;padding:10px 12px 10px 30px;background:var(--accbg);border-left:4px solid var(--acc);border-radius:8px;font-size:15px;list-style:disc}
#sheet ul.lead li{margin:3px 0}
#sheet .lb{color:var(--acc)}
#sheet .tags{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 6px}
#sheet .tag{background:var(--bg);color:inherit;font:inherit;border:1px solid var(--line);border-radius:99px;padding:2px 10px;font-size:13px}
#sheet .tag.use{cursor:pointer;color:var(--acc);border-color:var(--acc)}
#sheet p{margin:6px 0 2px;font-size:15px}
#sheet .sub2{margin:8px 0 2px;font-size:12.5px;font-weight:700;color:var(--sub)}
#sheet .grp{margin:8px 0 10px;padding:8px 10px;border-left:3px solid var(--line)}
#sheet .path{color:var(--sub);font-size:13px;margin-bottom:3px}
#sheet .gn{font-weight:700;font-size:15px;margin-bottom:5px}
#sheet .gn{display:flex;align-items:center;gap:8px}
#sheet button.jump{flex:none;display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;padding:0;background:none;border:1.5px solid var(--line);border-radius:50%;font:inherit;font-size:13px;line-height:1;color:var(--sub);cursor:pointer}
#sheet button.jump:hover,#sheet button.jump:focus-visible{border-color:var(--acc);color:var(--acc);background:var(--accbg);outline:none}
#sheet .chips{display:flex;flex-wrap:wrap;gap:6px}
#sheet .chip{background:var(--accbg);color:var(--ink);font:inherit;font-size:14px;cursor:pointer;border:1px solid transparent;border-radius:99px;padding:3px 11px}
#sheet .chip:hover,#sheet .chip:focus-visible{border-color:var(--acc);outline:none}
#sheet dl{margin:6px 0;font-size:14.5px}
#sheet dt{font-weight:700;margin-top:6px;color:var(--sub);font-size:13px}
#sheet dd{margin:2px 0 4px 10px}
#sheet ul{margin:3px 0 6px;padding-left:20px}
#sheet li{margin:2px 0}`;
  document.head.appendChild(st);
  const bg = document.createElement("div");
  bg.id = "sheetbg";
  bg.innerHTML = '<div id="sheet" role="dialog" aria-modal="true"><div id="sh-top"></div><div id="sh-body"></div></div>';
  document.body.appendChild(bg);
  const $ = id => document.getElementById(id);

  // ── 색인 ──
  const gIdx = new Map(); P.groups.forEach((g, i) => gIdx.set(g, i));
  const catById = {}; P.cats.forEach(c => catById[c.i] = c);
  const clsOf = {}; P.groups.forEach(g => g.d.forEach(id => (clsOf[id] = clsOf[id] || []).push(g)));
  const xOf = {}; P.groups.forEach(g => (g.x || []).forEach(id => (xOf[id] = xOf[id] || []).push(g)));
  const useById = {}; (P.uses || []).forEach(u => useById[u.i] = u);
  const UL = P.ulab || {};
  const us = u => (UL[u] && UL[u].s) || u;
  const ulab = u => { const l = UL[u]; return l && l.g ? `${l.g} · ${l.s}` : us(u); };
  const norm = s => String(s).replace(/\(.*?\)/g, "").replace(/[^0-9A-Za-z가-힣]/g, "").toLowerCase();
  const sameName = (a, b) => { const x = norm(a), y = norm(b); return !!x && x === y; };
  // ── 북마크(★): 기기에 저장 ──
  const SKEY = "pharmaStars";
  let stars = [];
  try { const v = JSON.parse(localStorage.getItem(SKEY) || "[]"); if (Array.isArray(v)) stars = v.filter(id => D[id]); } catch (e) {}
  const saveStars = () => { try { localStorage.setItem(SKEY, JSON.stringify(stars)); } catch (e) {} document.dispatchEvent(new CustomEvent("starschange", { detail: stars.length })); };
  const isStar = id => stars.includes(id);
  const toggleStar = id => { stars = isStar(id) ? stars.filter(x => x !== id) : [...stars, id]; saveStars(); };
  const chips = ids => `<div class="chips">${ids.map(id => D[id] ? `<button class="chip" data-id="${esc(id)}">${isStar(id) ? "★ " : ""}${esc(D[id].n)}</button>` : "").join("")}</div>`;

  // 교재 DB 원문(분류 설명 등)을 그대로 펼쳐 보여주는 트리
  const LBL = { site: "작용 부위", mechanism: "기전", characteristics: "특징", indications: "적응증", adverse: "부작용", contraindications: "금기", contraindication: "금기", uses: "용도", use: "용도", clinical_use: "임상 용도", therapeutic_use: "치료 용도", general: "일반", overview: "개요", note: "참고", type: "종류", members_labels: "구성 계열", members: "구성", mixtures: "혼합제", effects: "효과", class_info: "계열별 정보", group_info: "분류별 정보", subgroups: "세부 분류", ion_info: "이온 정보", classes: "계열" };
  Object.assign(LBL, { effect: "효과", pharmacokinetics: "약동학", actions: "작용", action: "작용", applications: "응용", side_effects: "부작용", side_effect: "부작용", notes: "참고", class_I_note: "Class I 설명", treatment_goals: "치료 목표", intro: "소개", labels: "하위 계열 표기", coccidium_mechanism: "콜시듐 작용 기전", irreversible: "비가역적", reversible: "가역적", binding_sites: "결합 부위", intensity_of_depression: "억제 강도", repolarization: "재분극", receptors: "수용체", endocrine: "내분비" });
  const lbl = k => LBL[k] || k;
  function tree(o) {
    if (o == null) return "";
    if (o && typeof o === "object" && !Array.isArray(o) && Object.keys(o).length === 1 && typeof o.text === "string") o = o.text;
    if (typeof o !== "object") return `<span>${esc(o)}</span>`;
    if (Array.isArray(o)) return o.length === 1 && typeof o[0] !== "object" ? tree(o[0]) : `<ul>${o.map(x => `<li>${tree(x)}</li>`).join("")}</ul>`;
    return `<dl>${Object.entries(o).map(([k, v]) => `<dt>${esc(lbl(k))}</dt><dd>${tree(v)}</dd>`).join("")}</dl>`;
  }

  // 카테고리 설명 중 이 약물의 분류와 관련된 항목만 골라서 보여줌
  function relDetail(c, g) {
    const d = c.d; if (!d) return null;
    const gp = norm(g.g || ""), gpre = norm((g.g || "").split(" - ")[0]), out = {};
    for (const [k, v] of Object.entries(d)) {
      if (["class_info", "subgroups", "notes", "labels", "classes"].includes(k) && v && typeof v === "object" && !Array.isArray(v)) {
        const m = Object.entries(v).filter(([kk]) => {
          const nk = norm(kk);
          if (k === "classes") return gp.replace("class", "") === nk;
          return !!nk && !!gp && (nk.startsWith(gpre) || gpre.startsWith(nk) || gp.includes(nk) || nk.includes(gp));
        });
        if (m.length) out[k] = Object.fromEntries(m);
      } else if (k === "class_I_note") { if (/^classi[abc]$/.test(gp)) out[k] = v; }
      else out[k] = v;
    }
    return Object.keys(out).length ? out : null;
  }
  // 항목 앞의 라벨(분류·기전·용도·주의 등)은 굵게
  const bullet = t => { const m = t.match(/^([^:]{1,12}):\s*(.*)$/); return m ? `<b class="lb">${esc(m[1])}</b> ${esc(m[2])}` : esc(t); };

  function show(top, body) {
    $("sh-top").innerHTML = (cur > 0 ? '<button class="bk" id="shbk" aria-label="뒤로" title="뒤로">←</button>' : "") + top + '<button class="x" id="sx" aria-label="닫기">✕</button>';
    $("sh-body").innerHTML = body;
    bg.classList.add("on"); document.body.style.overflow = "hidden";   // 팝업이 떠 있는 동안 뒤 화면 스크롤 잠금
    $("sx").onclick = close; if ($("shbk")) $("shbk").onclick = back; $("sh-body").scrollTop = 0;
  }
  function drawDrug(id) {
    const d = D[id]; if (!d) return;
    const cl = [...(clsOf[id] || []), ...(xOf[id] || [])];   // 주 분류 + 참조 분류를 구분 없이 나열
    const info = (d.an ? `<div class="tags">${d.an.map(a => `<span class="tag">${esc(a)}</span>`).join("")}</div>` : "") +
      (d.ac ? `<p><b>작용</b> ${esc(d.ac)}</p>` : "") + (d.si ? `<p><b>작용 부위</b> ${esc(d.si)}</p>` : "") +
      (d.us ? `<p><b>용도</b></p>${tree(d.us)}` : "") + (d.no ? `${d.us ? "<p><b>설명</b></p>" : ""}${tree(d.no)}` : "");
    const clsHtml = cl.map(g => {
      const c = catById[g.c], peers = [...g.d, ...(g.x || [])].filter(x => x !== id), rd = relDetail(c, g);
      return `<div class="grp"><div class="path">${esc(ulab(c.u))} › ${esc(c.n)}</div><div class="gn"><span>${esc(g.g && !sameName(g.g, c.n) ? g.g : c.n)}</span><button class="jump" data-jump="${gIdx.get(g)}" aria-label="약물 분류 정리에서 자세히 보기" title="약물 분류 정리에서 자세히 보기">↗</button></div>${g.i ? `<div class="sub2">기전·특징</div>${tree(g.i)}` : ""}${rd ? `<div class="sub2">분류 설명</div>${tree(rd)}` : ""}${peers.length ? `<div class="sub2">같은 분류의 약물</div>${chips(peers)}` : ""}</div>`;
    }).join("");
    show(`<div style="min-width:0"><div class="nm"><h2>${esc(d.n)}</h2><button class="star${isStar(id) ? " on" : ""}" data-star="${esc(id)}" aria-label="북마크" aria-pressed="${isStar(id)}" title="북마크">${isStar(id) ? "★" : "☆"}</button></div>${d.a ? `<div class="alias">${esc(d.a.join(" · "))}</div>` : ""}</div>`,
      (d.ds ? `<ul class="lead">${d.ds.map(t => `<li>${bullet(t)}</li>`).join("")}</ul>` : "") +
      (info ? `<h4>정보</h4>${info}` : "") +
      (d.u && d.u.length ? `<h4>용도</h4><div class="tags">${d.u.map(x => `<button class="tag use" data-use="${esc(x)}">${esc(useById[x] ? useById[x].n : x)}</button>`).join("")}</div>` : "") +
      `<h4>분류</h4>` + (clsHtml || "<span style='color:var(--sub)'>분류 정보 없음</span>"));
  }
  // 용도: 그 용도의 약물을 주 분류(약물군 › 세부 분류)별로 보여줌
  function drawUse(uid) {
    const u = useById[uid]; if (!u) return;
    const by = new Map();
    u.d.forEach(id => { const g = (clsOf[id] || [])[0], k = g ? `${catById[g.c].n} › ${g.g || catById[g.c].n}` : "분류 없음"; if (!by.has(k)) by.set(k, []); by.get(k).push(id); });
    show(`<div><h2>${esc(u.n)}</h2><div class="alias">용도 · ${esc(u.g)} · ${u.d.length}종 (AI 작성)</div></div>`,
      [...by].map(([k, ids]) => `<h5>${esc(k)}</h5>${chips(ids)}`).join(""));
  }
  // 북마크한 약물 모아 보기(약물군 › 세부 분류별)
  function drawStars() {
    const by = new Map();
    stars.forEach(id => { const g = (clsOf[id] || [])[0], k = g ? `${catById[g.c].n} › ${g.g || catById[g.c].n}` : "분류 없음"; if (!by.has(k)) by.set(k, []); by.get(k).push(id); });
    show(`<div><h2>★ 북마크</h2><div class="alias">${stars.length}종 · 약물 정보창의 ☆를 눌러 추가·해제</div></div>`,
      stars.length ? [...by].map(([k, ids]) => `<h5>${esc(k)}</h5><div class="chips">${ids.map(id => `<span class="sr"><button class="chip" data-id="${esc(id)}">${esc(D[id].n)}</button><button class="star on" data-star="${esc(id)}" aria-label="북마크 해제" aria-pressed="true" title="북마크 해제">★</button></span>`).join("")}</div>`).join("") + '<button class="stdel" id="stdel">모두 해제</button>'
        : '<div class="none">아직 북마크한 약물이 없어요. 약물 정보창 이름 옆의 ☆를 눌러 추가해 보세요.</div>');
    const del = $("stdel"); if (del) del.onclick = () => { if (confirm("북마크를 모두 해제할까요?")) { stars = []; saveStars(); drawStars(); } };
  }
  // 약물 분류 정리의 해당 세부 분류로 이동: 정리 페이지에서는 그 자리에서, 퀴즈·어미 정리에서는 새 탭(퀴즈 진행을 유지)
  function jump(gi) {
    if (typeof window.PharmaJump === "function") { close(); setTimeout(() => window.PharmaJump(gi), 150); return; }
    let idx = 0;
    try { const t = parent.TOPICS.find(x => x.id === "pharmacology"); const k = t.items.findIndex(i => /pharmacology\/notes\.html$/.test(i.file)); if (k >= 0) idx = k; } catch (e) {}
    window.open(new URL("../../index.html", location.href).href + "#/v/pharmacology/" + idx + "/g=" + gi, "_blank");
  }
  // ── 이동 기록 ──
  let stack = [], cur = -1, expect = 0, canHist = true;
  function draw(v) { if (v.t === "d") drawDrug(v.id); else if (v.t === "u") drawUse(v.id); else drawStars(); }
  function nav(v) {
    if (v.t === "d" && !D[v.id]) return;
    if (v.t === "u" && !useById[v.id]) return;
    if (!stack.length) { stack = [v]; cur = 0; } else { stack = stack.slice(0, cur + 1); stack.push(v); cur++; }
    if (canHist) { try { history.pushState({ sh: cur + 1 }, ""); } catch (e) { canHist = false; } }
    draw(v);
  }
  const open = id => nav({ t: "d", id }), openUse = id => nav({ t: "u", id }), openStars = () => nav({ t: "s" });
  function back() { if (cur <= 0) return; if (canHist) history.back(); else { cur--; draw(stack[cur]); } }
  function hide() { bg.classList.remove("on"); document.body.style.overflow = ""; }
  function close() {
    if (!stack.length) { hide(); return; }
    const n = cur + 1; hide(); stack = []; cur = -1;
    if (canHist && n > 0) { expect++; setTimeout(() => { if (expect > 0) expect = 0; }, 800); history.go(-n); }
  }
  // 브라우저 뒤로가기(마우스 옆 버튼 포함): 정보창이 열려 있으면 이전 화면으로, 처음 화면이면 정보창만 닫음(페이지는 유지)
  addEventListener("popstate", e => {
    if (expect > 0) { expect--; e.stopImmediatePropagation(); return; }
    if (!stack.length) return;
    e.stopImmediatePropagation();
    const d = e.state && e.state.sh;
    if (!d) { hide(); stack = []; cur = -1; return; }
    if (d <= stack.length) { cur = d - 1; draw(stack[cur]); }
  });

  bg.onclick = e => { if (e.target === bg) close(); };
  addEventListener("keydown", e => { if (e.key === "Escape") close(); });
  document.addEventListener("click", e => {
    const j = e.target.closest("[data-jump]");
    if (j) { jump(+j.dataset.jump); return; }
    const t = e.target.closest("[data-star]");
    if (t) { toggleStar(t.dataset.star); const on = isStar(t.dataset.star); t.classList.toggle("on", on); t.textContent = on ? "★" : "☆"; t.setAttribute("aria-pressed", on); const row = t.closest(".sr"); if (row) row.classList.toggle("off", !on); const sub = document.querySelector("#sh-top .alias"); if (sub && row) sub.textContent = `${stars.length}종 · 약물 정보창의 ☆를 눌러 추가·해제`; return; }
    const u = e.target.closest("[data-use]"); if (u) { openUse(u.dataset.use); return; }
    const b = e.target.closest(".chip"); if (b && b.dataset.id) open(b.dataset.id);
  });
  window.DrugSheet = { open, openUse, openStars, close, tree, stars: () => stars.slice(), isStar };
})();
