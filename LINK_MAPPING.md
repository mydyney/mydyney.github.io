# Naver to Hugo Link Mapping

> **Purpose:** Track Naver blog post URLs and their corresponding Hugo slugs for internal link conversion
> **Last Updated:** 2025-12-31
> **Status:** ✅ Complete - 110 posts mapped

---

## How to Use This File

When migrating a Naver blog post to Hugo:
1. Extract the Naver post ID from the HTML (`copyBtn` title attribute)
2. Add a new entry below with all internal links found
3. When all referenced posts are migrated, update internal links in Hugo posts
4. Use the conversion script at the bottom to batch replace links

---

## Quick Reference Table

| Naver ID | Hugo Slug (EN/JA/ZH-CN) | Date | Status |
|----------|-------------------|------|--------|
| 224024819592 | asakusa-complete-guide | 2025-09-28 | ✅ |
| 224038568654 | tokyo-halloween-festivals-2025 | 2025-10-12 | ✅ |
| 224086928640 | japan-convenience-store-oden-guide | 2025-11-25 | ✅ |
| 224046791144 | azabujuban-naniwaya-taiyaki | 2025-10-19 | ✅ |
| 224046408131 | tokyo-transportation-card-guide-2025 | 2025-10-19 | ✅ |
| 224044938913 | shinbashi-shiodome-evening-course | 2025-10-17 | ✅ |
| 224043919463 | odaiba-ariake-toyosu-complete-guide | 2025-10-17 | ✅ |
| 224038071853 | tokyo-autumn-foliage-best-spots-2025 | 2025-10-12 | ✅ |
| 224027835049 | omotesando-guide-2025 | 2025-10-01 | ✅ |
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
| 224033964477 | kaldi-coffee-farm-shopping-list | 2024-04-28 | ✅ |

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
| 224090178080 | shinjuku-gashapon-shops-best-7 | 2025-11-27 | ✅ |
| 224092707353 | jiyugaoka-tokyo-travel-guide | 2025-11-30 | ✅ |
| 224093593124 | hibiya-park-tokyo-guide | 2025-11-30 | ✅ |
| 224098870040 | shibuya-sushi-no-midori-lunch-guide | 2025-12-05 | ✅ |
| 224098592756 | shibuya-blue-cave-illumination-2025 | 2025-12-06 | ✅ |
| 224031114514 | shibuya-complete-guide-2025 | 2025-10-03 | ✅ |
| 224030294691 | harajuku-complete-guide-2025 | 2025-10-03 | ✅ |
| 224099089089 | odaiba-rainbow-fireworks-2025 | 2025-12-06 | ✅ |
| 224096781916 | omotesando-illumination-2025 | 2025-12-06 | ✅ |
| 224095124866 | shinjuku-neon-walk-tokyo-illumination-2025-2026 | 2025-12-02 | ✅ |
| 224095118118 | tokyo-countdown-2026 | 2025-12-06 | ✅ |
| 224034429817 | mitsui-outlet-kisarazu-guide | 2025-12-06 | ✅ |
| 224022065518 | don-quijote-shopping-guide-2025 | 2025-09-26 | ✅ |
| 224035271300 | shinjuku-guide-2025 | 2025-10-09 | ✅ |
| 224039113760 | japan-travel-discount-coupons-2025 | 2025-10-12 | ✅ |
| 224102752117 | tokyo-year-end-business-hours-2026 | 2025-12-08 | ✅ |
| 224121730136 | tokyo-countdown-2026 | 2025-12-24 | ✅ |
| 224122259609 | tokyo-sunrise-spots-2026 | 2025-12-25 | ✅ |
| 223988228389 | roppongi-attractions-guide | 2024-09-02 | ✅ |
| 223989943826 | ginza-guide-2025 | 2025-01-06 | ✅ |
| 224100382618 | shinjuku-hotels-best-10 | 2025-12-06 | ✅ |
| 224105333068 | shibuya-parco-kiwamiya-hamburg-waiting-menu | 2025-12-10 | ✅ |
| 224104049826 | shibuya-miyashita-park-yokocho-2025 | 2025-12-15 | ✅ |
| 224104602398 | tokyo-station-sawamura-lunch | 2025-12-18 | ✅ |
| 224110207709 | tokyo-station-year-end-hours-2026 | 2025-12-18 | ✅ |
| 224101626196 | shinjuku-chuo-park | 2025-12-18 | ✅ |
| 224106627092 | shibuya-parco-shopping-guide | 2025-12-12 | ✅ |
| 224106448442 | shibuya-parco-nintendo-pokemon-guide | 2025-12-13 | ✅ |
| 224105736326 | shibuya-human-made-offline-store-guide | 2025-12-11 | ✅ |
| 224112740096 | tokyo-station-okashi-land-jagariko-calbee-guide | 2025-12-27 | ✅ |
| 224107954391 | shibuya-station-coin-locker-luggage-storage-guide | 2025-12-13 | ✅ |
| 223689247336 | miyashita-park-illumination-2024 | 2024-12-17 | ✅ |
| 224113027853 | tokyo-station-tokyo-banana-creme-brulee-tart-guide | 2025-12-17 | ✅ |
| 224111977613 | tokyo-station-character-street-guide | 2025-12-16 | ✅ |
| 224003374650 | narita-airport-skyliner-guide | 2025-12-29 | ✅ |
| 224031937227 | akihabara-complete-guide | 2025-12-29 | ✅ |
| 224114567793 | tokyo-station-ekiben-guide | 2025-12-18 | ✅ |
| 224124979714 | tokyo-3-day-itinerary-disney-shibuya-sky | 2025-12-28 | ✅ |
| 224007949043 | narita-airport-arrival-guide | 2025-09-14 | ✅ |
| 224037272726 | tsukiji-market-restaurant-guide | 2025-10-11 | ✅ |
| 224026098490 | tokyo-subway-ticket-guide | 2025-09-29 | ✅ |
| 224010546735 | japanese-whisky-yamazaki-hibiki-price-guide | 2025-09-16 | ✅ |
| 224125943419 | tokyo-3-day-itinerary-landmark-series | 2025-12-29 | ✅ |
| 224025699867 | tokyo-subway-pass-vs-jr-tokunai-pass | 2025-09-29 | ✅ |
| 223707471582 | tokyo-ramen-street-best-8 | 2024-12-28 | ✅ |
| 224123307702 | tokyo-january-1-onsen-spa-24-hours | 2025-12-31 | ✅ |
| 224129178083 | tokyo-toshikoshi-soba-new-year-eve-guide | 2025-12-31 | ✅ |

