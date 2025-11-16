# 네이버 블로그 이미지 다운로드 가이드

## 준비물

Mac에 Python3가 설치되어 있어야 합니다. (대부분의 Mac에 기본 설치됨)

```bash
# Python 확인
python3 --version
```

## 사용 방법

### 1단계: 저장소 클론 (처음 한 번만)

```bash
cd ~/Desktop
git clone https://github.com/mydyney/mydyney.github.io.git
cd mydyney.github.io
```

### 2단계: 필요한 라이브러리 설치

```bash
pip3 install requests
```

### 3단계: 네이버 블로그 HTML 저장

1. 네이버 블로그 글 열기
2. F12 (개발자 도구) → Elements 탭
3. `<div class="se-main-container">` 찾기
4. 우클릭 → Copy → Copy outerHTML
5. 텍스트 에디터에 붙여넣기
6. `naver_blog.html` 로 저장 (저장소 폴더에)

### 4단계: 스크립트 실행

```bash
python3 download_naver_images.py naver_blog.html 포스트이름
```

**예시:**
```bash
python3 download_naver_images.py naver_blog.html kirimugiya-jinroku-shinjuku
```

### 5단계: Git 커밋 & 푸시

```bash
git add static/images/posts/
git add content/ko/posts/
git commit -m "Add images for blog post"
git push origin main
```

## 자동으로 하는 일

✅ HTML에서 모든 이미지 URL 추출
✅ 네이버 서버에서 이미지 다운로드
✅ `static/images/posts/` 폴더에 저장
✅ 마크다운 파일의 이미지 경로 자동 변경

## 트러블슈팅

### requests 모듈이 없다고 나오면:
```bash
pip3 install requests
```

### 권한 오류가 나오면:
```bash
chmod +x download_naver_images.py
```

### Python3가 없다고 나오면:
```bash
brew install python3
```

## 예시 전체 흐름

```bash
# 1. 저장소 이동
cd ~/Desktop/mydyney.github.io

# 2. 최신 코드 받기
git pull origin main

# 3. 브랜치 생성
git checkout -b claude/add-images-$(date +%s)

# 4. HTML 파일 준비 (직접 복사해서 naver.html로 저장)

# 5. 이미지 다운로드
python3 download_naver_images.py naver.html my-post-name

# 6. 커밋 & 푸시
git add .
git commit -m "Add images for blog post"
git push -u origin HEAD

# 7. GitHub에서 PR 생성 & 병합
```

## 주의사항

- 포스트이름은 마크다운 파일명과 동일해야 합니다
- 예: `kirimugiya-jinroku-shinjuku.md` → `kirimugiya-jinroku-shinjuku`
- HTML 파일은 `<div class="se-main-container">` 전체를 포함해야 합니다
