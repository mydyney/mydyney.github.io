# Ezoic Ad Placement Setup Guide

This guide explains how to add Ezoic ads to your Hugo site once you have Placement IDs from the Ezoic dashboard.

---

## Prerequisites

✅ **Step 1 Complete:** Ezoic scripts added to `head-additions.html`
✅ **Step 2 Complete:** ads.txt automation configured
⏳ **Step 3:** Waiting for Ezoic Placement IDs

---

## How to Get Placement IDs

1. Log in to your [Ezoic Dashboard](https://pubdash.ezoic.com/)
2. Go to **Monetization** → **Ad Placements**
3. Click **"Create New Placement"**
4. Configure placement settings (size, type, position)
5. Copy the **Placement ID** (e.g., `101`, `102`, etc.)

---

## Method 1: Add Ads in Markdown Posts (Recommended)

Use the `ezoic-ad` shortcode directly in your blog post content.

### Syntax

```markdown
{{< ezoic-ad PLACEMENT_ID >}}
```

### Example Usage in Blog Post

**File:** `content/en/posts/tokyo-guide.md`

```markdown
---
title: "Tokyo Travel Guide"
date: 2025-12-04T10:00:00+09:00
---

<div class="blog-container">

<p style="text-align: center; font-size: 1.1rem; color: #555;">
Welcome to our Tokyo travel guide!
</p>

<!-- Ad Placement: Top of Post (Below Intro) -->
{{< ezoic-ad 101 >}}

<h2>Best Things to Do in Tokyo</h2>

<p>Tokyo offers amazing attractions...</p>

<!-- Ad Placement: Middle of Post -->
{{< ezoic-ad 102 >}}

<h2>Where to Stay in Tokyo</h2>

<p>Accommodation recommendations...</p>

<!-- Ad Placement: Bottom of Post -->
{{< ezoic-ad 103 >}}

</div>
```

---

## Method 2: Add Ads in Layout Templates

For ads that appear on every page (e.g., sidebar, header, footer).

### Syntax

```go-html-template
{{ partial "ezoic-ad.html" (dict "id" PLACEMENT_ID) }}
```

### Example: Add Ad to Post Layout

**File:** `layouts/post/single.html`

```go-html-template
{{ define "main" }}
  <article>
    <h1>{{ .Title }}</h1>

    <!-- Ad Placement: After Title -->
    {{ partial "ezoic-ad.html" (dict "id" 101) }}

    <div class="content">
      {{ .Content }}
    </div>

    <!-- Ad Placement: After Content -->
    {{ partial "ezoic-ad.html" (dict "id" 102) }}
  </article>
{{ end }}
```

### Example: Add Ad to Sidebar

**File:** `layouts/partials/sidebar.html`

```go-html-template
<aside class="sidebar">
  <!-- Ad Placement: Top of Sidebar -->
  {{ partial "ezoic-ad.html" (dict "id" 201) }}

  <h3>Recent Posts</h3>
  {{ range first 5 .Site.RegularPages }}
    <a href="{{ .Permalink }}">{{ .Title }}</a>
  {{ end }}

  <!-- Ad Placement: Bottom of Sidebar -->
  {{ partial "ezoic-ad.html" (dict "id" 202) }}
</aside>
```

---

## Recommended Ad Positions for Blog Posts

Based on best practices for blog monetization:

| Position | Placement ID | Description | Performance |
|----------|--------------|-------------|-------------|
| **Top of Post** | 101 | Right after intro paragraph | 🔥 High visibility |
| **Mid-Article 1** | 102 | After first major section (H2) | ⭐ Good engagement |
| **Mid-Article 2** | 103 | After second major section | ⭐ Good engagement |
| **Bottom of Post** | 104 | End of content, before comments | ✅ Decent |
| **Sidebar Top** | 201 | Top of related posts sidebar | 🔥 Always visible |
| **Sidebar Bottom** | 202 | Below related posts | ✅ Decent |

**Note:** Use actual Placement IDs from your Ezoic dashboard. These are just examples.

---

## Multiple Ads on Same Page (Optimization)

If a page has multiple ads, you can load them all at once for better performance.

### Option A: Multiple Shortcodes (Automatic)

The shortcodes handle this automatically. Just add multiple instances:

```markdown
{{< ezoic-ad 101 >}}
...content...
{{< ezoic-ad 102 >}}
...content...
{{< ezoic-ad 103 >}}
```

Each ad loads independently.

### Option B: Manual Batch Loading (Advanced)

For better performance, you can create a custom partial that loads all ads at once:

**File:** `layouts/partials/ezoic-ads-batch.html`

```html
<!-- Ezoic Ad Placeholders -->
<div id="ezoic-pub-ad-placeholder-101"></div>
<div id="ezoic-pub-ad-placeholder-102"></div>
<div id="ezoic-pub-ad-placeholder-103"></div>

<!-- Load all ads with single call -->
<script>
    ezstandalone.cmd.push(function () {
        ezstandalone.showAds(101, 102, 103);
    });
</script>
```

**Usage in layout:**

```go-html-template
{{ partial "ezoic-ads-batch.html" . }}
```

---

## Important Notes

⚠️ **DO NOT add styling to ad containers**

```html
<!-- ❌ WRONG - May cause blank spaces -->
<div id="ezoic-pub-ad-placeholder-101" style="height: 250px; width: 300px;"></div>

<!-- ✅ CORRECT - No styling -->
<div id="ezoic-pub-ad-placeholder-101"></div>
```

⚠️ **Remove other ad network code**

Before Ezoic ads go live, remove any existing ad code (Google AdSense, etc.) to avoid conflicts.

---

## Testing

### Local Development

Ezoic ads won't display on `localhost`. To test:

1. Deploy to production (https://tripmate.news)
2. Visit your site in a browser
3. Check that ad placeholders appear correctly
4. Wait for Ezoic approval to see actual ads

### Verify Ad Placeholders

Check browser console for Ezoic messages:

```javascript
// Open Developer Tools → Console
// You should see Ezoic initialization messages
```

---

## Quick Setup Checklist

Once you receive Placement IDs from Ezoic:

- [ ] Create placements in Ezoic dashboard
- [ ] Note down Placement IDs (101, 102, 103, etc.)
- [ ] Add `{{< ezoic-ad ID >}}` shortcodes to blog posts
- [ ] Test on production site (ads won't show on localhost)
- [ ] Remove old ad network code (if any)
- [ ] Monitor Ezoic dashboard for performance

---

## Example: Full Blog Post with Ads

**File:** `content/en/posts/sample-post.md`

```markdown
---
title: "Complete Tokyo Restaurant Guide"
date: 2025-12-04T10:00:00+09:00
draft: false
tags: ["tokyo", "food", "restaurants"]
categories: ["Travel"]
featured_image: "/images/posts/tokyo-restaurants-01.jpg"
---

<div class="blog-container">

<p style="text-align: center; font-size: 1.1rem; color: #555;">
🍜 Discover the best restaurants in Tokyo!<br>
From ramen to sushi,<br>
Complete guide with locations and tips.
</p>

<!-- Ad: Top of Post -->
{{< ezoic-ad 101 >}}

<h2>Best Ramen Shops</h2>

<figure>
  <img src="/images/posts/tokyo-restaurants-02.jpg" alt="Ramen shop">
  <figcaption style="font-size: 0.7em; text-align: center;">Famous ramen shop in Shinjuku</figcaption>
</figure>

<p>Tokyo has amazing ramen shops...</p>

<!-- Ad: Mid-Article 1 -->
{{< ezoic-ad 102 >}}

<h2>Top Sushi Restaurants</h2>

<p>For the best sushi experience...</p>

<div class="info-box">
  <ul>
    <li><strong>Location:</strong> Tsukiji</li>
    <li><strong>Price:</strong> ¥5,000-10,000</li>
  </ul>
</div>

<!-- Ad: Mid-Article 2 -->
{{< ezoic-ad 103 >}}

<h2>Budget-Friendly Izakayas</h2>

<p>Great places for casual dining...</p>

<!-- Ad: Bottom of Post -->
{{< ezoic-ad 104 >}}

</div>
```

---

## Next Steps

1. **Wait for Ezoic approval** (usually 1-2 weeks)
2. **Create placements** in Ezoic dashboard
3. **Add shortcodes** to blog posts using this guide
4. **Deploy and test** on production site
5. **Monitor performance** in Ezoic dashboard

---

## Support

- **Ezoic Dashboard:** https://pubdash.ezoic.com/
- **Ezoic Support:** Contact your onboarding specialist
- **Hugo Docs:** https://gohugo.io/documentation/

---

**Last Updated:** 2025-12-04
**Integration Status:** Step 1 & 2 Complete, Step 3 Pending Placement IDs
