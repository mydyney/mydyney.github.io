# Hugo 블로그 마이그레이션 규칙 (네이버 블로그 → Hugo)

## 개요
네이버 블로그 HTML을 Hugo Ananke 테마에 최적화된 SEO 친화적 다국어 Markdown으로 자동 변환하는 통합 지침입니다.

---

## 전체 워크플로우

```
1. 네이버 블로그 HTML 추출
   ↓
2. 이미지 다운로드 (download_naver_images.py)
   ↓
3. HTML 구조 분석 및 파싱
   ↓
4. 한국어 콘텐츠 리라이팅
   ↓
5. Hugo Markdown 생성 (Front Matter + HTML)
   ↓
6. 영어/일본어 번역 생성
   ↓
7. 품질 검증 및 배포
```

---

## STEP 1: 네이버 블로그 HTML 입력

### HTML 추출 방법
1. 네이버 블로그 글 열기
2. F12 (개발자 도구) → Elements 탭
3. `<div class="se-main-container">` 전체 선택
4. 우클릭 → Copy → Copy outerHTML
5. 텍스트 파일로 저장: `naver-{slug}.html`

### 네이버 HTML 구조 이해
```html
<div class="se-main-container">
  <!-- 텍스트 컴포넌트 -->
  <div class="se-component se-text">
    <p class="se-text-paragraph">본문 텍스트</p>
  </div>

  <!-- 이미지 컴포넌트 -->
  <div class="se-component se-image">
    <img src="https://postfiles.pstatic.net/...">
  </div>

  <!-- 인용구 컴포넌트 -->
  <div class="se-component se-quotation">
    <blockquote>인용문</blockquote>
  </div>
</div>
```

---

## STEP 2: 이미지 다운로드

### download_naver_images.py 실행

```bash
# 저장소로 이동
cd ~/Desktop/mydyney.github.io

# 스크립트 실행
python3 download_naver_images.py naver-{slug}.html {post-slug}

# 예시
python3 download_naver_images.py naver-shibuya-ramen.html shibuya-ramen-guide
```

### 이미지 파일 규칙
- **저장 위치**: `static/images/posts/`
- **파일명 형식**: `{post-slug}-01.jpg`, `{post-slug}-02.jpg`, ...
- **Markdown 경로**: `/images/posts/{post-slug}-01.jpg`

### 스크립트 출력 확인
```
✓ 총 15개 이미지 다운로드 완료
✓ 마크다운 파일 업데이트 완료: content/ko/posts/{post-slug}.md
```

---

## STEP 3: HTML 구조 분석 및 파싱

### ⚠️ 광고 코드 자동 제거 (최우선 작업)

네이버 블로그 HTML에는 광고 코드가 포함되어 있으며, 이는 **반드시 콘텐츠 분석 전에 제거**해야 합니다.

#### 제거해야 할 광고 패턴

```html
<!-- 패턴 1: 네이버 광고 래퍼 -->
<div class="ad_power_content_wrap" data-gfp-slot-index="0">
    <a data-ssp="clk" target="_blank" href="...">
        <!-- 광고 이미지 및 콘텐츠 -->
    </a>
</div>

<!-- 패턴 2: SSP 광고 콘텐츠 -->
<div class="ssp-adcontent">
    <!-- 광고 내용 -->
</div>

<!-- 패턴 3: 인라인 광고 -->
<div class="se-component" data-ad="true">
    <!-- 광고 -->
</div>
```

#### 광고 제거 절차

1. **HTML 파싱 전 광고 블록 삭제**
   - `<div class="ad_power_content_wrap">...</div>` 전체 제거
   - `<div class="ssp-adcontent">...</div>` 전체 제거
   - `data-ad="true"` 속성이 있는 요소 제거

2. **광고 제거 후 이미지 개수 재확인**
   ```
   ❌ 잘못된 방법: HTML 전체에서 이미지 개수 카운트 (광고 이미지 포함)
   ✅ 올바른 방법: 광고 제거 → 실제 콘텐츠 이미지만 카운트
   ```

3. **검증 체크리스트**
   - [ ] 모든 광고 블록이 제거되었는가?
   - [ ] 광고 제거 후 이미지 개수 = 다운로드된 이미지 개수
   - [ ] 콘텐츠 구조가 손상되지 않았는가?

#### 실제 사례: 롯폰기 일루미네이션 포스트

