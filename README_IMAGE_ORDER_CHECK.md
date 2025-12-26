# 이미지 순서 검증 가이드

## 📋 개요

네이버 블로그에서 Hugo로 변환할 때 **이미지 순서 불일치**를 자동으로 검출하는 검증 스크립트입니다.

### 주요 기능

✅ 네이버 HTML의 모든 이미지를 순서대로 추출
✅ **이미지 그룹 (2~4개 이미지) 정확히 감지**
✅ Hugo 마크다운의 이미지와 1:1 매핑 검증
✅ 불일치 발견 시 상세 리포트 제공

---

## 🚀 사용 방법

### 1. 네이버 블로그 HTML 저장

```bash
# 네이버 블로그 포스트에서 HTML 저장
# 브라우저: 우클릭 → 페이지 소스 보기 → 전체 복사 → 파일로 저장
```

### 2. Hugo 마크다운 작성

```bash
# 네이버 HTML을 번역하여 Hugo 마크다운 작성
# content/en/posts/post-slug.md
# content/ja/posts/post-slug.md
```

### 3. 이미지 다운로드

```bash
# 사용자가 수동으로 네이버에서 이미지 다운로드
# static/images/posts/post-slug-01.jpg
# static/images/posts/post-slug-02.jpg
# ...
```

### 4. 검증 스크립트 실행

```bash
python3 check_image_order.py <naver_html_file> <post_slug>
```

**예시:**
```bash
python3 check_image_order.py naver_post.html japan-convenience-store-shopping-best-10
```

---

## 📊 검증 결과 예시

### ✅ 성공 케이스

```
================================================================================
📊 이미지 순서 검증: japan-convenience-store-shopping-best-10
================================================================================

📌 네이버 HTML: 21개 이미지
📌 Hugo 마크다운: 22개 이미지

📊 본문 이미지 비교:
   네이버: 21개
   Hugo:   21개

📋 상세 이미지 매핑:
--------------------------------------------------------------------------------

✅ 이미지 #1:
   네이버: 일본 3대 편의점 비교 총정리 쇼핑리스트 BEST10
   Hugo:   Japan's 3 major convenience stores: 7-Eleven, FamilyMart...
   파일:   japan-convenience-store-shopping-best-10-02.jpg (예상: 02.jpg)

✅ 이미지 #2:
   네이버: 일본 세븐일레븐 추천 1순위, 타마고산도(계란 샌드위치)의 먹음직스러운...
   Hugo:   7-Eleven's famous egg sandwich with fluffy egg salad
   파일:   japan-convenience-store-shopping-best-10-03.jpg (예상: 03.jpg)

...

================================================================================
✅ 모든 이미지가 올바른 순서로 매핑되었습니다!
================================================================================
```

### ❌ 실패 케이스 (불일치 발견)

```
================================================================================
📊 이미지 순서 검증: japan-convenience-store-shopping-best-10
================================================================================

📌 네이버 HTML: 21개 이미지
📌 Hugo 마크다운: 25개 이미지

📊 본문 이미지 비교:
   네이버: 21개
   Hugo:   24개

❌ 이미지 개수 불일치!
   차이: 3개
   ⚠️  Hugo에 3개의 추가 이미지가 있습니다!
   네이버에 없는 이미지를 Hugo에서 삭제해야 합니다.

📋 상세 이미지 매핑:
--------------------------------------------------------------------------------

✅ 이미지 #1:
   네이버: 일본 3대 편의점 비교 총정리 쇼핑리스트 BEST10
   Hugo:   Japan's 3 major convenience stores comparison
   파일:   japan-convenience-store-shopping-best-10-02.jpg (예상: 02.jpg)

❌ 이미지 #2:
   네이버: 일본 세븐일레븐 추천 1순위, 타마고산도
   Hugo:   7-Eleven storefront with signature green
   파일:   japan-convenience-store-shopping-best-10-03.jpg (예상: 03.jpg)

❌ 이미지 #3:
   네이버: 일본 세븐일레븐 추천 1순위, 타마고산도
   Hugo:   FamilyMart storefront with blue branding
   파일:   japan-convenience-store-shopping-best-10-04.jpg (예상: 04.jpg)

================================================================================
❌ 이미지 순서 불일치가 발견되었습니다!
================================================================================

💡 수정 방법:
   1. 네이버에 없는 이미지를 Hugo에서 삭제
   2. 이미지 번호를 올바르게 재배치
   3. 다시 검증 실행
```

---

## 🔍 네이버 이미지 구조 이해하기

### 1. 단일 이미지

```html
<div class="se-component se-image">
  <div class="se-module se-module-image">
    <img src="https://postfiles.pstatic.net/..." class="se-image-resource">
  </div>
  <div class="se-module se-module-text se-caption">
    <p>이미지 설명</p>
  </div>
</div>
```

→ **1개의 이미지로 카운트**

### 2. 이미지 그룹 (2~4개)

```html
<div class="se-component se-imageGroup">
  <div class="se-imageGroup-container">
    <div class="se-imageGroup-item se-imageGroup-col-2">
      <img src="..." class="se-image-resource">  <!-- 이미지 1 -->
      <img src="..." class="se-image-resource">  <!-- 이미지 2 -->
    </div>
  </div>
  <div class="se-module se-module-text se-caption">
    <p>그룹 이미지 설명</p>
  </div>
</div>
```

→ **2개의 이미지로 카운트** (각각 별도의 `<figure>` 필요)

---

## 📌 Hugo 변환 규칙

### 이미지 번호링

