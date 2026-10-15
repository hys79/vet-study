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
- 오른쪽 위 ⚙ 버튼에서 효과음/배경음악 켜기·끄기와 볼륨을 조절합니다. 배경음악은 기본 꺼짐(켜기 전에는 음악 파일을 내려받지 않아 데이터 절약).

## 이미지 자료 (확대/축소)
- `topics.js`에서 `file`을 이미지(png, jpg, webp, svg 등)로 지정하면 확대/축소 뷰어로 열립니다.
  PC는 마우스 휠, 모바일·태블릿은 핀치로 확대·축소하고 드래그로 이동, 더블클릭(두 번 탭)으로 확대/초기화합니다.
- 퀴즈 html 안에서 이미지를 보여줄 때는 `shared/zoom.js`를 불러와 `ZoomView.attach(박스, img)`를 호출하세요.

## 약리학 데이터 만들기 (`tools/`)
- `python tools/build_pharma.py` → `content/pharmacology/data.js` 생성 (원본 DB: `Desktop/pharmacology_data`)
- 약물 정보(AI 작성, 개조식): `tools/drug_info_1~3.py` + 교재 보강 `tools/drug_info_patch.py`, 교재 원문 문장은 `tools/gaejosik.py`로 개조식 변환, 단원·계열 참고(AI 작성): `tools/ref_unit_a.py`, `ref_unit_b.py`, `ref_family.py`
- 단원 이름 간소화·계열 구성·분류 묶음: `tools/build_pharma.py`의 `UNIT_LABELS`, `FAMILIES`, `GROUP_CLUSTERS`

## 약리학 퀴즈 유형 (content/pharmacology/quiz.html)
- 정보 → 약물 / 약물 → 정보(옳은·옳지 않은 설명) / 분류 → 약물 / 약물 → 분류 / 전체 랜덤 (부작용·금기·해독은 정보 유형에 포함)
- 약물 정보(분류·기전·용도·주의 …)와 교재 문장에서 문제를 자동 생성하며, 보기가 정답과 같은 단어를 공유하면 오답에서 제외해 정답이 둘이 되는 문제를 줄임
- 난이도(쉬움/어려움): 분류 → 약물 · 약물 → 분류 유형에 적용. 쉬움은 큰 분류(카테고리) 단위(같은 계열·단원 오답이 섞임), 어려움은 세부 분류 단위(같은 카테고리의 형제 분류가 오답). 선지 아래에 단원 › 카테고리 경로를 표시
- 출제 범위는 `tools/build_pharma.py`의 `SCOPE_CHUNKS`(큰 덩어리)로 선택
