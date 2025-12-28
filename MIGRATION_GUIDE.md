# MIGRATION_GUIDE.md - Naver Blog to Hugo Migration Guide

> **Last Updated:** 2025-12-26
> **Project:** Tokyo Mate (Trip Mate News Blog)
> **Purpose:** Step-by-step guide for migrating Naver blog posts to Hugo

This document provides comprehensive instructions for migrating blog posts from Naver Blog to Hugo static site.

---

## Table of Contents

1. [Migration Overview](#migration-overview)
2. [Step-by-Step Migration Workflow](#step-by-step-migration-workflow)
3. [Content Creation Guidelines](#content-creation-guidelines)
4. [Link Mapping System](#link-mapping-system)
5. [Migration Scripts](#migration-scripts)
6. [Pull Request Process](#pull-request-process)

**⚠️ IMPORTANT:** This guide covers the migration workflow and content translation rules. You MUST also review **[CONTENT_GUIDELINES.md](./CONTENT_GUIDELINES.md)** for blog formatting, SEO optimization, tags/categories, and image rules before creating any posts.

---

## Migration Overview

### Current Migration Status

**Source:** Naver Blog → Hugo Static Site

**Progress:**
- ✅ Site infrastructure set up
- ✅ Multilingual architecture configured
- ✅ Custom migration script created
- ✅ Sample posts migrated (2-3 restaurant reviews)
- 🔄 Ongoing content migration

**⚠️ IMPORTANT: Naver blocks automated image downloads (403 Forbidden errors)**

Due to Naver's security restrictions, images must be downloaded manually using the provided script.

---

## Step-by-Step Migration Workflow

### Step 1: User Provides Naver Blog URL

```
User: "https://blog.naver.com/tokyomate/[POST_ID]"
```

**⚠️ CRITICAL AGENT RULE:**
- **NEVER** try to fetch/scrape the Naver blog URL using browser tools or `read_url_content`.
- **ALWAYS** wait for the user to provide the content in `naver.md`.
- The user will manually copy the HTML to `naver.md` because of Naver's anti-bot protections.

### Step 2: User Updates naver.md with Blog Content

```
Claude: "Please update naver.md with the blog HTML content."
User: (Copies HTML from Naver blog and saves to naver.md)
User: "완료했습니다" or "Done"
```

**Instructions for User:**
- Open the Naver blog post in browser
- Copy the HTML content of the blog post
- Save it to `naver.md` in the project root directory
- Confirm completion

### Step 3: Claude Analyzes and Creates Blog Posts

**📚 REQUIRED READING BEFORE STARTING:**

Before creating any blog posts, you MUST review these documents in order:

1. **[MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md)** (this file) - Content creation workflow and translation rules
2. **[CONTENT_GUIDELINES.md](./CONTENT_GUIDELINES.md)** - Blog formatting, SEO optimization, tags/categories, image rules

**⚠️ CRITICAL: Both documents contain essential rules. Missing either will result in incomplete or incorrectly formatted posts!**

**Key areas in CONTENT_GUIDELINES.md:**
- Front matter structure and required fields
- Language-specific tags and categories (EN/JA/ZH-CN must match content language)
- SEO optimization (title/description length limits per language)
- Image naming convention and 1:1 matching rule
- Editor's Note section (mandatory)
- Chinese YAML syntax rules (no special quotation marks)
- Blog post format and structure

---

**⚠️ IMPORTANT: Incremental Creation Workflow**

To ensure quality and allow for early feedback, follow this incremental approach:

**Step 3.1: Analysis Phase**
- Extract publish date from Naver HTML
- **Determine Hugo slug for this post:**
  - Create SEO-friendly kebab-case slug
  - Rules: lowercase, hyphens, keyword-rich, under 60 chars
  - Example: `roppongi-christmas-illumination-2025`
  - **Immediately record in LINK_MAPPING.md** (Naver ID → Hugo slug mapping)
- Count images and verify order
- Load LINK_MAPPING.md for internal link conversion
- Identify all Naver links in content

**Step 3.1.5: Handling Long Naver Posts (Section-by-Section Approach)**

When encountering exceptionally long Naver posts (1,000+ lines of HTML), use a section-by-section creation approach:

**When to Use:**
- Naver HTML exceeds 1,000 lines
- Post contains 10+ tables or extensive lists
- Content is highly structured (e.g., comprehensive guides, store listings)
- Risk of exceeding response length limits

**Workflow:**
1. **Analyze and Plan:**
   - View entire `naver.md` to understand structure
   - Identify logical section breaks (headings, topics)
   - Create mental outline of 5-7 major sections

2. **Section-by-Section Creation:**
   - Generate English version section by section
   - Each section should be complete with:
     - Proper markdown formatting
     - Converted tables
     - Internal link placeholders
     - Images with captions
   - **DO NOT** request approval after each section
   - Continue until entire post is complete

3. **Integration:**
   - Combine all sections into single cohesive file
   - Ensure consistent formatting throughout
   - Verify all sections flow naturally
   - Check that front matter is complete

4. **User Review:**
   - Present complete English version for review
   - Wait for user "OK" before proceeding to JA/ZH-CN

**Example Structure:**
```markdown
## Section 1: Introduction + Warning
(Generate content)

## Section 2: Hatsuuri Strategy  
(Generate content)

## Section 3: Places Open on Jan 1
(Generate content)

## Section 4: Observatory Hours
(Generate content with tables)

## Section 5: Outlets
(Generate content)

## Section 6: Transportation
(Generate content)

## Section 7: Summary
(Generate content)
```

**Benefits:**
- Maintains focus on each section
- Reduces risk of incomplete content
- Easier to verify accuracy
- Better handling of complex tables
- Avoids response truncation

**Step 3.2: Create English Version FIRST**
- Create `content/en/posts/[slug].md` (using slug from Step 3.1)
- Apply all content creation guidelines (see below)
- Process all Naver links using Link Conversion Workflow (see "Link Mapping System" section)
  - Links to this new post will now work in other posts
  - Links to unmigrated posts will use TODO placeholders
- **STOP and request user review**
- Wait for user "OK" before proceeding

**Step 3.3: Create Japanese & Chinese Versions (After EN Approval)**
- Create `content/ja/posts/[slug].md`
- Create `content/zh-cn/posts/[slug].md`
- Apply same guidelines with language-specific adaptations

**Step 3.4: Finalize LINK_MAPPING.md**
- Verify new entry in Quick Reference Table (added in Step 3.1)
- Verify slug in `declare -A MAPPINGS` array (added in Step 3.1)
- Update Pending References section
- Note: Placeholder links in existing posts will be updated in future migrations

**Analysis:**

- **Extract publish date from Naver HTML:**
  ```bash
  # Find the publish date in the HTML
  grep -o 'se_publishDate[^>]*>[^<]*' naver.md
  # Format: "YYYY. MM. DD. HH:MM" (e.g., "2025. 12. 10. 11:49")
  # Convert to Hugo format: YYYY-MM-DDT00:00:00+09:00
  ```
  - **Location in HTML:** `<span class="se_publishDate pcol2">YYYY. MM. DD. HH:MM</span>`
  - **Use this date** for the `date:` field in frontmatter for all three language versions
  - **Critical:** Using correct publish date ensures posts appear in proper chronological order on homepage

- Count images and verify order
- Load LINK_MAPPING.md for internal link conversion
- Identify all Naver links in content

**Content Creation Requirements:**

**LINK_MAPPING.md Updates:**
- Add new entry to Quick Reference Table
- Add slug to `declare -A MAPPINGS` array
- Check and update Pending References
- Update placeholder links in existing posts

### Step 4: Claude Downloads Images

```bash
python3 download_naver_images.py naver.md "[slug]"
# Downloads to: static/images/posts/[slug]-01.jpg, [slug]-02.jpg, ...
# Auto-converts to JPG format
```

### Step 5: Claude Provides Local Preview Links

```
EN: http://localhost:1313/posts/[slug]/
JA: http://localhost:1313/ja/posts/[slug]/
ZH-CN: http://localhost:1313/zh-cn/posts/[slug]/
```

### Step 5.5: Claude Verifies Content Completeness

**MANDATORY VERIFICATION CHECKLIST:**

Before providing preview links to user, verify the following counts match between original Naver HTML and created Hugo posts:

1. **Image Count Verification:**
   ```bash
   # Count images in original Naver HTML
   grep -o '<img' naver.md | wc -l

   # Count images in Hugo posts (should match for each language)
   grep -o '<img' content/en/posts/[slug].md | wc -l
   grep -o '<img' content/ja/posts/[slug].md | wc -l
   grep -o '<img' content/zh-cn/posts/[slug].md | wc -l
   ```

2. **Figcaption Count Verification:**
   ```bash
   # Count captions in original (look for se-caption or similar)
   # Count figcaptions in Hugo posts (should match for each language)
   grep -o '<figcaption' content/en/posts/[slug].md | wc -l
   grep -o '<figcaption' content/ja/posts/[slug].md | wc -l
   grep -o '<figcaption' content/zh-cn/posts/[slug].md | wc -l
   ```

3. **Naver Link Count Verification:**
   ```bash
   # Count Naver blog links in original
   grep -o 'blog.naver.com/tokyomate' naver.md | wc -l

   # Count converted links + placeholders in Hugo posts (should match for each language)
   # Count: internal links (/posts/) + TODO placeholders
   grep -E '(/posts/|TODO: Update link)' content/en/posts/[slug].md | wc -l
   grep -E '(/posts/|TODO: Update link)' content/ja/posts/[slug].md | wc -l
   grep -E '(/posts/|TODO: Update link)' content/zh-cn/posts/[slug].md | wc -l
   ```

**Verification Report Format:**
```
✅ Image Count: Original [X] = EN [X] = JA [X] = ZH-CN [X]
✅ Caption Count: Original [X] = EN [X] = JA [X] = ZH-CN [X]
✅ Link Count: Original [X] = EN [X] = JA [X] = ZH-CN [X]
```

**If counts don't match:**
- Review original HTML to find missing images/captions/links
- Update all three language versions before providing preview links
- Re-verify counts until all match

### Step 6: User Reviews and Confirms

```
User: "OK" or provides feedback
```

### Step 7: Claude Deploys to GitHub

```bash
git add .
git commit -m "Add [slug] blog post (EN/JA/ZH-CN)

New Content:
- Created comprehensive [topic] guide
- Added [N] images
- All three language versions (EN/JA/ZH-CN)

Link Updates:
- Updated LINK_MAPPING.md
- Activated links in [N] existing posts

Naver ID: [POST_ID]
Slug: [slug]"
git push
```

---

## Content Creation Guidelines

### Critical Rules for Content Translation

#### ⚠️ CRITICAL: COMPLETE CONTENT TRANSLATION

* **Translate ALL text from original blog without omission:**
  - Every paragraph, sentence, and description must be translated
  - Do NOT summarize or skip any content
  - Do NOT add content not in the original
  - Maintain the same level of detail as the original

* **NEVER add content not in original blog:**
  - Do NOT add headings that don't exist in original
  - Do NOT add descriptions or explanations not in original
  - Do NOT add formatting not in original
  - Only translate what exists in the source HTML

* **Preserve ALL formatting from original HTML:**
  - Bold text (`<b>`, `<strong>`) → **Keep as HTML** (`<b>text</b>` or `<strong>text</strong>`)
  - Lists and bullet points → **Keep as HTML** (`<ul>`, `<li>` tags)
  - Section headings and subheadings → Markdown headings (`##`, `###`)
  - Quotation blocks → Markdown blockquotes (`>`)

  **⚠️ Why HTML for Bold & Lists:**
  - Markdown syntax (`**bold**`, `*`, `-` for lists) does NOT render inside `<div class="blog-container">`
  - Markdown symbols appear literally (e.g., `**text**` shows as `**text**` instead of bold)
  - **Solution:** Always use HTML tags (`<b>`, `<strong>`, `<ul>`, `<li>`) for these elements
  - Headings (`##`) and blockquotes (`>`) still work with Markdown

* **Match original structure exactly:**
  - Same number of sections
  - Same heading hierarchy
  - Same text emphasis patterns

* **Never add extra formatting not in original**

#### ⚠️ CRITICAL: IMAGE POSITIONING & CAPTIONS

* **Verify ALL images from original blog:**
  - Content MUST match image positions EXACTLY
  - Same image at same position = same content context
  - Never add content not in original blog

* **Image grouping is MANDATORY:**
  - Check for grouped images: Identify if images appear side-by-side in original
  - Preserve grouping: Use appropriate `image-group-X` class
  - Group image positions are MANDATORY - do NOT place grouped images separately

* **Preserve figcaptions - MANDATORY:**
  - **Extract ALL image captions from original HTML:**
    * Look for `<div class="se-module se-module-text se-caption">` in Naver HTML
    * Caption text is inside `<span class="se-fs- se-ff-">` tags
    * EVERY image with a caption MUST have figcaption in Hugo markdown

  - **REQUIRED: Use HTML for ALL images, not Markdown:**
    * Every single image must be wrapped in a `<figure>` tag.
    * Image groups MUST use specific `image-group-X` containers.

  - **Use proper figcaption format with styling:**
    ```html
    <figure>
      <img src="/images/posts/example.jpg" alt="Description">
      <figcaption style="font-size: 0.85em; text-align: center;">Caption text here</figcaption>
    </figure>
    ```
    * **Styling rules:**
      - Font size: `0.85em` (smaller than body text)
      - Text alignment: `center`
      - These styles are MANDATORY for all figcaptions

  - **Translation rules:**
    * Translate caption to target language (EN/JA/ZH-CN)
    * Keep same tone and style as original
    * **Preserve source links if present in original:**
      - If original caption has a link (e.g., "출처" link), include it in figcaption
      - Format: `Caption text (<a href="URL" target="_blank">Source</a>)`
      - Translate link text: "출처" → "Source" (EN), "出典" (JA), "来源" (ZH-CN)
    * Do NOT add captions if original doesn't have them
    * Do NOT skip captions that exist in original

#### ⚠️ CRITICAL: HTML STRUCTURE ANALYSIS

* **Completely analyze original HTML to identify and preserve exact positions:**
  - **Tables:** Count all tables and note their exact positions in content flow
  - **Links:** Identify all internal/external links and their positions
  - **Image Groups:** Detect grouped images (side-by-side) and their positions

* **Position Mapping:**
  - Map each element's position relative to surrounding text/headings
  - Preserve the exact order: text → table → text → image group → text
  - NEVER reorder or relocate these elements from original positions

* **Strict Linear Order (MANDATORY):**
  - **FOLLOW** the HTML element order exactly (e.g. Text -> Image -> Text).
  - **DO NOT** reorder elements to group "sections" together if the HTML has them interleaved.
  - **Example:** If HTML has `[Text A] -> [Image B] -> [Text C]`, you **MUST** output `[Text A] -> [Image B] -> [Text C]`.
  - **NEVER** move `[Text C]` to be before `[Image B]` just because it belongs to the same topic as `[Text A]`.

* **Inline Internal Links (MANDATORY):**
  - Treat blog post links (e.g., "See also [Title]") appearing in the middle of the text as **CONTENT**, not footer material.
  - **NEVER** move these links to a "Related Posts" section at the bottom.
  - **MUST** be placed exactly where they appear in the source HTML (e.g., between two paragraphs).
  - **Use left alignment** for Naver internal link sections (not centered).

* **Link Preservation (MANDATORY):**
  - **Duplicate URLs:** If a URL appears multiple times in different contexts (e.g., once as an image source, once as a "Check Availability" text link), you **MUST PRESERVE BOTH**. Never de-duplicate based on URL.
  - **Actionable Links:** Links that imply an action (e.g., "Reserve here", "Check availability", "Open in Google Maps") **MUST** be preserved as distinct, visible elements (e.g., Callout blocks or bold text). **NEVER** summarize them away or merge them into a general description.

* **Verification:**
  - **Step 0: Content Inventory (CRITICAL):** Before writing, list ALL headers/sections from the original HTML (e.g., 1F, 2F, 3F, B1) to ensure NOTHING is missed.
  - Cross-reference original HTML structure with created Hugo markdown
  - Ensure tables appear at same position as original
  - Ensure image groups maintain original grouping and position
  - Ensure links appear in same context as original

* **Strict Source Adherence (CRITICAL):**
  - **NO NEW INFORMATION:** Do NOT create, guess, or hallucinate listing details not present in the source HTML.
  - **Translate ONLY what exists:** If the source says "X is popular", do not add "and stylish". Stick to the source meaning.
  - **Exact List Match:** If the source lists 3 brands, do not list 5. If it lists 5, do not list 3. Match the item count exactly.

#### ⚠️ CRITICAL: TABLE FORMATTING

* **Use HTML tables, NOT markdown tables:**
  - Extract table structure from original Naver HTML
  - Preserve header row styling (background-color: #f7f7f7)
  - Center-align all table cells
  - Use clean, simplified HTML (remove unnecessary Naver classes)

* **Table format:**
  ```html
  <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
    <thead>
      <tr style="background-color: #f7f7f7;">
        <th style="padding: 12px; text-align: center; border: 1px solid #ddd;">Header 1</th>
        <th style="padding: 12px; text-align: center; border: 1px solid #ddd;">Header 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">Data 1</td>
        <td style="padding: 12px; text-align: center; border: 1px solid #ddd;">Data 2</td>
      </tr>
    </tbody>
  </table>
  ```

* **Styling rules:**
  - Header background: `#f7f7f7`
  - Cell padding: `12px`
  - Text alignment: `center`
  - Border: `1px solid #ddd`
  - Table width: `100%`
  - Margin: `20px 0`

#### ⚠️ CRITICAL: CULTURAL ADAPTATION & WRITING STYLE

**1. Translation System Prompts (USE THESE):**

* **English (EN):**
  > "You are a friendly travel blogger specializing in Tokyo travel for Western tourists. Please translate/transcreate the following Korean text into English. Guidelines:
  > Tone: Conversational, enthusiastic, and helpful. Like a local friend giving advice.
  > Keywords to weave in: Hidden gems, Authentic vibe, Local experience.
  > Goal: Highlight the unique experience from a foreigner's perspective but ensure the practical info is accurate."

* **Japanese (JA):**
  > "あなたは東京の魅力を発信する韓国人ブロガーです。以下の韓国語の文章を、日本の読者に向けて自然な日本語に翻訳・リライトしてください。 ガイドライン:
  > トーン: 丁寧語（です・ます調）。親しみやすく、かつ謙虚な姿勢で。
  > ポイント: 「韓国人の視点」からの新鮮な発見や、「コスパ」「穴場」「映え」などのキーワードを自然に盛り込んでください。"

* **Chinese (ZH-CN):**
  > "你是一位精通东京旅游的小红书(Xiaohongshu)博主。请把下面的韩文文章改写成中文（简体）。 指南:
  > 语气: 热情、直接、充满干货（Useful info）。使用一些流行的网络用语。
  > 关键词: 必须包含 '打卡', '避雷', '宝藏店铺' 等吸引人的词汇。
  > 排版: 适当添加 emoji (📍, ✨, 📷) 让文章读起来更有趣。"

**2. Specific Adaptation Rules:**

* **English (EN)**:
  - Use engaging, traveler-friendly expressions (American English)
  - Focus on what international visitors want to know

* **Japanese (JA)**:
  - **NEVER use "日本の" prefix** - readers are Japanese (e.g., "日本のコーヒー" → "コーヒー")
  - Use specific location names instead of "Japan"
  - **DELETE all tax-free/免税 sections** - only relevant to foreign tourists

* **Chinese (ZH-CN)**:
  - Use popular travel terminology: "攻略", "性价比", "必打卡"
  - Focus on practical information tourists need

#### ⚠️ CRITICAL: NO AI WRITING TRACES

* **NEVER leave any signs that content was AI-generated**
* Avoid overly formal or robotic language patterns
* No generic AI phrases like "In conclusion", "It's worth noting", "comprehensive guide"
* Use natural, human-like variations in sentence structure
* Include personal touches and authentic observations
* Write as a real travel blogger would, not as an AI assistant

---

## Link Mapping System

### Link Conversion Workflow (Step-by-Step)

**⚠️ MANDATORY: Follow this exact workflow for EVERY Naver link**

**📝 Note:** When creating a new post, the slug is determined in Step 3.1 and immediately recorded in LINK_MAPPING.md. This means other posts can now reference this new post using the slug.

For each Naver blog link found in the original HTML:

**Step 1: Extract Naver Post ID**
```
Example URL: https://blog.naver.com/tokyomate/224065668379
Extracted ID: 224065668379
```

**Step 2: Check LINK_MAPPING.md**
```bash
# Search for the ID in LINK_MAPPING.md
grep "224065668379" LINK_MAPPING.md
```

- **If found:** Extract Hugo slug from the mapping
  ```
  Example result: 224065668379 | roppongi-christmas-illumination-2025
  Hugo slug: roppongi-christmas-illumination-2025
  ```
- **If NOT found:** Skip to Step 4 (use placeholder)

**Step 3: Verify File Existence (MANDATORY)**

**⚠️ CRITICAL: Even if mapped, you MUST verify the file actually exists**

```bash
# Check if the Hugo post file exists
ls content/en/posts/roppongi-christmas-illumination-2025.md
```

- **If file exists (no error):** Proceed to Step 3a (convert link)
- **If file does NOT exist (error):** Proceed to Step 4 (use placeholder)

**Step 3a: Convert to Hugo Link**

Create working internal link with proper language prefix:

```html
<!-- English version: -->
<a href="/posts/roppongi-christmas-illumination-2025/">Related Article</a>

<!-- Japanese version: -->
<a href="/ja/posts/roppongi-christmas-illumination-2025/">関連記事</a>

<!-- Chinese version: -->
<a href="/zh-cn/posts/roppongi-christmas-illumination-2025/">相关文章</a>
```

**Step 4: Use TODO Placeholder**

When mapping doesn't exist OR file doesn't exist:

```html
<!-- TODO: Update link after migration
     Naver: https://blog.naver.com/tokyomate/224065668379
     Hugo: /posts/roppongi-christmas-illumination-2025/ -->
<a href="#" style="color: #667eea;">Related Article</a>
```

---

### Intelligent Link Mapping and Auto-Conversion

🎯 **Automated link conversion using LINK_MAPPING.md**

When creating Hugo posts, the AI will:

1. **Load LINK_MAPPING.md first** to check existing mappings

2. **For each internal Naver link found:**
   - Extract Naver post ID (e.g., `223681272647` from `https://blog.naver.com/tokyomate/223681272647`)
   - Check if mapping exists in LINK_MAPPING.md
   - **Use ls command to verify file existence**

   - **If mapped AND Hugo post file exists:** ✅ Automatically convert to Hugo link

     **⚠️ CRITICAL - Link Conversion Rules:**

     **Rule 1: Always verify file existence BEFORE creating working links**
     - Check if `content/en/posts/{slug}.md` actually exists
     - **If file exists:** Create working link with proper URL format
     - **If file does NOT exist:** Use `#` placeholder + TODO comment (even if mapped in LINK_MAPPING.md)

     **Rule 2: Link Format**
     - **English posts:** Use `/posts/slug/` (NO `/en/` prefix - English is default language)
     - **Japanese posts:** Use `/ja/posts/slug/` (WITH `/ja/` prefix)
     - **Chinese posts:** Use `/zh-cn/posts/slug/` (WITH `/zh-cn/` prefix)

     ```html
     <!-- Before (Naver) -->
     <a href="https://blog.naver.com/tokyomate/224065668379">Related Article</a>

     <!-- After (Hugo - Auto-converted) -->
     <!-- English version: -->
     <a href="/posts/roppongi-christmas-illumination-2025/">Related Article</a>

     <!-- Japanese version: -->
     <a href="/ja/posts/roppongi-christmas-illumination-2025/">関連記事</a>

     <!-- Chinese version: -->
     <a href="/zh-cn/posts/roppongi-christmas-illumination-2025/">相关文章</a>
     ```

   - **If not mapped OR file does not exist:** ⏳ **ALWAYS use `#` placeholder + TODO comment**

     **⚠️ CRITICAL: Never create broken links (404 errors)**
     - **ALWAYS use `href="#"` when Hugo post file doesn't exist**
     - **ALWAYS add TODO comment with Naver URL and expected Hugo URL**
     - This applies even if the post is mapped in LINK_MAPPING.md

     ```html
     <!-- Example 1: Not mapped at all -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/223681272647
          Hugo: /posts/[SLUG_TBD]/ -->
     <a href="#" style="color: #667eea;">Related Article</a>

     <!-- Example 2: Mapped but file doesn't exist yet -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/224022065518
          Hugo: /posts/don-quijote-shopping-guide-2025/ -->
     <a href="#" style="color: #667eea;"><strong>→ Tokyo Don Quijote Shopping Guide</strong></a>

     <!-- Example 3: Japanese version (same rules apply) -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/224022065518
          Hugo: /ja/posts/don-quijote-shopping-guide-2025/ -->
     <a href="#" style="color: #667eea;"><strong>➡️ 東京ドンキホーテショッピングガイド</strong></a>
     ```

     **Why this matters:**
     - ❌ `/posts/non-existent-slug/` → 404 error (bad user experience)
     - ✅ `#` placeholder → Page stays functional, link can be updated later
     - ✅ TODO comment → Easy to find and update when post is migrated

3. **Update LINK_MAPPING.md:**
   - Add new post to Quick Reference Table
   - Record all internal links found (both mapped and unmapped)
   - Update Pending Link References for unmapped links
   - Update batch conversion script with new post mapping

**Benefits:**
- ✅ Most links work immediately for known posts
- ✅ No manual link updates needed for existing posts
- ✅ Only unmapped posts need future updates
- ✅ Efficiency improves as more posts are migrated

**Example Processing:**

```
Internal Links Found: 6

1. Naver ID: 224065668379
   ├─ Check LINK_MAPPING.md: ✅ Found (roppongi-christmas-illumination-2025)
   ├─ Verify file: ls content/en/posts/roppongi-christmas-illumination-2025.md
   ├─ File exists: ✅ Yes
   └─ Result: ✅ AUTO-CONVERTED
       EN: /posts/roppongi-christmas-illumination-2025/
       JA: /ja/posts/roppongi-christmas-illumination-2025/
       ZH-CN: /zh-cn/posts/roppongi-christmas-illumination-2025/

2. Naver ID: 224055756731
   ├─ Check LINK_MAPPING.md: ✅ Found (tokyo-3-day-christmas-itinerary)
   ├─ Verify file: ls content/en/posts/tokyo-3-day-christmas-itinerary.md
   ├─ File exists: ✅ Yes
   └─ Result: ✅ AUTO-CONVERTED
       EN: /posts/tokyo-3-day-christmas-itinerary/
       JA: /ja/posts/tokyo-3-day-christmas-itinerary/
       ZH-CN: /zh-cn/posts/tokyo-3-day-christmas-itinerary/

3. Naver ID: 224045496649
   ├─ Check LINK_MAPPING.md: ❌ Not found
   └─ Result: ⏳ TODO PLACEHOLDER
       <!-- TODO: Update link after migration
            Naver: https://blog.naver.com/tokyomate/224045496649
            Hugo: /posts/[SLUG_TBD]/ -->

4. Naver ID: 224022065518
   ├─ Check LINK_MAPPING.md: ✅ Found (don-quijote-shopping-guide-2025)
   ├─ Verify file: ls content/en/posts/don-quijote-shopping-guide-2025.md
   ├─ File exists: ❌ No (file not created yet)
   └─ Result: ⏳ TODO PLACEHOLDER
       <!-- TODO: Update link after migration
            Naver: https://blog.naver.com/tokyomate/224022065518
            Hugo: /posts/don-quijote-shopping-guide-2025/ -->

5-6. [Similar pattern for remaining links]

Final Result: 2 links auto-converted, 4 TODO placeholders
```

See `/LINK_MAPPING.md` for complete tracking database.

### Additional Link Handling Rules

* **MANDATORY: Check LINK_MAPPING.md FIRST**
  - Load `LINK_MAPPING.md` before creating any content

* **Order:** All links MUST be included in the exact same order as the original post

* **Google Maps:** Standardize ALL map links with `📍` emoji suffix
  * Format: `[Link Text](https://maps.app.goo.gl/...) 📍`

* **After Content Creation:**
  - Add unmigrated Naver URLs to "Pending References" section in LINK_MAPPING.md
  - This creates a TODO list for future migrations

---

## Migration Scripts

### Primary Script: `download_naver_images.py` (Integrated Validation)

**File:** `download_naver_images.py`

**Purpose:** Validates Hugo markdown against Naver HTML, then downloads images only if validation passes.

**Key Features:**
- ✅ **HTML Parsing:** Uses BeautifulSoup to extract images from Naver HTML
- ✅ **Ad Block Removal:** Automatically removes `ssp-adcontent`, `ad_power_content_wrap`, `data-ad` elements
- ✅ **Image Group Detection:** Handles Naver image groups (2-4 images) correctly
- ✅ **1:1 Matching Validation:** Validates image count, order, and sequential numbering with exact 1:1 match BEFORE downloading
- ✅ **Detailed Error Reports:** Shows exactly what's wrong if validation fails
- ✅ **Smart Download:** Only downloads if validation passes (saves time/bandwidth)
- ✅ **Format Conversion:** Converts all images to JPG with optimization
- ✅ **Sequential Numbering:** 01.jpg, 02.jpg, 03.jpg... (1:1 matching with Naver HTML order)
- ✅ **CSS Grid Support:** Detects images inside `.image-group-2/3/4` divs correctly

**Regex Pattern for Hugo Markdown:**
```python
# Extracts ALL <figure> tags (standalone and inside image-group divs)
figure_pattern = re.compile(
    r'<figure[^>]*>\s*<img src="(/images/posts/[^"]+)"\s+alt="([^"]*)"[^>]*>',
    re.DOTALL
)
```

**Pattern Features:**
- `<figure[^>]*>` - Matches `<figure>` tag with any attributes
- `[^>]*` after `<img>` - Allows additional attributes on img tag
- **Does NOT require closing `</figure>`** - This allows matching figures inside `.image-group-N` divs where figcaption is outside individual figures
- `re.DOTALL` - Allows `.` to match newlines (multi-line patterns)
- **Works with CSS Grid layouts** - Detects all figures regardless of container structure

**Usage:**
```bash
python3 download_naver_images.py <naver_html_file> <post-slug>

# Example:
python3 download_naver_images.py naver.md japan-convenience-store-shopping-best-10
```

**Dependencies:**
```bash
pip3 install requests pillow beautifulsoup4 lxml
```

**Workflow:**
1. Reads Naver HTML → extracts all images in order
2. Reads Hugo markdown → extracts all images (featured_image + all `<figure>` tags)
3. Validates with **1:1 matching**: exact count match, sequential numbering (01, 02, 03...)
4. If validation fails → shows detailed error report, exits
5. If validation passes → downloads all images sequentially, converts to JPG

**See:** `README_IMAGE_DOWNLOAD.md` for comprehensive documentation

### Secondary Script: `check_image_order.py` (Standalone Validator)

**File:** `check_image_order.py`

**Purpose:** Standalone validation script for existing posts (legacy/debugging).

**Usage:**
```bash
python3 check_image_order.py <naver_html_file> <post-slug>
```

**Note:** Most users should use the integrated `download_naver_images.py` instead.

---

## Pull Request Process

### Step 5: Create Pull Request

After completing EN/JA/ZH-CN blog post creation, commit changes and create a PR with detailed information.

#### 5.1. Commit and Push

```bash
# Stage all changes
git add LINK_MAPPING.md content/en/posts/*.md content/ja/posts/*.md content/zh-cn/posts/*.md

# Commit with descriptive message
git commit -m "Add [Post Title] blog post (EN/JA/ZH-CN) with link conversion"

# Push to branch
git push -u origin claude/[branch-name]
```

#### 5.2. Create PR via GitHub Web Interface

⚠️ **Note:** The `gh` CLI is not available in this environment. Create PR manually via GitHub web interface.

**PR Title Format:**
```
Add [Post Title] Blog Post (EN/JA/ZH-CN) with [Key Feature]
```

**Examples:**
- `Add Meiji Jingu Gaien Christmas Market 2025 Blog Post (EN/JA/ZH-CN) with Full Link Conversion`
- `Add Roppongi Hills Illumination 2025 Blog Post (EN/JA/ZH-CN) with SEO Optimization`

**PR Description Template:**
```markdown
## Summary
[1-2 sentence overview of the blog post content and key features]

## Changes

### 1. New Blog Posts Created
- **English Version:** `content/en/posts/[slug].md`
  - SEO-optimized title ([X] chars): "[Full Title]"
  - Meta description ([X] chars) for social media preview
  - [X] image references with descriptive alt text
  - All [X] internal links converted to Hugo format

- **Japanese Version:** `content/ja/posts/[slug].md`
  - Japanese title ([X] chars): "[Japanese Title]"
  - Same translationKey for multilingual coordination
  - All [X] internal links converted with `/ja/` prefix
  - Same [X] image references

- **Chinese Version:** `content/zh-cn/posts/[slug].md`
  - Chinese title ([X] chars): "[Chinese Title]"
  - Same translationKey for multilingual coordination
  - All [X] internal links converted with `/zh-cn/` prefix
  - Same [X] image references

### 2. Link Mapping Database Updated
- **File:** `LINK_MAPPING.md`
- Added new post entry: `[Naver ID] → [slug]`
- Updated statistics: [N] → [N+1] posts migrated
- Removed post from "Pending Link References" section (if applicable)
- Added mapping to batch conversion script

## Internal Link Conversion Details

**Total Links Found:** [X]
**Successfully Converted:** [X] ([XX]% ✅)

Converted posts:
- [list of converted post slugs]

## Content Highlights

### Event/Topic Information Covered
- [Key point 1]
- [Key point 2]
- [Key point 3]

### SEO Optimization
- ✅ Keyword-rich titles (EN 50-80 chars, JA 35-55 chars, ZH-CN 40-60 chars)
- ✅ Meta descriptions within character limits
- ✅ Descriptive alt text for all images
- ✅ Structured H2/H3 headings with keywords
- ✅ Internal linking to related content
- ✅ Featured image for social media preview

## Testing

✅ All internal links verified against LINK_MAPPING.md
✅ TranslationKey consistent across EN/JA/ZH-CN versions
✅ Front matter validation (dates, categories, tags)
✅ Image paths follow naming convention
✅ Hugo syntax validation

## Files Changed

- `content/en/posts/[slug].md` (new, [X] lines)
- `content/ja/posts/[slug].md` (new, [X] lines)
- `content/zh-cn/posts/[slug].md` (new, [X] lines)
- `LINK_MAPPING.md` (modified, +[X] lines)

## Breaking Changes

None

## Next Steps After Merge

1. Download images using migration script:
   ```bash
   python3 download_naver_images.py naver.md [slug]
   ```

2. Commit and push images ([X] files)

3. Verify production deployment at:
   - EN: https://tripmate.news/posts/[slug]/
   - JA: https://tripmate.news/ja/posts/[slug]/
   - ZH-CN: https://tripmate.news/zh-cn/posts/[slug]/

## Related

- Naver Blog Post ID: [ID]
- Migration Session: [branch-name]
- LINK_MAPPING.md: Updated to [N] posts
```

#### 5.3. PR Creation Checklist

Before creating the PR, ensure:
- ✅ Branch name follows convention: `claude/[descriptive-name]-[session-id]`
- ✅ All files committed and pushed
- ✅ PR title is clear and descriptive
- ✅ PR description includes all sections (Summary, Changes, Testing, Files Changed)
- ✅ Internal link conversion details documented
- ✅ SEO optimization checklist completed
- ✅ Next steps clearly outlined

### Step 6: After PR Merge

- Download images using migration script
- Commit and push images to main branch
- Verify production deployment

---

**End of MIGRATION_GUIDE.md**
