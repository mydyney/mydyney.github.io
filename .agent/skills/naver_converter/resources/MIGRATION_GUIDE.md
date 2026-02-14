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
      <a href="#" style="color: #667eea;">Related Article</a>
      ```
- **⚠️ MANDATORY: Add Editor's Note section at the end**
  - Use the exact HTML format defined in **[CONTENT_GUIDELINES.md](./CONTENT_GUIDELINES.md#editors-note)**.
  - Position it after all content, before the closing `</div>` tag.
  - Replace `[NAVER_POST_ID]` with the actual ID from `LINK_MAPPING.md`.

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
   - Placeholder links (`href="#"`) in existing posts will be updated in future migrations
   - Each new migration will check LINK_MAPPING.md and convert placeholders to working links

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

## Migration Specific Rules

In addition to the general **[CONTENT_GUIDELINES.md](./CONTENT_GUIDELINES.md)**, follow these rules specific to Naver Blog migrations:

### ⚠️ CRITICAL: COMPLETE CONTENT TRANSLATION
- **Translate ALL text**: Paragraphs, sentences, and descriptions must be translated without omission.
- **NO OVER-SUMMARIZATION**: Do not compress detail-heavy sections like **Timetables**, **Menus**, **Transportation Tips**, or **Step-by-Step Guides**. Every row in a table and every item in a list must be preserved.
- **NEVER add new content**: Only translate what exists in the source HTML.
- **Preserve Linear Order**: Follow the HTML element order exactly (Text -> Image -> Text). Do not reorder elements to group sections if they are interleaved in the source.

### ⚠️ CRITICAL: IMAGE CAPTIONS & POSITIONING
- **Extract ALL captions**: Look for `se-caption` or similar module in Naver HTML.
- **Figure Wrapping**: Every single image must be wrapped in a `<figure>` tag.
- **1:1 Matching**: Image positions must match original context exactly. Use the numbering (01, 02...) generated by scripts.
- **CONTEXT VERIFICATION**: Double-check that the image content matches the surrounding text (e.g., ensure an Onsen image isn't mistakenly swapped with a Hotel image).

### ⚠️ CRITICAL: LINK CONVERSION
- **Inline Links**: Internal blog links appearing in the middle of text are **CONTENT**, not footer material. Place them exactly where they appear in the source.
- **Link Preservation**: If a URL appears multiple times (e.g., as a text link and a button), preserve both.

### ⚠️ CRITICAL: CULTURAL ADAPTATION
- Refer to the **[Cultural Adaptation & Writing Style](./CONTENT_GUIDELINES.md#3-cultural-adaptation-writing-style)** section in Content Guidelines for language-specific prompts and rules (EN/JA/ZH).

---

## Link Mapping System

### Converted Posts vs. TODO Placeholders

When creating Hugo posts, you must convert Naver internal links based on their migration status in `LINK_MAPPING.md`.

**1. Mapped & File Exists (✅ Converted Link)**
- If the Naver ID is in `LINK_MAPPING.md` **AND** the Hugo file `content/en/posts/[slug].md` actually exists.
- **English**: `/posts/[slug]/`
- **Japanese**: `/ja/posts/[slug]/`
- **Chinese**: `/zh-cn/posts/[slug]/`

**2. Not Mapped or File Missing (⏳ TODO Placeholder)**
- **ALWAYS** use `href="#"` to avoid 404 errors.
- **ALWAYS** add a TODO comment with the source Naver URL and target slug (if known).

```html
<!-- TODO: Update link after migration
     Naver: https://blog.naver.com/tokyomate/224022065518
     Hugo: /posts/don-quijote-shopping-guide-2025/ -->
<a href="#" style="color: #667eea;"><strong>➡️ Check the Shopping Guide</strong></a>
```

### Link Conversion Workflow

1. **Extract Naver ID** from the source link.
2. **Check `LINK_MAPPING.md`** for a matching slug.
3. **Verify File Existence** with `ls content/en/posts/[slug].md`.
4. **Choose Format**:
    - Build working link if verified.
    - Build TODO placeholder if not.
5. **Preserve Context**: Place the link exactly where it appears in the source text.

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
- ✅ **Flexible Container Support:** Detects images inside any container (inline flex divs or `.image-group-2/3/4` CSS classes)

**Regex Pattern for Hugo Markdown:**
```python
# Extracts ALL <figure> tags (standalone and inside flex/image-group containers)
figure_pattern = re.compile(
    r'<figure[^>]*>\s*<img src="(/images/posts/[^"]+)"\s+alt="([^"]*)"[^>]*>',
    re.DOTALL
)
```

**Pattern Features:**
- `<figure[^>]*>` - Matches `<figure>` tag with any attributes
- `[^>]*` after `<img>` - Allows additional attributes on img tag
- **Does NOT require closing `</figure>`** - This allows matching figures inside inline flex or `.image-group-N` containers where figcaption is outside individual figures
- `re.DOTALL` - Allows `.` to match newlines (multi-line patterns)
- **Works with any container** - Detects all `<figure>` tags regardless of container (inline flex or CSS classes)

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
- ✅ Klook affiliate links converted to Tripmate account with localization?
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