```
❌ 광고 제거 전:
- HTML에서 발견된 이미지: 15개 (광고 이미지 1개 포함)
- 다운로드된 이미지: 28개 (중복 포함)

✅ 광고 제거 후:
- 실제 콘텐츠 이미지: 14개
- 다운로드된 이미지: 14개 (01.jpg ~ 14.jpg)
- 결과: 숫자 일치 ✓
```

### 네이버 HTML → Hugo 변환 매핑

| 네이버 HTML | Hugo HTML | 비고 |
|-------------|-----------|------|
| `<div class="se-text">` | `<p>` | 일반 텍스트 |
| `<span class="se-fs-fs24">` | `<h2>` | 큰 텍스트 → 제목 |
| `<div class="se-quotation">` | `<blockquote>` | 인용구 유지 |
| `<div class="se-image">` | `<figure><img></figure>` | 이미지 최적화 |
| `<ul class="se-text-list">` | `<ul>` | 리스트 유지 |
| `<a class="se-link">` | `<a target="_blank">` | 외부 링크 |

### 콘텐츠 구조 식별 우선순위

1. **제목 (H1)**: 글의 첫 번째 큰 텍스트 또는 se-fs-fs24 이상
2. **대제목 (H2)**: `<blockquote>` 내 굵은 텍스트 또는 큰 폰트
3. **소제목 (H3)**: 번호나 항목으로 시작하는 텍스트
4. **인용구**: `<div class="se-quotation">`
5. **정보 박스**: 리스트 형태의 구조화된 데이터
6. **이미지**: `<div class="se-image">` 또는 `<div class="se-imageGroup">`
7. **일반 문단**: `<p class="se-text-paragraph">`

### ⚠️ 중요 원칙
- **이미지는 하나도 누락하지 않음** (순서대로 모두 포함)
- **이미지 위치는 원본 HTML과 동일하게 유지** (리라이팅 시에도 이미지 순서 변경 금지)
- **이미지 개수 검증 필수** (광고 제거 후 이미지 개수 = 다운로드된 이미지 개수)
- **HTML 태그는 닫힘 확인** (문법 오류 방지)
- **링크는 외부 속성 추가** (`target="_blank" rel="noopener noreferrer"`)

---

## STEP 4: 한국어 콘텐츠 리라이팅

### 리라이팅 원칙

#### ✅ 해야 할 것
1. **가독성 개선**: 긴 문장 → 짧게 분리
2. **불필요한 표현 제거**: "~하시면 됩니다", "~하시기 바랍니다" → 간결하게
3. **SEO 키워드 강화**: 자연스럽게 핵심 키워드 반복
4. **정보 구조화**: 산발적인 정보 → 리스트/박스로 정리
5. **행동 유도 문구 추가**: "지금 확인하세요", "꼭 방문해보세요"

#### ❌ 하지 말아야 할 것
1. **핵심 정보 삭제**: 영업시간, 위치, 가격 등 필수 정보 유지
2. **길이 대폭 변경**: 원문 ±20% 이내 유지
3. **의미 왜곡**: 원문의 취지와 맥락 변경 금지
4. **과도한 마케팅 문구**: 자연스러운 톤 유지
5. **🚨 이미지 위치 변경**: 원본 HTML의 이미지 순서와 위치를 그대로 유지해야 함

#### 🖼️ 이미지 위치 유지 규칙 (중요!)

리라이팅 시 **이미지의 순서와 위치**는 원본 HTML과 정확히 일치해야 합니다.

**원칙:**
1. **이미지 순서 변경 금지**: 01.jpg → 02.jpg → 03.jpg 순서 유지
2. **이미지 위치 고정**: 원본 HTML에서 이미지가 나타난 위치에 정확히 배치
3. **텍스트 조정**: 이미지 위치에 맞춰 텍스트를 조정 (이미지를 이동시키지 않음)

**예시:**

```
원본 HTML 구조:
- 서론 텍스트
- [이미지 1]
- 본론 텍스트 A
- [이미지 2]
- [이미지 3]
- 본론 텍스트 B
- [이미지 4]

✅ 올바른 리라이팅:
- 리라이팅된 서론
- [이미지 1]  ← 위치 유지
- 리라이팅된 본론 A
- [이미지 2]  ← 위치 유지
- [이미지 3]  ← 위치 유지
- 리라이팅된 본론 B
- [이미지 4]  ← 위치 유지

❌ 잘못된 리라이팅:
- 리라이팅된 서론
- 리라이팅된 본론 A
- [이미지 1]  ← 위치 변경됨!
- [이미지 2]
- 리라이팅된 본론 B
- [이미지 3]
- [이미지 4]
```

