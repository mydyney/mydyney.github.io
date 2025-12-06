# Naver to Hugo Link Mapping

> **Purpose:** Track Naver blog post URLs and their corresponding Hugo slugs for internal link conversion
> **Last Updated:** 2025-12-06
> **Status:** ✅ Complete - 65 posts mapped

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
| 224038568654 | tokyo-halloween-festivals-2025 | 2025-10-12 | ✅ |
| 224086928640 | japan-convenience-store-oden-guide | 2025-11-25 | ✅ |
| 224046791144 | azabujuban-naniwaya-taiyaki | 2025-10-19 | ✅ |
| 224046408131 | tokyo-transportation-card-guide-2025 | 2025-10-19 | ✅ |
| 224044938913 | shinbashi-shiodome-evening-course | 2025-10-17 | ✅ |
| 224043919463 | odaiba-ariake-toyosu-complete-guide | 2025-10-17 | ✅ |
| 224038071853 | tokyo-autumn-foliage-best-spots-2025 | 2025-10-12 | ✅ |
| 224045496649 | tokyo-christmas-markets-guide-2025 | 2025-10-18 | ✅ |
| 224026292057 | tokyo-october-festivals-2025 | 2025-09-29 | ✅ |
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
| 224052025195 | nakameguro-shabushabu-lettuce-main-store | 2025-10-24 | ✅ |
| 224050488006 | japan-convenience-store-shopping-best-10 | 2025-10-23 | ✅ |
| 224050101070 | ikebukuro-complete-guide | 2025-10-22 | ✅ |
| 224049240457 | tokyo-skytree-reservation-discount-guide | 2025-10-21 | ✅ |
| 224047793364 | toranomon-hills-complete-guide | 2025-10-20 | ✅ |
| 224047575500 | azabudai-hills-complete-guide | 2025-10-20 | ✅ |
| 224042431249 | tokyo-christmas-illumination-best-5-2025 | 2025-10-15 | ✅ |
| 224083451617 | tokyo-dome-city-christmas-illumination-2025 | 2025-11-21 | ✅ |
| 224084373557 | ueno-christmas-market-2025 | 2025-11-22 | ✅ |
| 224084462259 | haneda-amex-centurion-lounge-hours-2025 | 2025-11-22 | ✅ |
| 224085135200 | azabudai-hills-christmas-market-2025 | 2025-11-23 | ✅ |
| 224085358394 | roppongi-hills-christmas-market-2025 | 2025-11-23 | ✅ |
| 224085512487 | tokyo-node-dining-toranomon-hills-lunch | 2025-11-23 | ✅ |
| 224086214573 | meiji-jingu-gaien-christmas-market-2025 | 2025-11-24 | ✅ |
| 223664743235 | shinanoya-roppongi-hills-supermarket | 2024-11-18 | ✅ |
| 223992588094 | tokyo-september-festivals-2025 | 2025-09-02 | ✅ |
| 224089448937 | shinjuku-station-breakfast-best-8 | 2025-11-27 | ✅ |
| 224098870040 | shibuya-sushi-no-midori-lunch-guide | 2025-12-05 | ✅ |
| 224098592756 | shibuya-blue-cave-illumination-2025 | 2025-12-06 | ✅ |
| 224031114514 | shibuya-complete-guide-2025 | 2025-10-03 | ✅ |
| 224030294691 | harajuku-complete-guide-2025 | 2025-10-03 | ✅ |
| 224099089089 | odaiba-rainbow-fireworks-2025 | 2025-12-06 | ✅ |
| 224096781916 | omotesando-illumination-2025 | 2025-12-06 | ✅ |

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
| 223695518100 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Town Pokemon Center Detailed Review |
| 223913830951 | toranomon-hills-complete-guide | Yakitori Omakase, Nonotori Gencho Review |
| 223697732942 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Conveyor Belt Sushi Restaurant Triton (Queue Number Tips) |
| 223699626846 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Dessert Spot: Gion Tsujiri Matcha Ice Cream Review |
| 223700095268 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Free Observatory: SKYTREE VIEW |
| 223700200846 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Illumination & Christmas Market Detailed Review |
| 223987954990 | evangelion-30th-roppongi-2025 | 2025 Roppongi Hills Observatory Complete Guide |
| 223988228389 | evangelion-30th-roppongi-2025, roppongi-hills-hello-kitty-popup-2025, shinanoya-roppongi-hills-supermarket, meiji-jingu-gaien-ginkgo-avenue-tokyo, tokyo-christmas-markets-guide-2025, tokyo-october-festivals-2025, tokyo-september-festivals-2025, azabujuban-naniwaya-taiyaki, toranomon-hills-complete-guide, azabudai-hills-complete-guide | Complete Guide to Roppongi Attractions |
| 223991251786 | shinanoya-roppongi-hills-supermarket | Dassai 23, 39, 45 Official Japanese Prices and Brewery Tour Guide |
| 223993881300 | evangelion-30th-roppongi-2025 | Tokyo Roppongi Restaurant Map |
| 224010546735 | shinanoya-roppongi-hills-supermarket | Japanese Whisky Recommendations and Price Guide |
| 224007949043 | tokyo-transportation-card-guide-2025 | Narita Airport Arrival Guide (Including Suica/PASMO Issuance Locations) |
| 223995074888 | tokyo-transportation-card-guide-2025 | Haneda Airport Arrival Guide (Including Suica/PASMO Issuance Locations) |
| 224026098490 | tokyo-transportation-card-guide-2025 | Tokyo Subway Pass Complete Guide (Exchange Locations, Purchase, Usage) |
| 224002738158 | tokyo-transportation-card-guide-2025 | Narita Express (N'EX) Reservation, Prices, Timetable Complete Guide |
| 224024530348 | tokyo-september-festivals-2025 | Roppongi Art Night 2025 Detailed Guide with Recommended Lineup |
| 224032769630 | yebisu-garden-place-illumination-christmas-market-2025, tokyo-christmas-markets-guide-2025 | Yebisu Complete Guide (Garden Place, Beer Museum, Restaurants) |
| 223989943826 | tokyo-september-festivals-2025, tokyo-october-festivals-2025 | Ginza Must-Visit Spots Complete Guide (Shopping, Restaurants, Tips) |
| 224035271300 | ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025 | Shinjuku Attractions: From Shinjuku Gyoen to Restaurants and Shopping |
| 224038568654 | ikebukuro-complete-guide, tokyo-october-festivals-2025 | 2025 Tokyo Halloween Festival Top Spots BEST 4 (Ikebukuro) |
| 224039113760 | tamiya-plamodel-factory-tokyo-shimbashi, japan-convenience-store-shopping-best-10, ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025, tokyo-transportation-card-guide-2025, odaiba-ariake-toyosu-complete-guide | Japan Travel Discount Coupons Complete Guide (Don Quijote, Bic Camera, Department Stores) |
| 224022065518 | tamiya-plamodel-factory-tokyo-shimbashi, japan-convenience-store-shopping-best-10, tokyo-christmas-markets-guide-2025 | Japan Don Quijote Shopping List & Discount Coupons Guide |
| 224033964477 | tamiya-plamodel-factory-tokyo-shimbashi, japan-convenience-store-shopping-best-10, shibuya-sushi-no-midori-lunch-guide | Japan Kaldi Shopping List Must-Buy Recommendations |
| 224034429817 | tamiya-plamodel-factory-tokyo-shimbashi | Mitsui Outlet Park Kisarazu Discount Coupons & Brand Guide |
| 224027835049 | meiji-jingu-gaien-ginkgo-avenue-tokyo, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025 | Omotesando Complete Guide: Coffee, Shopping, Restaurants, Architecture |
| 224028694874 | ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025 | Ueno Attractions: Ameyoko Market, Restaurants to Ueno Park |
| ~~224031114514~~ | meiji-jingu-gaien-ginkgo-avenue-tokyo, shibuya-ikushika-rice-refill-restaurant, nakameguro-shabushabu-lettuce-main-store, ikebukuro-complete-guide, tokyo-autumn-foliage-best-spots-2025, shibuya-sushi-no-midori-lunch-guide | ✅ **MIGRATED** → shibuya-complete-guide-2025 |
| 224031611221 | ikebukuro-complete-guide | Tokyo Station Attractions: Character Street, Restaurants, Night Views, Luggage Storage |
| 224032086475 | nakameguro-shabushabu-lettuce-main-store | Nakameguro Complete Guide: Meguro River Cherry Blossoms, Trendy Cafes, Boutiques |
| 224032515713 | nakameguro-shabushabu-lettuce-main-store | Daikanyama Complete Guide: T-Site Bookstore, Fashion Shops, Cafe Hopping |
| ~~224030294691~~ | tokyo-autumn-foliage-best-spots-2025, shibuya-sushi-no-midori-lunch-guide, omotesando-complete-guide-2025, shinjuku-complete-guide-2025 | ✅ **MIGRATED** → harajuku-complete-guide-2025 |
| 224037212344 | tokyo-autumn-foliage-best-spots-2025 | Tokyo Kichijoji Must-Visit Places: Complete Course (with Ghibli Museum) |
| 224035533672 | tokyo-autumn-foliage-best-spots-2025 | Mitaka Ghibli Museum Reservation Guide |
| 224019480188 | tokyo-october-festivals-2025, tokyo-autumn-foliage-best-spots-2025 | Hakone Travel Perfect Course (Hakone Free Pass & Romancecar Reservation) |
| 224025699867 | tokyo-autumn-foliage-best-spots-2025, tokyo-transportation-card-guide-2025, odaiba-ariake-toyosu-complete-guide | Tokyo Metro Pass vs JR Tokunai Pass Complete Comparison |
| 224026292057 | tokyo-autumn-foliage-best-spots-2025 | 2025 Tokyo October Festivals & Must-Visit Places |
| 223979907748 | yokohama-chinatown-keitokuchin-mapo-tofu, tokyo-christmas-markets-guide-2025 | Yokohama 1-Day Course: Chinatown Restaurants, Akarenga, Night Views Complete Guide |
| 223976102621 | yokohama-chinatown-keitokuchin-mapo-tofu, tokyo-christmas-markets-guide-2025 | Yokohama Transportation Pass, 'Minato Burari Ticket' Complete Guide |
| 223672616108 | tokyo-christmas-markets-guide-2025, azabudai-hills-complete-guide | Tokyo Azabudai Hills teamLab Borderless Museum Guide |
| 223716380927 | tokyo-christmas-markets-guide-2025, azabudai-hills-complete-guide | Tokyo Azabudai Hills Observatory Cafe Sky Room Guide |
| 223968462793 | azabudai-hills-complete-guide | Comme'N Tokyo Azabudai Hills Bakery Review |
| 223708789355 | azabudai-hills-complete-guide | Criollo Chocolatier Review |
| 223671427079 | azabudai-hills-complete-guide | 2024 Tokyo Azabudai Hills Christmas Market Review |
| 223958175295 | azabudai-hills-complete-guide | Tokyo Azabudai Hills Summer Festival Review |
| 223915389552 | azabudai-hills-complete-guide | Series Michelin 1-Star Chinese Restaurant Review |
| 223980166231 | tokyo-october-festivals-2025 | Harajuku Omotesando Super Yosakoi Festival August Guide |
| 223989943826 | tokyo-october-festivals-2025 | Complete Guide to Ginza Attractions (Shopping, Restaurants, Tips) |
| 224019480188 | tokyo-october-festivals-2025 | Hakone Travel Day Trip vs Ryokan 1 Night Perfect Course (Hakone Free Pass, Romancecar) |
| 224024819592 | tokyo-christmas-markets-guide-2025, tokyo-october-festivals-2025, tokyo-skytree-reservation-discount-guide, odaiba-ariake-toyosu-complete-guide, odaiba-rainbow-fireworks-2025 | Tokyo Asakusa Attractions & Restaurant Complete Guide |
| ~~223690406760~~ | odaiba-ariake-toyosu-complete-guide | ✅ **MIGRATED** → odaiba-rainbow-fireworks-2025 |
| 224096203397 | shimokitazawa-tokyo-travel-guide | Shimokitazawa Vintage Shopping, Restaurants & Must-Visit Course |
| 224096781916 | shibuya-blue-cave-illumination-2025 | 2025 Omotesando Illumination Period, Hours, Location & Photo Spots Complete Guide |

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
  ["224038568654"]="tokyo-halloween-festivals-2025"
  ["224086928640"]="japan-convenience-store-oden-guide"
  ["224046791144"]="azabujuban-naniwaya-taiyaki"
  ["224046408131"]="tokyo-transportation-card-guide-2025"
  ["224044938913"]="shinbashi-shiodome-evening-course"
  ["224043919463"]="odaiba-ariake-toyosu-complete-guide"
  ["224038071853"]="tokyo-autumn-foliage-best-spots-2025"
  ["224045496649"]="tokyo-christmas-markets-guide-2025"
  ["224026292057"]="tokyo-october-festivals-2025"
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
  ["224052025195"]="nakameguro-shabushabu-lettuce-main-store"
  ["224050488006"]="japan-convenience-store-shopping-best-10"
  ["224050101070"]="ikebukuro-complete-guide"
  ["224049240457"]="tokyo-skytree-reservation-discount-guide"
  ["224047793364"]="toranomon-hills-complete-guide"
  ["224047575500"]="azabudai-hills-complete-guide"
  ["224042431249"]="tokyo-christmas-illumination-best-5-2025"
  ["224083451617"]="tokyo-dome-city-christmas-illumination-2025"
  ["224084373557"]="ueno-christmas-market-2025"
  ["224084462259"]="haneda-amex-centurion-lounge-hours-2025"
  ["224085135200"]="azabudai-hills-christmas-market-2025"
  ["224085358394"]="roppongi-hills-christmas-market-2025"
  ["224085512487"]="tokyo-node-dining-toranomon-hills-lunch"
  ["224086214573"]="meiji-jingu-gaien-christmas-market-2025"
  ["223664743235"]="shinanoya-roppongi-hills-supermarket"
  ["223992588094"]="tokyo-september-festivals-2025"
  ["224089448937"]="shinjuku-station-breakfast-best-8"
  ["224098870040"]="shibuya-sushi-no-midori-lunch-guide"
  ["224098592756"]="shibuya-blue-cave-illumination-2025"
  ["224031114514"]="shibuya-complete-guide-2025"
  ["224030294691"]="harajuku-complete-guide-2025"
  ["224099089089"]="odaiba-rainbow-fireworks-2025"
  ["224096781916"]="omotesando-illumination-2025"
  ["224024819592"]="asakusa-complete-guide-2025"
  ["224096203397"]="shimokitazawa-tokyo-travel-guide"
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

- **Total Posts Migrated:** 65
- **Naver IDs Tracked:** 65
- **Posts with Internal Links:** 29+ (shinbashi-shiodome-evening-course, odaiba-ariake-toyosu-complete-guide, evangelion, tokyo-3-day, hello-kitty-popup, yebisu-illumination, shinanoya-roppongi-hills, tamiya-plamodel-factory, meiji-jingu-gaien-ginkgo-avenue-tokyo, meiji-jingu-gaien-christmas-market-2025, yokohama-chinatown-keitokuchin-mapo-tofu, shibuya-ikushika-rice-refill-restaurant, nakameguro-shabushabu-lettuce-main-store, japan-convenience-store-shopping-best-10, ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025, tokyo-october-festivals-2025, tokyo-september-festivals-2025, tokyo-transportation-card-guide-2025, azabujuban-naniwaya-taiyaki, tokyo-skytree-reservation-discount-guide, toranomon-hills-complete-guide, azabudai-hills-complete-guide, shibuya-sushi-no-midori-lunch-guide, shibuya-blue-cave-illumination-2025, shibuya-complete-guide-2025, harajuku-complete-guide-2025, odaiba-rainbow-fireworks-2025)
- **Pending References:** 51 (removed 1: 223690406760 migrated to odaiba-rainbow-fireworks-2025)
- **Links Updated:** Verified & Fixed on 2025-12-06 (Updated 21 additional files)
- **Last Migration Date:** 2025-12-06 (Odaiba Rainbow Fireworks 2025)

---

## Maintenance Notes

- This file is tracked in Git for collaboration
- Update this file EVERY TIME you migrate a new post
- Extract internal links during migration workflow
- Run batch conversion script when ready to update all links
- Keep this file synchronized with actual migrated posts