```
{post-slug}-01.jpg  →  featured_image (Front Matter)
{post-slug}-02.jpg  →  첫 번째 본문 이미지
{post-slug}-03.jpg  →  두 번째 본문 이미지
{post-slug}-04.jpg  →  세 번째 본문 이미지
...
```

### Featured Image vs Body Image

```yaml
---
featured_image: "/images/posts/post-slug-01.jpg"  # 소셜 미디어 프리뷰용
---

<div class="blog-container">

<!-- 첫 번째 본문 이미지는 02.jpg -->
<figure>
  <img src="/images/posts/post-slug-02.jpg" alt="...">
  <figcaption>...</figcaption>
</figure>

<!-- 두 번째 본문 이미지는 03.jpg -->
<figure>
  <img src="/images/posts/post-slug-03.jpg" alt="...">
  <figcaption>...</figcaption>
</figure>
```

### 이미지 그룹 처리

**네이버 HTML:**
```html
<div class="se-imageGroup-item se-imageGroup-col-2">
  <img src="image1.jpg">
  <img src="image2.jpg">
</div>
<div class="se-caption">세븐일레븐과 패밀리마트 비교</div>
```

**Hugo 마크다운:**
```html
<!-- 각 이미지마다 별도의 figure 태그! -->
<figure>
  <img src="/images/posts/slug-10.jpg" alt="7-Eleven storefront">
  <figcaption>세븐일레븐과 패밀리마트 비교 [1/2]</figcaption>
</figure>

<figure>
  <img src="/images/posts/slug-11.jpg" alt="FamilyMart storefront">
  <figcaption>세븐일레븐과 패밀리마트 비교 [2/2]</figcaption>
</figure>
```

---

## 🛠️ 워크플로우 권장사항

### 1단계: 네이버 HTML 분석

```bash
# HTML 파일에서 이미지 개수 확인
python3 -c "
from bs4 import BeautifulSoup
html = open('naver.md').read()
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', class_='se-image-resource')
print(f'총 이미지 개수: {len(images)}')
"
```

### 2단계: Hugo 마크다운 작성

- **네이버의 이미지 개수를 확인**하고
- **정확히 같은 개수의 이미지를 Hugo에 삽입**
- **추가 이미지를 임의로 넣지 않기!**

### 3단계: 검증

```bash
python3 check_image_order.py naver.md post-slug
```

### 4단계: 수정 (불일치 발견 시)

1. Hugo 마크다운에서 네이버에 없는 이미지 삭제
2. 이미지 번호 재정렬
3. 다시 검증 실행

---

## ⚠️ 주의사항

### 1. 네이버에 없는 이미지를 Hugo에 추가하지 마세요

❌ **잘못된 예:**
```markdown
<!-- 네이버에는 없지만 Hugo에 추가 -->
<figure>
  <img src="/images/posts/slug-03.jpg" alt="7-Eleven storefront">
  <figcaption>7-Eleven storefront (네이버에 없음)</figcaption>
</figure>
```

✅ **올바른 예:**
```markdown
<!-- 네이버 HTML과 1:1 매핑 -->
<figure>
  <img src="/images/posts/slug-03.jpg" alt="타마고산도">
  <figcaption>네이버의 3번째 이미지와 동일</figcaption>
</figure>
```

### 2. 이미지 그룹은 각각 별도 figure로 처리

❌ **잘못된 예:**
```html
<!-- 그룹의 두 이미지를 하나의 figure로 처리 -->
<figure>
  <img src="/images/posts/slug-10.jpg">
  <img src="/images/posts/slug-11.jpg">  <!-- 잘못됨 -->
  <figcaption>두 이미지</figcaption>
</figure>
```

✅ **올바른 예:**
```html
<!-- 각 이미지마다 별도 figure -->
<figure>
  <img src="/images/posts/slug-10.jpg">
  <figcaption>이미지 1</figcaption>
</figure>

<figure>
  <img src="/images/posts/slug-11.jpg">
  <figcaption>이미지 2</figcaption>
</figure>
```

---

## 🎯 실전 체크리스트

Hugo 마크다운 작성 후 반드시 확인:

- [ ] 네이버 HTML에서 이미지 개수 확인 (단일 + 그룹)
- [ ] Hugo 마크다운에서 featured_image 1개 + body images N개 확인
- [ ] 총 이미지 개수: 네이버 N개 = Hugo N+1개 (featured 포함)
- [ ] `python3 check_image_order.py` 실행
- [ ] 검증 통과 확인 (✅ 모든 이미지가 올바른 순서로 매핑)
- [ ] 실패 시 불일치 이미지 수정 후 재검증

---

## 📞 문제 해결

### Q1: "se-main-container not found in HTML" 오류

**원인:** 잘못된 HTML 파일 또는 일부만 복사됨

**해결:**
- 브라우저에서 **전체 페이지 소스**를 복사
- `<div class="se-main-container">` 포함 여부 확인

### Q2: 이미지 개수가 맞는데도 실패

**원인:** 이미지 번호가 잘못 배치됨 (예: 02, 03, 05... - 04 누락)

**해결:**
- Hugo 마크다운에서 이미지 번호를 순차적으로 정렬
- 02, 03, 04, 05... (누락 없이)

### Q3: 이미지 그룹이 제대로 감지 안 됨

**원인:** 네이버 HTML 구조가 변경되었을 수 있음

**해결:**
- 스크립트 업데이트 필요
- GitHub Issue 제보

---

## 🔧 스크립트 실행 환경

**필수 패키지:**
```bash
pip3 install beautifulsoup4 lxml
```

**실행 권한:**
```bash
chmod +x check_image_order.py
```

---

**작성일:** 2025-11-20
**버전:** 1.0.0
