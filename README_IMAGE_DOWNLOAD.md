# 네이버 블로그 이미지 다운로드 가이드 (검증 통합 버전)

## 📋 개요

네이버 블로그에서 Hugo로 마이그레이션할 때 **자동으로 이미지를 검증하고 다운로드**하는 통합 스크립트입니다.

### 🎯 핵심 기능

✅ **네이버 HTML 분석**
- 광고 블록 자동 제거
- 단일 이미지 및 이미지 그룹(2~4개) 정확히 감지
- 순서대로 이미지 URL 추출

✅ **Hugo 마크다운 검증**
- featured_image 및 body images 추출
- 네이버와 Hugo 이미지 개수 비교
- 이미지 순서 검증 (02, 03, 04... 순차적)

✅ **검증 통과 후 다운로드**
- 검증 실패 시 다운로드 중단 및 상세 오류 리포트
- 검증 통과 시에만 이미지 다운로드 시작
- JPG 형식으로 자동 변환 및 최적화

---

## 🚀 사용 방법

### 1단계: 필수 패키지 설치

```bash
pip3 install requests pillow beautifulsoup4 lxml
```

### 2단계: 네이버 블로그 HTML 저장

```bash
# 1. 네이버 블로그 글 열기
# 2. 우클릭 → 페이지 소스 보기 (또는 Cmd+Option+U)
# 3. 전체 HTML 복사
# 4. naver.html 파일로 저장
```

### 3단계: Hugo 마크다운 작성

```bash
# content/en/posts/post-slug.md 작성
# content/ja/posts/post-slug.md 작성
# (이미지는 아직 다운로드 안 함, <figure> 태그만 작성)
```

### 4단계: 검증 및 다운로드 (한 번에!)

```bash
python3 download_naver_images.py naver.html post-slug
```

**예시:**
```bash
python3 download_naver_images.py naver.html japan-convenience-store-shopping-best-10
```

---

## ⭐ 이전 vs 현재 워크플로우 비교

### ❌ 이전 (2단계 - 비효율적)

```bash
# 1단계: 이미지 다운로드
python3 download_naver_images.py naver.html post-slug

# 2단계: 검증 (문제 발견)
python3 check_image_order.py naver.html post-slug
# → ❌ 문제 발견! 이미지 삭제하고 다시 다운로드...
```

### ✅ 현재 (1단계 - 효율적)

```bash
# 검증 + 다운로드 통합!
python3 download_naver_images.py naver.html post-slug
# → ✅ 검증 실패 시 다운로드 안 함 (시간 절약!)
# → ✅ 검증 통과 시에만 다운로드 시작
```

---

## 📊 실행 예시

### ✅ 성공 케이스

```bash
$ python3 download_naver_images.py naver.html japan-convenience-store-shopping-best-10

📖 읽기: naver.html
📖 읽기: content/en/posts/japan-convenience-store-shopping-best-10.md

🔍 네이버 HTML 분석 중...
✓ 발견된 이미지: 21개
   1. 일본 3대 편의점 비교 총정리 쇼핑리스트 BEST10...
   2. 일본 세븐일레븐 추천 1순위, 타마고산도...
   3. 로손의 디저트 추천1위, 프리미엄 롤케이크...
   ... 외 18개

🔍 Hugo 마크다운 분석 중...
✓ 발견된 이미지: 22개

================================================================================
🔍 이미지 순서 검증: japan-convenience-store-shopping-best-10
================================================================================

📊 이미지 개수:
   네이버 HTML: 21개
   Hugo 마크다운: 22개

📊 본문 이미지 비교:
   네이버: 21개
   Hugo:   21개 (featured 제외)

📋 이미지 매핑 검증:
--------------------------------------------------------------------------------
✅ 이미지 #1:
   네이버: 일본 3대 편의점 비교 총정리
   Hugo:   Japan's 3 major convenience stores
   파일:   japan-convenience-store-shopping-best-10-02.jpg (예상: 02.jpg)

✅ 이미지 #2:
   네이버: 타마고산도(계란 샌드위치)
   Hugo:   7-Eleven's famous egg sandwich
   파일:   japan-convenience-store-shopping-best-10-03.jpg (예상: 03.jpg)

... (모든 이미지 검증 통과)

================================================================================
✅ 검증 통과! 이미지 다운로드를 시작합니다.
================================================================================

💾 이미지 다운로드 시작
================================================================================

[1/21] featured_image (01.jpg):
  ✓ japan-convenience-store-shopping-best-10-01.jpg

[2/21] body image (03.jpg):
  ✓ japan-convenience-store-shopping-best-10-03.jpg

... (모든 이미지 다운로드)

================================================================================
✅ 다운로드 완료!
================================================================================
✓ 성공: 21/21개 이미지
✓ 저장 위치: static/images/posts/
✓ 파일 형식: japan-convenience-store-shopping-best-10-01.jpg ~ ...-22.jpg
================================================================================

🎉 모든 작업 완료!

📝 다음 단계:
   1. static/images/posts/ 디렉토리에서 다운로드된 이미지 확인
   2. Hugo 로컬 서버로 미리보기: hugo server -D
   3. 문제없으면 commit & push
```

