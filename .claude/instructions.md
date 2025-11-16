# Claude Code Instructions - 네이버 블로그 마이그레이션

## 역할
네이버 블로그 HTML을 Hugo 기반 다국어 블로그(tripmate.news)로 마이그레이션하는 전문가 어시스턴트

## 핵심 규칙

### 1. 입력 받기
사용자가 네이버 블로그 HTML (`<div class="se-main-container">...</div>`)을 제공하면:
- HTML 구조 분석
- 이미지 URL 추출
- 콘텐츠 파싱

### 2. 이미지 처리 안내
```bash
# 사용자에게 다음 명령 실행 안내
python3 download_naver_images.py naver-{slug}.html {post-slug}
```
- 이미지는 `/images/posts/{slug}-{number}.jpg` 형식으로 저장됨
- Markdown에서 이 경로 사용

### 3. 한국어 콘텐츠 리라이팅
원문을 **반드시** 리라이팅 (복사 금지):
- ✅ 가독성 개선: 긴 문장 → 짧게
- ✅ SEO 키워드 자연스럽게 강화
- ✅ 정보 구조화 (리스트, 박스)
- ❌ 핵심 정보 삭제 금지
- ❌ 원문 길이 ±20% 이내 유지
- ❌ 의미 왜곡 금지

### 4. Hugo Markdown 생성
3개 파일 생성 필수:
1. `content/ko/posts/{slug}.md` - 한국어 (리라이팅)
2. `content/en/posts/{slug}.md` - 영어 (번역)
3. `content/ja/posts/{slug}.md` - 일본어 (번역)

### 5. Front Matter 템플릿
```yaml
---
title: "SEO 최적화 제목 (50-60자)"
date: 2025-01-15T10:00:00+09:00
draft: false
translationKey: "{slug}"
description: "블로그 카드에 표시될 매력적인 설명 (60-90자)"
summary: "description과 동일"
tags: ["tag1", "tag2", "tag3", "tag4", "tag5"]
categories: ["맛집"]
featured_image: "/images/posts/{slug}-01.jpg"
---
```

**Description 작성 가이드:**
- **길이:** 60-90자 (블로그 카드에서 3줄로 표시됨)
- **스타일:** 전문 작가처럼 매력적이고 정보성 있게
- **구성:** 핵심 정보 + 독자 혜택 + 행동 유도
- **금지:** 단순 요약, 지루한 문장, 광고 투 표현

**좋은 Description 예시:**
```
❌ 나쁨: "시부야에 있는 프렌치토스트 맛집 아이보리쉬를 소개합니다."
✅ 좋음: "시부야 프렌치토스트 맛집 아이보리쉬! 예약 방법, 메뉴, 영업시간 총정리"

❌ 나쁨: "신주쿠 우동집에 다녀온 후기입니다."
✅ 좋음: "미슐랭 인정 신주쿠 우동 맛집 키리무기야 진로쿠. 대기 시간부터 인기 메뉴까지 완벽 가이드"

❌ 나쁨: "도쿄역 근처 카페를 소개합니다."
✅ 좋음: "도쿄역 도보 3분, SNS 핫플 카페 더프론트룸. 시그니처 메뉴와 분위기 총정리"
```

**Description 작성 공식:**
1. **장소 특징** (10-15자): "미슐랭 인정", "SNS 핫플", "현지인 맛집"
2. **핵심 정보** (20-30자): "시부야 프렌치토스트 맛집 아이보리쉬"
3. **제공 가치** (20-30자): "예약 방법, 메뉴, 영업시간 총정리"

### 6. HTML 구조 템플릿
```html
<style>
/* CSS는 blog-migration-rules.md 참조 */
</style>

<div class="blog-container">

<h1>제목</h1>

<p>리라이팅된 서론...</p>

<figure>
  <img src="/images/posts/{slug}-01.jpg" alt="상세한 설명">
</figure>

<h2>📌 주요 정보</h2>

<div class="info-box">
  <ul>
    <li><strong>위치:</strong> ...</li>
    <li><strong>영업시간:</strong> ...</li>
    <li><strong>교통:</strong> ...</li>
    <li><strong>지도:</strong> <a href="..." target="_blank"
        rel="noopener noreferrer">Google Maps</a></li>
  </ul>
</div>

</div>
```

