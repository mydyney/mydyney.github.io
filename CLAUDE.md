# CLAUDE.md - AI Assistant Guide

> **Last Updated:** 2025-11-18
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

**Note:** Korean language support has been removed. The blog now operates in English and Japanese only.

### Key Information

- **Hugo Version:** 0.128.0 extended (required)
- **Theme:** Ananke (MIT license)
- **Base URL:** https://tripmate.news
- **Custom Domain:** Configured via `/static/CNAME`
- **Analytics:** Google Analytics (G-NZ22T8HRR3)
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
│   │   └── head-additions.html     # CSS loader
│   └── post/
│       ├── list.html               # Post list layout
│       └── summary.html            # Post card component
│
├── public/                          # ⚠️ Generated output (21MB, committed)
│
├── resources/                       # Hugo-generated resources
│   └── _gen/
│       └── assets/                 # CSS, JS bundles
│
├── static/                          # Static assets (22MB)
│   ├── CNAME                       # Domain: tripmate.news
│   └── images/
│       ├── posts/                  # Post-specific images
│       │   ├── kirimugiya-jinroku-shinjuku-01.jpg
│       │   ├── tokyo-ramen-street-1.png
│       │   └── ...
│       └── [various images]        # Site images
│
├── themes/
│   └── ananke/                     # Theme (Git submodule, 2.3MB)
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
| `static/` | Files copied as-is to output (images, CNAME, etc.) | Images go in `/static/images/posts/` |
| `public/` | Build output (generated by Hugo) | ⚠️ Currently committed (unusual) |
| `resources/` | Hugo cache and generated assets | Can be regenerated |
| `themes/` | Ananke theme (Git submodule) | Do NOT modify directly |
| `.github/workflows/` | CI/CD configuration | Deployment automation |

---

## Development Workflows

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

### Multilingual Content

**Creating Linked Translations:**

1. Create post in **English and Japanese** with **identical `translationKey`**
2. Use same date across both versions
3. Place in respective language directories (`content/en/` and `content/ja/`)

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
```

**Language Switcher:** Hugo will automatically show language switcher when posts share `translationKey`.

**Note:** Korean language support has been removed. Only create English and Japanese versions.

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
4. **First Body Image** (with `<figure>` tag, using `{slug}-02.jpg`)
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

When Naver HTML contains image groups (e.g., `se-imageGroup-col-2`), use CSS Grid layout:

```html
<!-- 2 images side-by-side -->
<div class="image-group-2">
  <figure>
    <img src="/images/posts/post-slug-10.jpg" alt="First image">
  </figure>
  <figure>
    <img src="/images/posts/post-slug-11.jpg" alt="Second image">
  </figure>
  <figcaption style="font-size: 0.7em; text-align: center;">Caption for both images</figcaption>
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
  <figcaption style="font-size: 0.7em; text-align: center;">Caption for all three images</figcaption>
</div>

<!-- 4 images side-by-side -->
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
  <figcaption style="font-size: 0.7em; text-align: center;">Caption for all four images</figcaption>
</div>
```

**Important Notes:**
- ✅ All figcaptions MUST use inline style: `style="font-size: 0.7em; text-align: center;"`
- ✅ For image groups, figcaption goes OUTSIDE individual `<figure>` tags
- ✅ Each image in a group gets its own `<figure>` tag with unique number
- ✅ CSS Grid automatically arranges images horizontally (desktop) or vertically (mobile)
- ✅ Max-width constraints: 2 images (80%), 3 images (90%), 4 images (100%)

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

/* Image Group Layout (Side-by-Side) */
.image-group-2         /* 2 images horizontally (80% max-width) */
.image-group-3         /* 3 images horizontally (90% max-width) */
.image-group-4         /* 4 images horizontally (100% max-width) */
```

**CSS Grid Image Groups:**
- Uses CSS Grid for side-by-side layout on desktop
- Automatically switches to single column on mobile (< 768px)
- Different max-width constraints for natural sizing:
  - 2 images: 80% of container width
  - 3 images: 90% of container width
  - 4 images: 100% of container width
- Centered with `margin: 2rem auto`
- Preserves aspect ratios with `height: auto`

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
| Categories | Title Case | `["Travel", "Food"]` |
| Tags | lowercase | `["ramen", "tokyo", "michelin"]` |

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

```bash
# 1. Save Naver blog post HTML to file
# 2. Run migration script
python3 download_naver_images.py naver_post.html post-slug-name

# 3. Script will:
#    - Download all images
#    - Save to /static/images/posts/
#    - Create markdown with local image paths

# 4. Copy/adapt generated markdown to Hugo post
# 5. Add proper front matter
# 6. Test and commit
```

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
| `hugo.toml` | Main Hugo configuration | Site settings, languages, menus, params |
| `.github/workflows/hugo.yml` | CI/CD workflow | Automated build & deployment |
| `.gitmodules` | Git submodule config | Ananke theme reference |
| `static/CNAME` | Custom domain config | Contains: `tripmate.news` |

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

