# Naver to Hugo Link Mapping

> **Purpose:** Track Naver blog post URLs and their corresponding Hugo slugs for internal link conversion
> **Last Updated:** 2025-11-20
> **Status:** ✅ Complete - 35 posts mapped

---

## How to Use This File

When migrating a Naver blog post to Hugo:
1. Extract the Naver post ID from the HTML (`copyBtn` title attribute)
2. Add a new entry below with all internal links found
3. When all referenced posts are migrated, update internal links in Hugo posts
4. Use the conversion script at the bottom to batch replace links

---

## Quick Reference Table

| Naver ID | Hugo Slug (EN/JA) | Date | Status |
|----------|-------------------|------|--------|
| 224079692802 | tamiya-plamodel-factory-tokyo-shimbashi | 2025-11-18 | ✅ |
| 224079015302 | meiji-jingu-gaien-ginkgo-avenue-tokyo | 2025-11-17 | ✅ |
| 224078737491 | yebisu-garden-place-illumination-christmas-market-2025 | 2025-11-17 | ✅ |
| 224078087405 | toranomon-hills-hermes-event-2025 | 2025-11-16 | ✅ |
| 224077357970 | evangelion-30th-roppongi-2025 | 2025-11-16 | ✅ |
| 224076977654 | roppongi-midtown-christmas-2025 | 2025-11-15 | ✅ |
| 224076762296 | hibiya-midtown-illumination-2025 | 2025-11-15 | ✅ |
| 224076486004 | marunouchi-illumination-2025 | 2025-11-15 | ✅ |
| 224074888771 | tokyo-skytree-christmas-market-2025 | 2025-11-13 | ✅ |
| 224073553885 | mitsui-kisarazu-black-friday-2025 | 2025-11-12 | ✅ |
| 224073290696 | shinjuku-luggage-storage | 2025-11-12 | ✅ |
| 224072546243 | shinjuku-liquor-shops | 2025-11-11 | ✅ |
| 224072190712 | narita-to-shinjuku-2025 | 2025-11-11 | ✅ |
| 224071675259 | takumi-tatsuhiro-shinjuku-2025 | 2025-11-11 | ✅ |
| 224070032613 | shinjuku-gyoen-guide-2025 | 2025-11-09 | ✅ |
| 224068891338 | shinjuku-oiwake-dango-honpo | 2025-11-08 | ✅ |
| 224068585112 | shinjuku-golden-gai-vs-omoide-yokocho | 2025-11-08 | ✅ |
| 224067094205 | shinjuku-to-disneyland-bus-guide | 2025-11-06 | ✅ |
| 224066800060 | tokyo-crafts-popup-stores-guide | 2025-11-06 | ✅ |
| 224066173929 | shinjuku-epitaph-curry-review | 2025-11-06 | ✅ |
| 224065668379 | roppongi-christmas-illumination-2025 | 2025-11-05 | ✅ |
| 224064750249 | shinjuku-sekaido-stationery-shopping-guide | 2025-11-04 | ✅ |
| 224064132817 | narita-airport-terminal1-duty-free-coupon-guide | 2025-11-04 | ✅ |
| 224063760866 | shinjuku-kids-parks-guide | 2025-11-04 | ✅ |
| 224062023485 | tokyo-metropolitan-govt-observatory | 2025-11-04 | ✅ |
| 224060336353 | tokyo-disneyland-complete-guide | 2025-10-31 | ✅ |
| 224059082171 | yokohama-katsuretsuan-tonkatsu | 2025-10-30 | ✅ |
| 224057793409 | roppongi-hills-hello-kitty-popup-2025 | 2025-10-29 | ✅ |
| 224057078032 | yokohama-pavlov-cafe-pound-cake | 2025-10-28 | ✅ |
| 224055756731 | tokyo-3-day-christmas-illumination-itinerary | 2025-10-27 | ✅ |
| 224054635720 | daikanyama-asakura-house | 2025-10-26 | ✅ |
| 224052787206 | yokohama-vanilla-beans-cafe | 2025-10-24 | ✅ |
| 224052237062 | yokohama-chinatown-keitokuchin-mapo-tofu | 2025-10-24 | ✅ |
| 224052117830 | shibuya-ikushika-rice-refill-restaurant | 2025-10-24 | ✅ |
| 223664743235 | shinanoya-roppongi-hills-supermarket | 2024-11-18 | ✅ |

---

## Pending Link References

These Naver post IDs are referenced in migrated posts but not yet migrated themselves:

| Naver ID | Referenced In | Description |
|----------|---------------|-------------|
| 223665548720 | yebisu-garden-place-illumination-christmas-market-2025 | Yebisu Brewery Tokyo Beer Museum Guide |
| 223668328703 | yebisu-garden-place-illumination-christmas-market-2025 | Yebisu Garden Place Free Observatory Top of Yebisu Guide |
| 223668826357 | yebisu-garden-place-illumination-christmas-market-2025 | 2024 Yebisu Garden Place Christmas Archive |
| 223678791563 | yebisu-garden-place-illumination-christmas-market-2025 | How to Get to Yebisu Garden Place and Coin Locker Locations |
| 223681272647 | evangelion-30th-roppongi-2025, roppongi-hills-hello-kitty-popup-2025 | How to Get to Roppongi Hills and Coin Locker Locations |
| 223987954990 | evangelion-30th-roppongi-2025 | 2025 Roppongi Hills Observatory Complete Guide |
| 223988228389 | evangelion-30th-roppongi-2025, roppongi-hills-hello-kitty-popup-2025, shinanoya-roppongi-hills-supermarket, meiji-jingu-gaien-ginkgo-avenue-tokyo | Complete Guide to Roppongi Attractions |
| 223991251786 | shinanoya-roppongi-hills-supermarket | Dassai 23, 39, 45 Official Japanese Prices and Brewery Tour Guide |
| 223993881300 | evangelion-30th-roppongi-2025 | Tokyo Roppongi Restaurant Map |
| 224010546735 | shinanoya-roppongi-hills-supermarket | Japanese Whisky Recommendations and Price Guide |
| 224032769630 | yebisu-garden-place-illumination-christmas-market-2025 | Yebisu Complete Guide (Garden Place, Beer Museum, Restaurants) |
| 224042431249 | roppongi-hills-hello-kitty-popup-2025, yebisu-garden-place-illumination-christmas-market-2025 | 2025 Tokyo Christmas Illumination BEST 5 (Omotesando, Marunouchi) |
| 224045496649 | roppongi-hills-hello-kitty-popup-2025 | 2025 Tokyo Christmas Markets Guide (Ueno, Azabudai, etc.) |
| 224044938913 | tamiya-plamodel-factory-tokyo-shimbashi | Tokyo Shimbashi & Shiodome Must-Visit Places Guide (Restaurants, Night Views) |
| 224039113760 | tamiya-plamodel-factory-tokyo-shimbashi | Japan Travel Discount Coupons Complete Guide (Don Quijote, Bic Camera, Department Stores) |
| 224022065518 | tamiya-plamodel-factory-tokyo-shimbashi | Japan Don Quijote Shopping List & Discount Coupons Guide |
| 224033964477 | tamiya-plamodel-factory-tokyo-shimbashi | Japan Kaldi Shopping List Must-Buy Recommendations |
| 224050488006 | tamiya-plamodel-factory-tokyo-shimbashi | Japan Convenience Store Shopping List BEST 10 |
| 224034429817 | tamiya-plamodel-factory-tokyo-shimbashi | Mitsui Outlet Park Kisarazu Discount Coupons & Brand Guide |
| 224027835049 | meiji-jingu-gaien-ginkgo-avenue-tokyo | Omotesando Complete Guide: Coffee, Shopping, Restaurants, Architecture |
| 224031114514 | meiji-jingu-gaien-ginkgo-avenue-tokyo, shibuya-ikushika-rice-refill-restaurant | Shibuya Attractions: Shibuya Sky Reservations to Shopping and Restaurants |
| 224038071853 | meiji-jingu-gaien-ginkgo-avenue-tokyo | 2025 Tokyo Autumn Foliage Season & BEST 5 Recommended Spots |
| 223979907748 | yokohama-chinatown-keitokuchin-mapo-tofu | Yokohama 1-Day Course: Chinatown Restaurants, Akarenga, Night Views Complete Guide |
| 223976102621 | yokohama-chinatown-keitokuchin-mapo-tofu | Yokohama Transportation Pass, 'Minato Burari Ticket' Complete Guide |

**Note:** The `tokyo-3-day-christmas-illumination-itinerary` post contains 30+ internal links. Extract them for detailed tracking when updating links.

---

## Link Conversion Script

When a referenced post is migrated, use this pattern to update links:

```bash
# Find and replace Naver links with Hugo links
# Example: Convert 224065668379 to roppongi-christmas-illumination-2025

# English posts (no language prefix - default language)
sed -i 's|https://blog.naver.com/tokyomate/224065668379|/posts/roppongi-christmas-illumination-2025/|g' content/en/posts/*.md

# Japanese posts (with /ja/ prefix)
sed -i 's|https://blog.naver.com/tokyomate/224065668379|/ja/posts/roppongi-christmas-illumination-2025/|g' content/ja/posts/*.md
```

**Batch Conversion Script:**

```bash
#!/bin/bash
# Convert all known Naver links to Hugo links

declare -A MAPPINGS=(
  ["224079692802"]="tamiya-plamodel-factory-tokyo-shimbashi"
  ["224079015302"]="meiji-jingu-gaien-ginkgo-avenue-tokyo"
  ["224078737491"]="yebisu-garden-place-illumination-christmas-market-2025"
  ["224078087405"]="toranomon-hills-hermes-event-2025"
  ["224077357970"]="evangelion-30th-roppongi-2025"
  ["224076977654"]="roppongi-midtown-christmas-2025"
  ["224076762296"]="hibiya-midtown-illumination-2025"
  ["224076486004"]="marunouchi-illumination-2025"
  ["224074888771"]="tokyo-skytree-christmas-market-2025"
  ["224073553885"]="mitsui-kisarazu-black-friday-2025"
  ["224073290696"]="shinjuku-luggage-storage"
  ["224072546243"]="shinjuku-liquor-shops"
  ["224072190712"]="narita-to-shinjuku-2025"
  ["224071675259"]="takumi-tatsuhiro-shinjuku-2025"
  ["224070032613"]="shinjuku-gyoen-guide-2025"
  ["224068891338"]="shinjuku-oiwake-dango-honpo"
  ["224068585112"]="shinjuku-golden-gai-vs-omoide-yokocho"
  ["224067094205"]="shinjuku-to-disneyland-bus-guide"
  ["224066800060"]="tokyo-crafts-popup-stores-guide"
  ["224066173929"]="shinjuku-epitaph-curry-review"
  ["224065668379"]="roppongi-christmas-illumination-2025"
  ["224064750249"]="shinjuku-sekaido-stationery-shopping-guide"
  ["224064132817"]="narita-airport-terminal1-duty-free-coupon-guide"
  ["224063760866"]="shinjuku-kids-parks-guide"
  ["224062023485"]="tokyo-metropolitan-govt-observatory"
  ["224060336353"]="tokyo-disneyland-complete-guide"
  ["224059082171"]="yokohama-katsuretsuan-tonkatsu"
  ["224057793409"]="roppongi-hills-hello-kitty-popup-2025"
  ["224057078032"]="yokohama-pavlov-cafe-pound-cake"
  ["224055756731"]="tokyo-3-day-christmas-illumination-itinerary"
  ["224054635720"]="daikanyama-asakura-house"
  ["224052787206"]="yokohama-vanilla-beans-cafe"
  ["224052237062"]="yokohama-chinatown-keitokuchin-mapo-tofu"
  ["224052117830"]="shibuya-ikushika-rice-refill-restaurant"
  ["223664743235"]="shinanoya-roppongi-hills-supermarket"
)

for naver_id in "${!MAPPINGS[@]}"; do
  hugo_slug="${MAPPINGS[$naver_id]}"
  echo "Converting $naver_id to $hugo_slug..."

  # English (no language prefix - default language)
  find content/en/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/posts/$hugo_slug/|g" {} +

  # Japanese (with /ja/ prefix)
  find content/ja/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/ja/posts/$hugo_slug/|g" {} +
done

echo "Link conversion complete!"
```

---

## Statistics

- **Total Posts Migrated:** 35
- **Naver IDs Tracked:** 35
- **Posts with Internal Links:** 9+ (evangelion, tokyo-3-day, hello-kitty-popup, yebisu-illumination, shinanoya-roppongi-hills, tamiya-plamodel-factory, meiji-jingu-gaien-ginkgo-avenue-tokyo, yokohama-chinatown-keitokuchin-mapo-tofu, shibuya-ikushika-rice-refill-restaurant)
- **Pending References:** 24
- **Links Updated:** 0 (all links in shinanoya and tamiya posts need migration)
- **Last Migration Date:** 2025-11-20

---

## Maintenance Notes

- This file is tracked in Git for collaboration
- Update this file EVERY TIME you migrate a new post
- Extract internal links during migration workflow
- Run batch conversion script when ready to update all links
- Keep this file synchronized with actual migrated posts