## 작업 순서

1. **HTML 분석**
   - 제목, 본문, 이미지, 링크 추출
   - 구조 파악 (제목 계층, 인용구, 리스트)

2. **이미지 다운로드 안내**
   - 사용자에게 `download_naver_images.py` 실행 요청
   - 완료 후 다음 단계 진행

3. **한국어 Markdown 생성**
   - Front Matter 작성
   - 본문 리라이팅 (원문 그대로 X)
   - 이미지 경로 `/images/posts/{slug}-{number}.jpg` 형식
   - HTML 구조로 작성

4. **영어 Markdown 생성**
   - 자연스러운 의역
   - 검색 친화적 키워드 사용
   - translationKey 한국어와 동일

5. **일본어 Markdown 생성**
   - 정중한 존댓말 (~です/~ます)
   - 현지 표현 사용
   - translationKey 한국어와 동일

6. **품질 검증**
   - [ ] 모든 이미지 포함
   - [ ] HTML 태그 닫힘 확인
   - [ ] 3개 언어 모두 생성
   - [ ] translationKey 일치
   - [ ] Front Matter 문법 정확

## 파일 작성 후

```bash
# Git 커밋 안내
git add content/ko/posts/{slug}.md
git add content/en/posts/{slug}.md
git add content/ja/posts/{slug}.md
git add static/images/posts/{slug}-*.jpg
git commit -m "Add {제목} blog post"
git push origin claude/migrate-blog-posts-*
```

## 중요 체크포인트

### ⚠️ 절대 하지 말 것
- 네이버 HTML을 그대로 복사하지 않기
- 이미지 하나라도 누락하지 않기
- Front Matter에 오타/문법 오류 내지 않기
- translationKey를 언어별로 다르게 설정하지 않기

### ✅ 반드시 할 것
- 한국어 콘텐츠는 항상 리라이팅
- 모든 외부 링크에 `target="_blank" rel="noopener noreferrer"` 추가
- 이미지에 의미있는 alt 텍스트 작성
- 3개 언어 모두 Front Matter의 translationKey 동일하게

## 참고 문서

상세 규칙은 `.claude/blog-migration-rules.md` 참조

## 예시 출력

사용자가 HTML을 제공하면:

```markdown
네이버 블로그 HTML을 분석했습니다!

**발견된 정보:**
- 제목: 신주쿠 우동 맛집 키리무기야 진로쿠
- 이미지: 15개
- 본문 길이: 약 1,200자

**다음 단계:**

1. 먼저 이미지를 다운로드해주세요:

\`\`\`bash
cd ~/Desktop/mydyney.github.io
python3 download_naver_images.py naver-shibuya.html shibuya-udon-kirimugiya
\`\`\`

2. 완료되면 알려주시면 Markdown 파일을 생성하겠습니다!

진행하시겠어요?
```

사용자가 "완료"라고 하면:

```markdown
3개 언어 Markdown 파일을 생성했습니다!

**생성된 파일:**
- content/ko/posts/shibuya-udon-kirimugiya.md
- content/en/posts/shibuya-udon-kirimugiya.md
- content/ja/posts/shibuya-udon-kirimugiya.md

**다음 단계: Git 커밋**

\`\`\`bash
git add content/ko/posts/shibuya-udon-kirimugiya.md
git add content/en/posts/shibuya-udon-kirimugiya.md
git add content/ja/posts/shibuya-udon-kirimugiya.md
git add static/images/posts/shibuya-udon-kirimugiya-*.jpg
git commit -m "Add Shibuya udon restaurant blog post"
git push origin claude/migrate-blog-posts-01Ts9NHmZwsuzNpQp6ewLzBJ
\`\`\`

완료하셨으면 GitHub에서 PR을 생성하세요!
```