**검증 방법:**
- [ ] 원본 HTML에서 이미지 컴포넌트 위치 확인
- [ ] 리라이팅된 Markdown에서 동일한 위치에 이미지 배치
- [ ] 이미지 번호가 01부터 순서대로 사용되는지 확인
- [ ] 중복되거나 누락된 이미지가 없는지 확인

### 리라이팅 전후 비교 예시

#### 원문 (네이버 블로그)
```
도쿄 신주쿠의 키리무기야 진로쿠(切麦や 甚六) 는 아버지가 도쿄 칸다에서
운영하던 음식점 「진로쿠(甚六, 1957~1990)」의 가게 이름을 이어 받아
2015년 5월 신주쿠교엔마에에 문을 열었습니다. 합리적 가격과 훌륭한 맛으로
인정받아 미슐랭 빕 구르망에 2년 연속 선정되었습니다.
```

#### 리라이팅 버전
```
<p>도쿄 신주쿠 <strong>키리무기야 진로쿠</strong>는 1957년부터 이어온
가족의 우동 전통을 계승한 맛집입니다. 2015년 신주쿠교엔마에에 오픈한 이후,
합리적인 가격과 뛰어난 맛으로 <strong>미슐랭 빕 구르망에 2년 연속 선정</strong>되며
도쿄 최고의 우동 전문점으로 자리잡았습니다.</p>
```

**개선 사항:**
- ✅ 가독성: 긴 문장 2개로 분리
- ✅ SEO: "도쿄 신주쿠", "미슐랭" 강조
- ✅ 정보: 핵심 정보 모두 유지
- ✅ 길이: 원문과 유사

### 리라이팅 체크리스트

#### 문장 구조
- [ ] 한 문장 최대 2개 절까지
- [ ] 능동태 우선 사용
- [ ] 핵심 정보를 문장 앞쪽에 배치

#### 키워드 최적화
- [ ] 제목의 핵심 키워드 본문에 3-5회 반복
- [ ] 위치 키워드 자연스럽게 포함 (예: "신주쿠", "도쿄역")
- [ ] 카테고리 키워드 포함 (예: "맛집", "우동", "라멘")

#### 정보 완전성
- [ ] 영업시간, 위치, 교통 정보 누락 없음
- [ ] 특징 및 추천 메뉴 포함
- [ ] 가격대 또는 예산 정보 유지

#### 톤앤매너
- [ ] 친근하지만 전문적인 톤 유지
- [ ] 과도한 감탄사 제거 (예: "정말 대박!", "완전 최고!")
- [ ] 객관적 사실 기반 서술

---

## STEP 5: Hugo Markdown 생성

### Front Matter 구조

```yaml
---
title: "SEO 최적화된 제목 (50-60자)"
date: YYYY-MM-DDTHH:MM:SS+09:00
draft: false
translationKey: "unique-slug-in-english"
description: "행동 유도 메타 설명 (50-77자)"
summary: "description과 동일"
tags: ["키워드1", "키워드2", "키워드3", "키워드4", "키워드5"]
categories: ["맛집"]
featured_image: "/images/posts/{slug}-01.jpg"
---
```

### Front Matter 작성 규칙

#### Title (제목)
- **길이**: 50-60자 (검색 결과 노출 최적화)
- **형식**: `장소 + 주제 + 특징`
- **예시**:
  - "신주쿠 키리무기야 진로쿠 - 미슐랭 빕구르망 우동 맛집"
  - "도쿄역 라멘 스트리트 완벽 가이드 - 8곳 추천 맛집"

#### Description/Summary
- **길이**: 50-77자 (구글 스니펫 최적 길이)
- **구성**: 핵심 정보 + 행동 유도
- **예시**:
  - "도쿄 신주쿠 미슐랭 인정 우동 맛집! 영업시간, 메뉴, 교통편 총정리"
  - "도쿄역 지하 라멘 맛집 8곳 완벽 가이드. 지금 확인하고 맛집 투어 계획하세요"

#### Tags (5-7개 추천)
- **구성**: 지역 + 음식 종류 + 특징 + 카테고리
- **예시**:
  ```yaml
  tags: ["신주쿠맛집", "도쿄우동", "미슐랭", "일본맛집", "신주쿠교엔"]
  ```

