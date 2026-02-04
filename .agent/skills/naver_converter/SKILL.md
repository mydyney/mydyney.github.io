---
name: naver_converter
description: Guide and automate the migration of Naver blog posts to Hugo, ensuring strict adherence to formatting, SEO, and multilingual guidelines.
---

# Naver Converter Skill

This skill guides you through the process of migrating a Naver blog post to the Hugo static site structure (EN/JA/ZH-CN). 

*   **[MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md)**: **Workflow Document** (Process, scripts, verification checklists).
*   **[CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md)**: **Master Reference** (Formatting, HTML snippets, SEO, translation rules).

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
2.  **Create Artifact**: Write this inventory to `<appDataDir>/brain/<id>/content_inventory.md`.
3.  **Identify Duplicates/Errors**: Check if the source has duplicate links or incorrect descriptions and plan corrections in advance (documenting them in the implementation plan).

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
3.  **Determine Slug (MANDATORY CHECK)**:
    *   **Search `LINK_MAPPING.md` by Naver ID**: Before creating a new slug, you MUST search for the current Naver post's ID in `LINK_MAPPING.md`.
    *   **Reuse Existing Slug**: If the Naver ID is already present in the `## Quick Reference Table` or `## Pending Link References`, you MUST use the slug defined there (even if it's `pending`).
    *   **New Slug ONLY if Missing**: Only if the Naver ID is NOT found, create a new kebab-case slug (English keywords only, no years).
4.  **Register in `LINK_MAPPING.md` (MANDATORY)**:
    *   Add a new entry for the current Naver ID and Slug in the `## Quick Reference Table` of `LINK_MAPPING.md`.
    *   Set the status to `pending` immediately before starting generation to signal work in progress.
5.  **Category Mapping (Strict)**:
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
    *   **File Missing**: Use Placeholder + TODO (`href="#"`). **NEVER** use self-referential links or non-standard placeholders.
    *   **If Not Mapped**: Use the **Strict TODO Placeholder Format** with `href="#"`.
2.  **Link Prefix Rules**:
    *   **English (EN)**: Use `/posts/[slug]/` (**NO** `/en/` prefix).
    *   **Japanese (JA)**: Use `/ja/posts/[slug]/`.
    *   **Chinese (ZH)**: Use `/zh-cn/posts/[slug]/`.

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
2.  **Parity**: Maintain **1:1 structural parity**. Do not summarize detail-rich sections (timetables, menus).
3.  **Currency**: Standardize KRW/JPY to **USD** (e.g., 10k KRW ≈ $7.50).
4.  **Japanese**: Natural desu/masu tone. No "Japan's X" phrasing. Remove tax-free info for JA if it's a guide for domestic Japanese. Use original Japanese/Kanji names directly without parenthetical explanations or furigana/bracketed readings.
3.  **Chinese**: Engaging style with emojis. **NO** special quotes in front matter.
4.  **Shop Name Notation**: Refer to **[CONTENT_GUIDELINES.md](./resources/CONTENT_GUIDELINES.md#shop-name--terminology-notation-rules)** for strict rules (EN/ZH: `Name (Original)`, JA: `Original` only).
5.  **Klook Affiliate Links**: Convert all Klook links using the **Tripmate account (AID: 110453)** and localize language/currency for each version. Refer to **[CONTENT_GUIDELINES.md](./resources/CONTENT_GUIDELINES.md#klook-affiliate-link-conversion)** for the template.
6.  **Cultural Adaptation**: Follow the **[Cultural Adaptation & Writing Style](./resources/CONTENT_GUIDELINES.md#3-cultural-adaptation--writing-style)** master rules.

---

## Step 7: Verification Suite (MANDATORY)

Run these checks and document results:
1.  **Total Parity Check**:
    *   Images: `naver.md` count vs Hugo count (Must match 1:1).
    *   Captions: `naver.md` count vs Hugo count.
    *   Links: `naver.md` count vs Hugo count.
2.  **Structural Parity Check**: Compare EN, JA, and ZH side-by-side to ensure paragraph counts and heading structures are identical.
3.  **Markdown Leak Check (CRITICAL)**:
    *   Search for Markdown syntax inside the `blog-container` area.
    *   `grep -E '\*\*|\[.*\]\(.*\)|^- ' content/*/posts/[slug].md`
4.  **Footer Link Standard Check**: Ensure "👉" is inside the `<a>` tag and icons match EN.

---

## Common Errors and Fixes

### 1. Front Matter Image Field

**❌ WRONG**: Using `cover:` with nested fields
```yaml
cover:
  image: "/images/posts/slug-01.jpg"
  alt: "..."
  caption: "..."
```

**✅ CORRECT**: Use `featured_image:` (single line)
```yaml
featured_image: "/images/posts/slug-01.jpg"
```

### 2. Double Header Lines

**❌ WRONG**: Using double headers creates two horizontal lines
```markdown
## Yebisu Garden Place  
## Ebisu Brewery Tokyo Operating Hours
```

**✅ CORRECT**: Use single header only
```markdown
## Ebisu Brewery Tokyo Operating Hours
```

### 3. Image Group Classes

**❌ WRONG**: Generic `image-group` class
```html
<div class="image-group">
```

**✅ CORRECT**: Use column-specific class based on Naver source
- Check Naver HTML for `se-imageGroup-col-2`, `se-imageGroup-col-3`, or `se-imageGroup-col-4`
- Convert to `image-group-2`, `image-group-3`, or `image-group-4`

```html
<div class="image-group-2">  <!-- For 2-column layout -->
<div class="image-group-3">  <!-- For 3-column layout -->
<div class="image-group-4">  <!-- For 4-column layout -->
```

### 4. Editor's Note Format

**❌ WRONG**: Simple format without styling
```html
<div class="editor-note">
**Editor's Note**
This article was originally published...
</div>
```

**✅ CORRECT**: Use `editors-note` (plural) with proper styling
```html
<div class="editors-note">
  <p style="text-align: left; font-style: italic;"><strong>Editor's Note</strong></p>
  <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
    This article is based on the author's actual experiences and original content from <a href="https://blog.naver.com/tokyomate/[POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>. It has been translated and adapted to provide authentic travel information about Tokyo for global readers.
  </p>
</div>
```

### 5. HTML Escaping Issues

**Problem**: Backslashes (`\`) appearing before HTML tags causing literal text display

**Solution**: Ensure no escape characters in HTML. Use proper HTML tags without escaping:
```html
<div class="blog-container">  <!-- NOT: \<div class=\"blog-container\"\> -->
```

### 6. TODO Placeholder Link Format

**❌ WRONG**: Missing Naver source link in comment
```html
<p><strong>➡️</strong> <a href="#" style="color: #667eea; text-decoration: underline;"><!-- TODO: Update link when post is migrated --><strong>Post Title</strong></a></p>
```

**✅ CORRECT**: Always include Naver source link and Hugo expected path in comments
```html
<!-- TODO: Update link after migration 
     Naver: https://blog.naver.com/tokyomate/[POST_ID]
     Hugo: /posts/[expected-slug]/ -->
<p><strong>➡️</strong> <a href="#" style="color: #667eea; text-decoration: underline;"><strong>Post Title</strong></a></p>
```

### 7. Slug Mismatch with LINK_MAPPING.md

**❌ WRONG**: Creating a new slug without checking if one was already reserved for that Naver ID.
```markdown
# Analysis & Metadata
Slug: new-slug-name (Created from scratch)
```

**✅ CORRECT**: Always search `LINK_MAPPING.md` for the Naver ID first.
```markdown
# Analysis & Metadata
Naver ID: 223665548720
Found in LINK_MAPPING.md: yebisu-brewery-museum-guide
Action: Use the existing slug 'yebisu-brewery-museum-guide'
```

### 8. Forgetting to Register In LINK_MAPPING.md

**❌ WRONG**: Starting work without adding a `pending` entry, leading to possible duplicate work or slug conflicts.

**✅ CORRECT**: Add the Naver ID and Slug to `LINK_MAPPING.md` with `pending` status as the very first action after metadata analysis.

---

## Step 8: Finalization & PR

1.  **Update `LINK_MAPPING.md`**: Update the status from `pending` to `✅` in the `## Quick Reference Table`. This is a critical final step for tracking.
2.  **Commit**: `git add .` and `git commit`.

---

## References & Resources

The following files are included in this skill for reference:

*   **Guidelines**:
    *   [MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md): Complete workflow rules.
    *   [CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md): Formatting & SEO rules.
*   **Examples**:
    *   [Good Migration Example](examples/good_migration_example.md): A full reference implementation (`tokyo-christmas-markets-guide-2025`).
