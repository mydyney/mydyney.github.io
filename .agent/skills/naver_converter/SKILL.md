---
name: naver_converter
description: Guide and automate the migration of Naver blog posts to Hugo, ensuring strict adherence to formatting, SEO, and multilingual guidelines.
---

# Naver Converter Skill

This skill guides you through the process of migrating a Naver blog post to the Hugo static site structure (EN/JA/ZH-CN). 

*   **[MIGRATION_GUIDE.md](resources/MIGRATION_GUIDE.md)**: **Workflow Document** (Process, scripts, verification checklists).
*   **[CONTENT_GUIDELINES.md](resources/CONTENT_GUIDELINES.md)**: **Master Reference** (Formatting, HTML snippets, SEO, translation rules).

**CRITICAL PREREQUISITE**: The user will always prepare the Naver blog HTML in `naver.md` before starting. **ALWAYS use naver.md directly** - no verification or fetching needed.

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

## Step 0: Pre-Analysis Phase (MANDATORY - CRITICAL)

**Goal**: Complete structural analysis BEFORE starting any content generation to prevent errors.

### 0.1 Image Group Structure Analysis

**CRITICAL**: Extract ALL image group information from `naver.md` FIRST.

1.  **Count Total Images**:
    ```bash
    grep -o "se-image-resource" naver.md | wc -l
    ```

2.  **Extract Image Group Locations**:
    ```bash
    grep -n "se-imageGroup-col-" naver.md
    ```
    - Note the line numbers and group types (col-2, col-3, col-4)

3.  **Extract Exact Image Ratios**:
    ```bash
    grep -A 3 "se-imageGroup-col-2" naver.md | \
    grep "style=\"width" | \
    sed 's/.*width://g' | \
    sed 's/%.*//g' | \
    awk 'NR%2{printf "%s / ",$0;next;}1' | \
    nl -v 1 -s ". "
    ```
    - **RECORD EXACT PERCENTAGES** - DO NOT ESTIMATE

4.  **Create Image Mapping Table**:
    | Image # | Type | Ratio | Caption | Section |
    |---------|------|-------|---------|----------|
    | 1 | Single | - | "..." | Intro |
    | 2-3 | Group | 36/64 | "..." | Park |
    | ... | ... | ... | ... | ... |

### 0.2 Section Structure Analysis

1.  **Extract All Section Titles**:
    ```bash
    grep -o "se-fs- se-ff-nanumdasisijaghae" naver.md -A 1
    ```

2.  **Count Content Blocks per Section**:
    - Paragraphs
    - Lists (bullet/numbered)
    - Images
    - Links

3.  **Verify NO Arbitrary Additions**:
    - ❌ DO NOT add section headers not in original
    - ❌ DO NOT add content not in original
    - ❌ DO NOT reorganize structure
    - ✅ ONLY translate and format existing content

### 0.3 Create Pre-Analysis Artifact

**Write to**: `<appDataDir>/brain/<id>/pre_analysis.md`

```markdown
# Pre-Analysis: [Post Title]

## Image Inventory
- Total Images: XX
- Image Groups: XX
- Group Details:
  1. Images X-Y: Ratio A/B - "Caption"
  2. Images X-Y: Ratio A/B - "Caption"

## Section Structure
1. Section Title
   - Paragraphs: X
   - Images: X
   - Lists: X

## Verification Checklist
- [ ] All image ratios extracted
- [ ] All sections mapped
- [ ] No arbitrary additions planned
```

### 0.4 User Confirmation

**BEFORE starting content generation**:
1. Present the pre-analysis artifact to user
2. Confirm structure understanding
3. Get approval to proceed

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

**CRITICAL FRONT MATTER**:
*   **featured_image**: Must include `/images/posts/[slug]-01.jpg`.

**CRITICAL FORMATTING RULES**:
*   **STRICT HTML Only in Container**: Wrap content in `<div class="blog-container">`. Inside this, use **HTML tags** (`<strong>`, `<ul>`, `<li>`, `<p>`, `<a>`), **NEVER** Markdown (`**`, `-`, `[text](url)`).
*   **Google Maps Standard**:
    *   Format: `📍 <a href="..." target="_blank" rel="noopener" style="color: #667eea; text-decoration: underline;"><strong>View on Google Maps</strong></a>`
    *   JA: `<strong>Googleマップで見る</strong>`, ZH: `<strong>在 Google 地图上查看</strong>`.
