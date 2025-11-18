# Naver to Hugo Link Mapping

> **Purpose:** Track Naver blog post URLs and their corresponding Hugo slugs for internal link conversion
> **Last Updated:** 2025-11-18
> **Status:** 🔄 In Progress - Backfilling existing posts

---

## How to Use This File

When migrating a Naver blog post to Hugo:
1. Extract the Naver post ID from the HTML (`copyBtn` title attribute)
2. Add a new entry below with all internal links found
3. When all referenced posts are migrated, update internal links in Hugo posts

---

## Migrated Posts

### 2025-11-18: Evangelion 30th Anniversary Exhibition

**Naver URL:** `https://blog.naver.com/tokyomate/[TBD]`
**Hugo Slug (EN):** `evangelion-30th-roppongi-2025`
**Hugo Slug (JA):** `evangelion-30th-roppongi-2025`
**Title (Original):** [TBD]
**Created Date:** 2025-11-16
**Migration Date:** [Prior to tracking]
**Status:** ✅ Migrated (links need update)

**Internal Links Found:**
- `223681272647` → ⏳ Pending (How to Get to Roppongi Hills and Coin Locker Locations)
- `223987954990` → ⏳ Pending (2025 Roppongi Hills Observatory Complete Guide)
- `223988228389` → ⏳ Pending (Complete Guide to Roppongi Attractions)
- `223993881300` → ⏳ Pending (Tokyo Roppongi Restaurant Map)
- `224065668379` → ✅ Mapped to `roppongi-christmas-illumination-2025`

**Action Needed:**
- Find original Naver URL for this post
- Update 4 pending links once target posts are migrated

---

### [Template for New Entries]

**Naver URL:** `https://blog.naver.com/tokyomate/XXXXXXXXX`
**Hugo Slug (EN):** `slug-name`
**Hugo Slug (JA):** `slug-name`
**Title (Original):** Korean Title
**Created Date:** YYYY-MM-DD
**Migration Date:** YYYY-MM-DD
**Status:** ✅ Migrated / 🔄 In Progress / ⏳ Pending

**Internal Links Found:**
- `NNNNNNNNN` → Status (Description)

**Action Needed:**
- List of actions

---

## Quick Reference Table

| Naver ID | Hugo Slug (EN/JA) | Status | Links to Update |
|----------|-------------------|--------|-----------------|
| [TBD] | evangelion-30th-roppongi-2025 | ✅ | 4 pending |
| [TBD] | roppongi-christmas-illumination-2025 | ✅ | ? |
| [TBD] | marunouchi-illumination-2025 | ✅ | ? |
| [TBD] | hibiya-midtown-illumination-2025 | ✅ | ? |

---

## Pending Link References

These Naver post IDs are referenced but not yet migrated:

| Naver ID | Referenced In | Description |
|----------|---------------|-------------|
| 223681272647 | evangelion-30th-roppongi-2025 | How to Get to Roppongi Hills and Coin Locker Locations |
| 223987954990 | evangelion-30th-roppongi-2025 | 2025 Roppongi Hills Observatory Complete Guide |
| 223988228389 | evangelion-30th-roppongi-2025 | Complete Guide to Roppongi Attractions |
| 223993881300 | evangelion-30th-roppongi-2025 | Tokyo Roppongi Restaurant Map |

---

## Link Conversion Script

When a referenced post is migrated, use this pattern to update links:

```bash
# Find and replace Naver links with Hugo links
# Example: Convert 224065668379 to roppongi-christmas-illumination-2025

# English posts
sed -i 's|https://blog.naver.com/tokyomate/224065668379|/en/posts/roppongi-christmas-illumination-2025/|g' content/en/posts/*.md

# Japanese posts
sed -i 's|https://blog.naver.com/tokyomate/224065668379|/ja/posts/roppongi-christmas-illumination-2025/|g' content/ja/posts/*.md
```

---

## Statistics

- **Total Posts Migrated:** ~29 (EN) / ~28 (JA)
- **Posts with Naver Links:** 23 (EN) / 22 (JA)
- **Naver IDs Tracked:** 5
- **Links Updated:** 0
- **Pending Updates:** Many

---

## Notes

- This file is tracked in Git for collaboration
- Update this file EVERY TIME you migrate a new post
- Include Naver ID extraction in migration workflow
- Run link conversion script after batch migrations
