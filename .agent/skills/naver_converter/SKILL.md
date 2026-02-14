---
name: naver_converter
description: Migrate Naver blog posts to Hugo with strict formatting, SEO, and multilingual guidelines (EN/JA/ZH-CN).
---

# Naver Blog → Hugo Migration Skill

Migrates a Naver blog post to the Hugo static site in three languages (EN/JA/ZH-CN).

**References** (consult for detailed rules):
- [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md) — Formatting, SEO, tags, categories, Editor's Note
- [MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md) — Full workflow, link mapping, scripts
- [Good Example](examples/good_migration_example.md) — Reference implementation

**Prerequisite**: The user has prepared `naver.md` with the Naver blog HTML at the project root. **NEVER** try to fetch/scrape the Naver URL directly.

---

## Workflow Overview

| Step | Action | Approval Gate? |
|------|--------|---------------|
| 1 | Analysis & Planning | No |
| 2 | English Content Generation | No |
| 3 | Image Download | No |
| 4 | English Review | **YES — STOP** |
| 5 | Japanese & Chinese Versions | No |
| 6 | Verification & Review | **YES — STOP** |
| 7 | Finalization | No |

**Only 2 approval gates.** Do NOT stop for approval at any other point.

---

## Step 1: Analysis & Planning

**Goal**: Extract metadata, plan the migration, and present a summary to the user.

### 1.1 Read and Analyze `naver.md`

Read the file at the project root. If empty or missing, ask the user to provide content and STOP.

### 1.2 Extract Metadata

- **Publish date**: Look for `se_publishDate` or post metadata
- **Post title**: Extract from the document title section
- **Total image count**:
  ```bash
  grep -c "se-image-resource" naver.md
  ```
- **Image group locations**:
  ```bash
  grep -n "se-imageGroup-col-" naver.md
  ```
  Note group types (col-2, col-3, col-4) and their positions

### 1.3 Determine Slug

1. **Search `LINK_MAPPING.md` for the Naver post ID FIRST**
2. If found: **reuse the existing slug** (even if status is `pending`)
3. If NOT found: create new kebab-case slug (English keywords only, no years for evergreen content, under 60 chars)
4. **Register in `LINK_MAPPING.md`** Quick Reference Table with status `pending`

### 1.4 Scan Internal Links

```bash
grep -o 'blog.naver.com/tokyomate/[0-9]*' naver.md | sort -u
```

For each Naver link found, check `LINK_MAPPING.md`:
- **Status ✅ AND file exists** → use Hugo slug
- **Status pending OR not found** → use TODO placeholder format (see **Rule 6**). The link MUST be visible to readers as a clickable `<a href="#">` element — never use invisible HTML comments alone

### 1.5 Map Categories & Tags

Categories and tags MUST match content language:

| EN | JA | ZH-CN |
|----|-----|-------|
| Food & Dining | グルメ | 美食 |
| Travel Guide | 旅行ガイド | 旅游指南 |
| Shopping | ショッピング | 购物 |
| Events & Festivals | イベント＆フェスティバル | 活动与节日 |

See [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md) for full list.

### 1.6 Present Summary

Present analysis to the user (proposed slug, image count, link conversion plan, categories). Then **proceed immediately to Step 2** — do NOT wait for approval here.

---

## Step 2: English Content Generation

**Goal**: Create `content/en/posts/[slug].md`.

### 2.1 Front Matter

**Line 1 MUST be `---`** (Hugo ignores front matter if missing).

```yaml
---
title: "[SEO Title — 50-80 chars, key info in first 55]"
date: [Original date with +09:00 timezone]
draft: false
description: "[SEO description — 150-180 chars]"
categories: ["[English Category]"]
tags: ["[english-kebab-tags]"]
featured_image: "/images/posts/[slug]-01.jpg"
translationKey: "[slug]"
---
```

### 2.2 Content Structure