---

### ❌ 실패 케이스 (이미지 개수 불일치)

```bash
$ python3 download_naver_images.py naver.html post-slug

... (분석)

================================================================================
🔍 이미지 순서 검증: post-slug
================================================================================

📊 이미지 개수:
   네이버 HTML: 21개
   Hugo 마크다운: 25개

📊 본문 이미지 비교:
   네이버: 21개
   Hugo:   24개 (featured 제외)

❌ 이미지 개수 불일치!
   차이: 3개

⚠️  Hugo에 3개의 추가 이미지가 있습니다!
   네이버에 없는 이미지를 Hugo에서 삭제해야 합니다.

💡 수정 방법:
   1. Hugo 마크다운 파일을 열어 이미지 개수를 확인하세요
   2. 네이버 HTML과 동일한 개수로 맞추세요
   3. 다시 이 스크립트를 실행하세요

================================================================================

🛑 검증 실패로 다운로드를 중단합니다.
================================================================================
```

---

## 🎯 이미지 번호링 규칙

```
{slug}-01.jpg  →  featured_image (Front Matter)
{slug}-02.jpg  →  첫 번째 본문 이미지
{slug}-03.jpg  →  두 번째 본문 이미지
{slug}-04.jpg  →  세 번째 본문 이미지
...
```

### 예시: 21개 이미지

- 네이버: 21개 이미지
- Hugo featured: 01.jpg (네이버의 첫 번째 이미지)
- Hugo body: 02.jpg ~ 22.jpg (네이버의 1~21번째 이미지)
- **총 22개 파일 생성**

---

## 📌 Hugo 마크다운 작성 가이드

### ✅ 올바른 예시

```markdown
---
title: "Post Title"
featured_image: "/images/posts/post-slug-01.jpg"  # 01.jpg는 featured
---

<div class="blog-container">

<!-- 첫 번째 본문 이미지는 02.jpg -->
<figure>
  <img src="/images/posts/post-slug-02.jpg" alt="First image">
  <figcaption>First image caption</figcaption>
</figure>

<!-- 두 번째 본문 이미지는 03.jpg -->
<figure>
  <img src="/images/posts/post-slug-03.jpg" alt="Second image">
  <figcaption>Second image caption</figcaption>
</figure>

<!-- 세 번째 본문 이미지는 04.jpg -->
<figure>
  <img src="/images/posts/post-slug-04.jpg" alt="Third image">
  <figcaption>Third image caption</figcaption>
</figure>

</div>
```

### ❌ 잘못된 예시

```markdown
---
# ❌ featured_image 누락
title: "Post Title"
---

<!-- ❌ 번호가 순차적이지 않음 -->
<figure>
  <img src="/images/posts/post-slug-02.jpg">
</figure>

<!-- ❌ 03.jpg 누락! -->
<figure>
  <img src="/images/posts/post-slug-04.jpg">
</figure>

<!-- ❌ 네이버에 없는 이미지 추가 -->
<figure>
  <img src="/images/posts/post-slug-99.jpg">
</figure>
```

---

## 🛠️ 문제 해결

### Q1: "Hugo 마크다운 파일을 찾을 수 없습니다"

**원인:** Hugo 마크다운 파일이 없음

**해결:**
```bash
# 먼저 Hugo 마크다운 작성
# content/en/posts/post-slug.md 또는
# content/ja/posts/post-slug.md

# 그 다음 스크립트 실행
python3 download_naver_images.py naver.html post-slug
```

