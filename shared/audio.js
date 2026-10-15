// 효과음(웹 오디오로 직접 합성 → 별도 음원 파일 불필요) + 소리 설정 저장.
// 설정은 localStorage에 저장되어 첫 화면·퀴즈(iframe)가 함께 씁니다.
//   SFX.click() / SFX.ok() / SFX.no() / SFX.done()
// 이 파일을 불러온 페이지의 모든 버튼·링크 클릭에는 자동으로 클릭음이 나며,
// 소리를 끄고 싶은 요소에는 data-sfx="none" 을 붙입니다.
(function () {
  const KEY = "vs_settings3", DEF = { sfx: true, sfxVol: 0.6, bgm: false, bgmVol: 0.6 };
  // 배경음악 슬라이더 100% = 실제 음량 25% (최대 음량 상한). 효과음과의 균형용.
  const BGM_MAX = 0.25;
  window.VS = {
    bgmGain() { return this.get().bgmVol * BGM_MAX; },
    get() { try { return Object.assign({}, DEF, JSON.parse(localStorage.getItem(KEY) || "{}")); } catch (e) { return Object.assign({}, DEF); } },
    set(p) { try { localStorage.setItem(KEY, JSON.stringify(Object.assign(JSON.parse(localStorage.getItem(KEY) || "{}"), p))); } catch (e) {} }
  };
  let ctx;
  function tone(freq, t0, dur, type, vol, slideTo) {
    const s = VS.get();
    if (!s.sfx || s.sfxVol <= 0) return;
    try {
      ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
      if (ctx.state === "suspended") ctx.resume();
      const o = ctx.createOscillator(), g = ctx.createGain(), t = ctx.currentTime + t0, v = Math.max(vol * s.sfxVol, 0.0002);
      o.type = type; o.frequency.setValueAtTime(freq, t);
      if (slideTo) o.frequency.exponentialRampToValueAtTime(slideTo, t + dur);
      g.gain.setValueAtTime(0.0001, t);
      g.gain.exponentialRampToValueAtTime(v, t + 0.008);
      g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
      o.connect(g).connect(ctx.destination); o.start(t); o.stop(t + dur + 0.03);
    } catch (e) {}
  }
  window.SFX = {
    click() { tone(720, 0, 0.06, "triangle", 0.3, 480); },
    ok()    { tone(660, 0, 0.12, "sine", 0.35); tone(990, 0.1, 0.2, "sine", 0.35); },
    no()    { tone(240, 0, 0.25, "sawtooth", 0.18, 150); },
    done()  { [523, 659, 784, 1047].forEach((f, i) => tone(f, i * 0.11, 0.22, "triangle", 0.3)); }
  };
  document.addEventListener("click", e => {
    const el = e.target.closest && e.target.closest("button,a");
    if (el && !el.closest('[data-sfx="none"]')) SFX.click();
  }, true);
})();
