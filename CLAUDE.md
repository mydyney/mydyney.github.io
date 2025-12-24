# CLAUDE.md - AI Assistant Guide

> **Last Updated:** 2025-12-14
> **Project:** Tokyo Mate (Trip Mate News Blog)
> **Site:** https://tripmate.news
> **Type:** Hugo Static Site for GitHub Pages

This document provides comprehensive guidance for AI assistants working on this codebase.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture & Technology Stack](#architecture--technology-stack)
3. [Directory Structure](#directory-structure)
4. [Development Workflows](#development-workflows)
5. [Monetization](#monetization)
6. [Content Management](#content-management)
7. [Key Conventions](#key-conventions)
8. [Common Tasks](#common-tasks)
9. [Important Files](#important-files)
10. [Critical Considerations](#critical-considerations)
11. [Migration Context](#migration-context)

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
│   └── ja/                          # Japanese content
│       ├── _index.md               # Japanese homepage
│       └── posts/                  # Japanese blog posts
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
└── README_IMAGE_DOWNLOAD.md        # Script documentation
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

#### Step 2: User Updates naver.html with Blog Content
```
Claude: "Please update naver.html with the blog HTML content."
User: (Copies HTML from Naver blog and saves to naver.html)
User: "완료했습니다" or "Done"
```

**Instructions for User:**
- Open the Naver blog post in browser
- Copy the HTML content of the blog post
- Save it to `naver.html` in the project root directory
- Confirm completion

#### Step 3: Claude Analyzes and Creates Blog Posts

**Analysis:**
- **Extract publish date from Naver HTML:**
  ```bash
  # Find the publish date in the HTML
  grep -o 'se_publishDate[^>]*>[^<]*' naver.html
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
  * **Verification:**
    - Cross-reference original HTML structure with created Hugo markdown
    - Ensure tables appear at same position as original
    - Ensure image groups maintain original grouping and position
    - Ensure links appear in same context as original
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
    - Search for ALL Naver blog URLs found in original HTML
    - Verify if each Naver post has been migrated to Hugo
  * **Link Conversion Rules (MANDATORY):**
    - **ALL** internal links from the original Naver post MUST be included in the converted post. **DO NOT SKIP ANY LINK.**
    - **If migrated:** Replace Naver URL with Hugo internal link format: `/posts/[slug]/`
    - **If NOT migrated:** You MUST include it as a styled placeholder (see below), maintaining the flow of the original post.
    - **NEVER include raw Naver blog URLs** in the final markdown (unless explicitly instructed for a specific case, but generally use the placeholder).
  * **Placeholder Format for Unmigrated Posts:**
    ```markdown
    <!-- TODO: Add link when migrated - Original: https://blog.naver.com/tokyomate/[POST_ID] -->
    **➡️ [Link Text from Original]**
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
python3 download_naver_images.py naver.html "[slug]"
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
   grep -o '<img' naver.html | wc -l
   
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
   grep -o 'blog.naver.com/tokyomate' naver.html | wc -l
   
   # Count converted links + placeholders in Hugo posts (should match for each language)
   # Count: internal links (/posts/) + TODO placeholders
   grep -E '(/posts/|TODO: Add link)' content/en/posts/[slug].md | wc -l
   grep -E '(/posts/|TODO: Add link)' content/ja/posts/[slug].md | wc -l
   grep -E '(/posts/|TODO: Add link)' content/zh-cn/posts/[slug].md | wc -l
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
claude/claude-md-mi18nf00okdkyuyi-0117EAAGs2ZQwCgzw2nMBTyo
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
- `Redesign Related Posts Section with Modern Compact Sidebar Layout`
- `Add Evangelion 30th Anniversary Blog Post (EN/JA)`
- `Fix Responsive Layout Issues on Mobile Devices`

**PR Description Template:**

```markdown
## Summary
Brief overview of what this PR does (1-2 sentences).

## Changes
### 1. [First Major Change]
- Detail 1
- Detail 2

### 2. [Second Major Change]
- Detail 1
- Detail 2

## Visual Preview (if applicable)
**Before:** Description
**After:** Description

## Testing
✅ Test 1 description
✅ Test 2 description

## Files Changed
- `file/path/1` (new/modified)
- `file/path/2` (new/modified)

## Breaking Changes
None / Description of breaking changes

## Related
Any related issues or context
```

**Best Practices:**

1. **Title:**
   - Use action verbs (Add, Update, Fix, Redesign, Implement)
   - Be specific about what changed
   - Include the benefit or goal
   - Keep under 72 characters if possible

2. **Description:**
   - Start with a clear summary
   - Group changes logically by commit or feature
   - Use checkboxes (✅) for testing/verification items
   - Include visual comparisons for UI changes
   - List all affected files
   - Note any breaking changes explicitly

3. **When to Create PRs:**
   - After completing a feature or fix
   - Before merging to main branch
   - When work is ready for review/deployment
   - Even for solo work (documentation purposes)

4. **GitHub CLI Note:**
   - `gh` CLI is not available in this environment
   - PRs must be created via GitHub web interface
   - Push branch first, then create PR on GitHub

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

**Manual Ad Placement (Optional):**

If you need to manually place ads in specific locations, use the following partials:

1. **In-Article Ads:**
   ```hugo
   {{ partial "adsense-in-article.html" . }}
   ```
   Use this within blog post content for in-article ads.

2. **Display Ads:**
   ```hugo
   {{ partial "adsense-display.html" . }}
   ```
   Use this in layouts for standard display ads.

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

## Content Management

### Creating New Posts

**Recommended Method:**

```bash
# Create new post in English (default)
hugo new content/en/posts/my-new-post.md

# Create new post in Japanese
hugo new content/ja/posts/my-new-post.md
```

**Note:** Korean posts are no longer created. Only English and Japanese versions.

This uses the archetype template at `/archetypes/default.md`.

### Post Front Matter Structure

**Standard YAML Format:**

```yaml
---
title: "Your Post Title"
date: 2025-11-16T10:00:00+09:00
draft: false
categories: ["Category1", "Category2"]
tags: ["tag1", "tag2", "tag3"]
translationKey: "unique-identifier"
description: "SEO meta description"
summary: "Brief summary for listings"
featured_image: "/images/posts/featured.jpg"
---
```

**Required Fields:**
- `title` - Post title
- `date` - Publication date (use Asia/Seoul timezone: +09:00)

**Recommended Fields:**
- `draft` - Set to `false` when ready to publish
- `categories` - For organization
- `tags` - For topical classification
- `translationKey` - **REQUIRED for multilingual posts** (same key across languages)
- `description` - For SEO
- `summary` - For post listings

**⚠️ CRITICAL: YAML Syntax Rules for Chinese Content**

When creating Chinese (Simplified) blog posts, **NEVER** use the following characters inside YAML quoted strings:

❌ **FORBIDDEN in YAML front matter:**
- Chinese corner brackets: `「` `」` (U+300C, U+300D)
- Chinese quotation marks: `"` `"` (U+201C, U+201D)
- Chinese single quotes: `'` `'` (U+2018, U+2019)

✅ **ALLOWED alternatives:**
- Use plain text without special quotes in front matter
- Or use standard ASCII quotes: `"` (U+0022) and `'` (U+0027)

**Examples:**

```yaml
# ❌ WRONG - Will cause Hugo build failure
title: "東京「浪花家」完全攻略"
description: "在百年老店「浪花家」品嘗鯛魚燒"

# ✅ CORRECT - Safe for YAML parsing
title: "東京浪花家完全攻略"
description: "在百年老店浪花家品嘗鯛魚燒"
```

**Why this matters:**
- Chinese corner brackets `「」` inside YAML quoted strings break YAML parser
- Hugo cannot parse the front matter and skips the entire post
- Results in missing content on the website
- **All 86 Chinese posts must follow this rule**

**Validation:**
After creating Chinese posts, validate YAML with:
```bash
python3 -c "import yaml; yaml.safe_load(open('content/zh-cn/posts/[file].md').read().split('---')[1])"
```

### Multilingual Content

**Creating Linked Translations:**

1. Create post in **English, Japanese, and Chinese (Simplified)** with **identical `translationKey`**
2. Use same date across all versions
3. Place in respective language directories (`content/en/`, `content/ja/`, `content/zh-cn/`)

**Example:**

```yaml
# content/en/posts/tokyo-guide.md
---
title: "Tokyo Guide"
translationKey: "tokyo-guide-2025"
---

# content/ja/posts/tokyo-guide.md
---
title: "東京ガイド"
translationKey: "tokyo-guide-2025"
---

# content/zh-cn/posts/tokyo-guide.md
---
title: "东京旅游指南"
translationKey: "tokyo-guide-2025"
---
```

**Language Switcher:** Hugo will automatically show language switcher when posts share `translationKey`.

**Note:** Korean language support has been removed. Create English, Japanese, and Chinese (Simplified) versions.

### Tag Management and Multilingual Tags

**⚠️ CRITICAL RULE: Tags Must Match Content Language**

When creating or editing blog posts, **ALWAYS** ensure tags match the language of the post content:

- ✅ **English posts** (`content/en/posts/`) → **English tags only**
- ✅ **Japanese posts** (`content/ja/posts/`) → **Japanese tags only**
- ❌ **NEVER mix languages** in tags within a single post

**Why This Matters:**
- **SEO:** Search engines prefer language consistency
- **UX:** Users expect tags in the same language as the content
- **Discoverability:** Language-appropriate tags improve content discovery

**Examples:**

```yaml
# ✅ CORRECT - English post with English tags
# content/en/posts/toranomon-hills-complete-guide.md
---
title: "Tokyo Toranomon Hills 2025 Complete Guide"
tags: ["toranomon-hills", "tokyo-observatory", "tokyo-restaurants", "izakaya", "t-market"]
---

# ✅ CORRECT - Japanese post with Japanese tags
# content/ja/posts/toranomon-hills-complete-guide.md
---
title: "東京虎ノ門ヒルズ2025完全ガイド"
tags: ["虎ノ門ヒルズ", "東京展望台", "東京レストラン", "居酒屋", "Tマーケット"]
---

# ❌ WRONG - Japanese post with English tags
# content/ja/posts/toranomon-hills-complete-guide.md
---
title: "東京虎ノ門ヒルズ2025完全ガイド"
tags: ["toranomon-hills", "tokyo-observatory", "tokyo-restaurants"]  # ← ERROR!
---
```

### English-Japanese Tag Mapping

When creating new posts or converting existing content, use this mapping to ensure consistency across languages:

| English Tag | Japanese Tag | Category |
|-------------|--------------|----------|
| `andaz-hotel` | `アンダーズホテル` | Hotels |
| `anime-merchandise` | `アニメグッズ` | Shopping |
| `azabudai-hills` | `麻布台ヒルズ` | Locations |
| `azabujuban` | `麻布十番` | Locations |
| `business-district` | `ビジネス街` | Areas |
| `cash-only` | `現金のみ` | Payment |
| `cosplay` | `コスプレ` | Culture |
| `disneyland` | `ディズニーランド` | Attractions |
| `family-events` | `家族イベント` | Events |
| `gacha` | `ガチャ` | Entertainment |
| `gashapon` | `ガシャポン` | Entertainment |
| `halloween` | `ハロウィン` | Events |
| `ikebukuro` | `池袋` | Locations |
| `izakaya` | `居酒屋` | Dining |
| `kabukicho` | `歌舞伎町` | Locations |
| `michelin` | `ミシュラン` | Dining |
| `observation-deck` | `展望台` | Attractions |
| `pasmo` | `パスモ` | Transportation |
| `shibuya` | `渋谷` | Locations |
| `shinjuku` | `新宿` | Locations |
| `sky-room-cafe` | `スカイルームカフェ` | Dining |
| `solamachi` | `ソラマチ` | Shopping |
| `suica` | `スイカ` | Transportation |
| `sweets` | `スイーツ` | Food |
| `t-market` | `Tマーケット` | Shopping |
| `taiyaki` | `たい焼き` | Food |
| `teamlab-borderless` | `チームラボボーダレス` | Attractions |
| `ticket-discount` | `チケット割引` | Travel Tips |
| `tokyo` | `東京` | Locations |
| `tokyo-attractions` | `東京観光` | Travel |
| `tokyo-festivals` | `東京祭り` | Events |
| `tokyo-guide` | `東京ガイド` | Travel |
| `tokyo-node` | `東京ノード` | Locations |
| `tokyo-observatory` | `東京展望台` | Attractions |
| `tokyo-restaurants` | `東京レストラン` | Dining |
| `tokyo-shopping` | `東京ショッピング` | Shopping |
| `tokyo-skytree` | `東京スカイツリー` | Attractions |
| `tokyo-tower-view` | `東京タワービュー` | Views |
| `toranomon-hills` | `虎ノ門ヒルズ` | Locations |
| `traditional-food` | `和食` | Food |
| `transportation` | `交通` | Travel |
| `travel-tips` | `旅行情報` | Travel |
| `2025` | `2025` | Years (keep as-is) |

**Tag Naming Conventions:**

- **English tags:** Use `kebab-case` (lowercase with hyphens)
  - ✅ `tokyo-restaurants`, `christmas-market`, `travel-tips`
  - ❌ `Tokyo_Restaurants`, `ChristmasMarket`, `Travel Tips`

- **Japanese tags:** Use natural Japanese text (hiragana, katakana, kanji)
  - ✅ `東京レストラン`, `クリスマスマーケット`, `旅行情報`
  - ❌ No special formatting needed

- **Proper nouns/Brand names:** Keep original form in both languages
  - English: `t-market`, `tokyo-node`, `teamlab-borderless`
  - Japanese: `Tマーケット`, `東京ノード`, `チームラボボーダレス`

- **Numbers/Years:** Keep as-is in both languages
  - Both: `2025`, `2026`

**Updating the Tag Mapping:**

When you create a new tag that doesn't exist in the mapping above:

1. **Add both English and Japanese versions** to the table above
2. **Maintain alphabetical order** by English tag
3. **Include category** for better organization
4. **Update the conversion script** (`convert_tags_to_japanese.py`) with the new mapping:

```python
TAG_MAPPING = {
    # ... existing mappings ...
    "new-english-tag": "新しい日本語タグ",  # Add here
    # ... rest of mappings ...
}
```

5. **Document the update** in your commit message:
```bash
git commit -m "docs: Add new tag mapping for [tag-name]

Added English-Japanese tag mapping:
- English: new-english-tag
- Japanese: 新しい日本語タグ
- Category: [category-name]"
```

**Bulk Tag Conversion:**

If you need to convert multiple posts at once, use the provided utility script:

```bash
# Convert all English tags to Japanese in Japanese posts
python3 convert_tags_to_japanese.py

# The script will:
# 1. Scan all files in content/ja/posts/
# 2. Replace English tags with Japanese equivalents
# 3. Preserve tags already in Japanese
# 4. Report number of files processed
```

**Verification:**

Before committing tag changes, verify consistency:

```bash
# Check English posts have English tags
grep "^tags:" content/en/posts/*.md | head -5

# Check Japanese posts have Japanese tags
grep "^tags:" content/ja/posts/*.md | head -5

# Look for mixed language tags (should return nothing)
grep "^tags:" content/ja/posts/*.md | grep -E "[a-z]+-[a-z]+"
```

### Category Management and Multilingual Categories

**⚠️ CRITICAL RULE: Categories Must Match Content Language**

Just like tags, categories must match the language of the post content:

- ✅ **English posts** (`content/en/posts/`) → **English categories only**
- ✅ **Japanese posts** (`content/ja/posts/`) → **Japanese categories only**
- ❌ **NEVER mix languages** in categories within a single post

**Examples:**

```yaml
# ✅ CORRECT - English post with English categories
# content/en/posts/tokyo-guide.md
---
title: "Tokyo Travel Guide 2025"
categories: ["Travel Guide"]
---

# ✅ CORRECT - Japanese post with Japanese categories
# content/ja/posts/tokyo-guide.md
---
title: "東京旅行ガイド2025"
categories: ["旅行ガイド"]
---

# ❌ WRONG - Japanese post with English categories
# content/ja/posts/tokyo-guide.md
---
title: "東京旅行ガイド2025"
categories: ["Travel Guide"]  # ← ERROR!
---
```

### English-Japanese Category Mapping

When creating new posts, use this mapping to ensure category consistency:

| English Category | Japanese Category | Usage |
|------------------|-------------------|-------|
| `Travel Guide` | `旅行ガイド` | General travel guides |
| `Travel Info` | `旅行情報` | Travel information and tips |
| `Travel` | `旅行` | General travel content |
| `Tokyo Travel Guide` | `東京旅行ガイド` | Tokyo-specific guides |
| `Tokyo Travel Info` | `東京旅行情報` | Tokyo travel information |
| `Tokyo Itinerary` | `東京旅行プラン` | Tokyo trip planning |
| `Tokyo Sightseeing` | `東京観光` | Tokyo sightseeing spots |
| `Tokyo Attractions` | `東京観光スポット` | Tokyo attractions |
| `Restaurants` | `レストラン` | Restaurant content |
| `Food & Dining` | `グルメ` | Food and dining |
| `Food Guide` | `グルメガイド` | Food guides |
| `Tokyo Food` | `東京グルメ` | Tokyo food content |
| `Restaurant Reviews` | `レストランレビュー` | Restaurant reviews |
| `Shopping` | `ショッピング` | Shopping content |
| `Shopping & Guides` | `ショッピング・ガイド` | Shopping guides |
| `Tokyo Shopping` | `東京ショッピング` | Tokyo shopping |
| `Events` | `イベント` | Events |
| `Events & Festivals` | `イベント・フェスティバル` | Events and festivals |
| `Tokyo Events` | `東京イベント` | Tokyo events |
| `Festival Calendar` | `イベントカレンダー` | Festival calendars |
| `Festival Guide` | `フェスティバルガイド` | Festival guides |
| `Transportation` | `交通` | Transportation guides |
| `Disneyland` | `ディズニーランド` | Disneyland content |
| `Christmas` | `クリスマス` | Christmas events |
| `Shinjuku` | `新宿` | Shinjuku area |
| `Shinjuku/Shin-Okubo` | `新宿・新大久保` | Shinjuku/Shin-Okubo area |
| `Shibuya & Harajuku` | `渋谷・原宿` | Shibuya/Harajuku area |
| `Roppongi/Hiroo` | `六本木・広尾` | Roppongi/Hiroo area |
| `Meguro & Ebisu` | `目黒・恵比寿` | Meguro/Ebisu area |
| `Shinbashi/Shiodome` | `新橋・汐留` | Shinbashi/Shiodome area |
| `Yokohama` | `横浜` | Yokohama area |
| `Yokohama & Kamakura` | `横浜・鎌倉` | Yokohama/Kamakura area |
| `Narita Airport` | `成田空港` | Narita Airport |
| `Omotesando` | `表参道` | Omotesando area |
| `Ebisu` | `恵比寿` | Ebisu area |
| `Autumn in Tokyo` | `東京の秋` | Autumn in Tokyo |

**Category Best Practices:**

1. **Keep categories broad** - Use 1-2 categories per post
2. **Use specific area tags** - For location-specific content, use area names as tags instead of categories
3. **Consistency** - Stick to the mapping above for consistency across the site
4. **Update the mapping** - When adding new categories, update both this table and the conversion script

**Bulk Category Conversion:**

Use the provided utility script to convert categories:

```bash
# Convert all English categories to Japanese in Japanese posts
python3 convert_categories_to_japanese.py

# The script will:
# 1. Scan all files in content/ja/posts/
# 2. Replace English categories with Japanese equivalents
# 3. Preserve categories already in Japanese
# 4. Report number of files processed
```

**Verification:**

Before committing category changes, verify consistency:

```bash
# Check English posts have English categories
grep "^categories:" content/en/posts/*.md | head -5

# Check Japanese posts have Japanese categories
grep "^categories:" content/ja/posts/*.md | head -5

# Look for mixed language categories (should return nothing)
grep "^categories:" content/ja/posts/*.md | grep -E '"[A-Z][a-z]'
```

### SEO-Optimized Content Conversion (Korean → EN/JA)

When converting Korean Naver blog posts to English and Japanese, follow these SEO optimization guidelines:

#### 1. Title Optimization

**English Titles:**
- Length: **50-80 characters** (key info in first 55 chars for Google SERP display)
- Include primary keyword near the beginning (within first 50 chars)
- Use power words: "Complete Guide", "Best", "Top", "2025", etc.
- Format: `[Primary Keyword]: [Benefit/Detail] | [Year/Location]`
- Longer titles OK if main keyword is front-loaded

**Japanese Titles:**
- Length: **35-55 characters** (key info in first 35 chars)
- Include primary keyword (in Japanese) near the beginning
- Use engaging suffixes: `完全ガイド`, `徹底解説`, `おすすめ`, `まとめ`
- Format: `【場所/イベント】[キーワード]の[ベネフィット]` or `[場所][キーワード]完全ガイド`

**Examples:**
```yaml
# English (74 chars - OK because key info "Roppongi Christmas Illumination 2025" is in first 40)
title: "Roppongi Christmas Illumination 2025: Complete Guide to Tokyo's Best Light Display"

# Japanese (42 chars - OK because key info "六本木イルミネーション2025" is in first 20)
title: "六本木イルミネーション2025完全ガイド - 点灯時間、クリスマスマーケット"
```

#### 2. Meta Description Optimization

**English Description:**
- Length: **150-180 characters** (Google displays ~155-160, but longer is OK)
- Include primary + secondary keywords naturally
- Add call-to-action or value proposition
- Mention location (Tokyo, Japan) for local SEO
- Front-load important info within first 150 chars

**Japanese Description:**
- Length: **100-140 characters**
- Include relevant Japanese keywords
- Natural, engaging tone
- End with appeal: `必見です`, `チェック`, `おすすめ`, `完全ガイド`
- Front-load key info within first 100 chars

**Examples:**
```yaml
# English (168 chars)
description: "Complete guide to Roppongi Christmas Illumination 2025 in Tokyo. Dates, hours, best photo spots, access info, and insider tips for the perfect winter visit."

# Japanese (125 chars)
description: "六本木クリスマスイルミネーション2025の完全ガイド。開催期間、点灯時間、撮影スポット、アクセス情報を徹底解説。冬の東京観光に必見です。"
```

#### 3. URL Slug Optimization

**Rules:**
- Use **English keywords only** (even for Japanese posts)
- Lowercase, hyphen-separated
- Include primary keyword + location/year if relevant
- Keep under 60 characters
- Avoid stop words (the, a, an, of, etc.)

**Examples:**
```
✅ Good: roppongi-christmas-illumination-2025
✅ Good: shinjuku-gyoen-autumn-guide
✅ Good: tokyo-ramen-street-best-shops

❌ Bad: the-best-roppongi-christmas-illumination-of-2025
❌ Bad: 六本木イルミネーション (Japanese characters)
❌ Bad: roppongi_christmas_illumination (underscores)
```

#### 4. Heading Structure (H2/H3)

**SEO Heading Rules:**
- **H1**: Title only (automatically from front matter)
- **H2**: Main sections with keywords
- **H3**: Subsections for detailed topics
- Include keywords naturally in H2 headings

**English H2 Examples:**
```html
<h2>📍 Location & Access Information</h2>
<h2>🎄 2025 Event Schedule & Hours</h2>
<h2>📸 Best Photo Spots</h2>
<h2>🍽️ Nearby Restaurants & Cafes</h2>
<h2>💡 Insider Tips for Your Visit</h2>
```

**Japanese H2 Examples:**
```html
<h2>📍 アクセス・場所情報</h2>
<h2>🎄 2025年開催スケジュール</h2>
<h2>📸 おすすめ撮影スポット</h2>
<h2>🍽️ 周辺グルメ・カフェ情報</h2>
<h2>💡 訪問のコツ・注意点</h2>
```

#### 5. Image Alt Text Optimization

**Rules:**
- Describe the image content clearly
- Include relevant keywords naturally
- Language-specific alt text (EN for English posts, JA for Japanese)
- Max 125 characters

**Format:** `[Subject] [Action/State] [Location/Context]`

**Examples:**
```html
<!-- English -->
<img src="..." alt="Roppongi Hills Christmas illumination display with giant Christmas tree at night">
<img src="..." alt="Tokyo Skytree Christmas market food stalls with visitors">

<!-- Japanese -->
<img src="..." alt="六本木ヒルズのクリスマスイルミネーション、巨大ツリーの夜景">
<img src="..." alt="東京スカイツリーのクリスマスマーケット、屋台と来場者">
```

#### 6. Keyword Strategy by Language

**English Keywords Focus:**
- "Tokyo [topic] guide"
- "[Location] travel tips"
- "Best [topic] in Tokyo"
- "[Event] 2025 dates hours"
- "Japan travel [topic]"

**Japanese Keywords Focus:**
- 「東京 [トピック] おすすめ」
- 「[場所] 観光 ガイド」
- 「[イベント] 2025 日程」
- 「[場所] アクセス 行き方」
- 「[トピック] 完全ガイド」

#### 7. Content Structure for SEO

**Recommended Structure:**
1. **Intro** (100-150 words) - Hook + what reader will learn
2. **Key Info Box** - Dates, hours, location, admission (quick reference)
3. **Main Content** - H2 sections with images
4. **Practical Info** - Access, tips, nearby attractions
5. **Map Embed** - Google Maps for location
6. **Related Posts** - Internal links (auto-generated)

**Internal Linking:**
- Link to related posts using mapped Hugo URLs
- Use descriptive anchor text (not "click here")
- 2-3 internal links per 1000 words

#### 8. SEO Checklist for Each Post

Before finalizing any converted post, verify:

```
□ Title: EN 50-80 chars (key info in first 55) / JA 35-55 chars (key info in first 35)
□ Description: EN 150-180 chars / JA 100-140 chars with keyword front-loaded
□ Slug: English, keyword-rich, under 60 chars
□ H2 headings: Include keywords, use emojis for visual appeal
□ Images: All have descriptive alt text in target language
□ featured_image: Set for social media preview
□ translationKey: Identical across EN/JA versions
□ Tags: 5-7 relevant tags per post
□ Categories: 1-2 appropriate categories
□ Internal links: Link to related posts where relevant
```

### Images

**Naming Convention:**
```
{post-slug}-{number}.{ext}
```

**Examples:**
```
kirimugiya-jinroku-shinjuku-01.jpg
kirimugiya-jinroku-shinjuku-02.jpg
tokyo-ramen-street-01.jpg
tokyo-ramen-street-02.jpg
```

**⚠️ Image Format:**
- **Always use `.jpg` extension** for all blog post images
- The `download_naver_images.py` script saves all images as `.jpg`
- Use `.jpg` for consistency and optimal web performance

**📊 Image Numbering Structure (1:1 Matching):**
- **`{slug}-01.jpg`**: First image (used in both `featured_image` field AND first `<figure>` in body)
  - Serves dual purpose: social media preview + first visible image
- **`{slug}-02.jpg` and up**: Subsequent images in sequential order
  - `02.jpg`: Second image in post
  - `03.jpg`, `04.jpg`, etc.: Following images in order

**⚠️ CRITICAL: 1:1 Matching Rule**
- Naver HTML image count = Hugo markdown image count (exact match)
- If Naver has 22 images → Hugo must have 22 images (01.jpg through 22.jpg)
- **No separate counting** for featured vs body images anymore
- `featured_image` field uses the same 01.jpg that appears as first `<figure>` in body

**Example:**
```yaml
# Front Matter
featured_image: "/images/posts/tokyo-guide-01.jpg"  # Social media preview

# Body (after intro paragraph)
<figure>
  <img src="/images/posts/tokyo-guide-01.jpg" alt="...">  # Same image as featured
</figure>
<figure>
  <img src="/images/posts/tokyo-guide-02.jpg" alt="...">  # Second image
</figure>
<figure>
  <img src="/images/posts/tokyo-guide-03.jpg" alt="...">  # Third image
</figure>
```

**💡 Important:**
- Total images in Hugo = Total images in Naver HTML (1:1)
- If post has 22 images in Naver, create 22 `<figure>` tags in Hugo (01.jpg through 22.jpg)
- Featured_image field and first body image use the **same** 01.jpg file

**Storage Location:**
```
/static/images/posts/
```

**Referencing in Markdown:**
```markdown
![Alt text](/images/posts/your-image-02.jpg)
```

**Image Migration from Naver Blog:**

```bash
# Use the custom Python script
python3 download_naver_images.py <HTML_FILE> <POST_SLUG>

# Example:
python3 download_naver_images.py naver_blog.html tokyo-restaurant-guide
```

See `README_IMAGE_DOWNLOAD.md` for detailed instructions.

### Blog Post Format

**Standard Structure:**

All blog posts must follow this consistent format:

1. **Front Matter** (YAML)
2. **Opening `<div class="blog-container">`**
3. **Intro Paragraph** (centered, styled)
4. **First Body Image** (with `<figure>` tag, using `{slug}-01.jpg` - same as featured_image)
5. **Content** (sections with headings, images, info boxes, tables)
6. **Closing `</div>`**

**Required Front Matter:**
```yaml
---
title: "Post Title"
date: 2025-11-15T08:00:00+09:00
draft: false
translationKey: "unique-post-identifier"
description: "SEO meta description for social media preview"
summary: "Brief summary for post listings"
tags: ["tag1", "tag2", "tag3"]
categories: ["Category"]
featured_image: "/images/posts/post-slug-01.jpg"  # For social media/meta tags
---
```

**Intro Paragraph Format:**
```html
<div class="blog-container">

<p style="text-align: center; font-size: 1.1rem; color: #555;">🎄 Main intro text!<br>
Second line of intro,<br>
Third line with more details,<br>
Final line wrapping up intro.</p>
```

**Image Format (Using `<figure>` Tags):**

**Single Images:**
```html
<figure>
  <img src="/images/posts/post-slug-02.jpg" alt="Descriptive alt text">
  <figcaption style="font-size: 0.7em; text-align: center;">Image caption</figcaption>
</figure>
```

**Grouped Images (2, 3, or 4 images side-by-side):**

When Naver HTML contains image groups (e.g., `se-imageGroup-col-2`), use HTML containers with CSS Grid layout. **Do NOT use Markdown for these.**

```html
<!-- 2 images side-by-side -->
<div class="image-group-2">
  <figure>
    <img src="/images/posts/post-slug-10.jpg" alt="First image">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-11.jpg" alt="Second image">
  </figure>
  <figcaption style="font-size: 0.85em; text-align: center;">Caption for both images</figcaption>
</div>

<!-- 3 images side-by-side -->
<div class="image-group-3">
  <figure>
    <img src="/images/posts/post-slug-12.jpg" alt="First image">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-13.jpg" alt="Second image">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-14.jpg" alt="Third image">
  </figure>
  <figcaption style="font-size: 0.85em; text-align: center;">Caption for all three images</figcaption>
</div>

<!-- 4 images in 2x2 tile layout -->
<div class="image-group-4">
  <figure>
    <img src="/images/posts/post-slug-15.jpg" alt="...">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-16.jpg" alt="...">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-17.jpg" alt="...">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-18.jpg" alt="...">
  </figure>
  <figcaption style="font-size: 0.85em; text-align: center;">Caption for all four images</figcaption>
</div>
```

**Important Notes:**
- ✅ Every image, whether single or in a group, MUST be in its own `<figure>` tag.
- ✅ All figcaptions MUST use inline style: `style="font-size: 0.85em; text-align: center;"`
- ✅ For image groups, the figcaption goes OUTSIDE the individual `<figure>` tags but inside the `image-group-X` div.
- ✅ CSS Grid layout (predefined in CSS):
  - **2 images**: Side-by-side
  - **3 images**: Three in a row
  - **4 images**: 2x2 tile layout
- ✅ Mobile: All groups automatically switch to an appropriate responsive layout.

**Aesthetic Standards for Image Groups (Perfect Fit):**
- **Grid Alignment:** All images in an `image-group-X` must align perfectly along their edges.
- **Aspect Ratio:** All figures within a group share a uniform aspect ratio (enforced via CSS) to ensure even row heights (Square `1/1` for 2/4/9 groups, `4/3` for 3-groups).
- **Filling the Cell:** Always use `object-fit: cover` and `height: 100%` on images within groups to ensure they completely fill the grid cell without leaving white space or gaps.
- **Handling Mixed Dimensions:** When landscape and portrait images are mixed in a group, they MUST be cropped to the shared aspect ratio of the grid row to maintain alignment. This is handled by the `image-group-X` CSS.

**Google Maps Embed (Location Information):**

When a blog post includes a location (restaurant, attraction, etc.), add an interactive Google Maps embed with language-specific settings:

```html
<!-- English Version -->
<div style="margin: 2rem 0;">
  <iframe src="https://www.google.com/maps?q=LATITUDE,LONGITUDE&hl=en&z=17&output=embed"
          width="100%" height="400"
          style="border:0; border-radius:8px;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"></iframe>
  <p style="text-align:center; margin-top:0.5rem; font-size:0.9rem; color:#666;">
    <strong>Location Name</strong><br>
    Full Address in English<br>
    <a href="https://www.google.com/maps/place/Location+Name/@LATITUDE,LONGITUDE,17z?hl=en"
       target="_blank"
       style="color:#667eea;">View on Google Maps</a>
  </p>
</div>

<!-- Japanese Version -->
<div style="margin: 2rem 0;">
  <iframe src="https://www.google.com/maps?q=LATITUDE,LONGITUDE&hl=ja&z=17&output=embed"
          width="100%" height="400"
          style="border:0; border-radius:8px;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"></iframe>
  <p style="text-align:center; margin-top:0.5rem; font-size:0.9rem; color:#666;">
    <strong>場所名</strong><br>
    日本語の住所<br>
    <a href="https://www.google.com/maps/place/Location+Name/@LATITUDE,LONGITUDE,17z?hl=ja"
       target="_blank"
       style="color:#667eea;">Googleマップで見る</a>
  </p>
</div>
```

**Google Maps Parameters:**
- `q=LATITUDE,LONGITUDE` - Map coordinates
- `hl=en` or `hl=ja` - Interface language (English/Japanese)
- `z=17` - Zoom level (17 is good for detailed street view)
- `output=embed` - Embed mode for iframe

**Important Notes:**
- ✅ Always use language-specific `hl` parameter (en/ja)
- ✅ Include direct Google Maps link for full-screen view
- ✅ Use consistent styling (border-radius, height 400px)
- ✅ Add location name and address below the map
- 🗺️ Get coordinates from Google Maps by right-clicking on location

**Common CSS File:**
All blog posts share common styles through `/static/css/blog-post-common.css`.

**Available CSS Classes:**
```css
.blog-container        /* Main container for blog post content */
.blog-container h2     /* Section headings with blue underline */
.blog-container img    /* Images with rounded corners and shadow */
.info-box              /* Purple gradient info box */
.schedule-table        /* Styled table for schedules */
.tip-box               /* Yellow tip/warning box */
blockquote             /* Blue left-border quotations */

/* Image Group Layout (CSS Grid) */
.image-group-2         /* 2 images side-by-side (45% max-width) */
.image-group-3         /* 3 images in a row (45% max-width) */
.image-group-4         /* 4 images in 2x2 tile (50% max-width) */
```

**CSS Grid Image Groups:**
- Uses CSS Grid for flexible layout on desktop
- Automatically switches to single column on mobile (< 768px)
- Compact sizing for better visual balance:
  - **2 images**: Side-by-side, 45% max-width
  - **3 images**: Three in a row, 45% max-width
  - **4 images**: 2x2 tile layout (top 2, bottom 2), 50% max-width
- Centered with `margin: 2rem auto`
- Preserves aspect ratios with `height: auto`
- Gap between images: 1rem

**Complete Example:**
```html
---
title: "Tokyo Guide 2025"
date: 2025-11-15T10:00:00+09:00
draft: false
translationKey: "tokyo-guide-2025"
description: "Complete guide to Tokyo 2025 travel"
summary: "Complete guide to Tokyo 2025 travel"
tags: ["tokyo", "travel", "guide"]
categories: ["Travel Info"]
featured_image: "/images/posts/tokyo-guide-01.jpg"
---

<div class="blog-container">

<p style="text-align: center; font-size: 1.1rem; color: #555;">🗼 Tokyo Travel Guide 2025!<br>
Everything you need to know,<br>
From attractions to restaurants,<br>
Complete information at a glance.</p>

<figure>
  <img src="/images/posts/tokyo-guide-02.jpg" alt="Tokyo cityscape">
  <figcaption style="font-size: 0.7em; text-align: center;">Tokyo cityscape</figcaption>
</figure>

<p>Introduction paragraph...</p>

<h2>Section Title</h2>

<figure>
  <img src="/images/posts/tokyo-guide-03.jpg" alt="Another image">
  <figcaption style="font-size: 0.7em; text-align: center;">Image description</figcaption>
</figure>

<!-- Example of grouped images (2 side-by-side) -->
<div class="image-group-2">
  <figure>
    <img src="/images/posts/tokyo-guide-04.jpg" alt="First image">
  </figure>
  <figure>
    <img src="/images/posts/tokyo-guide-05.jpg" alt="Second image">
  </figure>
  <figcaption style="font-size: 0.7em; text-align: center;">Caption for both images</figcaption>
</div>

<div class="info-box">
  <ul>
    <li><strong>Info 1:</strong> Details</li>
    <li><strong>Info 2:</strong> More details</li>
  </ul>
</div>

<table class="schedule-table">
  <thead>
    <tr><th>Column 1</th><th>Column 2</th></tr>
  </thead>
  <tbody>
    <tr><td>Data 1</td><td>Data 2</td></tr>
  </tbody>
</table>

<div class="tip-box">
  <p><strong>Tip:</strong> Helpful information here</p>
</div>

</div>
```

**Important Notes:**
- ✅ DO use common CSS classes from `blog-post-common.css`
- ❌ DO NOT add inline `<style>` blocks in posts (except for figcaption styling)
- ✅ Wrap content in `<div class="blog-container">` for consistent styling
- ✅ ALL figcaptions MUST have inline style: `style="font-size: 0.7em; text-align: center;"`
- ✅ Use `.image-group-2/3/4` classes for side-by-side image layouts
- 🎨 CSS is automatically loaded via `layouts/partials/head-additions.html`

**CSS Files:**
- `/static/css/blog-cards.css` - Blog card styles (list pages)
- `/static/css/blog-post-common.css` - Blog post content styles
- `/static/css/related-posts.css` - Related posts sidebar styles
- All three are loaded globally via `head-additions.html`

### Related Posts

**Overview:**
The site features a modern related posts section that appears in the sidebar of individual blog posts. It automatically displays up to 6 related posts based on Hugo's built-in content relations (tags, categories, etc.).

**Design:**
- **Layout:** Compact horizontal cards (thumbnail left, content right)
- **Responsive:** Single column layout optimized for sidebar width
- **Visual:** Purple-blue gradient theme with smooth animations
- **Hover Effect:** Slides right with color transition

**Components:**
- **Thumbnail:** 80px × 80px on desktop, 70px × 70px on mobile
- **Title:** 2-line truncated post title
- **Metadata:** Publication date (tags hidden to save space)
- **Placeholder:** Gradient background with SVG icon for posts without images

**Implementation:**
```
layouts/partials/menu-contextual.html  # Custom partial (overrides theme)
static/css/related-posts.css           # Styling
```

**Customization:**
To change the number of related posts, edit `menu-contextual.html` line 18:
```go
{{ $related := .Site.RegularPages.Related . | collections.First 6 }}
```
Change `6` to desired number.

**Features:**
- ✅ Automatic content matching via Hugo's Related Content feature
- ✅ Featured image support with fallback placeholder
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Dark mode support (auto-detects user preference)
- ✅ Staggered fade-in animation on load
- ✅ Optimized for narrow sidebar layout

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
| Tags (EN) | kebab-case | `["tokyo-restaurants", "travel-tips"]` |
| Tags (JA) | Natural Japanese | `["東京レストラン", "旅行情報"]` |

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
- For new styles, add to `blog-post-common.css` for reusability

**Commit Messages:**
- Use descriptive messages
- Mix of English/Korean is acceptable
- Include context (e.g., "Add images for [post-name]")

---

## Common Tasks

### 1. Adding a New Blog Post

**NOTE:** Blog posts are created from Korean Naver HTML. AI translates to English and Japanese only.

```bash
# 1. Create post in English and Japanese ONLY
hugo new content/en/posts/my-post.md
hugo new content/ja/posts/my-post.md

# 2. Edit each file:
#    - Add same translationKey to both
#    - Fill in content
#    - Set draft: false when ready

# 3. Add images (if needed)
#    - Save to /static/images/posts/
#    - Use naming: my-post-01.jpg, my-post-02.jpg, etc.

# 4. Test locally
hugo server -D

# 5. Commit and push
git add .
git commit -m "Add new blog post: My Post"
git push -u origin <your-branch>

# 6. Create PR to main branch
```

### 2. Migrating Content from Naver Blog

**Complete Workflow:**

```bash
# STEP 1: Fetch Naver Blog Content
# User provides Naver blog URL
python3 fetch_content.py "https://blog.naver.com/tokyomate/[POST_ID]"
# Output: naver.html

# STEP 2: Analyze HTML & Check LINK_MAPPING.md
# - Count images (including grouped images)
# - Load LINK_MAPPING.md to check internal links
# - Verify slugs in 'declare -A MAPPINGS' array
# - Add new slugs if needed

# STEP 3: Create Blog Posts (EN/JA)
# Following CLAUDE.md guidelines:
# - Analyze Naver HTML structure
# - Create content/en/posts/[slug].md (English version)
# - Create content/ja/posts/[slug].md (Japanese version)
# - Use # placeholders for unmapped internal links with TODO comments
# - Include Naver link and intended slug in TODO comments
# Format: <!-- TODO: Update link after migration
#              Naver: https://blog.naver.com/tokyomate/[ID]
#              Hugo: /posts/[slug]/ -->
#         <a href="#">Link Text</a>

# STEP 4: Update LINK_MAPPING.md
# A. Add to Quick Reference Table
#    | [NAVER_ID] | [slug] | [DATE] | ✅ |
#
# B. Add to MAPPINGS array (if not exists)
#    ["[NAVER_ID]"]="[slug]"
#
# C. Update Pending Link References
#    - Mark migrated post as MIGRATED
#    - Add new unmapped links to pending table

# STEP 5: Download Images
python3 download_naver_images.py naver.html "[slug]"
# Downloads all images to static/images/posts/[slug]-01.jpg, 02.jpg, etc.

# STEP 6: Local Preview
# Provide user with local preview links:
# - http://localhost:1313/posts/[slug]/
# - http://localhost:1313/ja/posts/[slug]/

# STEP 7: User Confirmation
# Wait for user to review and approve ("OK")

# STEP 8: Git Deployment
git add content/en/posts/[slug].md content/ja/posts/[slug].md \
        static/images/posts/[slug]-*.jpg LINK_MAPPING.md
git commit -m "Add [Title] (EN/JA)

- Created comprehensive guide covering [topics]
- Added [N] images
- Updated LINK_MAPPING.md with new slug and pending references

Naver ID: [NAVER_ID]
Slug: [slug]"
git push

# STEP 9: Update Existing Posts with New Links
# After deployment, update all posts that referenced this Naver ID
# Find all posts with TODO placeholders for this Naver ID
grep -l "[NAVER_ID]" content/en/posts/*.md content/ja/posts/*.md

# Replace TODO placeholders with live links
# English posts: href="#" → href="/posts/[slug]/"
# Japanese posts: href="#" → href="/ja/posts/[slug]/"

# Example Python script:
python3 << 'EOF'
import re, os

naver_id = "[NAVER_ID]"
en_slug = "/posts/[slug]/"
ja_slug = "/ja/posts/[slug]/"

# Update English files
for file in ["content/en/posts/*.md"]:
    content = open(file).read()
    # Replace TODO + placeholder with live link
    content = re.sub(
        r'<!-- TODO:.*?' + naver_id + r'.*?-->\s*<a href="#"([^>]*)>([^<]+)</a>',
        r'<a href="' + en_slug + r'"\1>\2</a>',
        content, flags=re.DOTALL
    )
    open(file, 'w').write(content)

# Update Japanese files (same pattern with ja_slug)
EOF

# STEP 10: Commit Link Updates
git add content/en/posts/*.md content/ja/posts/*.md
git commit -m "Update internal links to [Title] in existing posts

- Replaced TODO placeholders with live links
- Updated [N] English posts
- Updated [N] Japanese posts

Naver ID: [NAVER_ID] → [slug]"
git push
```

**Key Points:**

1. **Always create both EN and JA versions** - No Korean
2. **Use TODO placeholders** for unmapped links with Naver ID and intended slug
3. **Update LINK_MAPPING.md** in 3 places: QRT, MAPPINGS, Pending References
4. **Download images** using the provided script
5. **Get user approval** before deployment
6. **Update existing posts** after deployment to activate new links
7. **Commit twice**: First for new post, second for link updates in existing posts


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

### 4. Adding a New Page (Non-Post)

```bash
# Create about page in English and Japanese
hugo new content/en/about.md
hugo new content/ja/about.md

# Add to menu in hugo.toml if needed
```

### 5. Updating Theme

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

### 6. Building for Production

```bash
# Local production build
hugo --minify

# Output will be in /public/
# (Deployment is automatic via GitHub Actions)
```

### 7. Fixing Sitemap URLs (localhost → production)

**Problem:** If `public/sitemap.xml` contains localhost URLs, Google Search Console cannot fetch it.

**Detection:**
```bash
# Check if sitemap has localhost URLs
grep "localhost" public/sitemap.xml

# Or check all sitemap files
grep -r "localhost" public/*.xml
```

**Fix:**
```bash
# Replace all localhost URLs with production domain
find public -name "sitemap.xml" -exec sed -i 's|http://localhost:1313|https://tripmate.news|g' {} +

# Verify the fix
grep "tripmate.news" public/sitemap.xml

# Commit and push
git add public/
git commit -m "Fix sitemap.xml: Replace localhost URLs with production domain"
git push

# After merge to main, verify at:
# https://tripmate.news/sitemap.xml
```

**Prevention:**
- Avoid committing `public/` directory after local builds
- Let GitHub Actions generate production sitemap automatically
- If you must commit `public/`, always verify sitemap URLs first

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

### Scripts & Documentation

| File | Purpose |
|------|---------|
| `download_naver_images.py` | Migrate images from Naver Blog |
| `README_IMAGE_DOWNLOAD.md` | Documentation for migration script |
| `LINK_MAPPING.md` | **Naver→Hugo link mapping database** - Tracks internal blog links for conversion |

### Design & Style Files

| File | Purpose | Notes |
|------|---------|-------|
| `static/css/blog-cards.css` | Blog card styles for post listings | Modern magazine-style cards with gradients |
| `static/css/blog-post-common.css` | Shared styles for blog post content | Classes: `.blog-container`, `.info-box`, `.schedule-table`, `.tip-box`, `.image-group-2/3/4` |
| `static/css/related-posts.css` | Related posts sidebar styles | Compact horizontal card layout with thumbnails |
| `layouts/partials/head-additions.html` | CSS loader for custom styles | Automatically loads all three CSS files |
| `layouts/partials/menu-contextual.html` | Related posts sidebar component | Custom partial overriding theme default, displays up to 6 related posts |
| `layouts/post/list.html` | Post listing page layout | CSS Grid with responsive breakpoints |
| `layouts/post/summary.html` | Blog card component | Individual card template |

### Key Content Files

**Homepage Content:**
- `content/en/_index.md` - English homepage (default)
- `content/ja/_index.md` - Japanese homepage

**Example Posts:**
- `content/en/posts/evangelion-30th-roppongi-2025.md` - Evangelion exhibition guide
- `content/en/posts/marunouchi-illumination-2025.md` - Illumination guide
- Corresponding Japanese translations in `/ja/posts/`

**Note:** Korean content has been removed from the repository.

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

4. **Do NOT** change language codes (ko, en, ja)
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

## Migration Context

### Current Migration Status

**Source:** Naver Blog → Hugo Static Site

**Progress:**
- ✅ Site infrastructure set up
- ✅ Multilingual architecture configured
- ✅ Custom migration script created
- ✅ Sample posts migrated (2-3 restaurant reviews)
- 🔄 Ongoing content migration

### Migration Workflow (Naver Blog → Hugo)

**⚠️ IMPORTANT: Naver blocks automated image downloads (403 Forbidden errors)**

Due to Naver's security restrictions, images must be downloaded manually. Follow this workflow:

**Step 1: Save Naver Blog HTML**
- Visit the Naver blog post
- Save the complete HTML (Ctrl+S or right-click → Save As)
- Save to repository root (e.g., `naver_post.html`)

**Step 2: Analyze HTML and Create English/Japanese Versions Only**
- Count total images in the HTML
- **⚠️ CRITICAL: Image groups contain multiple images**
  - Naver Blog uses `<div class="se-imageGroup-item">` for grouped images
  - Each image in a group MUST get its own `<figure>` tag and unique number
### Formatting & Visuals
*   **HTML over Markdown:** For bullet points and bold text within blog posts, use HTML tags instead of Markdown syntax to ensure consistent styling.
    *   **Lists:** Use `<ul>` and `<li>` tags.
    *   **Bold:** Use `<b>` tags.
*   **Images:**
    *   Use `<figure>` and `<figcaption>` for individual images.
    *   Use `<div class="image-group-2">` (or 3/4) for grouping multiple images side-by-side.
    *   Images should be center-aligned.
    *   Include descriptive `alt` text.
  - Example: `<div class="se-imageGroup-col-2">` = 2 images = create 2 separate `<figure>` tags
  - DO NOT merge multiple images from a group into one figure
  - Count carefully: if you see 10 `<img>` tags, you need 10 figure tags (even if grouped)
- **⚠️ CRITICAL: Image Numbering (1:1 Matching)**
  - `{slug}-01.jpg`: First image - used in BOTH `featured_image` field AND first `<figure>` in body
  - `{slug}-02.jpg`: Second image in post body
  - `{slug}-03.jpg`, `04.jpg`, etc.: Subsequent body images in order
  - **Total images in Hugo = Total images in Naver HTML (exact 1:1 match)**
  - Example: If HTML has 21 images → 21 Hugo images (01.jpg through 21.jpg)
  - **Note:** The `featured_image` field and first body `<figure>` share the same 01.jpg file
- **Translate Korean HTML content to English and Japanese ONLY** (do NOT create Korean version)
- Create blog posts in 2 languages: English and Japanese
- Maintain original image positions from Korean HTML
- Use `<figure>` tags with `<figcaption>` for each body image
- Add proper Front Matter with `featured_image` (always `{slug}-01.jpg`), `description`, `summary`
- Use centered intro paragraph
- **⚠️ PRESERVE external source links:** If the Korean HTML contains source attribution links (e.g., `<a href="...">출처</a>`), maintain the HTML link structure in translations:
  - English: `<a href="..." target="_blank">Source</a>`
  - Japanese: `<a href="..." target="_blank">出典</a>`
  - Keep original URL and target attribute
  - Common source patterns: `(출처)`, `출처:`, `이미지 출처`
- **Extract and record internal links** (see Link Mapping below)
- Commit both English and Japanese versions

**Step 2.5: Intelligent Link Mapping and Auto-Conversion**

🎯 **NEW: Automated link conversion using LINK_MAPPING.md**

When creating Hugo posts, the AI will:

1. **Load LINK_MAPPING.md first** to check existing mappings (currently 31 posts mapped)

2. **For each internal Naver link found:**
   - Extract Naver post ID (e.g., `223681272647` from `https://blog.naver.com/tokyomate/223681272647`)
   - Check if mapping exists in LINK_MAPPING.md

   - **If mapped AND Hugo post file exists:** ✅ Automatically convert to Hugo link

     **⚠️ CRITICAL - Link Conversion Rules:**

     **Rule 1: Always verify file existence BEFORE creating working links**
     - Check if `content/en/posts/{slug}.md` actually exists
     - **If file exists:** Create working link with proper URL format
     - **If file does NOT exist:** Use `#` placeholder + TODO comment (even if mapped in LINK_MAPPING.md)

     **Rule 2: Link Format**
     - **English posts:** Use `/posts/slug/` (NO `/en/` prefix - English is default language)
     - **Japanese posts:** Use `/ja/posts/slug/` (WITH `/ja/` prefix)

     ```html
     <!-- Before (Naver) -->
     <a href="https://blog.naver.com/tokyomate/224065668379">Related Article</a>

     <!-- After (Hugo - Auto-converted) -->
     <!-- English version: -->
     <a href="/posts/roppongi-christmas-illumination-2025/">Related Article</a>

     <!-- Japanese version: -->
     <a href="/ja/posts/roppongi-christmas-illumination-2025/">関連記事</a>
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
          Hugo: /posts/[SLUG_TBD]/ -->  <!-- English: no /en/ prefix -->
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
- ✅ Most links work immediately (30/30 mapped posts = 100% for known posts)
- ✅ No manual link updates needed for existing posts
- ✅ Only unmapped posts need future updates
- ✅ Efficiency improves as more posts are migrated

**Example Processing:**

```
Internal Links Found: 6
├─ 224065668379 (roppongi-christmas-illumination-2025) → ✅ Auto-converted
│   EN: /posts/roppongi-christmas-illumination-2025/
│   JA: /ja/posts/roppongi-christmas-illumination-2025/
├─ 224055756731 (tokyo-3-day-christmas-itinerary) → ✅ Auto-converted
│   EN: /posts/tokyo-3-day-christmas-itinerary/
│   JA: /ja/posts/tokyo-3-day-christmas-itinerary/
├─ 224045496649 (not yet mapped) → ⏳ TODO comment added
├─ 224042431249 (not yet mapped) → ⏳ TODO comment added
├─ 223681272647 (not yet mapped) → ⏳ TODO comment added
└─ 223988228389 (not yet mapped) → ⏳ TODO comment added

Result: 2 links work immediately, 4 marked for future update
```

See `/LINK_MAPPING.md` for complete tracking database with 30 mapped posts.

**Step 3: Validation and Image Download (Integrated)**
- Run integrated validation and download script:
  ```bash
  python3 download_naver_images.py naver.html post-slug
  ```
- Script performs automated validation:
  - Analyzes Naver HTML (extracts all images, removes ad blocks)
  - Handles image groups (2-4 images) correctly
  - Validates against Hugo markdown with **1:1 matching** (count, order, sequential numbering)
  - Reports detailed errors if validation fails
- Only downloads images if validation passes:
  - Downloads to `/static/images/posts/` with naming: `{post-slug}-{number}.jpg`
  - Converts to JPG format with optimization
  - Numbers sequentially: **01.jpg, 02.jpg, 03.jpg...** (1:1 matching with Naver order)
- If validation fails:
  - Fix Hugo markdown based on error report
  - Re-run script until validation passes
- User commits and pushes images

**Step 4: Test Locally**
- Test locally with `hugo server -D`
- Verify all images display correctly
- Check social media preview (featured_image)
- Verify all internal links work correctly
- Test responsive design on mobile/tablet

**Step 5: Create Pull Request**

After completing EN/JA blog post creation, commit changes and create a PR with detailed information.

**5.1. Commit and Push:**
```bash
# Stage all changes
git add LINK_MAPPING.md content/en/posts/*.md content/ja/posts/*.md

# Commit with descriptive message
git commit -m "Add [Post Title] blog post (EN/JA) with link conversion"

# Push to branch
git push -u origin claude/[branch-name]
```

**5.2. Create PR via GitHub Web Interface:**

⚠️ **Note:** The `gh` CLI is not available in this environment. Create PR manually via GitHub web interface.

**PR Title Format:**
```
Add [Post Title] Blog Post (EN/JA) with [Key Feature]
```

**Examples:**
- `Add Meiji Jingu Gaien Christmas Market 2025 Blog Post (EN/JA) with Full Link Conversion`
- `Add Roppongi Hills Illumination 2025 Blog Post (EN/JA) with SEO Optimization`

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
- ✅ Keyword-rich titles (EN 50-60 chars, JA 30-35 chars)
- ✅ Meta descriptions within character limits
- ✅ Descriptive alt text for all images
- ✅ Structured H2/H3 headings with keywords
- ✅ Internal linking to related content
- ✅ Featured image for social media preview

## Testing

✅ All internal links verified against LINK_MAPPING.md
✅ TranslationKey consistent across EN/JA versions
✅ Front matter validation (dates, categories, tags)
✅ Image paths follow naming convention
✅ Hugo syntax validation

## Files Changed

- `content/en/posts/[slug].md` (new, [X] lines)
- `content/ja/posts/[slug].md` (new, [X] lines)
- `LINK_MAPPING.md` (modified, +[X] lines)

## Breaking Changes

None

## Next Steps After Merge

1. Download images using migration script:
   ```bash
   python3 download_naver_images.py naver.html [slug]
   ```

2. Commit and push images ([X] files)

3. Verify production deployment at:
   - EN: https://tripmate.news/posts/[slug]/
   - JA: https://tripmate.news/ja/posts/[slug]/

## Related

- Naver Blog Post ID: [ID]
- Migration Session: [branch-name]
- LINK_MAPPING.md: Updated to [N] posts
```

**5.3. PR Creation Checklist:**

Before creating the PR, ensure:
- ✅ Branch name follows convention: `claude/[descriptive-name]-[session-id]`
- ✅ All files committed and pushed
- ✅ PR title is clear and descriptive
- ✅ PR description includes all sections (Summary, Changes, Testing, Files Changed)
- ✅ Internal link conversion details documented
- ✅ SEO optimization checklist completed
- ✅ Next steps clearly outlined

**Step 6: After PR Merge**
- Download images using migration script
- Commit and push images to main branch
- Verify production deployment

**Example Workflow:**

```bash
# Step 1: After user provides HTML
# (AI analyzes HTML and counts images)

# Step 2: AI translates Korean HTML to English and Japanese with smart linking
# - Loads LINK_MAPPING.md (30 posts currently mapped)
# - Finds 4 internal links in post:
#   ✅ 224065668379 → Auto-converted to /posts/roppongi-christmas-illumination-2025/ (EN)
#                     Auto-converted to /ja/posts/roppongi-christmas-illumination-2025/ (JA)
#   ✅ 224055756731 → Auto-converted to /posts/tokyo-3-day-christmas-itinerary/ (EN)
#                     Auto-converted to /ja/posts/tokyo-3-day-christmas-itinerary/ (JA)
#   ⏳ 223681272647 → TODO comment added (not yet migrated)
#   ⏳ 223988228389 → TODO comment added (not yet migrated)
#
# Creates:
# content/en/posts/marunouchi-illumination-2025.md (22 images, 2 working links)
# content/ja/posts/marunouchi-illumination-2025.md (22 images, 2 working links)
# Updates LINK_MAPPING.md with new post entry
# (NO Korean version created)

# Step 3: Run integrated validation and download script
python3 download_naver_images.py naver.html marunouchi-illumination-2025
# Script validates (count, order, numbering) then downloads if valid
# Downloads to: static/images/posts/marunouchi-illumination-2025-01.jpg
#               static/images/posts/marunouchi-illumination-2025-02.jpg
#               ... (22 total, auto-converted to JPG)

# Step 4: Test locally
hugo server -D
# User verifies everything works (including auto-converted links!)

# Step 5: Create Pull Request
# 5.1. Commit and push blog posts
git add LINK_MAPPING.md content/en/posts/marunouchi-illumination-2025.md content/ja/posts/marunouchi-illumination-2025.md
git commit -m "Add Marunouchi Illumination 2025 blog post (EN/JA) with link conversion"
git push -u origin claude/translate-korean-doc-01HHJyhanP2K842HsBJapxDG

# 5.2. Create PR via GitHub web interface with:
#   - Title: "Add Marunouchi Illumination 2025 Blog Post (EN/JA) with Full Link Conversion"
#   - Description: Use PR template from Step 5 above
#   - Include: Summary, Changes, Link Conversion Details, Testing, Files Changed

# Step 6: After PR merge - Download and commit images
python3 download_naver_images.py naver.html marunouchi-illumination-2025
git add static/images/posts/marunouchi-illumination-2025-*.jpg
git commit -m "Add images for Marunouchi Illumination 2025"
git push
```

### Migration Scripts

#### Primary Script: `download_naver_images.py` (Integrated Validation)

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
python3 download_naver_images.py naver.html japan-convenience-store-shopping-best-10
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

#### Secondary Script: `check_image_order.py` (Standalone Validator)

**File:** `check_image_order.py`

**Purpose:** Standalone validation script for existing posts (legacy/debugging).

**Usage:**
```bash
python3 check_image_order.py <naver_html_file> <post-slug>
```

**Note:** Most users should use the integrated `download_naver_images.py` instead.

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
hugo new content/en/posts/name.md   # New English post
hugo new content/ja/posts/name.md   # New Japanese post

# Git
git submodule update --init --recursive   # Init theme
git push -u origin claude/branch-name     # Push to branch

# Migration (Naver Blog)
# Step 1: User provides HTML
# Step 2: AI creates 2 language versions (EN/JA) with smart link conversion
#         - Loads LINK_MAPPING.md (31 mapped posts)
#         - Auto-converts known Naver links to Hugo links
#         - Adds TODO comments for unmapped links
#         ⚠️ CRITICAL: IMAGE POSITIONING
#         - Verify ALL images from original blog
#         - Content MUST match image positions EXACTLY
#         - Same image at same position = same content context
#         - Never add content not in original blog
#         ⚠️ CRITICAL: CULTURAL ADAPTATION
#         - Adapt content for US/Japan cultural contexts
#         - EN: American English, US cultural references
#         - JA: Japanese cultural nuances and expressions
#         - Proper localization, not just translation
# Step 3: Run integrated validation & download script
python3 download_naver_images.py naver.html post-slug
#         - Validates image count/order against Hugo markdown
#         - Downloads only if validation passes
#         - Auto-converts to JPG format
# Step 4: Test with hugo server -D

# Note: public/ is gitignored - no need to verify sitemap URLs manually
# GitHub Actions generates correct production URLs automatically
```

### Key URLs

- **Production Site:** https://tripmate.news
- **GitHub Repo:** https://github.com/mydyney/mydyney.github.io
- **Local Preview:** http://localhost:1313
- **Theme Docs:** https://github.com/theNewDynamic/gohugo-theme-ananke

### Important Paths

```
Content:         /content/{en,ja}/posts/*.md
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

**Last Updated:** 2025-12-14
**Updated By:** Claude (AI Assistant)
**Next Review:** When significant project changes occur

**Recent Updates (2025-12-14 - Latest):**
- **Blog Writing Guidelines Enhancement:**
  - **CRITICAL: Added "NO AI WRITING TRACES" rule**
  - Updated "CULTURAL ADAPTATION & WRITING STYLE" section with detailed guidelines:
    * English: Traveler's perspective for international tourists
    * Japanese: Local reader perspective, avoid "日本の" prefix
    * Chinese: Traveler's perspective similar to English approach
  - Added specific writing style requirements for each language
  - Emphasized natural, human-like writing without AI patterns
  - **Impact:** Ensures all blog content feels authentic and human-written

- **Chinese Language Support Documentation:**
  - Added Chinese (Simplified) to "Languages Supported" section
  - **CRITICAL: Added YAML syntax rules for Chinese content**
  - Documented forbidden characters in YAML front matter:
    * Chinese corner brackets `「」` (U+300C, U+300D)
    * Chinese quotation marks `"` `"` (U+201C, U+201D)
    * Chinese single quotes `'` `'` (U+2018, U+2019)
  - Added examples of correct vs incorrect YAML formatting
  - Added validation command for Chinese posts
  - Updated "Multilingual Content" section to include Chinese
  - **Impact:** Prevents Hugo build failures caused by YAML parsing errors in Chinese posts

**Previous Updates (2025-12-13):**
- **Critical Considerations Enhancement:**
  - Added new prohibition rule #10: "Do NOT create documents or files unless explicitly requested"
  - Clarified that AI should only create content when user specifically asks for it
  - Exception: Required files for completing a specific task (e.g., blog posts during migration)
  - Prevents proactive creation of README files, documentation, or other unrequested files
  - **Impact:** Ensures AI assistant stays focused on user-requested tasks only

**Recent Updates (2025-12-12):**
- **Documentation Clarity Improvements:**
  - Fixed inconsistent image numbering rules throughout the document
  - Clarified that `{slug}-01.jpg` serves dual purpose: featured_image + first body image
  - Updated "Blog Post Format" section to correctly reference `{slug}-01.jpg` for first body image
  - Clarified 1:1 matching rule: Naver image count = Hugo image count (no +1 for featured)
  - Enhanced "Naming Conventions" table to explicitly show EN/JA differences for tags and categories
  - **Impact:** Eliminates confusion about image numbering, ensuring consistent blog post creation

**Recent Updates (2025-12-05):**
- **Tag and Category Management Guidelines:**
  - Added comprehensive "Tag Management and Multilingual Tags" section
  - Added comprehensive "Category Management and Multilingual Categories" section
  - **CRITICAL RULE:** English posts must use English tags/categories, Japanese posts must use Japanese tags/categories
  - Added complete English-Japanese tag mapping table (45+ tag pairs)
  - Added complete English-Japanese category mapping table (35+ category pairs)
  - Included tag and category naming conventions for both languages
  - Added instructions for updating mappings when creating new tags/categories
  - Documented bulk conversion scripts usage (tags and categories)
  - Added verification commands to check tag and category consistency
  - **Impact:** Ensures SEO consistency and better user experience across multilingual content

**Recent Updates (2025-11-25):**
- **CRITICAL FIX: GitHub Actions baseURL Configuration:**
  - Fixed 404/403 errors caused by incorrect baseURL in workflow
  - **Removed** `--baseURL "${{ steps.pages.outputs.base_url }}/"` from hugo build command
  - Build command now correctly uses: `hugo --minify` (no baseURL flag)
  - Hugo now uses baseURL from `hugo.toml` (https://tripmate.news) matching custom domain
  - Added comprehensive warnings in CLAUDE.md to prevent future mistakes
  - **Impact:** Prevents site-wide 404/403 errors when deploying to GitHub Pages with custom domain

- **UI/UX Improvements:**
  - Changed blog card image aspect ratio from 5:3 to 16:9 for better visual balance
  - Updated mobile breakpoint from 768px to 800px for improved responsiveness
  - Fixed table styling in info-box: dark header (#2d3748) with white text for readability
  - Fixed Tokyo Skytree guide HTML structure: corrected image-group-2 closing tag
  - Reverted custom single.html layout to restore theme default behavior

**Recent Updates (2025-11-24):**
- **Migration Workflow Enhancement:**
  - Added **Step 5: Create Pull Request** to migration workflow
  - Comprehensive PR title and description template with examples
  - PR creation checklist for quality assurance
  - Updated example workflow to include PR creation step
  - Restructured workflow: Test Locally (Step 4) → Create PR (Step 5) → Download Images (Step 6)
  - Ensures all EN/JA blog post migrations include proper documentation via PRs

**Recent Updates (2025-11-24 - Morning):**
- **SEO Optimization:**
  - Added `robots.txt` with sitemap references
  - Added `favicon.svg` (TM logo with purple gradient)
  - Added `site.webmanifest` for PWA support
  - Added hreflang tags for EN/JA multilingual SEO
  - Added Google Search Console verification code
  - Added theme-color and mobile meta tags
- **Git Cleanup:**
  - Added `.gitignore` file (excludes `public/`, `resources/`, temp files)
  - Removed stale `public/` directory from Git tracking (was causing 404 errors)
  - `public/` is now auto-generated by GitHub Actions on each deploy
- **Documentation:** Updated CLAUDE.md to reflect new SEO files and gitignore changes

**Previous Updates (2025-11-20):**
- **CSS Update:** Optimized image group sizing for better visual balance
  - `.image-group-2`: 80% → 45% max-width (more compact)
  - `.image-group-3`: 90% → 45% max-width (more compact)
  - `.image-group-4`: Changed from 4-in-a-row to 2x2 tile layout (top 2, bottom 2), 50% max-width
- **BREAKING CHANGE:** Simplified `download_naver_images.py` - removed all validation logic
- Updated 1:1 matching: Featured_image field and first body image use the **same** 01.jpg file
- Added figcaption styling standard (font-size: 0.7em, center-aligned)

**Update This Document When:**
- Project structure changes significantly
- New workflows are established
- Build/deployment process changes
- New conventions are adopted
- Migration completes

---

**End of CLAUDE.md**