### Q2: "이미지 개수 불일치"

**원인:** 네이버와 Hugo의 이미지 개수가 다름

**해결:**
1. 네이버 HTML에서 이미지 개수 확인 (스크립트 출력 참고)
2. Hugo 마크다운에서 `<figure>` 태그 개수 확인
3. 정확히 같은 개수로 맞추기
4. 다시 스크립트 실행

### Q3: "이미지 순서 불일치"

**원인:** Hugo 이미지 번호가 순차적이지 않음

**해결:**
1. Hugo 마크다운에서 이미지 경로 확인
2. 02, 03, 04, 05... 순차적으로 수정
3. 네이버에 없는 이미지는 삭제
4. 다시 스크립트 실행

### Q4: requests 또는 PIL 모듈이 없다고 나오면

```bash
pip3 install requests pillow beautifulsoup4 lxml
```

### Q5: 권한 오류가 나오면

```bash
chmod +x download_naver_images.py
```

---

## 📝 체크리스트

### 다운로드 전 확인

- [ ] 네이버 HTML 파일 준비 (전체 페이지 소스)
- [ ] Hugo 마크다운 작성 완료 (`content/en/posts/` 또는 `content/ja/posts/`)
- [ ] Hugo featured_image 설정 (`{slug}-01.jpg`)
- [ ] Hugo body images 작성 (`{slug}-02.jpg`, `{slug}-03.jpg`, ...)
- [ ] 이미지 번호 순차적 (누락 없이)
- [ ] 네이버와 Hugo 이미지 개수 일치

### 다운로드 후 확인

- [ ] `static/images/posts/` 디렉토리에 모든 이미지 다운로드 확인
- [ ] 파일명 형식: `{slug}-01.jpg` ~ `{slug}-NN.jpg`
- [ ] `hugo server -D`로 로컬 미리보기
- [ ] 이미지가 올바르게 표시되는지 확인
- [ ] 설명과 이미지가 일치하는지 확인

---

## 🔧 자동으로 하는 일

✅ **네이버 HTML 분석**
- 광고 블록 자동 제거 (`ssp-adcontent`, `ad_power_content_wrap`)
- 단일 이미지 감지 (`se-image`)
- 이미지 그룹 감지 (`se-imageGroup-col-2`, `se-imageGroup-col-3`, ...)

✅ **Hugo 마크다운 검증**
- featured_image 존재 확인
- body images 개수 확인
- 이미지 번호 순서 검증

✅ **이미지 다운로드**
- 네이버 서버에서 고해상도 이미지 다운로드
- PNG/GIF/WebP → JPG 자동 변환
- `static/images/posts/` 폴더에 저장

---

## 📦 전체 워크플로우 예시

```bash
# 1. 저장소 이동
cd ~/mydyney.github.io

# 2. 최신 코드 받기
git pull origin main

# 3. 브랜치 생성
git checkout -b claude/add-post-images-$(date +%s)

# 4. 네이버 HTML 저장 (브라우저에서 직접 복사)
# → naver.html로 저장

# 5. Hugo 마크다운 작성
# → content/en/posts/post-slug.md
# → content/ja/posts/post-slug.md

# 6. 검증 및 다운로드 (한 번에!)
python3 download_naver_images.py naver.html post-slug

# 7. 로컬 미리보기
hugo server -D
# → http://localhost:1313 에서 확인

# 8. 커밋 & 푸시
git add static/images/posts/
git add content/
git commit -m "Add images for post-slug"
git push -u origin HEAD

# 9. GitHub에서 PR 생성 & 병합
```

---

## 주의사항

⚠️ **포스트 슬러그 일치**
- 마크다운 파일명과 동일해야 합니다
- 예: `japan-convenience-store-shopping-best-10.md` → `japan-convenience-store-shopping-best-10`

⚠️ **전체 HTML 필요**
- `<div class="se-main-container">` 전체를 포함해야 합니다
- 부분 HTML은 작동하지 않습니다

⚠️ **Hugo 마크다운 먼저 작성**
- 이미지 다운로드 전에 Hugo 마크다운을 작성해야 합니다
- 검증을 위해 `<figure>` 태그가 필요합니다

---

**작성일:** 2025-11-20
**버전:** 2.0.0 (검증 통합)
**이전 버전:** 1.0.0 (별도 검증)
