---
name: naver_converter
description: Guide and automate the migration of Naver blog posts to Hugo, ensuring strict adherence to formatting, SEO, and multilingual guidelines.
---

# Naver Converter Skill

This skill guides you through the process of migrating a Naver blog post to the Hugo static site structure (EN/JA/ZH-CN). It encapsulates the rules from `MIGRATION_GUIDE.md` and `CONTENT_GUIDELINES.md`.

**CRITICAL PREREQUISITE**: The user MUST have already copied the Naver blog HTML into `naver.md` in the project root. If `naver.md` is empty or missing, ASK the user to provide the content first.

## Workflow Overview

1.  [Step 1: Analysis & Metadata](#step-1-analysis--metadata)
2.  [Step 2: Link Analysis & Mapping](#step-2-link-analysis--mapping)
3.  [Step 3: English Content Generation](#step-3-english-content-generation)
4.  [Step 4: Image Download](#step-4-image-download)
5.  [Step 5: User Review](#step-5-user-review)
6.  [Step 6: Multilingual Expansion](#step-6-multilingual-expansion)
7.  [Step 7: Verification Suite](#step-7-verification-suite)
8.  [Step 8: Finalization & PR](#step-8-finalization--pr)

---

## Step 1: Analysis & Metadata

**Goal**: Extract core metadata and validate limits.

1.  **Read `naver.md`**: Identify the Publish Date, Total Image Count, and logical sections.
2.  **Structural Mapping (CRITICAL)**:
    *   List all H1/H2/H3 headers from `naver.md` to ensure no sections are missed during generation.
    *   Count the number of textual paragraphs to ensure no major content blocks are skipped.
2.  **Determine Slug**:
    *   Create a kebab-case slug (English keywords only, no years unless event-specific).
    *   Example: `roppongi-christmas-illumination` (Good), `roppongi-illumination-2025` (Avoid unless necessary).
    *   **Image**: `/images/posts/{slug}-01.jpg` (Must be absolute path).
3.  **Draft Front Matter (Mental or Scratchpad)**:
    *   Title: EN (50-80 chars), JA (35-55 chars), ZH (40-60 chars).
    *   **Summary (Required)**: 1-2 sentence hook for the hero section (different from description).
    *   **Featured Image (Required)**: `featured_image: /images/posts/{slug}-01.jpg` (Must use this exact key for hero layout).
    *   **Guideline Check**: Ensure titles and descriptions contain keywords and fit character limits.
4.  **Category Mapping (Strict)**:
    *   **Food & Dining**: EN `Food & Dining` | JA `グルメ` | ZH `美食`
    *   **Travel Guide**: EN `Travel Guide` | JA `旅行ガイド` | ZH `旅游指南`
    *   **Shopping**: EN `Shopping` | JA `ショッピング` | ZH `购物`
    *   **Events**: EN `Events & Festivals` | JA `イベント＆フェスティバル` | ZH `节日攻略`
    *   **Tokyo**: EN `Tokyo` | JA `東京` | ZH `东京`
    *   *Reference `CONTENT_GUIDELINES.md` for full list.*
5.  **Strict Language Rule for Taxonomy**:
    *   **English Posts**: Categories/Tags MUST be in **English**.
    *   **Japanese Posts**: Categories/Tags MUST be in **Japanese**.
    *   **Chinese Posts**: Categories/Tags MUST be in **Simplified Chinese**.
    *   *CRITICAL: Never mix languages. An English post cannot have Japanese tags, and vice versa.*

## Step 2: Link Analysis & Mapping

**Goal**: intelligent handling of internal links to prevent 404s.

1.  **Scan for Links**: `grep -o 'blog.naver.com/tokyomate/[0-9]*' naver.md`
2.  **Check `LINK_MAPPING.md`**: For each Naver ID found:
    *   **If Mapped**: Check if the local file exists (`content/en/posts/[slug].md`).
        *   **File Exists**: Use the mapped slug (e.g., `/posts/[slug]/`).
        *   **File Missing**: Use Placeholder + TODO (`href="#"`).
    *   **If Not Mapped**: Use the **Strict TODO Placeholder Format**:
        ```html
        <!-- TODO: Update link after migration
             Naver: https://blog.naver.com/tokyomate/[NAVER_ID]
             Hugo: /posts/[SLUG_TBD]/ -->
        <a href="#" style="color: #667eea;">Link Text</a>
        ```
    *   **CRITICAL**: Do NOT leave broken links (e.g. `/posts/undefined/`). Always use `#` if the target file does not exist.

## Step 3: English Content Generation

**Goal**: Create `content/en/posts/[slug].md`.

**CRITICAL FORMATTING RULES**:
*   **HTML Only in Container**: Wrap content in `<div class="blog-container">`. Inside this, use **HTML tags** (`<strong>`, `<ul>`, `<li>`), NOT Markdown (`**`, `-`).
    *   **WARNING**: Do NOT indent HTML tags inside the container (e.g. 4 spaces). This causes Markdown to render them as code blocks. Keep HTML tags flush left or minimal indentation (2 spaces max if safe).
*   **Headings**: Use Markdown (`##`, `###`) for headings.
*   **Images**:
    *   **1:1 Matching**: Every image in Naver HTML must be present.
    *   **High-Res Quality**: You MUST extract the `src` from `data-linkdata` and append `?type=w966` to the URL. (e.g. `.../image.jpg?type=w966`). Naver defaults to small thumbnails (5KB) if no size is specified or if the wrong URL is used. **Verify file size > 50KB**.
    *   **Extraction Tip**: Use a script to parse `data-linkdata` JSON rather than simple regex, as attributes can vary.
    *   **Format**: Use `<figure>` tags.
    *   **Paths**: Must be absolute, e.g., `/images/posts/{slug}-01.jpg` (assuming images are in `static/images/posts/`).
    *   **Files**: `{slug}-01.jpg` (Featured), `{slug}-02.jpg`, etc.
    *   **Groups**: Detect side-by-side images in original. **CRITICAL**: Wrap the entire group (`<div class="image-group-2">...</div>`) AND the `<figcaption>` in a parent `<figure>` tag.
        ```html
        <figure>
          <div class="image-group-2">
            <figure><img ...></figure>
            <figure><img ...></figure>
          </div>
          <figcaption>Caption...</figcaption>
        </figure>
        ```
    *   **Captions**: If original has a caption, add `<figcaption style="font-size: 0.85em; text-align: center;">Transaction...</figcaption>`.
*   **Japanese Translation Guidelines**:
    *   **Native Perspective**: Write from a **Japanese reader's perspective**, not a Korean tourist's view. Remove Korean-specific references (e.g., "한화로 약 2만원" → "約2,680円").
    *   **Natural Expression**: Use proper Japanese notation - prefer kanji over katakana for established brand names (e.g., "果実園リーベル" not "カジツエンリーベル", "治一郎" not "ジイチロ").
    *   **Cultural Adaptation**: Adapt content to Japanese cultural context - prices in yen only, local perspective on locations and accessibility.
    *   **Tone**: Use polite desu/masu form (です・ます体) throughout.
*   **Tables**: Convert to pure HTML tables with centered text and header background `#f7f7f7`. NO Markdown tables.
*   **Editor's Note**: Append the mandatory "Editor's Note" block at the bottom. **Use this EXACT HTML (do not modify styles):**

    ```html
    <!-- English Version -->
    <div class="editors-note">
      <p style="text-align: left; font-style: italic;"><strong>Editor's Note</strong></p>
      <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
        This article is based on the author's actual experiences and original content from <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>. It has been translated and adapted to provide authentic travel information about Tokyo for global readers.
      </p>
    </div>
    ```
    *(See `MIGRATION_GUIDE.md` for JA/ZH versions)*

## Step 4: Image Download

**Goal**: Get images ready for review.

**TIMING**: Run this **IMMEDIATELY** after creating the English draft, *before* asking for review.

**Action**: Extract high-res image URLs (`?type=w966`) and download them manually to the correct path.

```bash
# 1. Image Extraction Script (Recommended)
# Create a python script to parse `data-linkdata`, extract `src`, append `?type=w966`, and generate curl commands.
# This prevents missing images that simple grep might overlook.

# 2. Verify Order
# Compare the downloaded file list against the images in `naver.md`.
# Ensure {slug}-01.jpg matches the first image in the post, etc. 
```

## Step 5: User Review

1.  **Start Server**: Run `hugo server -D` in the background (using `run_command` with `WaitMsBeforeAsync: 3000`) to ensure the preview link works.
2.  **Action**: Notify the user.
    *   Provide the preview link: `http://localhost:1313/posts/[slug]/`
    *   Ask for approval on formatting, content, and image positioning.
    *   **WAIT** for "OK" before proceeding.

## Step 6: Multilingual Expansion

**Goal**: Create `content/ja/posts/[slug].md` and `content/zh-cn/posts/[slug].md`.

1.  **Common**: Use the **SAME** `translationKey` and images as English.
2.  **Japanese**:
    *   **Tags/Categories**: Must be in Japanese (check `CONTENT_GUIDELINES.md` for mapping).
    *   **Content**: Natural Japanese (desu/masu). No "Japan's X" phrasing. Remove tax-free info if irrelevant.
3.  **Chinese**:
    *   **YAML Safety**: **NO** special quotes (`「`, `」`) in front matter strings.
    *   **Tags/Categories**: Must be in Chinese.
    *   **Content**: "Xiaohongshu" style (engaging, emojis).

## Step 7: Verification Suite

**Goal**: Mathematical proof of completeness.

Run these commands to verify parity:

```bash
# 1. Image Counts
grep -o '<img' naver.md | wc -l
grep -o '<img' content/en/posts/[slug].md | wc -l
grep -o '<img' content/ja/posts/[slug].md | wc -l
grep -o '<img' content/zh-cn/posts/[slug].md | wc -l

# 2. Caption Counts
grep -o 'se-caption' naver.md | wc -l  # adjust based on raw HTML class
grep -o '<figcaption' content/en/posts/[slug].md | wc -l
# ... repeat for JA/ZH

# 3. Link Counts
grep -o 'blog.naver.com/tokyomate' naver.md | wc -l
grep -E '(/posts/|TODO: Update link)' content/en/posts/[slug].md | wc -l
# ... repeat for JA/ZH
```

**Report** results to the user (e.g., "✅ Images: Source 15 = EN 15 = JA 15 = ZH 15").

## Step 8: Finalization & PR

1.  **Update `LINK_MAPPING.md`**: Add the new slug, set status to ✅.
2.  **Commit**: `git add .` and `git commit`.
3.  **Check Clean Build** (if categories changed): `hugo --cleanDestinationDir`.
4.  **Prepare PR Description**: Use the template below.

### PR Description Template

```markdown
## Summary
[Brief overview]

## Changes
### 1. New Blog Posts
- EN/JA/ZH versions created for [Slug].
- SEO: Title lengths verified.
- Images: [N] images, 1:1 match.
- Links: [N] links converted.

### 2. Database
- Updated LINK_MAPPING.md.

## Verification
- ✅ Image Count: [N]
- ✅ Links Verified
- ✅ Front Matter Validated
```

## References & Resources

The following files are included in this skill for reference:

*   **Guidelines**:
    *   [MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md): Complete workflow rules.
    *   [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md): Formatting & SEO rules.
*   **Examples**:
    *   [Good Migration Example](examples/good_migration_example.md): A full reference implementation (`tokyo-christmas-markets-guide-2025`).