#### Translation Key
- **형식**: `location-type-topic`
- **예시**:
  - `shinjuku-udon-kirimugiya`
  - `tokyo-station-ramen-guide`
  - `shibuya-cafe-morning`

### HTML 본문 구조

```html
<style>
/* 반응형 CSS */
.blog-container {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.8;
  color: #333;
}

.blog-container h2 {
  color: #2c3e50;
  border-bottom: 3px solid #3498db;
  padding-bottom: 0.5rem;
  margin: 2rem 0 1rem;
}

.blog-container img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  margin: 1.5rem 0;
}

.info-box {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1.5rem;
  border-radius: 12px;
  margin: 1.5rem 0;
}

.info-box ul {
  list-style: none;
  padding: 0;
}

.info-box li {
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255,255,255,0.2);
}

.info-box li:last-child {
  border-bottom: none;
}

blockquote {
  border-left: 4px solid #3498db;
  padding: 1rem 1.5rem;
  background: #ecf0f1;
  font-style: italic;
  margin: 1.5rem 0;
}

@media (max-width: 768px) {
  .blog-container { font-size: 0.95rem; }
  .info-box { padding: 1rem; }
}
</style>

<div class="blog-container">

<h1>제목</h1>

<p>리라이팅된 서론 텍스트...</p>

<figure>
  <img src="/images/posts/{slug}-01.jpg" alt="상세한 이미지 설명">
  <figcaption>이미지 캡션 (선택사항)</figcaption>
</figure>

<h2>📌 주요 정보</h2>

<div class="info-box">
  <ul>
    <li><strong>위치:</strong> 도쿄 신주쿠구...</li>
    <li><strong>영업시간:</strong> 11:00-22:00</li>
    <li><strong>교통:</strong> 신주쿠역 2번 출구 도보 5분</li>
    <li><strong>지도:</strong> <a href="https://maps.app.goo.gl/..."
        target="_blank" rel="noopener noreferrer" style="color: white; text-decoration: underline;">
        Google Maps</a></li>
  </ul>
</div>

<h2>메뉴 소개</h2>

<p>리라이팅된 메뉴 설명...</p>

<figure>
  <img src="/images/posts/{slug}-02.jpg" alt="메뉴 사진 설명">
</figure>

<blockquote>"고객 리뷰 또는 중요한 인용문"</blockquote>

<h2>방문 팁</h2>

<ul>
  <li>주말에는 대기가 길 수 있으니 평일 방문 추천</li>
  <li>현금 결제만 가능</li>
  <li>영어 메뉴판 있음</li>
</ul>

</div>
```

### 이미지 처리 규칙

```html
<!-- 단일 이미지 -->
<figure>
  <img src="/images/posts/{slug}-01.jpg"
       alt="신주쿠 키리무기야 진로쿠 외관 전경">
</figure>

<!-- 이미지 갤러리 (2-3개) -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
  <figure>
    <img src="/images/posts/{slug}-02.jpg" alt="우동 메뉴판">
  </figure>
  <figure>
    <img src="/images/posts/{slug}-03.jpg" alt="시그니처 우동">
  </figure>
</div>
```

---

## STEP 6: 영어/일본어 번역 생성

### 영어 번역 (en)

#### Front Matter
```yaml
---
title: "Kirimugiya Jinroku Shinjuku - Michelin Bib Gourmand Udon Restaurant"
date: YYYY-MM-DDTHH:MM:SS+09:00
draft: false
translationKey: "shinjuku-udon-kirimugiya"
description: "Discover Tokyo's best udon! Michelin-rated Kirimugiya Jinroku complete guide"
summary: "Discover Tokyo's best udon! Michelin-rated Kirimugiya Jinroku complete guide"
tags: ["tokyo-travel", "udon-restaurant", "michelin-guide", "shinjuku", "japanese-food"]
categories: ["restaurants"]
featured_image: "/images/posts/{slug}-01.jpg"
---
```

#### 번역 원칙
- **자연스러운 의역 우선**
- **검색 친화적 키워드 활용**
  - "맛집" → "must-try restaurant", "top-rated spot"
  - "가는 방법" → "How to Get There", "Access"
  - "운영시간" → "Opening Hours", "Business Hours"
- **현지 표현 방식**
  - "라스트오더" → "Last Order (L.O.)"
  - "연중무휴" → "Open Daily" / "Open Year-Round"

