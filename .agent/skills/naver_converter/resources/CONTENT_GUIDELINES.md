# CONTENT_GUIDELINES.md - Blog Content & Formatting Guide

> **Last Updated:** 2025-12-31
> **Project:** Tokyo Mate (Trip Mate News Blog)
> **Purpose:** Comprehensive guide for blog post creation, formatting, and SEO optimization

This document provides detailed guidelines for creating and formatting blog content for the Tokyo Mate multilingual travel blog.

---

## Table of Contents

1. [Post Front Matter Structure](#post-front-matter-structure)
2. [Multilingual Content](#multilingual-content)
3. [Tag Management](#tag-management)
4. [Category Management](#category-management)
5. [SEO Optimization](#seo-optimization)
6. [Images](#images)
7. [Blog Post Format](#blog-post-format)
8. [Editor's Note](#editors-note)
9. [Related Posts](#related-posts)
10. [Related Guides / Footer Links](#related-guides--footer-links)
11. [Klook Affiliate Link Conversion](#klook-affiliate-link-conversion)

**⚠️ IMPORTANT:** This guide covers blog formatting, SEO, and content structure. If you're migrating from Naver Blog, you MUST also review **[MIGRATION_GUIDE.md](./MIGRATION_GUIDE.md)** for the complete migration workflow and content translation rules.

---

## Post Front Matter Structure

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

---

## Multilingual Content

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

---

## 3. Cultural Adaptation & Writing Style

### Translation System Prompts

Use these prompts when translating or transcreating content:

#### English (EN)
> "You are a friendly travel blogger specializing in Tokyo travel for Western tourists. Please translate/transcreate the following text into English. Guidelines:
> - **Tone**: Conversational, enthusiastic, and helpful. Like a local friend giving advice.
> - **Keywords**: Hidden gems, Authentic vibe, Local experience.
> - **Goal**: Highlight the unique experience from a foreigner's perspective but ensure practical info is accurate."

#### Japanese (JA)
> "あなたは東京の魅力を発信する案内人です。以下の韓国語の文章を、日本の読者に向けて自然な日本語に翻訳・リライトしてください。 ガイドライン:
> - **トーン**: 丁寧語（です・ます調）。親しみやすく、かつ謙虚な姿勢で。
> - **ポイント**: 「外国人（韓国人）の視点」からの新鮮な発見や、「コスパ」「穴場」「映え」などのキーワードを盛り込んでください。"

#### Chinese (ZH-CN)
> "你是一位精通东京旅游的小红书(Xiaohongshu)博主。请把下面的韩文文章改写成中文（简体）。 指南:
> - **语气**: 热情、直接、充满干货（Useful info）。使用一些流行的网络用语。
> - **关键词**: 打卡, 避雷, 宝藏店铺, 必去。
> - **排版**: 适当添加 emoji (📍, ✨, 📷) 让文章读起来更有趣。"

### Specific Adaptation Rules

- **English (EN)**: Use engaging, traveler-friendly expressions (American English). Focus on what international visitors want to know.
- **Japanese (JA)**:
    - **NEVER use "日本の" prefix** - readers are Japanese (e.g., "日本のコーヒー" → "コーヒー").
    - Use specific location names instead of "Japan".
    - **DELETE all tax-free/免税 sections** - only relevant to foreign tourists.
- **Chinese (ZH-CN)**:
    - Use popular travel terminology: "攻略", "性价比", "必打卡".
    - Focus on practical information tourists need.

### 4. Financial Information & Pricing
- **Standardize Currency to USD**: For global accessibility, convert Korean Won (KRW) or Japanese Yen (JPY) estimates to **USD** in the text content (not headers).
    - **Standard Rate (KRW to USD)**: 10,000 KRW ≈ **$7.50** | 13,000 KRW ≈ **$10**.
    - **Standard Rate (JPY to USD)**: Use current approximate rates (e.g., 1,500 JPY ≈ $10).
    - **Format**: Use the `$` symbol (e.g., "only about $7.50").

### No AI Writing Traces
- Avoid overly formal or robotic language patterns.
- No generic AI phrases like "In conclusion", "It's worth noting".
- Use natural, human-like variations in sentence structure.
- Include personal touches and authentic observations.

---

## Tag Management

### Tag Management and Multilingual Tags

**⚠️ CRITICAL RULE: Tags Must Match Content Language**

When creating or editing blog posts, **ALWAYS** ensure tags match the language of the post content:

- ✅ **English posts** (`content/en/posts/`) → **English tags only**
- ✅ **Japanese posts** (`content/ja/posts/`) → **Japanese tags only**
- ✅ **Chinese posts** (`content/zh-cn/posts/`) → **Chinese tags only**
- ❌ **NEVER mix languages** in tags within a single post

### Shop Name & Terminology Notation Rules

To ensure clarity and professional presentation across all languages, follow these rules for shop names and specific terminology:

**1. English & Chinese (Simplified) Posts:**
- Use the **English/International Name** followed by the **Original Japanese (Kanji/Kana)** in parentheses.
- **NEVER** repeat the same notation in both places.
- ✅ **CORRECT:** `Suzukien (壽々喜園)`, `Asakusa Silk Pudding (浅草シルクプリン)`
- ❌ **WRONG:** `Kagetsu-do (Kagetsu-do)`, `Asakusa Menchi (Asakusa Menchi)`

**2. Japanese Posts:**
- Use the **Original Japanese/Kanji** directly.
- **STRICT PROHIBITION**: **NEVER** add parenthetical explanations, English notations, or furigana/bracketed readings for standard names.
- ✅ **CORRECT:** `浅草花月堂`, `和からし`, `壽々喜園`, `来宮神社`
- ❌ **WRONG:** `浅草花月堂（かげつどう）`, `和からし（マスタード）`, `壽々喜園（すずきえん）`, `来宮神社（きのみやじんじゃ）`
- ❌ **WRONG:** `熱海プリン (熱海プリン)` (Redundant repetition)

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

### Tag Naming Conventions

**English-Japanese Tag Mapping:**

For complete tag mapping reference, see existing blog posts or use the conversion script `convert_tags_to_japanese.py`.

**Key Examples:**
- `tokyo` → `東京`
- `tokyo-restaurants` → `東京レストラン`
- `tokyo-guide` → `東京ガイド`
- `shinjuku` → `新宿`
- `shibuya` → `渋谷`

**Tag Format Rules:**

- **English tags:** Use `kebab-case` (lowercase with hyphens)
  - ✅ `tokyo-restaurants`, `christmas-market`, `travel-tips`
  - ❌ `Tokyo_Restaurants`, `ChristmasMarket`, `Travel Tips`

- **Japanese tags:** Use natural Japanese text (hiragana, katakana, kanji)
  - ✅ `東京レストラン`, `クリスマスマーケット`, `旅行情報`

- **Numbers/Years:** Keep as-is in both languages
  - Both: `2025`, `2026`

---

## Category Management

### Category Management and Multilingual Categories

**⚠️ CRITICAL RULE: Categories Must Match Content Language**

Just like tags, categories must match the language of the post content:

- ✅ **English posts** (`content/en/posts/`) → **English categories only**
- ✅ **Japanese posts** (`content/ja/posts/`) → **Japanese categories only**
- ✅ **Chinese posts** (`content/zh-cn/posts/`) → **Chinese categories only**
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

### Category Naming Conventions

**English-Japanese Category Mapping:**

For complete category mapping reference, see existing blog posts or use the conversion script `convert_categories_to_japanese.py`.

**Common Categories:**
- `Travel Guide` → `旅行ガイド`
- `Tokyo Travel Guide` → `東京旅行ガイド`
- `Food & Dining` → `グルメ`
- `Shopping` → `ショッピング`
- `Events & Festivals` → `イベント＆フェスティバル`

**⚠️ Standardized Japanese Categories (Strict):**
To avoid duplication, use these exact terms for Japanese posts:
- **`イベント＆フェスティバル`** (Unified from `イベント`, `イベント・フェスティバル`)
- **`グルメ`** (Unified from `グルメガイド`)
- **`レストラン`** (Unified from `レストランレビュー`, `東京レストラン`)

**Category Best Practices:**

1. **Keep categories broad** - Use 1-2 categories per post
2. **Use specific area tags** - For location-specific content, use area names as tags instead of categories
3. **Consistency** - Stick to existing category patterns for consistency across the site

---

## SEO Optimization

### SEO-Optimized Content Conversion (Korean → EN/JA/ZH-CN)

When converting Korean Naver blog posts to English, Japanese, and Chinese (Simplified), follow these SEO optimization guidelines:

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

**Chinese (Simplified) Titles:**
- Length: **40-60 characters** (key info in first 40 chars for Baidu/Google CN)
- Include primary keyword in Chinese at the beginning
- Use popular suffixes: `完全攻略`, `最全指南`, `必看`, `推荐`
- Format: `[地点/活动][关键词]完全攻略` or `【地点】[关键词]最全指南`
- Use numbers for appeal: `2025年`, `TOP 10`, `必打卡`

**Examples:**
```yaml
# English (74 chars - OK because key info "Roppongi Christmas Illumination 2025" is in first 40)
title: "Roppongi Christmas Illumination 2025: Complete Guide to Tokyo's Best Light Display"

# Japanese (42 chars - OK because key info "六本木イルミネーション2025" is in first 20)
title: "六本木イルミネーション2025完全ガイド - 点灯時間、クリスマスマーケット"

# Chinese (48 chars - key info "六本木圣诞灯光秀2025" in first 20)
title: "六本木圣诞灯光秀2025完全攻略 - 点灯时间、圣诞市集、交通指南"
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

**Chinese (Simplified) Description:**
- Length: **120-160 characters** (Baidu displays ~140-160)
- Include primary Chinese keywords naturally
- Use engaging language: `超详细`, `必看`, `干货满满`, `实用攻略`
- Front-load key info within first 120 chars
- End with call-to-action: `快来看看吧`, `收藏备用`, `建议收藏`

**Examples:**
```yaml
# English (168 chars)
description: "Complete guide to Roppongi Christmas Illumination 2025 in Tokyo. Dates, hours, best photo spots, access info, and insider tips for the perfect winter visit."

# Japanese (125 chars)
description: "六本木クリスマスイルミネーション2025の完全ガイド。開催期間、点灯時間、撮影スポット、アクセス情報を徹底解説。冬の東京観光に必見です。"

# Chinese (148 chars)
description: "六本木圣诞灯光秀2025完全攻略。活动时间、点灯时刻、最佳拍照地点、交通指南一网打尽。东京冬季旅游必看，超详细实用信息，建议收藏。"
```

#### 3. URL Slug Optimization

**Rules:**
- Use **English keywords only** (even for Japanese and Chinese posts)
- Lowercase, hyphen-separated
- Include primary keyword + location if relevant
- **Do NOT** include years or dates (e.g., `2025`, `2026`). Evergreen URLs are better for SEO.
- Keep under 60 characters
- Avoid stop words (the, a, an, of, etc.)

**Examples:**
```
✅ Good: roppongi-christmas-illumination
✅ Good: shinjuku-gyoen-autumn-guide
✅ Good: tokyo-ramen-street-best-shops

❌ Bad: roppongi-christmas-illumination-2025 (Do not use years)
❌ Bad: the-best-roppongi-christmas-illumination-of-2025
❌ Bad: 六本木イルミネーション (Japanese characters)
❌ Bad: 六本木圣诞灯光秀 (Chinese characters)
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

**Chinese (Simplified) H2 Examples:**
```html
<h2>📍 交通位置信息</h2>
<h2>🎄 2025年活动时间安排</h2>
<h2>📸 最佳拍照打卡点</h2>
<h2>🍽️ 周边美食餐厅推荐</h2>
<h2>💡 实用游览小贴士</h2>
```

#### 5. Image Alt Text Optimization

**Rules:**
- Describe the image content clearly
- Include relevant keywords naturally
- Language-specific alt text (EN for English, JA for Japanese, ZH-CN for Chinese)
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

<!-- Chinese (Simplified) -->
<img src="..." alt="六本木之丘圣诞灯光秀，巨型圣诞树夜景">
<img src="..." alt="东京晴空塔圣诞市集美食摊位和游客">
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

**Chinese (Simplified) Keywords Focus:**
- 「东京 [主题] 攻略」
- 「[地点] 旅游 指南」
- 「[活动] 2025 时间 门票」
- 「[地点] 交通 怎么去」
- 「[主题] 完全攻略 推荐」
- 「打卡 必去 [地点]」
- 「[地点] 美食 购物 推荐」

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
□ Title: EN 50-80 chars (key info in first 55) / JA 35-55 chars (key info in first 35) / ZH-CN 40-60 chars (key info in first 40)
□ Description: EN 150-180 chars / JA 100-140 chars / ZH-CN 120-160 chars with keyword front-loaded
□ Slug: English, keyword-rich, under 60 chars
□ H2 headings: Include keywords, use emojis for visual appeal
□ Images: All have descriptive alt text in target language
□ featured_image: Set for social media preview
□ translationKey: Identical across EN/JA/ZH-CN versions
□ Tags: 5-7 relevant tags per post (in target language)
□ Categories: 1-2 appropriate categories (in target language)
□ Internal links: Link to related posts where relevant
```

---

## Images

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
# Use the custom Python script (automatically reads from naver.md)
python3 download_naver_images.py <POST_SLUG>

# Example:
python3 download_naver_images.py tokyo-restaurant-guide
```

See `README_IMAGE_DOWNLOAD.md` for detailed instructions.

---

## Blog Post Format

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

**Grouped Images (2, 3, or 4+ images side-by-side):**

When Naver HTML contains image groups (e.g., `se-imageGroup-col-2`), use **inline flex styles** to preserve the original image ratios from the Naver source. **Do NOT use Markdown for these.**

**How to determine ratios:**
1. Find the group in `naver.md` (look for `se-imageGroup-col-N`)
2. Extract each image's `width:XX%` value
3. Convert to flex decimal (e.g., `width:51.77%` → `flex: 0.518`)
4. Verify ratios in each row sum to ~1.0

```html
<!-- 2 images side-by-side (extract exact ratios from naver.md) -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.518;">
    <img src="/images/posts/post-slug-10.jpg" alt="First image" style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.482;">
    <img src="/images/posts/post-slug-11.jpg" alt="Second image" style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">Caption for both images</figcaption>

<!-- 3 images side-by-side -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.333;">
    <img src="/images/posts/post-slug-12.jpg" alt="First image" style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.333;">
    <img src="/images/posts/post-slug-13.jpg" alt="Second image" style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.334;">
    <img src="/images/posts/post-slug-14.jpg" alt="Third image" style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">Caption for all three images</figcaption>

<!-- 4+ images: use multiple flex rows (one row per N columns) -->
<!-- Row 1 -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.5;">
    <img src="/images/posts/post-slug-15.jpg" alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.5;">
    <img src="/images/posts/post-slug-16.jpg" alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<!-- Row 2 -->
<div style="display: flex; gap: 10px; margin: 0 0 20px 0;">
  <figure style="margin: 0; flex: 0.5;">
    <img src="/images/posts/post-slug-17.jpg" alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.5;">
    <img src="/images/posts/post-slug-18.jpg" alt="..." style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">Caption for all four images</figcaption>
```

**Important Notes:**
- ✅ Every image, whether single or in a group, MUST be in its own `<figure>` tag.
- ✅ All figcaptions MUST use inline style: `style="font-size: 0.7em; text-align: center;"`
- ✅ For image groups, the `figcaption` goes OUTSIDE the flex `<div>`, not inside.
- ✅ For multi-row groups (4+ images), use one flex `<div>` per row.
- ✅ Multi-row margin pattern: first row `margin: 20px 0`, middle rows `margin: 0`, last row `margin: 0 0 20px 0`.
- ❌ NEVER estimate ratios — always extract exact values from `naver.md`.
- ❌ Do NOT use CSS classes (`image-group-2/3/4`) for Naver migrations — use inline flex for ratio preservation.

**Google Maps Link (Location Information):**

When a blog post includes a location (restaurant, attraction, etc.), do **NOT** use an interactive map embed (`<iframe>`). Instead, add a simple text link.

**Format:**
`📍 [Location Name] Google Map Link`

**Example (English):**
`<p>📍 <a href="https://maps.app.goo.gl/..." target="_blank" rel="noopener" style="color: #667eea; text-decoration: underline;"><strong>View on Google Maps</strong></a></p>`

**Example (Japanese):**
`<p>📍 <a href="https://maps.app.goo.gl/..." target="_blank" rel="noopener" style="color: #667eea; text-decoration: underline;"><strong>Googleマップで見る</strong></a></p>`

**Example (Chinese):**
`<p>📍 <a href="https://maps.app.goo.gl/..." target="_blank" rel="noopener" style="color: #667eea; text-decoration: underline;"><strong>在 Google 地图上查看</strong></a></p>`

**Important Notes:**
- 🚫 **NO** `<iframe>` embeds.
- ✅ Link text should be standardized as shown above (**BOLD** and using specific language phrases).
- ✅ Add a `📍` emoji at the beginning of the line.
- ✅ Use `style="color: #667eea; text-decoration: underline;"` for the anchor tag.

---

## Klook Affiliate Link Conversion
When migrating Naver Blog posts containing Klook affiliate links, you MUST convert them to the **Tripmate account** and localize them for each language.

### 1. Tripmate Affiliate IDs
- **Affiliate ID (AID)**: `110453`
- **Ad ID (ADID)**: `1208343`
- **UTM Source**: `tripmate`

### 2. Localization Rules
You must explicitly set the language path and currency per language version to ensure a localized experience.

| Language | URL Path | Currency Parameters |
| :--- | :--- | :--- |
| **English (EN)** | `/en-US/` | `?currency=USD&n_currency=USD&ignore_ip=1` |
| **Japanese (JA)** | `/ja/` | `?currency=JPY&n_currency=JPY&ignore_ip=1` |
| **Chinese (ZH-CN)** | `/zh-CN/` | `?currency=CNY&n_currency=CNY&ignore_ip=1` |

### 3. Conversion Workflow
1.  **Extract Destination**: Identify the original product page URL (the `k_site` parameter).
2.  **Clean Legacy Params**: Remove Naver-specific tracking (e.g., `clickId`, `aff_klick_id`).
3.  **Localize Destination**: Swap the language prefix and append the **double currency** parameters + `ignore_ip=1`.
4.  **Rebuild Wrapper**: Combine with Tripmate AID/ADID and `utm_source=tripmate`.

**Example (Original Post Redirect):**
`https://affiliate.klook.com/redirect?aid=110453&aff_adid=1208343&utm_source=tripmate&k_site=https%3A%2F%2Fwww.klook.com%2Fen-US%2Factivity%2F1410-skyliner-tokyo%2F%3Fcurrency%3DUSD%26n_currency%3DUSD%26ignore_ip%3D1`

---

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

/* Image Group Layout — use inline flex for Naver migrations        */
/* .image-group-2/3/4 CSS classes exist but inline flex is preferred */
/* to preserve original Naver image ratios (see SKILL.md Step 2.3)  */
```

**Image Groups for Naver Migrations:**
- Use inline flex styles (NOT CSS classes) to preserve original Naver ratios
- Extract exact `width:XX%` values from `naver.md` and convert to `flex` decimals
- For multi-row groups (4+ images), use one flex `<div>` per row
- See **SKILL.md Step 2.3** for complete examples and rules
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

<!-- Example of grouped images (2 side-by-side with inline flex) -->
<div style="display: flex; gap: 10px; margin: 20px 0;">
  <figure style="margin: 0; flex: 0.5;">
    <img src="/images/posts/tokyo-guide-04.jpg" alt="First image" style="width: 100%; height: auto; display: block;">
  </figure>
  <figure style="margin: 0; flex: 0.5;">
    <img src="/images/posts/tokyo-guide-05.jpg" alt="Second image" style="width: 100%; height: auto; display: block;">
  </figure>
</div>
<figcaption style="font-size: 0.7em; text-align: center;">Caption for both images</figcaption>

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
- ✅ Use inline flex styles for side-by-side image layouts (preserves original Naver ratios)
- 🎨 CSS is automatically loaded via `layouts/partials/head-additions.html`

**CSS Files:**
- `/static/css/blog-cards.css` - Blog card styles (list pages)
- `/static/css/blog-post-common.css` - Common blog post content styles
- `/static/css/related-posts.css` - Related posts sidebar styles

**⚠️ CSS Loading Best Practice:**
To ensure robust CSS loading across all page depths (especially taxonomy pages), use root-relative paths in `layouts/partials/site-style.html`. Always prefer direct `partial` calls over `partials.IncludeCached` if context issues arise.
- `/static/css/blog-post-common.css` - Blog post content styles
- `/static/css/related-posts.css` - Related posts sidebar styles
- All three are loaded globally via `head-additions.html`

---

## Related Guides / Footer Links

For the "Related Guides" section at the bottom of the post, follow these strict styling rules to ensure 1:1 cross-lingual consistency:

### 1. Emoji & Anchor Tag
The "👉" emoji must be placed **INSIDE** the `<a>` tag to ensure it inherits the link styling and is part of the clickable area.

*   ✅ **CORRECT**: `<p><a href="...">👉 <strong>Title</strong></a></p>`
*   ❌ **WRONG**: `<p>👉 <a href="..."><strong>Title</strong></a></p>`

### 2. Icon Consistency
The icons used in the H3 headers for related guides (⛩️, 🍺, 🏙️, 🍭, etc.) must match the English version exactly across all Japanese and Chinese versions.

### 3. Link Prefix Rules
- **English (EN)**: Use `/posts/[slug]/` (**NO** `/en/` prefix).
- **Japanese (JA)**: Use `/ja/posts/[slug]/`.
- **Chinese (ZH)**: Use `/zh-cn/posts/[slug]/`.

### 4. Placeholder Rules (Unmigrated Posts)
- **Strictly use `href="#"`** when the target Hugo file does not exist.
- **DO NOT** use self-referential links (current post slug) as placeholders.
- **TODO Comment**: Always add the mandatory TODO comment above the link as defined in `MIGRATION_GUIDE.md`.
- **Text Suffixes**: **DO NOT** add custom text suffixes like "(Coming Soon)" or "(即将上线)" unless explicitly requested. The placeholder state is managed via the TODO comment.

### 5. Formatting Snippet
```html
### ⛩️ Related Guide Title
<p>Description text goes here.</p>
<!-- TODO: Update link after migration
     Naver: https://blog.naver.com/tokyomate/[ID]
     Hugo: /posts/[SLUG]/ -->
<p><a href="#" style="color: #667eea;">👉 <strong>Standardized Link Title</strong></a></p>
```

---

## Editor's Note

### Editor's Note Section

**⚠️ MANDATORY: Add Editor's Note to ALL blog posts - NO EXCEPTIONS**

**CRITICAL RULE:** Every single blog post MUST include an Editor's Note section at the bottom (before closing `</div>` tag) with language-specific content and the correct Naver blog URL.

**This is NOT optional.** All blog posts, regardless of content type or source, require this section.

**Format:**

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

**How to Find Naver Post ID:**

1. Open `LINK_MAPPING.md`
2. Find the Hugo slug in the Quick Reference Table
3. Use the corresponding Naver ID from the first column
4. Replace `[NAVER_POST_ID]` with the actual ID

**Example:**

For post `shinjuku-chuo-park`:
- Naver ID from LINK_MAPPING.md: `224101626196`
- Editor's Note link: `https://blog.naver.com/tokyomate/224101626196`

**Placement:**
- Position: After all content, before closing `</div>` tag
- Always at the very end of the blog post body

**Styling:**
- Title: Left-aligned, italic, bold
- Box: Light gray background (#f7f7f7), blue left border (#667eea)
- Padding: 15px
- Link color: Purple-blue (#667eea) with underline

---

## Related Posts

### Related Posts Section

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

**End of CONTENT_GUIDELINES.md**