*   **Headings**: Use Markdown (`##`, `###`) for headings.
*   **Images** (CRITICAL - STRICT RULES):
    *   **1:1 Matching**: Every image in Naver HTML must be present - NO additions, NO deletions.
    *   **High-Res Quality**: Append `?type=w966` to the URL.
    *   **Image Groups** (MANDATORY PROCESS):
        1. **Use Inline Flex Styles** (NOT CSS classes):
           ```html
           <div style="display: flex; gap: 10px; margin: 20px 0;">
             <figure style="margin: 0; flex: 0.XXX;">
               <img src="..." style="width: 100%; height: auto; display: block;">
             </figure>
             <figure style="margin: 0; flex: 0.YYY;">
               <img src="..." style="width: 100%; height: auto; display: block;">
             </figure>
           </div>
           <figcaption style="font-size: 0.85em; text-align: center; margin-top: -10px;">Caption</figcaption>
           ```
        2. **Extract EXACT ratios** from naver.md `style="width:XX%"` - convert to decimal (e.g., 51.77% → 0.518)
        3. **Verify ratio sum = 1.0** for each group
        4. **For 4-image groups (2x2)**: Create TWO separate flex divs (one per row)
    *   **Captions**: Every caption in `naver.md` MUST be translated and added.
    *   **Image Numbering**: 
        - ❌ NEVER renumber existing images
        - ✅ Only add new images with next available number
        - ✅ Keep original numbering even if images are deleted

---

## Step 4: Image Download

**Action**: Extract high-res image URLs (`?type=w966`) and download them immediately.
```bash
python3 download_naver_images.py "[slug]"
```

---

## Step 5: User Verification

1.  **User Verification Only**: The agent does not perform visual or server-based verification. The user is responsible for checking the output.
2.  **Self-Correction**: Perform a `grep` search for Markdown syntax inside the `.md` file to catch any `**` or `[` characters that shouldn't be there before proceeding to other languages.
    ```bash
    grep -E '\*\*|\[.*\]\(.*\)' content/en/posts/[slug].md
    ```
3.  **WAIT FOR USER**: **CRITICAL**: You MUST NOT proceed to Step 6 until the user explicitly provides a "next" command. After completing Step 5, inform the user you are waiting for their review.

---

## Step 6: Multilingual Expansion

**Goal**: Create Japanese (`ja`) and Chinese (`zh-cn`) versions.

**PREREQUISITE**: **Only proceed if the user has said "next"** after verifying the English version in Step 5.


**CRITICAL: HTML Formatting Rules Apply to ALL Languages**

> [!IMPORTANT]
> The HTML formatting rules from Step 3 apply **EQUALLY** to Japanese and Chinese versions:
> - ✅ **USE**: `<strong>`, `<ul>`, `<li>`, `<p>`, `<a>` inside `blog-container`
> - ❌ **NEVER**: `**text**`, `- item`, `[link](url)` inside `blog-container`
> - 📋 **Process**: Translate text content ONLY, keep ALL HTML tags intact
> - 🔍 **Verify**: Run Markdown leak check after each language (see Step 7.4)

**Translation Guidelines**:

1.  **Consistency**: Use the **SAME** `translationKey` and images as English.
2.  **Parity**: Maintain **1:1 structural parity**. Do not summarize detail-rich sections (timetables, menus).
3.  **Currency**: Standardize KRW/JPY to **USD** (e.g., 10k KRW ≈ $7.50).
4.  **Japanese**: Natural desu/masu tone. No "Japan's X" phrasing. Remove tax-free info for JA if it's a guide for domestic Japanese. Use original Japanese/Kanji names directly without parenthetical explanations or furigana/bracketed readings.
5.  **Chinese**: Engaging style with emojis. **NO** special quotes in front matter.
6.  **Shop Name Notation**: Refer to **[CONTENT_GUIDELINES.md](./resources/CONTENT_GUIDELINES.md#shop-name--terminology-notation-rules)** for strict rules (EN/ZH: `Name (Original)`, JA: `Original` only).
7.  **Klook Affiliate Links**: Convert all Klook links using the **Tripmate account (AID: 110453)** and localize language/currency for each version. Refer to **[CONTENT_GUIDELINES.md](./resources/CONTENT_GUIDELINES.md#klook-affiliate-link-conversion)** for the template.
8.  **Cultural Adaptation**: Follow the **[Cultural Adaptation & Writing Style](./resources/CONTENT_GUIDELINES.md#3-cultural-adaptation--writing-style)** master rules.

**Translation Example** (Correct vs Incorrect):

```html
<!-- ✅ CORRECT: HTML preserved -->
English: <strong>Must-Visit Restaurant</strong>
Japanese: <strong>必訪レストラン</strong>
Chinese: <strong>必访餐厅</strong>

<!-- ❌ INCORRECT: Converted to Markdown -->
Japanese: **必訪レストラン**  ← NEVER DO THIS
Chinese: **必访餐厅**  ← NEVER DO THIS
```

---

## Step 7: Verification Suite (MANDATORY)

### 7.1 Automated Verification Scripts

**Create and run these verification scripts**:

1.  **Image Count Verification**:
    ```bash
    #!/bin/bash
    NAVER_COUNT=$(grep -o "se-image-resource" naver.md | wc -l | tr -d ' ')
    HUGO_COUNT=$(grep -o '<img' content/en/posts/[slug].md | wc -l | tr -d ' ')
    echo "Naver: $NAVER_COUNT | Hugo: $HUGO_COUNT"
    [ $NAVER_COUNT -eq $HUGO_COUNT ] && echo "✅ PASS" || echo "❌ FAIL"
    ```

2.  **Image Group Count Verification**:
    ```bash
    #!/bin/bash
    NAVER_GROUPS=$(grep -c "se-imageGroup-col-2" naver.md)
    HUGO_GROUPS=$(grep -c "display: flex" content/en/posts/[slug].md)
    echo "Naver: $NAVER_GROUPS | Hugo: $HUGO_GROUPS"
    [ $NAVER_GROUPS -eq $HUGO_GROUPS ] && echo "✅ PASS" || echo "❌ FAIL"
    ```

3.  **Image Ratio Verification**:
    ```bash
    #!/bin/bash
    # Extract all flex ratios and verify they sum to ~1.0 per group
    grep "flex: 0\." content/en/posts/[slug].md | \
    awk -F'flex: 0\\.' '{print $2}' | \
    awk -F';' '{print $1}' | \
    awk '{sum+=$1; if(NR%2==0){print sum/1000; sum=0}}'
    # Each output should be ~1.0 (e.g., 0.998-1.002)
    ```

4.  **Markdown Leak Verification** (CRITICAL):
    ```bash
    #!/bin/bash
    # Check for Markdown syntax inside blog-container (should be 0)
    echo "=== Markdown Leak Check ==="
    for lang in en ja zh-cn; do
      COUNT=$(grep -c '\*\*' content/$lang/posts/[slug].md 2>/dev/null || echo 0)
      if [ "$COUNT" -gt 0 ]; then
        echo "❌ $lang: Found $COUNT Markdown bold (**)"
        echo "   Fix: sed -i '' 's/\*\*\([^*]*\)\*\*/\<strong\>\1\<\/strong\>/g' content/$lang/posts/[slug].md"
      else
        echo "✅ $lang: No Markdown leaks"
      fi
    done
    ```

5.  **Section Count Verification**:
    sed 's/.*flex: //g' | sed 's/;.*//g' | \
    awk 'NR%2{sum=$1;next}{sum+=$1; print sum}' | \
    awk '{if($1<0.99||$1>1.01)print "❌ FAIL: "$1; else print "✅ PASS: "$1}'
    ```

### 7.2 Manual Verification Checklist

Run these checks and document results:
1.  **Total Parity Check**:
    *   Images: `naver.md` count vs Hugo count (Must match 1:1).
    *   Captions: `naver.md` count vs Hugo count.
    *   Links: `naver.md` count vs Hugo count.
    *   Image Groups: `naver.md` count vs Hugo count.
2.  **Image Group Ratio Check**:
    *   Compare each group's ratios with naver.md source
    *   Verify all ratios sum to 1.0 (±0.01 tolerance)
3.  **Structural Parity Check**: Compare EN, JA, and ZH side-by-side to ensure paragraph counts and heading structures are identical.
4.  **Markdown Leak Check (CRITICAL)**:
    *   Search for Markdown syntax inside the `blog-container` area.
    *   `grep -E '\*\*|\[.*\]\(.*\)|^- ' content/*/posts/[slug].md`
5.  **Footer Link Standard Check**: Ensure "👉" is inside the `<a>` tag and icons match EN.
6.  **Content Fidelity Check**:
    *   ❌ NO section headers added that don't exist in naver.md
    *   ❌ NO content reorganization
    *   ✅ ALL sections from naver.md present

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

### 3. Image Group Classes (DEPRECATED)

**❌ WRONG**: Using CSS classes
```html
<div class="image-group-2">
```

**✅ CORRECT**: Use inline flex styles
```html
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.518;">
    <img src="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.482;">
    <img src="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.85em; text-align: center; margin-top: -10px;">Caption</figcaption>
```

### 4. Image Group Ratio Errors (NEW - CRITICAL)

**❌ WRONG**: Estimating ratios visually
```html
<figure style="margin: 0; flex: 0.5;">  <!-- Guessed 50/50 -->
<figure style="margin: 0; flex: 0.5;">
```

**✅ CORRECT**: Extract exact ratios from naver.md
```bash
# Extract from naver.md: width:51.76899063475546%
# Convert to decimal: 0.518
<figure style="margin: 0; flex: 0.518;">
<figure style="margin: 0; flex: 0.482;">
```

### 5. Missing Image Groups (NEW - CRITICAL)

**❌ WRONG**: Skipping image groups from naver.md
- Missing standalone images between sections
- Deleting image groups that seem duplicate

**✅ CORRECT**: Include ALL images from naver.md
- Use pre-analysis to map every single image
- Verify image count matches: `naver.md` vs `Hugo`
- Never skip images even if they seem redundant

### 6. Arbitrary Section Additions (NEW - CRITICAL)

**❌ WRONG**: Adding section headers not in original
```markdown
## Traditional Izakaya & Specialty Coffee  <!-- NOT in naver.md -->
```

**✅ CORRECT**: Only use sections from naver.md
- Extract all section titles from naver.md FIRST
- Never add headers for "better organization"
- Translate existing structure exactly

### 7. Image Numbering Errors (NEW - CRITICAL)

**❌ WRONG**: Renumbering images after additions/deletions
```
Original: 1-21
After adding image 2: Renumber 13-21 → 13-19  <!-- WRONG -->
```

**✅ CORRECT**: Keep original numbers, only add new
```
Original: 1, 3-21 (missing 2)
After adding image 2: 1-21 (all present)  <!-- Keep original numbers -->
```

### 8. Editor's Note Format

**❌ WRONG**: Simple format without styling
```markdown
> Editor's Note: This is a note
```

**✅ CORRECT**: Use styled blockquote
```html
<blockquote style="background: #f9f9f9; border-left: 4px solid #667eea; padding: 15px 20px; margin: 20px 0;">
<p style="margin: 0;"><strong>✏️ Editor's Note:</strong> Content here</p>
</blockquote>
```

---

## Critical Reminders

1. **ALWAYS run pre-analysis BEFORE content generation**
2. **NEVER estimate image ratios - extract exact values**
3. **NEVER add content not in naver.md**
4. **NEVER renumber existing images**
5. **ALWAYS verify with automated scripts**
6. **ALWAYS maintain 1:1 parity with source**

---

## Quick Reference: Verification Commands

```bash
# Image count
grep -o "se-image-resource" naver.md | wc -l
grep -o '<img' content/en/posts/[slug].md | wc -l

# Image group count
grep -c "se-imageGroup-col-2" naver.md
grep -c "display: flex" content/en/posts/[slug].md

# Extract image ratios
grep -A 3 "se-imageGroup-col-2" naver.md | \
grep "style=\"width" | \
sed 's/.*width://g' | sed 's/%.*//g'
```

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
