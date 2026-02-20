# MIGRATION_GUIDE.md - Naver Blog to Hugo Migration Guide

> **Last Updated:** 2026-01-11
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

**Step 3.1: Verify naver.md and Analysis Phase**

**✅ FIRST: Read and verify naver.md contains new blog content**
```bash
# Verify naver.md exists and has content
cat naver.md | head -20
```

**Then proceed with analysis:**
- Extract publish date from Naver HTML
- **Determine Hugo slug for this post:**
  - Create SEO-friendly kebab-case slug
  - Rules: lowercase, hyphens, keyword-rich, under 60 chars
  - **Do NOT include years/dates** (e.g., `2025`, `2026`) unless it is a specific one-time event log. For evergreen content (guides, recommendations), keep the URL clean.
  - Example: `roppongi-christmas-illumination` (NOT `roppongi-christmas-illumination-2025`)
  - **Check if already recorded in LINK_MAPPING.md:**
    - Look for the Naver ID in the `Quick Reference Table`.
    - **If NOT found:** Add a new row with Status `pending` and Date `-`.
    - This reserves the slug for consistency across future posts.
- Count images and verify order in naver.md
- Load LINK_MAPPING.md for internal link conversion
- Identify all Naver blog links in content


**Step 3.2: Create English Version FIRST**
- Create `content/en/posts/[slug].md` (using slug from Step 3.1)
- Apply all content creation guidelines (see below)
  - **Handling Naver Posts (Mandatory Workflow):**
    1. **Analyze and Plan:**
       - View entire `naver.md` to understand structure.
       - **If `naver.md` is too long:** Identify logical section breaks (headings, topics) and split into 5-7 major sections.
       - Create mental outline of sections.
    2. **Section-by-Section Creation:**
       - Generate English version section by section.
       - Each section should be complete with:
         - Proper markdown formatting
         - Converted tables
         - Internal link placeholders
         - Images with captions
       - **DO NOT** request approval after each section.
       - Continue until entire post is complete.
    3. **Integration:**
       - Combine all sections into a single cohesive file.
       - Ensure consistent formatting throughout.
       - Verify all sections flow naturally.
       - Check that front matter is complete.
- **⚠️ CRITICAL: Process ALL Naver links using Link Conversion Workflow:**
  1. **Identify all Naver links** in the source content:
     ```bash
     grep -o 'blog.naver.com/tokyomate/[0-9]*' naver.md | sort -u
     ```
  2. **For EACH Naver link, check LINK_MAPPING.md Quick Reference Table:**
     - **CRITICAL:** Check the **"Status" column** (4th column).
     - **If Status = ✅:** Post is migrated → Use Hugo slug (e.g., `/posts/[slug]/`).
     - **If Status = pending:** Slug is reserved but not yet migrated → Use TODO placeholder.

   3. **Use TODO Placeholder (when mapping doesn't exist OR file doesn't exist):**

      ```html
      <!-- TODO: Update link after migration
           Naver: https://blog.naver.com/tokyomate/224065668379
           Hugo: /posts/roppongi-christmas-illumination-2025/ -->
      <strong>Related Article</strong>
      ```
      Note: Use plain text (no `<a>` tag) for unmigrated links. The TODO comment allows `grep TODO` tracking. When the post is migrated, wrap the text with `<a href="/posts/[slug]/" style="color: #667eea;">...</a>`.
- **⚠️ MANDATORY: Add Editor's Note section at the end** (CRITICAL: Use exact format below)

  **EXACT FORMAT TO USE (DO NOT MODIFY):**

  ```html
  <!-- English Version -->
  <div class="editors-note">
    <p style="text-align: left; font-style: italic;"><strong>Editor's Note</strong></p>
    <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
      This article is based on the author's actual experiences and original content from <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>. It has been translated and adapted to provide authentic travel information about Tokyo for global readers.
    </p>
  </div>

  <!-- Japanese Version -->
  <div class="editors-note">
    <p style="text-align: left; font-style: italic;"><strong>編集者注</strong></p>
    <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
      本記事は、筆者の実際の体験に基づき、公式ブログ <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a> に掲載されたオリジナルコンテンツを翻訳・再構成したものです。リアルな東京の旅情報をお届けします。
    </p>
  </div>

  <!-- Chinese Version -->
  <div class="editors-note">
    <p style="text-align: left; font-style: italic;"><strong>编者按</strong></p>
    <p style="background-color: #f7f7f7; padding: 15px; border-left: 4px solid #667eea; margin: 10px 0;">
      本文基于作者的亲身经历，编译自韩国原创博客 <a href="https://blog.naver.com/tokyomate/[NAVER_POST_ID]" target="_blank" style="color: #667eea; text-decoration: underline;">blog.naver.com/tokyomate</a>。内容经过翻译与调整，旨在为您分享真实可靠的东京旅行资讯。
    </p>
  </div>
  ```

  **CRITICAL RULES:**
  - ❌ DO NOT use `## Editor's Note` heading format
  - ❌ DO NOT simplify the HTML structure
  - ✅ MUST use `<div class="editors-note">` wrapper
  - ✅ MUST include all inline styles exactly as shown
  - ✅ Replace `[NAVER_POST_ID]` with actual ID from LINK_MAPPING.md
  - ✅ Place before closing `</div>` tag at end of post