```html
<div class="blog-container">

<p style="text-align: center; font-size: 1.1rem; color: #555;">[Intro text]</p>

[Content with ## headings, images, tables, info boxes]

<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>Editor's Note</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    This article is based on the author's actual experiences and original content from <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>. It has been translated and adapted to provide authentic travel information about Tokyo for global readers.
  </p>
</div>

</div>
```

### 2.3 Formatting Rules

**Rule 1: HTML only inside `blog-container`**
- ✅ Use: `<strong>`, `<ul>`, `<li>`, `<p>`, `<a>`, `<table>`
- ❌ Never: `**bold**`, `- list item`, `[link](url)`
- Exception: Headings use Markdown (`##`, `###`)

**Rule 2: Images — strict 1:1 matching with naver.md**
- Every image in naver.md MUST appear in Hugo — NO additions, NO deletions
- Preserve the exact linear order from naver.md
- Never renumber existing images
- ⚠️ **CRITICAL: Figcaption source links** — If a Naver image caption contains an external source link (이미지출처, 사진출처, Source), the `<figcaption>` MUST include a clickable `<a>` tag linking to the original source. Never render source credits as plain text only.
  - ✅ `(<a href="https://example.com" target="_blank" rel="noopener" style="color: #667eea;">Source: example.com</a>)`
  - ❌ `(Source: example.com)` — plain text, no link

**Single images:**
```html
<figure>
  <img src="/images/posts/[slug]-XX.jpg" alt="[descriptive alt text]">
  <figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>
</figure>
```

**Image groups** (2, 3, or 4 side-by-side) — use inline flex with EXACT Naver ratios:

**Step A: Extract exact ratios from naver.md**
```bash
# Find all image groups and their width percentages
grep -B2 -A5 "se-imageGroup-col-" naver.md | grep -o 'width:[0-9.]*%'
```
Convert percentages to decimals (e.g., `width:51.77%` → `flex: 0.518`, `width:48.23%` → `flex: 0.482`). Ratios in each group MUST sum to ~1.0.

**Step B: Apply to HTML**
```html
<!-- 2-image group -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.518;">
    <img src="/images/posts/[slug]-XX.jpg" alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.482;">
    <img src="/images/posts/[slug]-YY.jpg" alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>

<!-- 3-image group -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.333;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.333;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.334;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>

<!-- 4-image group (2x2): use TWO separate flex rows -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.5;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.5;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<div style="display: flex; gap: 10px; margin: 0 0 20px 0;">
  <figure style="margin: 0; flex: 0.5;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.5;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>
```

**Multi-row groups (5+ images):**

Naver uses `se-imageGroup-col-N` where N is the number of columns per row. For groups with more images than columns, Naver wraps them into multiple rows.

**How to determine the layout:**
1. Find the column class: `se-imageGroup-col-2`, `col-3`, `col-4`
2. Count total images inside that group
3. Split into rows of N images each (last row may have fewer)
4. Extract the `width:XX%` for EACH image in EACH row

**Example: 6 images in a col-3 group (3+3 layout)**
```html
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.333;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.333;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.334;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<div style="display: flex; gap: 10px; margin: 0 0 20px 0;">
  <figure style="margin: 0; flex: 0.333;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.333;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.334;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>
```

**Example: 5 images in a col-2 group (2+2+1 layout)**
```html
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.518;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.482;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<div style="display: flex; gap: 10px; margin: 0;">
  <figure style="margin: 0; flex: 0.518;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.482;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<div style="display: flex; gap: 10px; margin: 0 0 20px 0;">
  <figure style="margin: 0; flex: 1;">
    <img src="..." alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>
```

**Example: 9 images in a col-3 group (3+3+3 layout)**
```html
<!-- Row 1 -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.333;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
  <figure style="margin: 0; flex: 0.333;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
  <figure style="margin: 0; flex: 0.334;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
</div>
<!-- Row 2 -->
<div style="display: flex; gap: 10px; margin: 0;">
  <figure style="margin: 0; flex: 0.333;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
  <figure style="margin: 0; flex: 0.333;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
  <figure style="margin: 0; flex: 0.334;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
</div>
<!-- Row 3 -->
<div style="display: flex; gap: 10px; margin: 0 0 20px 0;">
  <figure style="margin: 0; flex: 0.333;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
  <figure style="margin: 0; flex: 0.333;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
  <figure style="margin: 0; flex: 0.334;"><img src="..." alt="..." style="width: 100%; height: auto; display: block;"></figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">[Caption]</figcaption>
```