2. **Public Directory Committed & Sitemap Issues**
   - Unusual: `public/` (21MB) is currently committed to repo
   - Normally this is in `.gitignore`
   - ⚠️ **CRITICAL**: Never commit sitemap.xml with localhost URLs
   - If you build locally with `hugo server`, sitemap will contain `http://localhost:1313`
   - Always verify sitemap URLs before committing: `grep -r "localhost" public/*.xml`
   - If localhost URLs found, fix with: `find public -name "sitemap.xml" -exec sed -i 's|http://localhost:1313|https://tripmate.news|g' {} +`
   - Google Search Console will fail to fetch sitemap with localhost URLs
   - GitHub Actions builds with production URLs automatically

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

8. **Do NOT** commit sitemap.xml with localhost URLs
   - Never run `hugo` or `hugo server` and commit the resulting `public/sitemap.xml`
   - Always check: `grep "localhost" public/sitemap.xml` before committing
   - Use the fix command if localhost URLs are found (see "Public Directory Committed" section)
   - Let GitHub Actions generate production sitemap automatically

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
11. **Verify sitemap URLs** before committing changes to `public/` directory
12. **After main branch merge**, verify sitemap at https://tripmate.news/sitemap.xml has production URLs

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
  - Example: `<div class="se-imageGroup-col-2">` = 2 images = create 2 separate `<figure>` tags
  - DO NOT merge multiple images from a group into one figure
  - Count carefully: if you see 10 `<img>` tags, you need 10 figure tags (even if grouped)
- **⚠️ CRITICAL: Image Numbering**
  - `{slug}-01.jpg`: Featured image (Front Matter `featured_image` field only)
  - `{slug}-02.jpg`: First image in post body (after intro paragraph)
  - `{slug}-03.jpg`, `04.jpg`, etc.: Subsequent body images in order
  - **Total images = body images + 1 (featured)**
  - Example: If HTML has 21 images → 22 total (01.jpg for featured + 02.jpg through 22.jpg for body)
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

   - **If mapped:** ✅ Automatically convert to Hugo link

     **⚠️ CRITICAL - Link Format Rules:**
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

   - **If not mapped:** ⏳ Add TODO comment for future migration
     ```html
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/223681272647
          Hugo: /posts/[SLUG_TBD]/ -->  <!-- English: no /en/ prefix -->
     <a href="#" style="color: #667eea;">Related Article</a>

     <!-- For bold links, wrap text in <strong> tags: -->
     <a href="#" style="color: #667eea;"><strong>→ [See Details] Complete Guide</strong></a>

     <!-- Japanese TODO: -->
     <!-- TODO: Update link after migration
          Naver: https://blog.naver.com/tokyomate/223681272647
          Hugo: /ja/posts/[SLUG_TBD]/ -->  <!-- Japanese: with /ja/ prefix -->
     <a href="#" style="color: #667eea;">関連記事</a>

     <!-- For bold links, wrap text in <strong> tags: -->
     <a href="#" style="color: #667eea;"><strong>→ [詳しく見る] 完全ガイド</strong></a>
     ```

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

**Step 4: Test and Deploy**
- Test locally with `hugo server -D`
- Verify all images display correctly
- Check social media preview (featured_image)
- Push to remote branch
- Create Pull Request

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

# Step 4: Test and deploy
hugo server -D
# User verifies everything works (including auto-converted links!)
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
# Step 3: Run integrated validation & download script
python3 download_naver_images.py naver.html post-slug
#         - Validates image count/order against Hugo markdown
#         - Downloads only if validation passes
#         - Auto-converts to JPG format
# Step 4: Test with hugo server -D

# Sitemap verification (IMPORTANT!)
grep "localhost" public/sitemap.xml   # Check for localhost URLs
find public -name "sitemap.xml" -exec sed -i 's|http://localhost:1313|https://tripmate.news|g' {} +  # Fix
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

**Last Updated:** 2025-11-20
**Updated By:** Claude (AI Assistant)
**Next Review:** When significant project changes occur

**Recent Updates (2025-11-20):**
- **BREAKING CHANGE:** Simplified image validation to 1:1 matching (removed featured image exclusion logic)
- Updated `download_naver_images.py` validation: Naver count = Hugo count (exact match)
- Changed sequential numbering: 01, 02, 03... (previously 02, 03, 04...)
- Updated regex pattern to detect images inside CSS Grid `.image-group-2/3/4` divs
- Featured_image field and first body image now use the **same** 01.jpg file
- Added figcaption styling standard (font-size: 0.7em, center-aligned)
- Documented CSS Grid image group layout (`.image-group-2/3/4`)

**Update This Document When:**
- Project structure changes significantly
- New workflows are established
- Build/deployment process changes
- New conventions are adopted
- Migration completes

---

**End of CLAUDE.md**
