# CLAUDE.md - AI Assistant Guide

> **Last Updated:** 2025-12-26
> **Project:** Tokyo Mate (Trip Mate News Blog)
> **Site:** https://tripmate.news
> **Type:** Hugo Static Site for GitHub Pages

This document provides essential guidance for AI assistants working on this codebase.

**📚 Additional Documentation:**
- **[CONTENT_GUIDELINES.md](./CONTENT_GUIDELINES.md)** - Blog post formatting, SEO optimization, tags, categories, images
- **[MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md)** - Naver blog to Hugo migration workflow, scripts, link mapping

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture & Technology Stack](#architecture--technology-stack)
3. [Directory Structure](#directory-structure)
4. [Development Workflows](#development-workflows)
5. [Monetization](#monetization)
6. [Key Conventions](#key-conventions)
7. [Common Tasks](#common-tasks)
8. [Important Files](#important-files)
9. [Critical Considerations](#critical-considerations)
10. [Quick Reference](#quick-reference)
11. [Getting Help](#getting-help)

---

## Project Overview

### What is this project?

**Tokyo Mate** (도쿄메이트 / 東京メイト) is a multilingual travel blog focused on Tokyo, Japan. It covers:
- Restaurant reviews and guides
- Travel information and tips
- Tourism recommendations
- Tokyo neighborhood explorations

### Languages Supported

1. **English** (en) - Primary/Default language
2. **Japanese** (ja) - Secondary
3. **Chinese (Simplified)** (zh-cn) - Tertiary

**Note:** Korean language support has been removed. The blog now operates in English, Japanese, and Chinese (Simplified).

### Key Information

- **Hugo Version:** 0.128.0 extended (required)
- **Theme:** Ananke (MIT license)
- **Base URL:** https://tripmate.news
- **Custom Domain:** Configured via `/static/CNAME`
- **Analytics:** Google Analytics (G-NZ22T8HRR3)
- **Search Console:** Google verified (code in `hugo.toml`)
- **Timezone:** Asia/Seoul (UTC+09:00)
- **Deployment:** Automated via GitHub Actions to GitHub Pages

---

## Architecture & Technology Stack

### Core Technologies

```
Hugo (v0.128.0 extended)
├── Theme: Ananke (Git submodule)
│   └── CSS Framework: Tachyons
├── Markup: Goldmark (CommonMark)
├── Syntax Highlighting: GitHub style
└── Deployment: GitHub Actions → GitHub Pages
```

### Dependencies

**Required for Development:**
- Hugo 0.128.0 extended (for Sass/SCSS)
- Git (for submodules)
- Python 3 + requests library (for image migration script)

**Runtime Dependencies:**
- None (static site)

**Theme Dependency:**
- Ananke theme installed as Git submodule at `/themes/ananke/`

### Hugo Layout System

**Layout Priority (Hugo Template Lookup Order):**

Hugo follows a specific priority order when looking for templates. More specific paths override general ones:

1. `layouts/[type]/[layout].html` (e.g., `layouts/post/list.html`)
2. `layouts/_default/[layout].html` (e.g., `layouts/_default/list.html`)
3. `themes/[theme]/layouts/[type]/[layout].html`
4. `themes/[theme]/layouts/_default/[layout].html`

**Current Layout Structure:**
```
layouts/
├── _default/
│   ├── list.html              # Default list page layout
│   └── summary.html           # Default summary card
├── partials/
│   ├── head-additions.html    # Custom CSS loader
│   └── menu-contextual.html   # Related posts sidebar
└── post/
    ├── list.html              # Post-specific list layout
    └── summary.html           # Post-specific card component
```

**Important Notes:**
- 🎨 Both `layouts/_default/` and `layouts/post/` are used for different purposes
- ✅ Keep both directories - they serve different layout contexts
- 📂 Hugo uses template lookup order to find the right layout
- ⚠️ Do NOT delete files thinking they are duplicates - verify usage first
- 🔍 Custom layouts automatically override theme defaults

---

## Directory Structure

```
mydyney.github.io/
│
├── .github/
│   └── workflows/
│       └── hugo.yml                 # CI/CD: Build & deploy workflow
│
├── .gitignore                       # Git ignore rules (public/, resources/, etc.)
│
├── archetypes/
│   └── default.md                   # Template for new posts
│
├── content/                         # ALL CONTENT - Organized by language
│   ├── en/                          # English content (DEFAULT/PRIMARY)
│   │   ├── _index.md               # English homepage
│   │   └── posts/                  # English blog posts
│   ├── ja/                          # Japanese content
│   │   ├── _index.md               # Japanese homepage
│   │   └── posts/                  # Japanese blog posts
│   └── zh-cn/                       # Chinese (Simplified) content
│       ├── _index.md               # Chinese homepage
│       └── posts/                  # Chinese blog posts
│
├── layouts/                         # Custom layouts (override theme)
│   ├── _default/
│   │   ├── list.html               # Default list layout
│   │   └── summary.html            # Default summary card
│   ├── partials/
│   │   └── head-additions.html     # CSS loader + SEO tags + favicon
│   └── post/
│       ├── list.html               # Post list layout
│       └── summary.html            # Post card component
│
├── public/                          # ✅ Generated output (gitignored, auto-generated by GitHub Actions)
│
├── resources/                       # Hugo-generated resources (gitignored)
│   └── _gen/
│       └── assets/                 # CSS, JS bundles
│
├── static/                          # Static assets
│   ├── CNAME                       # Domain: tripmate.news
│   ├── favicon.svg                 # Site favicon (SVG)
│   ├── robots.txt                  # Search engine crawl rules
│   ├── site.webmanifest            # PWA manifest
│   ├── css/                        # Custom stylesheets
│   │   ├── blog-cards.css
│   │   ├── blog-post-common.css
│   │   └── related-posts.css
│   └── images/
│       ├── posts/                  # Post-specific images
│       └── [various images]        # Site images
│
├── themes/
│   └── ananke/                     # Theme (Git submodule)
│
├── hugo.toml                        # Main Hugo configuration
├── download_naver_images.py        # Custom migration script
├── CLAUDE.md                        # This file - Core AI guide
├── CONTENT_GUIDELINES.md            # Blog formatting & SEO guide
├── MIGRATION_GUIDE.md               # Naver→Hugo migration guide
├── LINK_MAPPING.md                  # Naver-Hugo link mapping database
└── README_IMAGE_DOWNLOAD.md        # Image migration script docs
```

### Key Directories Explained

| Directory | Purpose | Notes |
|-----------|---------|-------|
| `content/` | All markdown content, organized by language | NEVER create content outside these directories |
| `layouts/` | Custom layouts that override theme | Both `_default/` and `post/` directories are used |
| `static/` | Files copied as-is to output (images, CNAME, SEO files) | Images go in `/static/images/posts/` |
| `public/` | Build output (generated by Hugo) | ✅ Gitignored - auto-generated by GitHub Actions |
| `resources/` | Hugo cache and generated assets | Gitignored, can be regenerated |
| `themes/` | Ananke theme (Git submodule) | Do NOT modify directly |
| `.github/workflows/` | CI/CD configuration | Deployment automation |

---

## Development Workflows

### Blog Migration Workflow (Naver → Hugo)

Complete step-by-step process for migrating a Naver blog post to Hugo:

#### Step 1: User Provides Naver Blog URL
```
User: "https://blog.naver.com/tokyomate/[POST_ID]"
```

**⚠️ CRITICAL AGENT RULE:**
- **NEVER** try to fetch/scrape the Naver blog URL using browser tools or `read_url_content`.
- **ALWAYS** wait for the user to provide the content in `naver.md`.
- The user will manually copy the HTML to `naver.md` because of Naver's anti-bot protections.

#### Step 2: User Updates naver.md with Blog Content
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

#### Step 3: Claude Analyzes and Creates Blog Posts

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

**Content Creation:**
- Create `content/en/posts/[slug].md`
- Create `content/ja/posts/[slug].md`
- Create `content/zh-cn/posts/[slug].md`
- ⚠️ **CRITICAL: COMPLETE CONTENT TRANSLATION**
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
    - Bold text (`<b>`, `<strong>`) → Markdown bold (`**text**`)
    - Section headings and subheadings → Markdown headings (`##`, `###`)
    - Quotation blocks → Markdown blockquotes (`>`)
    - Lists and bullet points → Markdown lists
  * **Match original structure exactly:**
    - Same number of sections
    - Same heading hierarchy
    - Same text emphasis patterns
  * **Never add extra formatting not in original**
- ⚠️ **CRITICAL: IMAGE POSITIONING & CAPTIONS**
  * **Verify ALL images from original blog:**
    - Content MUST match image positions EXACTLY
    - Same image at same position = same content context
    - Never add content not in original blog
  * **Image grouping is MANDATORY:**
    - Check for grouped images: Identify if images appear side-by-side in original
    - Preserve grouping: Use appropriate `image-group-X` class (see "Grouped Images" section below)
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
- ⚠️ **CRITICAL: HTML STRUCTURE ANALYSIS**
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
    - **NO NEW INFORMATION:** Do NOT create, guess, or hallucinations listing details not present in the source HTML.
    - **Translate ONLY what exists:** If the source says "X is popular", do not add "and stylish". Stick to the source meaning.
    - **Exact List Match:** If the source lists 3 brands, do not list 5. If it lists 5, do not list 3. Match the item count exactly.
- ⚠️ **CRITICAL: TABLE FORMATTING**
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
- ⚠️ **CRITICAL: CULTURAL ADAPTATION & WRITING STYLE**

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
- ⚠️ **CRITICAL: NO AI WRITING TRACES**
  * **NEVER leave any signs that content was AI-generated**
  * Avoid overly formal or robotic language patterns
  * No generic AI phrases like "In conclusion", "It's worth noting", "comprehensive guide"
  * Use natural, human-like variations in sentence structure
  * Include personal touches and authentic observations
  * Write as a real travel blogger would, not as an AI assistant
- ⚠️ **CRITICAL: LINK HANDLING**
  * **MANDATORY: Check LINK_MAPPING.md FIRST**
    - Load `LINK_MAPPING.md` before creating any content
  * **Link Conversion Rules (MANDATORY):**
    - **Step 1: VERIFY EXISTENCE:** Before creating a live link, you **MUST** verify that the destination file actually exists in the `content` directory (e.g., using `ls`).
    - **Step 2: Apply Link:**
        - **If file EXISTS:** Replace Naver URL with Hugo internal link: `/posts/[slug]/`
        - **If file DOES NOT EXIST (Unmigrated):** You **MUST** use the styled placeholder format below. **NEVER** create a dead link to a non-existent file.
    - **ALL** internal links from the original Naver post MUST be included (either as live link or placeholder). **DO NOT SKIP ANY LINK.**
  * **Placeholder Format for Unmigrated Posts:**
    ```html
    <!-- TODO: Update link after migration
         Naver: https://blog.naver.com/tokyomate/[POST_ID]
         Hugo: /posts/[SLUG]/ -->
    <p style="text-align: center;"><strong>☕</strong> <a href="#" style="color: #667eea;"><strong>[Link Text]</strong></a><br>
    ```
  * **Order:** All links MUST be included in the exact same order as the original post
  * **Google Maps:** Standardize ALL map links with `📍` emoji suffix
    * Format: `[Link Text](https://maps.app.goo.gl/...) 📍`
  * **After Content Creation:**
    - Add unmigrated Naver URLs to "Pending References" section in LINK_MAPPING.md
    - This creates a TODO list for future migrations

**LINK_MAPPING.md Updates:**
- Add new entry to Quick Reference Table
- Add slug to `declare -A MAPPINGS` array
- Check and update Pending References
- Update placeholder links in existing posts

#### Step 4: Claude Downloads Images
```bash
python3 download_naver_images.py naver.md "[slug]"
# Downloads to: static/images/posts/[slug]-01.jpg, [slug]-02.jpg, ...
# Auto-converts to JPG format
```

#### Step 5: Claude Provides Local Preview Links
```
EN: http://localhost:1313/posts/[slug]/
JA: http://localhost:1313/ja/posts/[slug]/
```

#### Step 5.5: Claude Verifies Content Completeness

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

#### Step 6: User Reviews and Confirms
```
User: "OK" or provides feedback
```

#### Step 7: Claude Deploys to GitHub
```bash
git add .
git commit -m "Add [slug] blog post (EN/JA)

New Content:
- Created comprehensive [topic] guide
- Added [N] images
- Both English and Japanese versions

Link Updates:
- Updated LINK_MAPPING.md
- Activated links in [N] existing posts

Naver ID: [POST_ID]
Slug: [slug]"
git push
```

---

### Local Development

```bash
# Start local development server with drafts
hugo server -D

# Start server (production-like)
hugo server

# Build site locally
hugo

# Build with minification (production)
hugo --minify
```

**Local preview:** http://localhost:1313

### Git Workflow

**Branch Naming Convention:**
```
claude/{descriptive-name}-{session-id}
```

**Example:**
```
claude/migrate-blog-posts-01Ts9NHmZwsuzNpQp6ewLzBJ
```

**Typical Development Flow:**

1. Create feature branch with `claude/` prefix
2. Make changes and commit with descriptive messages
3. Push to branch: `git push -u origin <branch-name>`
4. Create Pull Request to `main` (see PR guidelines below)
5. Merge triggers automatic deployment

### Pull Request Guidelines

**⚠️ IMPORTANT:** Always create a Pull Request with a clear title and comprehensive description.

**PR Title Format:**
```
[Action] [Component/Feature] with [Key Benefit]
```

**Examples:**
- `Add Evangelion 30th Anniversary Blog Post (EN/JA/ZH-CN)`
- `Fix Responsive Layout Issues on Mobile Devices`
- `Redesign Related Posts Section with Modern Compact Sidebar Layout`

**PR Description Best Practices:**

1. **Title:**
   - Use action verbs (Add, Update, Fix, Redesign, Implement)
   - Be specific about what changed
   - Include the benefit or goal

2. **Description:**
   - Start with a clear summary
   - Group changes logically
   - Use checkboxes (✅) for testing/verification items
   - Include visual comparisons for UI changes
   - List all affected files
   - Note any breaking changes explicitly

3. **When to Create PRs:**
   - After completing a feature or fix
   - Before merging to main branch
   - When work is ready for review/deployment

**Important Git Notes:**

- Git submodules are used (theme)
- Clone with: `git clone --recursive` OR after clone: `git submodule update --init --recursive`
- Push requires branch to start with `claude/` and match session ID (403 error otherwise)
- Retry failed pushes with exponential backoff (2s, 4s, 8s, 16s)

### Deployment (Automated)

**Trigger:** Push to `main` branch OR manual workflow dispatch

**GitHub Actions Workflow:** `.github/workflows/hugo.yml`

**Build Steps:**
1. Install Hugo 0.128.0 extended
2. Install Dart Sass
3. Checkout with submodules
4. Build with Hugo (minified, production environment)
5. Upload to GitHub Pages
6. Deploy

**Environment Variables:**
- `HUGO_ENVIRONMENT=production`
- `TZ=Asia/Seoul`

**⚠️ CRITICAL: baseURL Configuration:**
- **NEVER** use `--baseURL "${{ steps.pages.outputs.base_url }}/"` in workflow
- **ALWAYS** let Hugo use `baseURL` from `hugo.toml` (https://tripmate.news)
- GitHub Pages auto-generated URL does NOT match custom domain
- Using wrong baseURL causes 404/403 errors across entire site
- Correct build command: `hugo --minify` (no baseURL flag)

**Deployment URL:** https://tripmate.news (via GitHub Pages)

---

## Monetization

### Google AdSense

The site uses Google AdSense for monetization with Auto Ads enabled.

**Configuration:**

- **Publisher ID:** `ca-pub-8704780774924832`
- **Configuration File:** `hugo.toml` (`params.adsense_publisher_id`)
- **Auto Ads Script:** Loaded in `layouts/partials/head-additions.html`

**Auto Ads:**

Google Auto Ads automatically places ads in optimal positions across the site. No manual placement is required.

The AdSense script is loaded in the `<head>` section of every page via `head-additions.html`:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8704780774924832"
     crossorigin="anonymous"></script>
```

**Important Notes:**

- Auto Ads may take 1-2 days to start showing after initial setup
- AdSense account must be approved by Google before ads will display
- Test ads won't show in localhost development
- Monitor AdSense dashboard for performance and policy compliance

**AdSense Setup Steps:**

1. ✅ AdSense account created
2. ✅ Site added to AdSense: `https://tripmate.news`
3. ✅ Auto Ads code added to site
4. ⏳ Waiting for Google AdSense approval (can take 1-2 weeks)
5. ⏳ Ads will automatically appear once approved

---

## Key Conventions

### Naming Conventions

| Item | Convention | Examples |
|------|------------|----------|
| Post files | Kebab-case `.md` | `tokyo-ramen-street-guide.md` |
| Post slugs | Kebab-case | `kirimugiya-jinroku-shinjuku` |
| Image files | `{slug}-{number}.{ext}` | `tokyo-guide-01.jpg` |
| Git branches | `claude/{name}-{id}` | `claude/add-feature-abc123` |
| Categories (EN) | Title Case | `["Travel Guide", "Food & Dining"]` |
| Categories (JA) | Natural Japanese | `["旅行ガイド", "グルメ"]` |
| Categories (ZH-CN) | Natural Chinese | `["旅游指南", "美食"]` |
| Tags (EN) | kebab-case | `["tokyo-restaurants", "travel-tips"]` |
| Tags (JA) | Natural Japanese | `["東京レストラン", "旅行情報"]` |
| Tags (ZH-CN) | Natural Chinese | `["东京餐厅", "旅行信息"]` |

### Content Patterns

**Front Matter Format:** YAML (not TOML)

**Timezone:** Always use `+09:00` for dates (Asia/Seoul)

**Draft Workflow:**
1. Create post with `draft: true`
2. Work on content locally with `hugo server -D`
3. When ready, set `draft: false`
4. Commit and push

**HTML in Markdown:**
- Allowed (unsafe HTML is enabled in Goldmark)
- Use common CSS classes from `/static/css/blog-post-common.css`
- Wrap post content in `<div class="blog-container">`
- DO NOT add inline `<style>` blocks (use shared CSS instead)
- **⚠️ IMPORTANT:** Inside `blog-container`, use HTML for bold (`<b>`, `<strong>`) and lists (`<ul>`, `<li>`) - Markdown syntax doesn't render

### Code Style

**Markdown:**
- Use proper heading hierarchy (h1 → h2 → h3)
- Include alt text for images
- Use semantic HTML when needed

**Blog Post Styling:**
- Use shared CSS file: `/static/css/blog-post-common.css`
- Available classes: `.blog-container`, `.info-box`, `.schedule-table`, `.tip-box`, `.image-group-2/3/4`
- DO NOT add `<style>` blocks in individual posts (except figcaption inline styles)
- ALL figcaptions MUST use: `style="font-size: 0.7em; text-align: center;"`
- Use `.image-group-N` for side-by-side image layouts (2, 3, or 4 images)

**Commit Messages:**
- Use descriptive messages
- Mix of English/Korean is acceptable
- Include context (e.g., "Add images for [post-name]")

---

## Common Tasks

### 1. Adding a New Blog Post

**NOTE:** Blog posts are typically created from Korean Naver HTML. AI translates to English, Japanese, and Chinese (Simplified).

```bash
# 1. Create post in all three languages
hugo new content/en/posts/my-post.md
hugo new content/ja/posts/my-post.md
hugo new content/zh-cn/posts/my-post.md

# 2. Edit each file:
#    - Add same translationKey to all three
#    - Fill in content (see CONTENT_GUIDELINES.md)
#    - Set draft: false when ready

# 3. Add images (if needed)
#    - Save to /static/images/posts/
#    - Use naming: my-post-01.jpg, my-post-02.jpg, etc.

# 4. Test locally
hugo server -D

# 5. Commit and push
git add .
git commit -m "Add new blog post: My Post (EN/JA/ZH-CN)"
git push -u origin <your-branch>

# 6. Create PR to main branch
```

**📚 For detailed blog post formatting rules, see [CONTENT_GUIDELINES.md](./CONTENT_GUIDELINES.md)**

### 2. Migrating Content from Naver Blog

**📚 For complete migration workflow, see [MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md)**

**Quick Overview:**

1. User provides Naver blog URL
2. User copies HTML to `naver.md`
3. Claude analyzes and creates EN/JA/ZH-CN posts
4. Download images: `python3 download_naver_images.py naver.md [slug]`
5. Test locally and get user approval
6. Deploy to GitHub

### 3. Updating Site Configuration

**File:** `hugo.toml`

```bash
# 1. Edit hugo.toml
# 2. Test changes locally
hugo server

# 3. Verify in browser
# 4. Commit changes
git add hugo.toml
git commit -m "Update site configuration: [description]"
git push
```

### 4. Updating Theme

```bash
# Theme is a Git submodule
cd themes/ananke
git pull origin main
cd ../..

# Commit submodule update
git add themes/ananke
git commit -m "Update Ananke theme to latest version"
git push
```

---

## Important Files

### Configuration Files

| File | Purpose | Notes |
|------|---------|-------|
| `hugo.toml` | Main Hugo configuration | Site settings, languages, menus, params, SEO |
| `.github/workflows/hugo.yml` | CI/CD workflow | Automated build & deployment |
| `.gitignore` | Git ignore rules | Excludes `public/`, `resources/`, temp files |
| `.gitmodules` | Git submodule config | Ananke theme reference |
| `static/CNAME` | Custom domain config | Contains: `tripmate.news` |

### SEO Files

| File | Purpose | Notes |
|------|---------|-------|
| `static/robots.txt` | Search engine crawl rules | Sitemap locations, crawl directives |
| `static/favicon.svg` | Site favicon | TM logo with purple gradient |
| `static/site.webmanifest` | PWA manifest | App name, icons, theme color |
| `layouts/partials/head-additions.html` | SEO meta tags | hreflang, favicon, verification codes |

### Content Templates

| File | Purpose |
|------|---------|
| `archetypes/default.md` | Template for `hugo new` command |

### Documentation Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Core AI assistant guide (this file) |
| `CONTENT_GUIDELINES.md` | Blog formatting, SEO, tags, categories |
| `MIGRATION_GUIDE.md` | Naver→Hugo migration workflow |
| `LINK_MAPPING.md` | Naver-Hugo link mapping database |
| `README_IMAGE_DOWNLOAD.md` | Image migration script documentation |

### Design & Style Files

| File | Purpose | Notes |
|------|---------|-------|
| `static/css/blog-cards.css` | Blog card styles for post listings | Modern magazine-style cards with gradients |
| `static/css/blog-post-common.css` | Shared styles for blog post content | Classes: `.blog-container`, `.info-box`, `.schedule-table`, `.tip-box`, `.image-group-2/3/4` |
| `static/css/related-posts.css` | Related posts sidebar styles | Compact horizontal card layout with thumbnails |
| `layouts/partials/head-additions.html` | CSS loader for custom styles | Automatically loads all three CSS files |
| `layouts/partials/menu-contextual.html` | Related posts sidebar component | Displays up to 6 related posts |
| `layouts/post/list.html` | Post listing page layout | CSS Grid with responsive breakpoints |
| `layouts/post/summary.html` | Blog card component | Individual card template |

---

## Critical Considerations

### ⚠️ Things to Be Careful About

1. **Git Submodules**
   - Theme is a submodule - always clone with `--recursive`
   - Don't modify theme files directly
   - Update submodule properly with git commands

2. **Public Directory (Gitignored)**
   - ✅ `public/` is now properly gitignored
   - GitHub Actions generates fresh `public/` on every deploy
   - Local `hugo server` output won't affect production
   - No need to worry about localhost URLs in sitemap anymore

3. **Branch Naming for Pushes**
   - Branches MUST start with `claude/` and match session ID
   - Push will fail with 403 error otherwise
   - Retry logic: exponential backoff (2s, 4s, 8s, 16s)

4. **Hugo Version Requirement**
   - Must use Hugo 0.128.0 **extended** (for Sass/SCSS)
   - CI/CD enforces this version
   - Local development should match

5. **Multilingual TranslationKey**
   - MUST be identical across language versions
   - Typos break language switcher
   - Validate when creating multilingual content

6. **Timezone Consistency**
   - Always use `+09:00` (Asia/Seoul) for dates
   - CI/CD sets `TZ=Asia/Seoul`
   - Inconsistent timezones cause post ordering issues

7. **Image Paths**
   - Use absolute paths from site root: `/images/posts/...`
   - NOT relative paths: `../../static/images/...`
   - Paths are case-sensitive

8. **CNAME File**
   - `/static/CNAME` contains custom domain
   - DO NOT delete or modify unless changing domain
   - Required for custom domain to work

9. **GitHub Actions baseURL (CRITICAL)**
   - **NEVER** override baseURL in `.github/workflows/hugo.yml`
   - Build command must be: `hugo --minify` (no --baseURL flag)
   - Let Hugo use baseURL from `hugo.toml` (https://tripmate.news)
   - Using `--baseURL "${{ steps.pages.outputs.base_url }}/"` causes 404/403 errors
   - GitHub Pages auto URL doesn't match custom domain

### 🚫 Do NOT Do

1. **Do NOT** modify files inside `/themes/ananke/` directly
   - Create custom layouts in root `/layouts/` to override

2. **Do NOT** hardcode localhost URLs or absolute URLs in content
   - Use Hugo's `baseURL` and relative paths

3. **Do NOT** commit with `draft: true` to main branch
   - Drafts won't show on production site
   - Can cause confusion

4. **Do NOT** change language codes (en, ja, zh-cn)
   - Breaks existing URL structure
   - Affects SEO and external links

5. **Do NOT** skip submodule initialization
   - Site won't build without theme
   - Always use `git submodule update --init --recursive`

6. **Do NOT** delete layout files assuming they are duplicates
   - Both `layouts/_default/` and `layouts/post/` may be needed
   - Verify the actual usage before removing files
   - Test locally after any layout changes

7. **Do NOT** add inline `<style>` blocks in blog posts
   - Use shared CSS: `/static/css/blog-post-common.css`
   - Keeps styles consistent and maintainable

8. **Do NOT** commit the `public/` directory
   - It's now gitignored - GitHub Actions generates it automatically
   - If accidentally staged, use `git rm -r --cached public/`

9. **Do NOT** add `--baseURL` flag to GitHub Actions workflow
   - Causes 404/403 errors by overriding custom domain
   - Build command must be: `hugo --minify` only
   - Never use: `--baseURL "${{ steps.pages.outputs.base_url }}/"`
   - Let Hugo use `hugo.toml` baseURL setting

10. **Do NOT** create documents or files unless explicitly requested
    - Only create content when user specifically asks for it
    - Do not proactively generate README files, documentation, or other markdown files
    - Exception: Required files for completing a specific task (e.g., blog posts during migration)
    - If uncertain whether to create a file, ask the user first

### ✅ Best Practices

1. **Always test locally** with `hugo server` before pushing
2. **Use descriptive commit messages** with context
3. **Maintain consistent front matter** across posts
4. **Follow image naming conventions** strictly
5. **Link translations** with `translationKey`
6. **Check CI/CD logs** if deployment fails
7. **Keep theme submodule updated** periodically
8. **Use shared CSS files** for blog post styles (blog-post-common.css)
9. **Test layout changes locally** before pushing to production
10. **Wrap blog post content** in `<div class="blog-container">` for consistent styling
11. **SEO verification codes** are configured in `hugo.toml` under `[params]`
12. **After main branch merge**, verify site at https://tripmate.news works correctly

---

## Quick Reference

### Essential Commands

```bash
# Local development
hugo server -D              # Serve with drafts
hugo server                 # Serve production-like

# Build
hugo                        # Build site
hugo --minify              # Build with minification

# Content creation
hugo new content/en/posts/name.md      # New English post
hugo new content/ja/posts/name.md      # New Japanese post
hugo new content/zh-cn/posts/name.md   # New Chinese post

# Git
git submodule update --init --recursive   # Init theme
git push -u origin claude/branch-name     # Push to branch

# Migration (Naver Blog) - See MIGRATION_GUIDE.md for details
python3 download_naver_images.py naver.md post-slug
```

### Key URLs

- **Production Site:** https://tripmate.news
- **GitHub Repo:** https://github.com/mydyney/mydyney.github.io
- **Local Preview:** http://localhost:1313
- **Theme Docs:** https://github.com/theNewDynamic/gohugo-theme-ananke

### Important Paths

```
Content:         /content/{en,ja,zh-cn}/posts/*.md
Images:          /static/images/posts/
Config:          /hugo.toml
Theme:           /themes/ananke/ (submodule)
CI/CD:           /.github/workflows/hugo.yml
Build Output:    /public/
```

---

## Getting Help

### Hugo Documentation
- Hugo Official Docs: https://gohugo.io/documentation/
- Hugo Multilingual: https://gohugo.io/content-management/multilingual/
- Hugo Front Matter: https://gohugo.io/content-management/front-matter/

### Theme Documentation
- Ananke Theme: https://github.com/theNewDynamic/gohugo-theme-ananke
- Theme Demo: https://gohugo-ananke-theme-demo.netlify.app/

### GitHub Actions
- Hugo Actions: https://github.com/peaceiris/actions-hugo
- GitHub Pages Deploy: https://github.com/peaceiris/actions-gh-pages

---

## Document Maintenance

**Last Updated:** 2025-12-26
**Updated By:** Claude (AI Assistant)
**Next Review:** When significant project changes occur

**Recent Updates (2025-12-26 - Latest):**
- **MAJOR RESTRUCTURING:**
  - Split CLAUDE.md into 3 focused files for better AI comprehension
  - Created CONTENT_GUIDELINES.md (blog formatting, SEO, tags, categories)
  - Created MIGRATION_GUIDE.md (Naver→Hugo workflow, scripts, link mapping)
  - Reduced CLAUDE.md from 2,856 lines to ~800 lines (72% reduction)
  - Added references to new documentation files throughout
  - **Impact:** Dramatically improves AI's ability to find and follow guidelines during blog migration

**Recent Updates (2025-12-14):**
- **Blog Writing Guidelines Enhancement:**
  - **CRITICAL: Added "NO AI WRITING TRACES" rule**
  - Updated "CULTURAL ADAPTATION & WRITING STYLE" section with detailed guidelines
  - Added specific writing style requirements for each language
  - Emphasized natural, human-like writing without AI patterns

- **Chinese Language Support Documentation:**
  - Added Chinese (Simplified) to "Languages Supported" section
  - **CRITICAL: Added YAML syntax rules for Chinese content**
  - Documented forbidden characters in YAML front matter
  - Added validation command for Chinese posts

**Recent Updates (2025-12-13):**
- **Critical Considerations Enhancement:**
  - Added new prohibition rule #10: "Do NOT create documents or files unless explicitly requested"
  - Clarified that AI should only create content when user specifically asks for it

**Recent Updates (2025-12-12):**
- **Documentation Clarity Improvements:**
  - Fixed inconsistent image numbering rules throughout the document
  - Clarified that `{slug}-01.jpg` serves dual purpose: featured_image + first body image
  - Enhanced "Naming Conventions" table to explicitly show EN/JA/ZH-CN differences

**Recent Updates (2025-12-05):**
- **Tag and Category Management Guidelines:**
  - Added comprehensive tag and category management sections
  - **CRITICAL RULE:** English posts must use English tags/categories, Japanese posts must use Japanese, Chinese posts must use Chinese
  - Added complete mapping tables and conversion scripts

**Update This Document When:**
- Project structure changes significantly
- New workflows are established
- Build/deployment process changes
- New conventions are adopted

---

**End of CLAUDE.md**