---

## Excluded from Migration (Do Not Process)

The following posts are explicitly excluded from migration (e.g., outdated content, irrelevant links):

| Naver ID | Description | Reason |
|----------|-------------|--------|
| 223669458145 | Ueno Museum Monet Exhibition | Outdated content/irrelevant to current project |


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
| 223914118735 | ueno-ameyoko-guide | Tokyo Ramen Guide (Kangnami's Treasure Box) |
| 223695518100 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Town Pokemon Center Detailed Review |
| 223913830951 | toranomon-hills-complete-guide | Yakitori Omakase, Nonotori Gencho Review |
| 223697732942 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Conveyor Belt Sushi Restaurant Triton (Queue Number Tips) |
| 223699626846 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Dessert Spot: Gion Tsujiri Matcha Ice Cream Review |
| 223700095268 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Free Observatory: SKYTREE VIEW |
| 223700200846 | tokyo-skytree-reservation-discount-guide | Tokyo Skytree Illumination & Christmas Market Detailed Review |
| 223987954990 | evangelion-30th-roppongi-2025, roppongi-attractions-guide | 2025 Roppongi Hills Observatory Complete Guide |
| ~~223988228389~~ | evangelion-30th-roppongi-2025, roppongi-hills-hello-kitty-popup-2025, shinanoya-roppongi-hills-supermarket, meiji-jingu-gaien-ginkgo-avenue-tokyo, tokyo-christmas-markets-guide-2025, tokyo-october-festivals-2025, tokyo-september-festivals-2025, azabujuban-naniwaya-taiyaki, toranomon-hills-complete-guide, azabudai-hills-complete-guide | ✅ **MIGRATED** → roppongi-attractions-guide |
| 223991251786 | shinanoya-roppongi-hills-supermarket, roppongi-attractions-guide | Dassai 23, 39, 45 Official Japanese Prices and Brewery Tour Guide |
| 223993881300 | evangelion-30th-roppongi-2025, roppongi-attractions-guide | Tokyo Roppongi Restaurant Map |
| 224010546735 | shinanoya-roppongi-hills-supermarket, roppongi-attractions-guide | Japanese Whisky Recommendations and Price Guide |
| 223666751487 | roppongi-attractions-guide | St. Moritz: 80-Year-Old Traditional Bakery in Roppongi |
| 223667306537 | roppongi-attractions-guide | Streamer Coffee Company: Special Roppongi Cafe |
| 223667593440 | roppongi-attractions-guide | rem Roppongi: Best Value Hotel Right in Front of Roppongi Station |
| 223674804939 | roppongi-attractions-guide | Tokyo Roppongi Hills Summer Festival: Doraemon |
| 223687520605 | roppongi-attractions-guide | August Tokyo Festivals: Roppongi Hills Bon Odori & Azabujuban Summer Festival |
| 223696568926 | roppongi-attractions-guide | Roppongi Hills Christmas Market: A Little Germany in Tokyo |
| 223913424029 | roppongi-attractions-guide | Iruca Tokyo Roppongi: Michelin Ramen Restaurant |
| 223957316412 | roppongi-attractions-guide | Tsurutontan Roppongi: Sanuki Udon Restaurant |
| 223969429024 | roppongi-attractions-guide | Sarashina Horii Main Store: Roppongi Soba Restaurant |
| 223985958480 | roppongi-attractions-guide | Imakatsu Roppongi Main Store: Tokyo Tonkatsu Restaurant |
| 223986407872 | roppongi-attractions-guide | Tsujihan Midtown: Roppongi Kaisendon Restaurant |
| 223987115708 | roppongi-attractions-guide | Tempura Meshi Kaneko Hannosuke: Roppongi Hills Tempura Restaurant |
| ~~224007949043~~ | tokyo-transportation-card-guide-2025 | ✅ **MIGRATED** → narita-airport-arrival-guide |
| 223995074888 | tokyo-transportation-card-guide-2025 | Haneda Airport Arrival Guide (Including Suica/PASMO Issuance Locations) |
| ~~224026098490~~ | tokyo-transportation-card-guide-2025 | ✅ **MIGRATED** → tokyo-subway-ticket-guide |

| 224024530348 | tokyo-september-festivals-2025 | Roppongi Art Night 2025 Detailed Guide with Recommended Lineup |

| ~~224106448442~~ | shibuya-parco-shopping-guide | ✅ **MIGRATED** → shibuya-parco-nintendo-pokemon-guide |
| ~~224107954391~~ | shibuya-parco-shopping-guide | ✅ **MIGRATED** → shibuya-station-coin-locker-luggage-storage-guide |
| 224032769630 | yebisu-garden-place-illumination-christmas-market-2025, tokyo-christmas-markets-guide-2025 | Yebisu Complete Guide (Garden Place, Beer Museum, Restaurants) |
| ~~223989943826~~ | tokyo-september-festivals-2025, tokyo-october-festivals-2025 | ✅ **MIGRATED** → ginza-guide-2025 |
| 223694057318 | ginza-guide-2025 | Ginza Six Rooftop Free Observation Deck & Ice Rink |
| 223709608832 | ginza-guide-2025 | Ginza Lotte Duty Free Shopping (Dassai 23, Yamazaki 12 Year) |
| 223698121379 | ginza-guide-2025 | Ginza Six Imadeya Sake & Whisky Shopping |
| 223703326263 | ginza-guide-2025 | Ginza Shiseido Parlour Gift Shopping Guide |
| 223693467715 | ginza-guide-2025 | Yamanoue Tempura Omakase Ginza Six Restaurant |
| 223702371242 | ginza-guide-2025 | Ginza Tenryu Grilled Gyoza Restaurant |
| 224010770861 | ginza-guide-2025 | Ginza Hachigo Reservation & Waiting Guide |
| 223715784445 | ginza-guide-2025 | Ginza WAKO Tea Salon (Reservation Tips) |
| 223912913938 | ginza-guide-2025 | Pain Maison Ginza Salt Bread Online Reservation |
| 223702865232 | ginza-guide-2025 | Sapporo The Bar Ginza Perfect Draft Beer |
| ~~224035271300~~ | ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025 | ✅ **MIGRATED** → shinjuku-guide-2025 |
| 224038568654 | ikebukuro-complete-guide, tokyo-october-festivals-2025 | 2025 Tokyo Halloween Festival Top Spots BEST 4 (Ikebukuro) |
| 224039113760 | tamiya-plamodel-factory-tokyo-shimbashi, japan-convenience-store-shopping-best-10, ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025, tokyo-transportation-card-guide-2025, odaiba-ariake-toyosu-complete-guide | Japan Travel Discount Coupons Complete Guide (Don Quijote, Bic Camera, Department Stores) |
| ~~224022065518~~ | tamiya-plamodel-factory-tokyo-shimbashi, japan-convenience-store-shopping-best-10, tokyo-christmas-markets-guide-2025 | ✅ **MIGRATED** → don-quijote-shopping-guide-2025 |
| 224033964477 | tamiya-plamodel-factory-tokyo-shimbashi, japan-convenience-store-shopping-best-10, shibuya-sushi-no-midori-lunch-guide, mitsui-outlet-kisarazu-guide | Japan Kaldi Shopping List Must-Buy Recommendations |
| 224014619007 | don-quijote-shopping-guide-2025 | Suntory Whisky Official Japan Price Guide |

| 224027835049 | meiji-jingu-gaien-ginkgo-avenue-tokyo, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025 | Omotesando Complete Guide: Coffee, Shopping, Restaurants, Architecture |
| 223691371517 | tokyo-station-guide | Tokyo Station Pokemon Store & Pikachu Card Review |
| 223681848151 | tokyo-station-guide | KITTE Marunouchi Christmas Tree & Free Observatory |
| 223675706489 | tokyo-station-guide | Tokyo Station Breakfast: The Front Room French Toast |
| 223675952285 | tokyo-station-guide | Marunouchi Building Free Observatory Sunset View |
| 223684908680 | tokyo-station-guide | Shin-Marunouchi Building Garden Terrace Dinner (Night View) |
| 223685676173 | tokyo-station-guide | Wadakura Fountain Park Starbucks Review (Night View) |
| 224028694874 | ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, asakusa-complete-guide | Ueno Attractions: Ameyoko Market, Restaurants to Ueno Park |
| ~~224031114514~~ | meiji-jingu-gaien-ginkgo-avenue-tokyo, shibuya-ikushika-rice-refill-restaurant, nakameguro-shabushabu-lettuce-main-store, ikebukuro-complete-guide, tokyo-autumn-foliage-best-spots-2025, shibuya-sushi-no-midori-lunch-guide | ✅ **MIGRATED** → shibuya-complete-guide-2025 |
| 224031611221 | ikebukuro-complete-guide, mitsui-outlet-kisarazu-guide | Tokyo Station Attractions: Character Street, Restaurants, Night Views, Luggage Storage |
| 224032086475 | nakameguro-shabushabu-lettuce-main-store | Nakameguro Complete Guide: Meguro River Cherry Blossoms, Trendy Cafes, Boutiques |
| 224032515713 | nakameguro-shabushabu-lettuce-main-store | Daikanyama Complete Guide: T-Site Bookstore, Fashion Shops, Cafe Hopping |
| ~~224030294691~~ | tokyo-autumn-foliage-best-spots-2025, shibuya-sushi-no-midori-lunch-guide, omotesando-complete-guide-2025, shinjuku-complete-guide-2025 | ✅ **MIGRATED** → harajuku-complete-guide-2025 |
| 224037212344 | tokyo-autumn-foliage-best-spots-2025 | Tokyo Kichijoji Must-Visit Places: Complete Course (with Ghibli Museum) |
| 224035533672 | tokyo-autumn-foliage-best-spots-2025 | Mitaka Ghibli Museum Reservation Guide |
| 224008430188 | japan-travel-discount-coupons-2025 | Ginza LOTTE Duty Free Whisky Purchase Guide (Yamazaki, Hibiki, Free Tasting) |
| 224002738158 | narita-express-guide | Narita Express (N'EX) Reservation, Price, Timetable |



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

| 224019480188 | tokyo-october-festivals-2025 | Hakone Travel Day Trip vs Ryokan 1 Night Perfect Course (Hakone Free Pass, Romancecar) |
| 224024819592 | tokyo-christmas-markets-guide-2025, tokyo-october-festivals-2025, tokyo-skytree-reservation-discount-guide, odaiba-ariake-toyosu-complete-guide, odaiba-rainbow-fireworks-2025 | Tokyo Asakusa Attractions & Restaurant Complete Guide |
| 224039113760 | japan-travel-discount-coupons-2025 | Japan Travel Discount Coupons (Don Quijote, Bic Camera, etc.) |
| ~~224035271300~~ | shinjuku-guide-2025 | ✅ **MIGRATED** → shinjuku-guide-2025 |
| 223693165027 | ginza-itoya-stationery-guide | Tokyo Ginza Representative Stationery Store: Itoya Main Store |
| ~~223690406760~~ | odaiba-ariake-toyosu-complete-guide | ✅ **MIGRATED** → odaiba-rainbow-fireworks-2025 |
| 224096203397 | shimokitazawa-tokyo-travel-guide | Shimokitazawa Vintage Shopping, Restaurants & Must-Visit Course |
| 224007665631 | asakusa-complete-guide | Narita Airport to Asakusa Subway Guide |
| 223980220327 | asakusa-complete-guide | August Tokyo Festivals: Sumida River Lantern Floating |
| 224025343414 | asakusa-complete-guide | Asakusa Asahi Beer Sky Room Night View Guide |
| 224031937227 | akihabara-complete-guide | Akihabara Attractions & Anime Pilgrimage Guide |
| 224096781916 | shibuya-blue-cave-illumination-2025 | 2025 Omotesando Illumination Period, Hours, Location & Photo Spots Complete Guide |
| 223915132048 | shinbashi-shiodome-evening-course | Tokyo Shinbashi Tonkatsu Restaurant | Kurobuta Horiichi Michelin Black Pork Tonkatsu Review |
| 223670085459 | tokyo-christmas-illumination-best-5-2025, roppongi-attractions-guide | 2024 Roppongi Tokyo Midtown Christmas Illumination and Santa Tree |
| 223688700265 | tokyo-christmas-illumination-best-5-2025 | 2024 Tokyo Omotesando Illumination and Harajuku Free Observatory |
| 223689247336 | tokyo-christmas-illumination-best-5-2025 | 2024 Tokyo Shibuya Miyashita Park Christmas Illumination |
| 223691772722 | nihonbashi-tokyo-guide | Tokyo Nihonbashi Pokemon Center Tokyo DX & Pokemon Cafe Guide |

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

# Chinese (Simplified) posts (with /zh-cn/ prefix)
sed -i 's|https://blog.naver.com/tokyomate/224065668379|/zh-cn/posts/roppongi-christmas-illumination-2025/|g' content/zh-cn/posts/*.md
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
  ["224090178080"]="shinjuku-gashapon-shops-best-7"
  ["224092707353"]="jiyugaoka-tokyo-travel-guide"
  ["224093593124"]="hibiya-park-tokyo-guide"
  ["224098870040"]="shibuya-sushi-no-midori-lunch-guide"
  ["224098592756"]="shibuya-blue-cave-illumination-2025"
  ["224031114514"]="shibuya-complete-guide-2025"
  ["224030294691"]="harajuku-complete-guide-2025"
  ["224099089089"]="odaiba-rainbow-fireworks-2025"
  ["224096781916"]="omotesando-illumination-2025"
  ["224095124866"]="shinjuku-neon-walk-tokyo-illumination-2025-2026"
  ["224095118118"]="tokyo-countdown-2026"
  ["224024819592"]="asakusa-complete-guide"
  ["224096203397"]="shimokitazawa-tokyo-travel-guide"
  ["224035271300"]="shinjuku-guide-2025"
  ["223693165027"]="ginza-itoya-stationery-guide"
  ["224039113760"]="japan-travel-discount-coupons-2025"
  ["224033964477"]="kaldi-coffee-farm-shopping-list"
  ["224022065518"]="don-quijote-shopping-guide-2025"
  ["224100382618"]="shinjuku-hotels-best-10"
  ["224105333068"]="shibuya-parco-kiwamiya-hamburg-waiting-menu"
  ["223671427079"]="azabudai-hills-christmas-market-review-2024"
  ["223987954990"]="roppongi-hills-observatory-guide"
  ["223988228389"]="roppongi-attractions-guide"
  ["223993881300"]="roppongi-restaurant-map"
  ["223914223908"]="shinjuku-udon-guide"
  ["224019480188"]="hakone-day-trip-course"
  ["224035533672"]="ghibli-museum-reservation-guide"
  ["224031611221"]="tokyo-station-guide"
  ["224003374650"]="skyliner-reservation-guide"
  ["224002738158"]="narita-express-guide"
  ["224007949043"]="narita-airport-arrival-guide"
  ["224004709356"]="narita-airport-limousine-guide"
  ["223989943826"]="ginza-guide-2025"
  ["223694057318"]="ginza-six-rooftop-garden"
  ["223709608832"]="ginza-lotte-duty-free-shopping"
  ["223698121379"]="ginza-six-imadeya-sake-shopping"
  ["223703326263"]="ginza-shiseido-parlour-gift-guide"
  ["223693467715"]="yamanoue-tempura-omakase-ginza"
  ["223702371242"]="ginza-tenryu-gyoza-restaurant"
  ["224010770861"]="ginza-hachigo-reservation-guide"
  ["223715784445"]="ginza-wako-tea-salon"
  ["223912913938"]="pain-maison-ginza-salt-bread"
  ["223702865232"]="sapporo-the-bar-ginza"
  ["224032515713"]="daikanyama-guide"
  ["223995074888"]="haneda-airport-arrival-guide"
  ["224010546735"]="japanese-whisky-yamazaki-hibiki-price-guide"
  ["224035895968"]="tokyo-dome-city-guide"
  ["224034429817"]="mitsui-outlet-kisarazu-guide"
  ["223694645793"]="ginza-akebono-strawberry-mochi"
  ["224025044772"]="ginza-kuya-monaka-reservation-guide"
  ["223686466421"]="hibiya-midtown-illumination-review-2024"
  ["223979907748"]="yokohama-one-day-itinerary"
  ["223976102621"]="yokohama-minato-burari-ticket-guide"
  ["224026098490"]="tokyo-subway-ticket-guide"
  ["224027835049"]="omotesando-guide-2025"
  ["223691371517"]="tokyo-station-pokemon-store-review"
  ["223707471582"]="tokyo-ramen-street-best-8"
  ["223681848151"]="kitte-marunouchi-christmas-tree-observatory"
  ["223675706489"]="tokyo-station-breakfast-the-front-room"
  ["223675952285"]="marunouchi-building-free-observatory"
  ["223684908680"]="shin-marunouchi-building-terrace-dinner"
  ["223685676173"]="wadakura-fountain-park-starbucks-review"
  ["224028694874"]="ueno-ameyoko-guide"
  ["224037272726"]="tsukiji-market-restaurant-guide"
  ["223914321510"]="sumiyaki-unafuji-yurakucho"
  ["224042267263"]="nihonbashi-guide"
  ["223680263119"]="tokyo-station-nemuro-hanamaru-sushi-guide"
  ["224032515713"]="daikanyama-guide"
  ["224032086475"]="nakameguro-guide"
  ["223695518100"]="tokyo-skytree-pokemon-center-review"
  ["223697732942"]="tokyo-skytree-triton-sushi-guide"
  ["223699626846"]="tokyo-skytree-gion-tsujiri-matcha"
  ["223700200846"]="tokyo-skytree-illumination-guide"
  ["223700095268"]="tokyo-skytree-free-observatory"
  ["223913830951"]="toranomon-hills-yakitori-nonotori"
  ["223716380927"]="azabudai-hills-sky-room-cafe-guide"
  ["223672616108"]="azabudai-hills-teamlab-borderless-guide"
  ["223968462793"]="azabudai-hills-commen-bakery-review"
  ["223708789355"]="azabudai-hills-criollo-chocolate-review"
  ["223958175295"]="azabudai-hills-summer-festival-review"
  ["223915389552"]="azabudai-hills-series-chinese-restaurant"
  ["224025699867"]="tokyo-subway-pass-vs-jr-tokunai-pass"
  ["224032769630"]="yebisu-complete-guide"
  ["223915132048"]="shinbashi-tonkatsu-horiichi"
  ["223670085459"]="roppongi-midtown-christmas-review-2024"
  ["223688700265"]="omotesando-illumination-harajuku-observatory-review-2024"
  ["223689247336"]="miyashita-park-illumination-2024"
  ["223691772722"]="nihonbashi-pokemon-center-dx-cafe-guide"
  ["224008430188"]="ginza-lotte-duty-free-whisky-guide"
  ["224007665631"]="narita-to-asakusa-subway-guide"
  ["223980220327"]="tokyo-august-festivals-sumida-river"
  ["224025343414"]="asakusa-asahi-beer-sky-room-guide"
  ["224031937227"]="akihabara-complete-guide"
  ["224014619007"]="suntory-whisky-price-guide-japan"
  ["223991251786"]="dassai-sake-price-guide-japan"
  ["224024530348"]="roppongi-art-night-guide"
  ["223666751487"]="st-moritz-roppongi-bakery"
  ["223667306537"]="streamer-coffee-roppongi-guide"
  ["223667593440"]="rem-roppongi-hotel-guide"
  ["223674804939"]="roppongi-hills-summer-festival-doraemon"
  ["223687520605"]="roppongi-azabujuban-summer-festivals"
  ["223696568926"]="roppongi-hills-christmas-market-2025"
  ["223913424029"]="iruca-tokyo-roppongi-ramen-guide"
  ["223914118735"]="tokyo-ramen-guide-kangnami"
  ["223957316412"]="tsurutontan-roppongi-udon-guide"
  ["223969429024"]="sarashina-horii-roppongi-soba"
  ["223985958480"]="imakatsu-roppongi-tonkatsu-guide"
  ["223986407872"]="tsujihan-midtown-kaisendon-guide"
  ["223987115708"]="kaneko-hannosuke-roppongi-tempura"
  ["224100382618"]="shinjuku-hotels-best-10"
  ["224106627092"]="shibuya-parco-shopping-guide"
  ["224106448442"]="shibuya-parco-nintendo-pokemon-guide"
  ["224107954391"]="shibuya-station-coin-locker-luggage-storage-guide"
  ["224112740096"]="tokyo-station-okashi-land-jagariko-calbee-guide"
  ["224105736326"]="shibuya-human-made-offline-store-guide"
  ["224124979714"]="tokyo-3-day-itinerary-disney-shibuya-sky"
  ["224113027853"]="tokyo-station-tokyo-banana-creme-brulee-tart-guide"
  ["224007949043"]="narita-airport-arrival-guide"
  ["224037272726"]="tsukiji-market-restaurant-guide"
  ["224010546735"]="japanese-whisky-yamazaki-hibiki-price-guide"
  ["224125943419"]="tokyo-3-day-itinerary-landmark-series"
  ["223707471582"]="tokyo-ramen-street-best-8"
)

for naver_id in "${!MAPPINGS[@]}"; do
  hugo_slug="${MAPPINGS[$naver_id]}"
  echo "Converting $naver_id to $hugo_slug..."

  # English (no language prefix - default language)
  find content/en/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/posts/$hugo_slug/|g" {} +

  # Japanese (with /ja/ prefix)
  find content/ja/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/ja/posts/$hugo_slug/|g" {} +

  # Chinese (Simplified) (with /zh-cn/ prefix)
  find content/zh-cn/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/zh-cn/posts/$hugo_slug/|g" {} +
done

echo "Link conversion complete!"
```

---

## Statistics

- **Total Posts Migrated:** 110
- **Naver IDs Tracked:** 110
- **Posts with Internal Links:** 35+ (shinbashi-shiodome-evening-course, odaiba-ariake-toyosu-complete-guide, evangelion, tokyo-3-day, hello-kitty-popup, yebisu-illumination, shinanoya-roppongi-hills, tamiya-plamodel-factory, meiji-jingu-gaien-ginkgo-avenue-tokyo, meiji-jingu-gaien-christmas-market-2025, yokohama-chinatown-keitokuchin-mapo-tofu, shibuya-ikushika-rice-refill-restaurant, nakameguro-shabushabu-lettuce-main-store, japan-convenience-store-shopping-best-10, ikebukuro-complete-guide, tokyo-christmas-markets-guide-2025, tokyo-autumn-foliage-best-spots-2025, tokyo-october-festivals-2025, tokyo-september-festivals-2025, tokyo-transportation-card-guide-2025, azabujuban-naniwaya-taiyaki, tokyo-skytree-reservation-discount-guide, toranomon-hills-complete-guide, azabudai-hills-complete-guide, shibuya-sushi-no-midori-lunch-guide, shibuya-blue-cave-illumination-2025, shibuya-complete-guide-2025, harajuku-complete-guide-2025, odaiba-rainbow-fireworks-2025, don-quijote-shopping-guide-2025, shinjuku-hotels-best-10, shibuya-parco-kiwamiya-hamburg-waiting-menu, tsukiji-market-restaurant-guide, tokyo-subway-ticket-guide, narita-airport-arrival-guide)
- **Pending References:** 46
- **Links Updated:** Verified & Fixed on 2025-12-28
- **Last Migration Date:** 2025-12-31 (Tokyo 3-Day Itinerary Guide)

---

## Maintenance Notes

- This file is tracked in Git for collaboration
- Update this file EVERY TIME you migrate a new post
- Extract internal links during migration workflow
- Run batch conversion script when ready to update all links
- Keep this file synchronized with actual migrated posts

