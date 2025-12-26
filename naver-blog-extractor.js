// 네이버 블로그 HTML 추출 북마클릿
// 사용법: 이 코드를 북마크의 URL로 저장하고, 네이버 블로그 글 페이지에서 클릭

javascript:(function(){
  // 네이버 블로그 본문 컨테이너 찾기
  const contentSelectors = [
    '.se-main-container',      // 스마트에디터 ONE
    '#postViewArea',           // 구형 에디터
    '.se-component-content',   // 대체 셀렉터
    '#viewTypeSelector'        // 추가 대체
  ];
  
  let content = null;
  for (let selector of contentSelectors) {
    content = document.querySelector(selector);
    if (content) break;
  }
  
  if (!content) {
    alert('블로그 본문을 찾을 수 없습니다. 네이버 블로그 글 페이지에서 실행해주세요.');
    return;
  }
  
  // outerHTML 추출
  const html = content.outerHTML;
  
  // Blob 생성 및 다운로드
  const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'naver.md';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  // 성공 메시지
  alert('✅ naver.md 다운로드 완료!\n\n다운로드 폴더에서 파일을 프로젝트 루트로 이동해주세요.');
})();