**Multi-row margin pattern:**
- First row: `margin: 20px 0;` (top spacing)
- Middle rows: `margin: 0;` (no extra spacing, gap only)
- Last row: `margin: 0 0 20px 0;` (bottom spacing)
- Single row: `margin: 20px 0;` (both)

**Critical rules for image groups:**
- ❌ NEVER estimate ratios — always extract exact values from `naver.md`
- ❌ NEVER use CSS classes (`image-group-2`) — use inline flex for ratio preservation
- ✅ Extract the column count from `se-imageGroup-col-N` to determine images per row
- ✅ Extract `width:XX%` for EACH image — ratios may differ between rows
- ✅ Verify each ROW's flex values sum to ~1.0 (±0.01)
- ✅ For the last row with fewer images (e.g., 1 remaining), use `flex: 1` for single image
- ✅ Always include `alt` text on every `<img>` (required for SEO and download script validation)
- ✅ `figcaption` goes OUTSIDE all flex `<div>` rows, not inside

**Rule 3: Tables — always use `schedule-table` class for visible borders**
```html
<table class="schedule-table">
  <thead>
    <tr>
      <th style="background-color:#e2f7ff; text-align: center;">Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;">Cell content</td>
    </tr>
  </tbody>
</table>
```
- ✅ Always add `class="schedule-table"` — this provides visible cell borders via `/static/css/blog-post-common.css`
- ✅ Use `<thead>` for header rows with background color
- ❌ NEVER use plain `<table>` without the class — cells become hard to read without borders

**Rule 4: Google Maps links**
```html
<p>📍 <a href="[URL]" target="_blank" rel="noopener" style="color: #667eea; text-decoration: underline;"><strong>View on Google Maps</strong></a></p>
```

**Rule 5: Internal link prefixes**
- EN: `/posts/[slug]/` (NO `/en/` prefix)
- JA: `/ja/posts/[slug]/`
- ZH-CN: `/zh-cn/posts/[slug]/`

**Rule 6: TODO placeholders** (for unmigrated links)
- ⚠️ **CRITICAL**: Every Naver internal link MUST produce a visible link in the output — even unmigrated ones
- ❌ NEVER use only an invisible HTML comment (`<!-- TODO -->`) — readers will see nothing
- ✅ ALWAYS include the visible `<a href="#">` element so the link text appears on the page
```html
<!-- TODO: Update link after migration
     Naver: https://blog.naver.com/tokyomate/[POST_ID]
     Hugo: /posts/[expected-slug]/ -->
<p><a href="#" style="color: #667eea;"><strong>👉 [Link Text]</strong></a></p>
```

**Rule 7: Content fidelity**
- ❌ Never add sections/headers not in naver.md
- ❌ Never reorganize or restructure content
- ❌ Never summarize detail-rich sections (timetables, menus, step-by-step guides)
- ✅ Translate ALL content faithfully — every paragraph, list item, and tip
- ✅ Preserve exact physical sequence of text, images, and links

**Rule 8: Editor's Note is MANDATORY**
- Every post MUST end with the `editors-note` div (see format in 2.2 above)
- Place after all content, before closing `</div>`
- Replace `[NAVER_POST_ID]` with the actual Naver post ID

**Rule 9: Related guides / footer links**
- The `👉` emoji MUST be inside the `<a>` tag
- ✅ `<a href="...">👉 <strong>Title</strong></a>`
- ❌ `👉 <a href="..."><strong>Title</strong></a>`

After creating the English version, **proceed immediately to Step 3** — do NOT wait for approval.

---

## Step 3: Image Download

Run immediately after creating the English version:

```bash
python3 download_naver_images.py "[slug]"
```

