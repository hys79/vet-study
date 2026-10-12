// 배경음악 파일(mp3 등). 파일을 assets/bgm/ 폴더에 넣고 이름을 여기에 적으세요.
// 여러 개를 적으면 순서대로 이어서 재생하고, 한 개면 반복 재생합니다.
window.BGM_FILES = ["assets/bgm/bgm.mp3"];
// 공부 항목 목록. 새 항목을 추가할 때는 이 파일만 고치면 됩니다.
// type: "quiz"(퀴즈 html) | "note"(정리 파일: .html / .md / .pdf / 이미지)
window.TOPICS = [
  {
    id: "virus-classification",
    subject: "미생물·전염병",
    title: "바이러스 분류",
    desc: "볼티모어 분류 · 과(Family)별 질병 · 외피 유무",
    emoji: "🦠",
    items: [
      { type: "quiz", title: "바이러스 분류 퀴즈", file: "content/virus-classification/quiz.html" }
    ]
  }
];
