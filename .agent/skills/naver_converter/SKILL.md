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

## Step 0: Content Mapping (NEW & MANDATORY)

**Goal**: Create a visual/mental inventory of the source content to ensure 1:1 parity and correct sequencing.

1.  **Inventory `naver.md`**:
    *   List every heading (H2, H3).
    *   Count every paragraph block.
    *   List every image with its corresponding caption (if any).
    *   List every link and its purpose (e.g., "Google Maps link for Item X").
2.  **Identify Duplicates/Errors**: Check if the source has duplicate links or incorrect descriptions and plan corrections in advance (documenting them in the implementation plan).

---

## Step 1: Analysis & Metadata

**Goal**: Extract core metadata and validate limits.

1.  **Verify `naver.md` exists and has content**:
    *   Read the file at the project root: `/Users/tommygo/Desktop/personal-project/mydyney.github.io/naver.md`
    *   If the file is empty or missing, STOP and ask the user to provide the content first.
2.  **Extract Metadata from `naver.md`**:
    *   **Publish Date**: Look for `se_publishDate`.
    *   **Total Image Count**: Count all `<img>` tags.
    *   **Post Title**: Extract from the document title section.
3.  **Determine Slug**:
    *   Create a kebab-case slug (English keywords only, no years).
    *   **Check `LINK_MAPPING.md`**: Ensure the slug matches the mapping if one exists.
4.  **Category Mapping (Strict)**:
    *   **Food & Dining**: EN `Food & Dining` | JA `グルメ` | ZH `美食`
    *   **Travel Guide**: EN `Travel Guide` | JA `旅行ガイド` | ZH `旅游指南`
    *   **Shopping**: EN `Shopping` | JA `ショッピング` | ZH `购物`
    *   *Reference `CONTENT_GUIDELINES.md` for full list.*

---

## Step 2: Link Analysis & Mapping

**Goal**: Detailed verification of all links.

1.  **Scan for Links**: `grep -o 'blog.naver.com/tokyomate/[0-9]*' naver.md`
2.  **Verify Source Correctness**: For Google Maps links, check if they actually point to the correct location for each item. If the source has duplicates (e.g., same link for two different shops), search for the correct link and use it.
3.  **Check `LINK_MAPPING.md`**: For each Naver ID found:
    *   **If Mapped**: Check if the local file exists (`content/en/posts/[slug].md`).
        *   **File Exists**: Use the mapped slug (e.g., `/posts/[slug]/`).
        *   **File Missing**: Use Placeholder + TODO (`href="#"`).
    *   **If Not Mapped**: Use the **Strict TODO Placeholder Format**.

---

## Step 3: English Content Generation

**Goal**: Create `content/en/posts/[slug].md`.

**CRITICAL FORMATTING RULES**:
*   **STRICT HTML Only in Container**: Wrap content in `<div class="blog-container">`. Inside this, use **HTML tags** (`<strong>`, `<ul>`, `<li>`, `<p>`, `<a>`), **NEVER** Markdown (`**`, `-`, `[text](url)`).
*   **Google Maps Standard**:
    *   Format: `📍 <a href="..." target="_blank" rel="noopener" style="color: #667eea; text-decoration: underline;"><strong>View on Google Maps</strong></a>`
    *   JA: `<strong>Googleマップで見る</strong>`, ZH: `<strong>在 Google 地图上查看</strong>`.
*   **Headings**: Use Markdown (`##`, `###`) for headings.
*   **Images**:
    *   **1:1 Matching**: Every image in Naver HTML must be present.
    *   **High-Res Quality**: Append `?type=w966` to the URL.
    *   **Groups**: Wrap groups in `<div class="image-group-X">` inside a `<figure>`.
    *   **Captions**: Every caption in `naver.md` MUST be translated and added via `<figcaption style="font-size: 0.85em; text-align: center;">`.

---

## Step 4: Image Download

**Action**: Extract high-res image URLs (`?type=w966`) and download them immediately.
```bash
python3 download_naver_images.py "[slug]"
```

---

## Step 5: User Review

1.  **Start Server**: `hugo server -D`.
2.  **Notification**: Provide the link `http://localhost:1313/posts/[slug]/`.
3.  **Self-Correction**: Before notifying the user, do a `grep` search for Markdown syntax inside the `.md` file to catch any `**` or `[` characters that shouldn't be there.

---

## Step 6: Multilingual Expansion

**Goal**: Create Japanese (`ja`) and Chinese (`zh-cn`) versions.

1.  **Consistency**: Use the **SAME** `translationKey` and images as English.
2.  **Japanese**: Natural desu/masu tone. No "Japan's X" phrasing. Remove tax-free info for JA if it's a guide for domestic Japanese. Use original Japanese/Kanji names directly without parenthetical explanations or furigana.
3.  **Chinese**: Engaging style with emojis. **NO** special quotes in front matter. Use "English/International Name (Kanji/Original)" format for shop names.
4.  **Shop Name Notation**: Refer to `CONTENT_GUIDELINES.md` for strict parenthetical notation rules (EN/ZH: `Name (Original)`, JA: `Original` only).

---

## Step 7: Verification Suite (MANDATORY)

Run these checks:
```bash
# 1. Total Parity Check
# Images: naver.md count vs Hugo count
# Captions: naver.md count vs Hugo count
# Links: naver.md count vs Hugo count

# 2. Markdown Leak Check (CRITICAL)
# Search for Markdown syntax inside the blog-container area.
grep -E '\*\*|\[.*\]\(.*\)|^- ' content/*/posts/[slug].md
```

---

## Step 8: Finalization & PR

1.  **Update `LINK_MAPPING.md`**: Set status to ✅.
2.  **Commit**: `git add .` and `git commit`.

## References & Resources

The following files are included in this skill for reference:

*   **Guidelines**:
    *   [MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md): Complete workflow rules.
    *   [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md): Formatting & SEO rules.
*   **Examples**:
    *   [Good Migration Example](examples/good_migration_example.md): A full reference implementation (`tokyo-christmas-markets-guide-2025`).