This script:
- Reads `naver.md` and extracts all images in sequential order
- Validates against the English markdown (1:1 matching)
- Downloads all images to `static/images/posts/`
- Auto-converts to JPG: `{slug}-01.jpg`, `{slug}-02.jpg`, etc.

If validation fails, fix the image references in the English version and re-run.

After download completes, **proceed immediately to Step 4**.

---

## Step 4: English Review

### ⏸️ APPROVAL GATE 1 — Wait for user approval

1. **Start Hugo server** (if not already running):
   ```bash
   hugo server -D
   ```

2. **Run self-check** for Markdown leaks inside blog-container:
   ```bash
   grep -E '\*\*|\[.*\]\(.*\)' content/en/posts/[slug].md
   ```
   Fix any matches before presenting to user.

3. **Present preview link to user**:
   ```
   English Version: http://localhost:1313/posts/[slug]/
   ```

4. **Wait for user response**:
   - "OK", "next", "완료" → proceed to Step 5
   - Feedback → make corrections, re-present preview
   - **Do NOT proceed to Step 5 until user explicitly approves**

**If user reports fidelity errors**: Re-analyze the FULL naver.md to catch any other missed nuances.

---

## Step 5: Japanese & Chinese Versions

**Only proceed after user approves English version in Step 4.**

Create both files:
- `content/ja/posts/[slug].md`
- `content/zh-cn/posts/[slug].md`

### 5.1 Shared Rules (All Languages)

- Same `translationKey`, `date`, and image references as EN
- Language-specific tags and categories (JA tags for JA, ZH-CN tags for ZH-CN)
- Same HTML structure — translate text content ONLY, keep all HTML tags intact
- ✅ Use: `<strong>`, `<ul>`, `<li>`, `<p>`, `<a>` inside blog-container
- ❌ Never: `**text**`, `- item`, `[link](url)` inside blog-container
- Internal links: add `/ja/` or `/zh-cn/` prefix

### 5.2 Japanese-Specific Rules

| Aspect | Rule |
|--------|------|
| Tone | Polite です/ます, friendly and approachable |
| Shop names | Original Japanese only — `壽々喜園` (NO parenthetical readings) |
| Currency | Keep JPY as-is (domestic readers) |
| "日本の" prefix | NEVER use — readers are Japanese |
| Tax-free info | DELETE (only relevant to foreign tourists) |
| Google Maps text | `<strong>Googleマップで見る</strong>` |
| Editor's Note title | `編集者注` |

### 5.3 Chinese-Specific Rules

| Aspect | Rule |
|--------|------|
| Tone | Engaging, practical, uses emojis (小红书 style) |
| Shop names | English (Original) format — `Suzukien (壽々喜園)` |
| Currency | Convert to USD (10,000 KRW ≈ $7.50) |
| YAML front matter | ❌ NEVER use `「」` or `""` in quoted strings |
| Google Maps text | `<strong>在 Google 地图上查看</strong>` |
| Editor's Note title | `编者按` |

### 5.4 Editor's Note Templates

**Japanese:**
```html
<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>編集者注</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    本記事は、筆者の実際の体験に基づき、公式ブログ <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a> に掲載されたオリジナルコンテンツを翻訳・再構成したものです。リアルな東京の旅情報をお届けします。
  </p>
</div>
```

**Chinese:**
```html
<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>编者按</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    本文基于作者的亲身经历，编译自韩国原创博客 <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>。内容经过翻译与调整，旨在为您分享真实可靠的东京旅行资讯。
  </p>
</div>
```

### 5.5 Klook Affiliate Links

Convert all Klook links to the Tripmate account and localize:
- **AID**: `110453`, **ADID**: `1208343`
- EN: `/en-US/` + `?currency=USD&n_currency=USD&ignore_ip=1`
- JA: `/ja/` + `?currency=JPY&n_currency=JPY&ignore_ip=1`
- ZH-CN: `/zh-CN/` + `?currency=CNY&n_currency=CNY&ignore_ip=1`

