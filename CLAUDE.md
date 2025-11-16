# CLAUDE.md - AI Assistant Guide

> **Last Updated:** 2025-11-16
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
5. [Content Management](#content-management)
6. [Key Conventions](#key-conventions)
7. [Common Tasks](#common-tasks)
8. [Important Files](#important-files)
9. [Critical Considerations](#critical-considerations)
10. [Migration Context](#migration-context)

---

## Project Overview

### What is this project?

**Tokyo Mate** (도쿄메이트 / 東京メイト) is a multilingual travel blog focused on Tokyo, Japan. It covers:
- Restaurant reviews and guides
- Travel information and tips
- Tourism recommendations
- Tokyo neighborhood explorations

### Languages Supported

1. **Korean** (ko) - Primary/Default language
2. **English** (en) - Secondary
3. **Japanese** (ja) - Tertiary

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
├── partials/
│   └── head-additions.html    # Custom CSS loader
└── post/
    ├── list.html              # Post listing (overrides theme)
    └── summary.html           # Blog card component
```

**Important Notes:**
- ✅ Place custom layouts in **specific directories** (e.g., `layouts/post/`)
- ❌ Avoid creating duplicates in `layouts/_default/` - unnecessary due to priority system
- 🎨 Custom layouts automatically override theme defaults
- 📂 Keep layouts organized by content type (`post/`, `page/`, etc.)

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
│   ├── en/                          # English content
│   │   ├── _index.md               # English homepage
│   │   └── posts/                  # English blog posts
│   ├── ja/                          # Japanese content
│   │   ├── _index.md               # Japanese homepage
│   │   └── posts/                  # Japanese blog posts
│   └── ko/                          # Korean content (PRIMARY)
│       ├── _index.md               # Korean homepage
│       └── posts/                  # Korean blog posts
│
├── layouts/                         # Custom layouts (override theme)
│   ├── partials/
│   │   └── head-additions.html     # CSS loader
│   └── post/
│       ├── list.html               # Post listing page
│       └── summary.html            # Blog card component
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
| `layouts/` | Custom layouts that override theme | Use specific paths (e.g., `post/`) not `_default/` |
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
4. Create Pull Request to `main`
5. Merge triggers automatic deployment

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

## Content Management

### Creating New Posts

**Recommended Method:**

```bash
# Create new post in Korean (default)
hugo new content/ko/posts/my-new-post.md

# Create new post in English
hugo new content/en/posts/my-new-post.md

# Create new post in Japanese
hugo new content/ja/posts/my-new-post.md
```

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

1. Create post in all three languages with **identical `translationKey`**
2. Use same date across all versions
3. Place in respective language directories

**Example:**

```yaml
# content/ko/posts/tokyo-guide.md
---
title: "도쿄 가이드"
translationKey: "tokyo-guide-2025"
---

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

### Images

**Naming Convention:**
```
{post-slug}-{number}.{ext}
```

**Examples:**
```
kirimugiya-jinroku-shinjuku-01.jpg
kirimugiya-jinroku-shinjuku-02.jpg
tokyo-ramen-street-1.png
tokyo-ramen-street-2.png
```

**Storage Location:**
```
/static/images/posts/
```

**Referencing in Markdown:**
```markdown
![Alt text](/images/posts/your-image-01.jpg)
```

**Image Migration from Naver Blog:**

```bash
# Use the custom Python script
python3 download_naver_images.py <HTML_FILE> <POST_SLUG>

# Example:
python3 download_naver_images.py naver_blog.html tokyo-restaurant-guide
```

See `README_IMAGE_DOWNLOAD.md` for detailed instructions.

### Blog Post Styles

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
```

**Usage in Markdown:**
```html
---
title: "Your Post Title"
---

<div class="blog-container">

<div class="info-box">
  <ul>
    <li>Information item 1</li>
    <li>Information item 2</li>
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
- ❌ DO NOT add inline `<style>` blocks in posts
- ✅ Wrap content in `<div class="blog-container">` for consistent styling
- 🎨 CSS is automatically loaded via `layouts/partials/head-additions.html`

**CSS Files:**
- `/static/css/blog-cards.css` - Blog card styles (list pages)
- `/static/css/blog-post-common.css` - Blog post content styles
- Both are loaded globally via `head-additions.html`

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
- Available classes: `.blog-container`, `.info-box`, `.schedule-table`, `.tip-box`
- DO NOT add `<style>` blocks in individual posts
- For new styles, add to `blog-post-common.css` for reusability

**Commit Messages:**
- Use descriptive messages
- Mix of English/Korean is acceptable
- Include context (e.g., "Add images for [post-name]")

---

## Common Tasks

### 1. Adding a New Blog Post

```bash
# 1. Create post in all languages
hugo new content/ko/posts/my-post.md
hugo new content/en/posts/my-post.md
hugo new content/ja/posts/my-post.md

# 2. Edit each file:
#    - Add same translationKey to all
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
# Create about page in all languages
hugo new content/ko/about.md
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

### Design & Style Files

| File | Purpose | Notes |
|------|---------|-------|
| `static/css/blog-cards.css` | Blog card styles for post listings | Modern magazine-style cards with gradients |
| `static/css/blog-post-common.css` | Shared styles for blog post content | Classes: `.blog-container`, `.info-box`, `.schedule-table`, `.tip-box` |
| `layouts/partials/head-additions.html` | CSS loader for custom styles | Automatically loads both CSS files |
| `layouts/post/list.html` | Post listing page layout | CSS Grid with responsive breakpoints |
| `layouts/post/summary.html` | Blog card component | Individual card template |

### Key Content Files

**Homepage Content:**
- `content/ko/_index.md` - Korean homepage
- `content/en/_index.md` - English homepage
- `content/ja/_index.md` - Japanese homepage

**Example Posts:**
- `content/ko/posts/kirimugiya-jinroku-shinjuku.md` - Michelin restaurant review
- `content/ko/posts/second-post.md` - Tokyo Ramen Street guide
- Corresponding translations in `/en/` and `/ja/`

---

## Critical Considerations

### ⚠️ Things to Be Careful About

1. **Git Submodules**
   - Theme is a submodule - always clone with `--recursive`
   - Don't modify theme files directly
   - Update submodule properly with git commands

2. **Public Directory Committed**
   - Unusual: `public/` (21MB) is currently committed to repo
   - Normally this is in `.gitignore`
   - Be cautious when modifying - may affect deployment

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

6. **Do NOT** create duplicate layout files in `_default/`
   - Use specific type directories (`layouts/post/`) for custom layouts
   - Hugo prioritizes specific over default, making `_default/` duplicates unnecessary
   - Example: Use `layouts/post/list.html` NOT both `post/` and `_default/`

7. **Do NOT** add inline `<style>` blocks in blog posts
   - Use shared CSS: `/static/css/blog-post-common.css`
   - Keeps styles consistent and maintainable

### ✅ Best Practices

1. **Always test locally** with `hugo server` before pushing
2. **Use descriptive commit messages** with context
3. **Maintain consistent front matter** across posts
4. **Follow image naming conventions** strictly
5. **Link translations** with `translationKey`
6. **Check CI/CD logs** if deployment fails
7. **Keep theme submodule updated** periodically
8. **Use shared CSS files** for blog post styles (blog-post-common.css)
9. **Place custom layouts in specific directories** (e.g., `layouts/post/` not `_default/`)
10. **Wrap blog post content** in `<div class="blog-container">` for consistent styling

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

### Migration Workflow

1. **Export from Naver Blog:** Save HTML of blog post
2. **Download Images:** Use `download_naver_images.py` script
3. **Convert Content:** Transform HTML to Markdown
4. **Add Front Matter:** Use Hugo conventions
5. **Create Translations:** Add English and Japanese versions
6. **Review & Publish:** Test locally, commit, push

### Migration Script Features

**File:** `download_naver_images.py`

**Capabilities:**
- Extracts images from Naver Blog HTML
- Downloads from `postfiles.pstatic.net`
- Deduplicates URLs
- Numbers sequentially with zero-padding
- Updates markdown with local paths
- Handles user-agent requirements

**Usage:**
```bash
python3 download_naver_images.py <HTML_FILE> <POST_SLUG>
```

**Dependencies:**
- Python 3
- `requests` library (`pip install requests`)

**See:** `README_IMAGE_DOWNLOAD.md` for detailed instructions

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
hugo new content/ko/posts/name.md   # New Korean post
hugo new content/en/posts/name.md   # New English post

# Git
git submodule update --init --recursive   # Init theme
git push -u origin claude/branch-name     # Push to branch

# Migration
python3 download_naver_images.py naver.html slug
```

### Key URLs

- **Production Site:** https://tripmate.news
- **GitHub Repo:** https://github.com/mydyney/mydyney.github.io
- **Local Preview:** http://localhost:1313
- **Theme Docs:** https://github.com/theNewDynamic/gohugo-theme-ananke

### Important Paths

```
Content:         /content/{ko,en,ja}/posts/*.md
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

**Last Updated:** 2025-11-16
**Updated By:** Claude (AI Assistant)
**Next Review:** When significant project changes occur

**Update This Document When:**
- Project structure changes significantly
- New workflows are established
- Build/deployment process changes
- New conventions are adopted
- Migration completes

---

**End of CLAUDE.md**