**Step 3.3: Download Images**

**⚠️ IMPORTANT: Download images immediately after creating English version**

This ensures images are available when user reviews the preview.

```bash
python3 download_naver_images.py "[slug]"
```

**What this script does:**
- Reads `naver.md` and extracts all images in sequential order
- Validates against English markdown (1:1 matching)
- Downloads all images to `static/images/posts/`
- Auto-converts to JPG format
- Sequential numbering: `{slug}-01.jpg`, `{slug}-02.jpg`, `{slug}-03.jpg`, ...

**Why download before user review:**
- ✅ User can see actual images during English version review
- ✅ Verify image positions match content flow
- ✅ Catch any image-related issues early
- ✅ Japanese and Chinese versions will use the same images

**Step 3.4: Start or Verify Local Hugo Server**

**Before providing preview links, ensure Hugo server is running:**

```bash
# Check if hugo server is already running
# If running, you'll see "Web Server is available at http://localhost:1313/"
# If NOT running, start it:
hugo server -D
```

**Expected output when server starts:**
```
Web Server is available at http://localhost:1313/
Press Ctrl+C to stop
```

**Important Notes:**
- If server is already running, skip this step
- Server auto-reloads when new content is added
- Keep server running throughout the migration session
- The `-D` flag includes draft posts in preview

**Step 3.5: Provide English Preview Link & Request User Approval**

**⏸️ STOP HERE - Wait for user approval before proceeding**

Provide the English preview link:
```
English Version: http://localhost:1313/posts/[slug]/
```

**Request user to review:**
- ✅ Content accuracy and completeness
- ✅ Image positions and captions
- ✅ All images displaying correctly
- ✅ Internal links working correctly
- ✅ Formatting and styling
- ✅ SEO elements (title, description)

**Wait for user confirmation:**
- User will respond with "OK" or "완료" or provide feedback
- If feedback received, make corrections and re-submit for review
- **Only proceed to Japanese/Chinese versions after approval**

**Step 3.6: Create Japanese & Chinese Versions (After EN Approval)**

**✅ Only start after user approves English version**

Create both language versions:
- Create `content/ja/posts/[slug].md`
- Create `content/zh-cn/posts/[slug].md`

**Apply same guidelines with language-specific adaptations:**
- Same `translationKey` as English version (critical for language switcher)
- Same `date` field as English version
- Same image references (`{slug}-01.jpg`, `{slug}-02.jpg`, ...)
- Language-specific tags and categories (JA tags for JA post, ZH-CN tags for ZH-CN post)
- Translated content following MIGRATION_GUIDE cultural adaptation rules
- Language-appropriate Editor's Note (use exact format from Step 3.2)
- Process internal links with language prefix (`/ja/posts/` for JA, `/zh-cn/posts/` for ZH-CN)

**Step 3.7: Provide All Language Preview Links**

**After creating Japanese and Chinese versions, provide all preview links:**

```
EN: http://localhost:1313/posts/[slug]/
JA: http://localhost:1313/ja/posts/[slug]/
ZH-CN: http://localhost:1313/zh-cn/posts/[slug]/
```

**User can verify:**
- All three language versions display correctly
- Consistent images across all languages
- Proper language switching functionality
- TranslationKey linkage working
- Language-specific tags and categories

**Step 3.8: Verify Content Completeness**

**MANDATORY VERIFICATION CHECKLIST:**

After creating all three language versions, verify the following counts match between original Naver HTML and created Hugo posts:

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
- Update all three language versions
- Re-verify counts until all match

**Step 3.9: Finalize LINK_MAPPING.md**

**Update LINK_MAPPING.md with the new post:**

1. **Update Quick Reference Table:**
   - Change Status from `pending` to `✅`
   - Update Date from `-` to current date (YYYY-MM-DD)
   - Verify Naver ID and Hugo slug are correct

2. **Remove from Pending References (if applicable):**
   - If the ID was listed in `## Pending Link References` section, remove it
   - This post is now fully migrated

3. **Note about placeholder links:**
   - Unmigrated links appear as plain text (no `<a>` tag) with a `<!-- TODO -->` comment
   - Each new migration will check LINK_MAPPING.md and convert plain-text placeholders to working `<a>` links
   - Use `grep -r 'TODO: Update link' content/` to find all pending placeholders

---

### Step 4: User Reviews and Confirms

```
User: "OK" or "완료" or provides feedback
```