See [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md#klook-affiliate-link-conversion) for full template.

After creating both versions, **proceed immediately to Step 6**.

---

## Step 6: Verification & Review

**Goal**: Run all automated checks, present results and preview links to user.

### 6.1 Image Count (must match across all versions)

```bash
SLUG="[slug]"
NAVER=$(grep -c "se-image-resource" naver.md)
EN=$(grep -c '<img' content/en/posts/$SLUG.md)
JA=$(grep -c '<img' content/ja/posts/$SLUG.md)
ZH=$(grep -c '<img' content/zh-cn/posts/$SLUG.md)
echo "Images — Naver: $NAVER | EN: $EN | JA: $JA | ZH: $ZH"
```

### 6.1b Image Group Count & Ratio Check

```bash
# Group count comparison
NAVER_GROUPS=$(grep -c "se-imageGroup-col-" naver.md)
EN_GROUPS=$(grep -c "display: flex" content/en/posts/$SLUG.md)
echo "Image Groups — Naver: $NAVER_GROUPS | EN: $EN_GROUPS"

# Verify flex ratios sum to ~1.0 per row
grep -o 'flex: [0-9.]*' content/en/posts/$SLUG.md | awk -F': ' '{print $2}'
# Manually verify: group values by row and confirm each row sums to ~1.0
```

### 6.2 Caption Count

```bash
echo "Captions — EN: $(grep -c '<figcaption' content/en/posts/$SLUG.md) | JA: $(grep -c '<figcaption' content/ja/posts/$SLUG.md) | ZH: $(grep -c '<figcaption' content/zh-cn/posts/$SLUG.md)"
```

### 6.3 Markdown Leak Check (must be 0)

```bash
for lang in en ja zh-cn; do
  COUNT=$(grep -c '\*\*' content/$lang/posts/$SLUG.md 2>/dev/null || echo 0)
  [ "$COUNT" -gt 0 ] && echo "❌ $lang: $COUNT markdown bold leaks" || echo "✅ $lang: clean"
done
```

### 6.4 Front Matter Check

```bash
for lang in en ja zh-cn; do
  HEAD=$(head -1 content/$lang/posts/$SLUG.md)
  [ "$HEAD" = "---" ] && echo "✅ $lang: front matter OK" || echo "❌ $lang: missing --- on line 1"
done
```

### 6.5 Link Count

```bash
NAVER_LINKS=$(grep -c 'blog.naver.com/tokyomate' naver.md)
EN_LINKS=$(grep -cE '(/posts/|TODO: Update link)' content/en/posts/$SLUG.md)
echo "Links — Naver: $NAVER_LINKS | EN converted+TODO: $EN_LINKS"
```

### 6.6 Structural Parity

Compare EN, JA, ZH-CN side-by-side:
- Paragraph counts match
- Heading structures identical
- Image positions identical
- `👉` emoji is INSIDE `<a>` tags
- Footer link icons match EN version

### 6.7 Present Results

**Report format:**
```
✅ Image Count: Naver [X] = EN [X] = JA [X] = ZH-CN [X]
✅ Caption Count: EN [X] = JA [X] = ZH-CN [X]
✅ Markdown Leaks: None
✅ Front Matter: All OK
✅ Links: Naver [X] → EN [X] converted+TODO
```

**Provide all preview links:**
```
EN:    http://localhost:1313/posts/[slug]/
JA:    http://localhost:1313/ja/posts/[slug]/
ZH-CN: http://localhost:1313/zh-cn/posts/[slug]/
```

### ⏸️ APPROVAL GATE 2 — Wait for user to review all languages

- "OK", "완료" → proceed to Step 7
- Feedback → make corrections, re-verify, re-present

---

## Step 7: Finalization

After user confirms:

### 7.1 Update LINK_MAPPING.md

- Change status from `pending` to `✅`
- Set date to today's date (YYYY-MM-DD)

### 7.2 Commit

```bash
git add content/en/posts/[slug].md content/ja/posts/[slug].md content/zh-cn/posts/[slug].md static/images/posts/[slug]-* LINK_MAPPING.md
git commit -m "feat: Add [slug] blog post (EN/JA/ZH-CN) with [N] images

New Content:
- Created [topic] guide in 3 languages
- Added [N] images
- All three language versions (EN/JA/ZH-CN)

Link Updates:
- Updated LINK_MAPPING.md (Status: ✅)
- Converted [N] internal links

Naver ID: [POST_ID]
Slug: [slug]"
```

---

## Common Errors

### 1. Wrong front matter image field
- ❌ `cover: image: "..."` → ✅ `featured_image: "/images/posts/[slug]-01.jpg"`

### 2. Markdown syntax inside blog-container
- ❌ `**bold**` → ✅ `<strong>bold</strong>`
- ❌ `- item` → ✅ `<ul><li>item</li></ul>`
- ❌ `[text](url)` → ✅ `<a href="url">text</a>`

### 3. Missing or wrong Editor's Note
- ❌ `> Editor's Note:` (blockquote) → ✅ Use `<div class="editors-note">` with exact format from Step 2.2
- ❌ `<div class="editor-note">` → ✅ `<div class="editors-note">` (plural)

### 4. Wrong figcaption style
- ❌ `font-size: 0.85em` → ✅ `style="font-size: 0.7em; text-align: center;"`

### 5. Adding content not in original
- ❌ Adding section headers not in naver.md
- ❌ Reorganizing content structure
- ✅ Translate existing content exactly as structured

### 6. Image numbering errors
- ❌ Renumbering images after additions/deletions
- ✅ Keep original numbers, only add with next available number

### 7. Wrong TODO placeholder
- ❌ `href="/posts/unknown/"` → ✅ `href="#"` with TODO comment including Naver URL and expected Hugo path

### 8. Slug not checked against LINK_MAPPING.md
- Always search LINK_MAPPING.md for the Naver ID FIRST before creating a new slug

### 9. Chinese YAML special characters
- ❌ `title: "东京「浪花家」攻略"` → ✅ `title: "东京浪花家攻略"`
- Never use `「」`, `""`, or `''` in Chinese YAML front matter

### 10. Mixed-language tags/categories
- ❌ English tags on JA post → ✅ JA tags on JA post, ZH-CN tags on ZH-CN post

### 11. Double headers
- ❌ Two consecutive `##` headings → ✅ Single heading only

### 12. `👉` emoji outside link
- ❌ `👉 <a href="...">` → ✅ `<a href="...">👉 <strong>Title</strong></a>`

### 13. HTML escaping
- ❌ `\<div\>` with backslashes → ✅ `<div>` clean HTML

### 14. Missing LINK_MAPPING.md registration
- Always add Naver ID + slug with `pending` status BEFORE starting content generation

---

## Quick Reference

### Verification Commands

```bash
SLUG="[slug]"

# Image count comparison
echo "Naver: $(grep -c 'se-image-resource' naver.md)"
echo "EN: $(grep -c '<img' content/en/posts/$SLUG.md)"

# Image group count
echo "Naver groups: $(grep -c 'se-imageGroup-col-' naver.md)"
echo "EN groups: $(grep -c 'display: flex' content/en/posts/$SLUG.md)"

# Markdown leak check
grep -c '\*\*' content/en/posts/$SLUG.md

# Front matter check
head -1 content/en/posts/$SLUG.md

# Internal link scan
grep -o 'blog.naver.com/tokyomate/[0-9]*' naver.md | sort -u
```

### SEO Limits

| | EN | JA | ZH-CN |
|---|---|---|---|
| Title | 50-80 chars | 35-55 chars | 40-60 chars |
| Description | 150-180 chars | 100-140 chars | 120-160 chars |
| Tags | kebab-case | Japanese text | Chinese text |

### Image Download

```bash
python3 download_naver_images.py "[slug]"
# Dependencies: pip3 install requests pillow beautifulsoup4 lxml
```

---

## References

- [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md) — Formatting, SEO, tags, categories
- [MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md) — Full workflow, link mapping, scripts
- [Good Example](examples/good_migration_example.md) — Reference implementation (`tokyo-christmas-markets-guide-2025`)