### 일본어 번역 (ja)

#### Front Matter
```yaml
---
title: "新宿切麦や甚六 - ミシュランビブグルマン認定うどん名店"
date: YYYY-MM-DDTHH:MM:SS+09:00
draft: false
translationKey: "shinjuku-udon-kirimugiya"
description: "東京新宿のミシュラン認定うどん名店！営業時間・メニュー・アクセス完全ガイド"
summary: "東京新宿のミシュラン認定うどん名店！営業時間・メニュー・アクセス完全ガイド"
tags: ["東京グルメ", "うどん", "ミシュランガイド", "新宿", "和食"]
categories: ["グルメ"]
featured_image: "/images/posts/{slug}-01.jpg"
---
```

#### 번역 원칙
- **정중한 존댓말 표현**: "～です", "～ます" 통일
- **음식 용어 정확히 번역**
  - "츠케멘" → "つけ麺"
  - "돈코츠" → "豚骨"
  - "시오라멘" → "塩ラーメン"
- **현지 생활 표현**
  - "맛집" → "名店", "人気店"
  - "대기" → "行列"
  - "추천" → "おすすめ"

---

## STEP 7: 품질 검증 체크리스트

### 🚨 광고 제거 검증 (최우선)
- [ ] 모든 `<div class="ad_power_content_wrap">` 블록이 제거되었는가?
- [ ] 모든 `<div class="ssp-adcontent">` 블록이 제거되었는가?
- [ ] 광고 관련 이미지가 제거되었는가?
- [ ] 광고 제거 후 콘텐츠 구조가 정상인가?

### 🖼️ 이미지 검증
- [ ] 광고 제거 후 이미지 개수 = 다운로드된 이미지 개수인가?
- [ ] 모든 이미지가 01.jpg부터 순서대로 사용되었는가?
- [ ] 이미지 위치가 원본 HTML과 동일한가?
- [ ] 중복되거나 누락된 이미지가 없는가?
- [ ] 모든 이미지에 alt 텍스트가 있는가?

### HTML 문법 검증
- [ ] 모든 태그가 올바르게 닫혔는가?
- [ ] 외부 링크에 `target="_blank" rel="noopener noreferrer"` 있는가?
- [ ] CSS 스타일이 올바르게 적용되었는가?

### 콘텐츠 검증
- [ ] 네이버 원문의 모든 정보가 포함되었는가?
- [ ] 리라이팅이 원문 길이 ±20% 이내인가?
- [ ] 핵심 키워드가 적절히 포함되었는가?

### SEO 검증
- [ ] Title 길이가 50-60자인가?
- [ ] Description 길이가 50-77자인가?
- [ ] Tags가 5-7개인가?
- [ ] Featured image 경로가 올바른가?

### 다국어 검증
- [ ] 3개 언어 모두 같은 translationKey를 사용하는가?
- [ ] 영어 번역이 자연스러운가?
- [ ] 일본어 존댓말이 일관되는가?

### Hugo 빌드 검증
```bash
# 로컬 Hugo 서버 실행
hugo server -D

# 오류 없이 빌드되는지 확인
hugo

# 브라우저에서 확인
# http://localhost:1313
```

---

## 부록: 자주 사용하는 템플릿

### 맛집 정보 박스
```html
<div class="info-box">
  <ul>
    <li><strong>📍 위치:</strong> 도쿄 신주쿠구...</li>
    <li><strong>🕐 영업시간:</strong> 월-금 11:00-22:00, 토-일 10:00-23:00</li>
    <li><strong>💰 가격대:</strong> 1,000-2,000엔</li>
    <li><strong>💳 결제:</strong> 현금, 카드 가능</li>
    <li><strong>🚇 교통:</strong> 신주쿠역 2번 출구 도보 5분</li>
    <li><strong>🗺️ 지도:</strong> <a href="..." target="_blank" rel="noopener noreferrer"
        style="color: white; text-decoration: underline;">Google Maps</a></li>
  </ul>
</div>
```

