// 네트워크 우선, 실패하면 캐시 → 한 번 열어본 자료는 오프라인에서도 열림
// GitHub Pages는 파일을 10분간 브라우저 캐시에 두게 하므로, 항상 서버에 최신 여부를 확인해서(no-cache) 수정사항이 바로 보이게 함
const C = "vet-study-v2";
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(
  caches.keys().then(ks => Promise.all(ks.filter(k => k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())
));
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET" || !e.request.url.startsWith(self.location.origin)) return;
  if (e.request.headers.has("range")) return; // 음악 등 부분 요청은 브라우저에 맡김
  e.respondWith(
    fetch(e.request, { cache: "no-cache" }).then(r => {
      if (r.status === 200) { const copy = r.clone(); caches.open(C).then(c => c.put(e.request, copy)); }
      return r;
    }).catch(() => caches.match(e.request))
  );
});
