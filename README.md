# 수의사 국시 공부방

## 새 항목 추가하는 법
1. `content/` 아래에 폴더를 만들고 자료를 넣는다. (퀴즈 `.html`, 정리 `.md` / `.html` / `.pdf` / 이미지)
2. `topics.js`에 항목 하나를 추가한다. 기존 항목을 복사해서 고치면 된다.

## 내 컴퓨터에서 미리보기
```
python -m http.server 8000
```
브라우저에서 http://localhost:8000 을 연다. (`index.html`을 더블클릭해도 열리지만 `.md` 자료와 오프라인 기능은 서버로 열 때만 동작)

## 퀴즈에 문제 수 슬라이더 넣기
새 퀴즈 html에 아래 두 가지만 넣으면 모드 선택 화면에 슬라이더가 생기고, 값은 모든 퀴즈가 공유합니다.
1. `<script src="../../shared/qn.js"></script>` (경로는 퀴즈 위치에 맞게)
2. 출제할 때 `QNum.get()`으로 문제 수를 읽고, 모드 선택 화면을 그린 뒤 `QNum.mount(첫번째_버튼_요소)`를 호출
(`content/virus-classification/quiz.html` 참고)
## 소리 설정
- 클릭·정답·오답 효과음은 코드로 합성하므로 파일이 필요 없습니다. (`shared/audio.js`)
- 배경음악은 `assets/bgm/bgm.mp3` 로 넣으면 됩니다. 다른 이름이나 여러 곡은 `topics.js`의 `BGM_FILES`에 적으세요.
- 오른쪽 위 ⚙ 버튼에서 효과음/배경음악 켜기·끄기와 볼륨을 조절합니다.

## 이미지 자료 (확대/축소)
- `topics.js`에서 `file`을 이미지(png, jpg, webp, svg 등)로 지정하면 확대/축소 뷰어로 열립니다.
  PC는 마우스 휠, 모바일·태블릿은 핀치로 확대·축소하고 드래그로 이동, 더블클릭(두 번 탭)으로 확대/초기화합니다.
- 퀴즈 html 안에서 이미지를 보여줄 때는 `shared/zoom.js`를 불러와 `ZoomView.attach(박스, img)`를 호출하세요.