### 메뉴 소개 템플릿
```html
<h3>추천 메뉴</h3>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">

  <div style="border: 1px solid #ddd; border-radius: 8px; padding: 1rem;">
    <h4 style="margin-top: 0; color: #3498db;">특제 우동</h4>
    <p style="margin: 0.5rem 0;"><strong>1,500엔</strong></p>
    <p style="font-size: 0.9rem; color: #666;">두툼한 면발과 진한 육수가 특징</p>
  </div>

  <div style="border: 1px solid #ddd; border-radius: 8px; padding: 1rem;">
    <h4 style="margin-top: 0; color: #3498db;">튀김 우동</h4>
    <p style="margin: 0.5rem 0;"><strong>1,800엔</strong></p>
    <p style="font-size: 0.9rem; color: #666;">바삭한 새우튀김과 함께</p>
  </div>

</div>
```

### 방문 팁 템플릿
```html
<h2>💡 방문 전 꼭 알아두세요</h2>

<div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 1rem 1.5rem; margin: 1.5rem 0;">
  <h4 style="margin-top: 0; color: #856404;">⏰ 최적 방문 시간</h4>
  <p>평일 오후 2-5시가 대기 시간이 가장 짧습니다.</p>

  <h4 style="color: #856404;">💳 결제 방법</h4>
  <p>현금만 가능하니 미리 준비하세요.</p>

  <h4 style="color: #856404;">🗣️ 언어</h4>
  <p>영어 메뉴판 제공, 간단한 영어 소통 가능</p>
</div>
```

---

## 마이그레이션 실행 예시

### 전체 프로세스
```bash
# 1. 네이버 블로그 HTML 저장
# naver-shibuya-ramen.html 파일 생성

# 2. 이미지 다운로드
cd ~/Desktop/mydyney.github.io
python3 download_naver_images.py naver-shibuya-ramen.html shibuya-ramen-guide

# 3. Markdown 파일 생성 (Claude에게 HTML 제공)
# → 한국어 리라이팅
# → Hugo Markdown 생성
# → 영어/일본어 번역

# 4. Git 커밋
git add content/ko/posts/shibuya-ramen-guide.md
git add content/en/posts/shibuya-ramen-guide.md
git add content/ja/posts/shibuya-ramen-guide.md
git add static/images/posts/shibuya-ramen-guide-*.jpg
git commit -m "Add Shibuya ramen guide blog post"

# 5. GitHub 푸시
git push origin claude/migrate-blog-posts-01Ts9NHmZwsuzNpQp6ewLzBJ

# 6. PR 생성 및 병합
# GitHub에서 Pull Request 생성 → main 병합

# 7. 배포 확인
# https://tripmate.news 에서 3-5분 후 확인
```

---

## 트러블슈팅

### 이미지 개수가 일치하지 않는 경우

**증상:**
- HTML에서 발견된 이미지: 15개
- 다운로드된 이미지: 28개 (또는 다른 숫자)
- Hugo 서버에서 중복 이미지 표시

**원인:**
- 네이버 블로그 HTML에 광고 코드가 포함되어 있음
- 광고 이미지가 실제 콘텐츠 이미지로 잘못 카운트됨

**해결 방법:**
1. HTML에서 광고 블록 제거
   ```html
   <!-- 제거해야 할 패턴 -->
   <div class="ad_power_content_wrap">...</div>
   <div class="ssp-adcontent">...</div>
   ```

2. 광고 제거 후 이미지 재확인
   ```bash
   # 실제 콘텐츠 이미지만 카운트
   # 예: 14개
   ```

3. Markdown 파일 재생성
   - 광고 이미지 제외
   - 실제 이미지만 01.jpg ~ 14.jpg 순서대로 사용

### 이미지가 표시되지 않는 경우
1. 이미지 파일 경로 확인: `/images/posts/{slug}-01.jpg`
2. 파일이 실제로 다운로드되었는지 확인: `ls static/images/posts/`
3. Git에 커밋되었는지 확인: `git status`

### Hugo 빌드 오류
1. Front Matter YAML 문법 확인 (들여쓰기, 따옴표)
2. HTML 태그 닫힘 확인
3. 로컬에서 테스트: `hugo server -D`

### 번역이 부자연스러운 경우
1. 문화적 맥락 고려 (직역보다 의역)
2. 현지 표현 사용 (영어: must-try, 일본어: おすすめ)
3. 검색 키워드 자연스럽게 포함

---

## 참고 자료

- [Hugo 공식 문서](https://gohugo.io/documentation/)
- [Ananke 테마](https://github.com/theNewDynamic/gohugo-theme-ananke)
- [Google SEO 가이드](https://developers.google.com/search/docs)
- [Markdown 문법](https://www.markdownguide.org/)