**If user requests changes:**
- Make corrections to the affected language version(s)
- Re-run verification if needed
- Provide updated preview links
- Wait for final "OK"

---

### Step 5: Maintenance & Cleanup (MANDATORY after Category/Tag Changes)

Whenever you rename or merge categories/tags in the content files, you MUST perform a clean build to remove "ghost" entries from the UI.

1. **Perform Clean Build:**
   ```bash
   hugo --cleanDestinationDir
   ```

2. **Verify Taxonomy Pages:**
   Ensure the old category names no longer appear in the footer or category list pages.

3. **Verify CSS Integrity:**
   If UI breakage occurs on taxonomy pages, verify that `layouts/partials/site-style.html` is using root-relative paths for CSS assets.

**If counts don't match:**
- Review original HTML to find missing images/captions/links
- Update all three language versions
- Re-verify counts until all match

### Step 6: Deploy to GitHub

**After user confirms "OK", commit and push all changes:**

```bash
git add .
git commit -m "Add [slug] blog post (EN/JA/ZH-CN)

New Content:
- Created comprehensive [topic] guide
- Added [N] images
- All three language versions (EN/JA/ZH-CN)

Link Updates:
- Updated LINK_MAPPING.md (Status: ✅)
- Converted [N] internal links

Naver ID: [POST_ID]
Slug: [slug]"
git push
```

**Important Notes:**
- Push to the current branch (e.g., `claude/[name]-[session-id]`)
- GitHub Actions will auto-deploy to production after merge to main
- Verify deployment at https://tripmate.news after merge

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

  **⚠️ CRITICAL: HTML vs Markdown in Block Elements**
  - **The Issue:** The entire blog post is wrapped in `<div class="blog-container">`. In Hugo, **Markdown syntax (bold `**`, lists `-`) DOES NOT RENDER** inside block-level HTML tags.
  - **Symptom:** You will see raw asterisks (e.g., `**Text**`) or raw hyphens (`- Item`) in the final output instead of bold text or bullet points.
  - **Strict Rule for Lists (Access/Info Sections):**
    - **NEVER** use Markdown lists (`- Item` or `1. Item`) inside the blog container.
    - **ALWAYS** use HTML `<ul>`, `<ol>`, and `<li>` tags.
    - *Example:* "Access" or "Info Box" sections MUST use HTML lists.
  - **Strict Rule for Bold/Emphasis:**
    - **NEVER** use `**text**` inside the blog container.
    - **ALWAYS** use `<strong>text</strong>` for bold.
  - *Exception:* Headings (`##`) and blockquotes (`>`) are the only Markdown elements that reliably work because they are block-level elements themselves. For everything else (inline styles, lists), use HTML.

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

   - **If not mapped OR file does not exist:** ⏳ **Use plain text + TODO comment**

     **⚠️ CRITICAL: Never create broken or dead links**
     - ❌ **NEVER use `href="#"`** — broken links hurt AdSense review and user experience
     - ❌ **NEVER use `/posts/non-existent-slug/`** — causes 404 errors
     - ✅ **Use plain text (no `<a>` tag)** so readers see the text but can't click a dead link
     - ✅ **ALWAYS add TODO comment** with Naver URL and expected Hugo URL for tracking

     ```html
     <!-- Example 1: Not mapped at all -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/223681272647
          Hugo: /posts/[SLUG_TBD]/ -->
     <strong>Related Article</strong>

     <!-- Example 2: Mapped but file doesn't exist yet -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/224022065518
          Hugo: /posts/don-quijote-shopping-guide-2025/ -->
     <strong>→ Tokyo Don Quijote Shopping Guide</strong>

     <!-- Example 3: Japanese version (same rules apply) -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/224022065518
          Hugo: /ja/posts/don-quijote-shopping-guide-2025/ -->
     <strong>➡️ 東京ドンキホーテショッピングガイド</strong>
     ```

     When the target post is migrated later, wrap the text with a real link:
     ```html
     <a href="/posts/don-quijote-shopping-guide-2025/" style="color: #667eea;"><strong>→ Tokyo Don Quijote Shopping Guide</strong></a>
     ```

     **Why this matters:**
     - ❌ `href="#"` → Dead link that hurts AdSense review and looks broken
     - ❌ `/posts/non-existent-slug/` → 404 error (bad user experience)
     - ✅ Plain text → Readers see the content, no broken clicks
     - ✅ TODO comment → Easy to find with `grep TODO` and update when post is migrated

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

* **Google Maps:** Standardize ALL map links with `📍` emoji **PREFIX**
  * Rule: Add `📍` at the **beginning** of the link text ONLY if it is not already present. If it's already there, do not add another one.
  * Format: `📍 [Link Text](https://maps.app.goo.gl/...)`

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
python3 download_naver_images.py <post-slug>

# Example:
python3 download_naver_images.py japan-convenience-store-shopping-best-10
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
   python3 download_naver_images.py [slug]
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
