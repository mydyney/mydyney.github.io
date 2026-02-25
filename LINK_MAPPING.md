# Naver to Hugo Link Mapping

> **Purpose:** Track Naver blog post URLs and their corresponding Hugo slugs for internal link conversion
> **Status:** ⏳ In Progress - 175 posts migrated, 49 pending (224 total mapped)

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
| 224194466616 | shibuya-conveyor-belt-sushi-ranking | 2026-02-24 | ✅ |
| 224187041918 | tokyo-cherry-blossom-top-10-spots | 2026-02-18 | ✅ |
| 224180161370 | chidorigafuchi-cherry-blossom-boat-guide | 2026-02-16 | ✅ |
| 224180541373 | shinjuku-gyoen-cherry-blossom-guide | 2026-02-16 | ✅ |
| 224181078856 | starbucks-japan-valentine-2026-menu-guide | 2026-02-16 | ✅ |
| 224184289415 | grand-hyatt-tokyo-keyakizaka-teppanyaki-guide | 2026-02-15 | ✅ |
| 224181904705 | new-york-perfect-cheese-cookie-guide | 2026-02-15 | ✅ |
| 224153746833 | tokyo-station-jiichiro-kitte-baumkuchen-guide | 2026-02-15 | ✅ |
| 223911732881 | im-donut-nakameguro-seongsu-guide | 2026-02-14 | ✅ |
| 224177943474 | starbucks-reserve-roastery-tokyo-guide | 2026-02-14 | ✅ |
| 224177420032 | nakameguro-cherry-blossom-guide | 2026-02-14 | ✅ |
| 224183302811 | shibuya-hikarie-11f-sky-lobby-guide | 2026-02-14 | ✅ |
| 224182368714 | daikanyama-dior-bamboo-pavilion-guide | 2026-02-14 | ✅ |
| 224163357798 | shibuya-ichiran-ramen-location-wait-time | 2026-02-08 | ✅ |
| 224172555287 | shibuya-drone-show-dig-shibuya-2026 | 2026-02-08 | ✅ |
| 224174086158 | kaldi-valentine-chocolate-guide | 2026-02-06 | ✅ |
| 224174540869 | pokemon-park-kanto-yomiuriland-guide | 2026-02-07 | ✅ |
| 224035533672 | ghibli-museum-reservation-guide | 2025-10-09 | ✅ |
| 224037212344 | kichijoji-complete-guide-2025 | 2025-10-11 | ✅ |
| 224170137639 | asakusa-imahan-kokusaidori-guide | 2026-02-03 | ✅ |
| 224025343414 | asakusa-asahi-sky-room | 2026-02-04 | ✅ |
| 223665548720 | ebisu-brewery-tokyo | 2026-02-04 | ✅ |
| 224163039620 | atami-kawazu-cherry-blossom-festival-guide | 2026-01-28 | ✅ |
| 224149088534 | kamakura-day-trip-guide | 2026-01-16 | ✅ |
| 224151789346 | tokyo-kajitsuen-liebel-strawberry-parfait-guide | 2026-01-19 | ✅ |
| 224160652498 | tokyo-observatory-comparison | 2026-01-28 | ✅ |
| 224155602660 | tokyo-station-kantaro-ichibangai-sushi | 2026-01-22 | ✅ |
| 224184108901 | tokyo-rainy-day-itinerary-guide | 2026-02-20 | ✅ |
| 224189758086 | gotokuji-maneki-neko-cat-day-guide | 2026-02-20 | ✅ |
| 224156966219 | tokyo-cherry-blossom-forecast-2026 | 2026-01-23 | ✅ |
| 224145944230 | japan-mcdonalds-happy-set-2026-01 | 2026-01-16 | ✅ |
| 224146568943 | ginza-kagari-chicken-paitan-ramen-guide | 2026-02-21 | ✅ |
| 224146973824 | tokyo-nihonbashi-manten-sushi-guide | 2026-01-15 | ✅ |
| 224144304263 | ginza-nemuro-hanamaru-sushi-guide | 2026-01-15 | ✅ |
| 224142352662 | ginza-sato-yosuke-inaniwa-udon-guide | 2026-01-15 | ✅ |
| 224140812174 | ginza-shopping-discount-guide-2026 | 2026-01-09 | ✅ |
| 224038866606 | hakone-open-air-museum-guide-discount-tips | 2025-10-12 | ✅ |
| 224138433650 | tokyo-february-weather-clothing-guide | 2026-01-08 | ✅ |
| 224135063751 | tokyo-subway-map-guide | 2026-02-20 | ✅ |
| 224148214290 | tokyo-travel-preparation-guide | 2026-02-20 | ✅ |
| 224131055243 | shinjuku-department-store-guest-card-discount | - | pending |
| 224109119129 | azabudai-hills-parlor-yazawa-guide | 2026-02-20 | ✅ |
| 223681505340 | azabudai-hills-sky-room-sunset-view | 2026-02-20 | ✅ |
| 223671427079 | azabudai-hills-christmas-market-2024 | - | pending |
| 224134693622 | yanaka-ginza-menchi-katsu-yuyake-dandan-guide | 2026-01-05 | ✅ |
| 224129178083 | tokyo-toshikoshi-soba-new-year-eve-guide | 2025-12-31 | ✅ |
| 224032086475 | nakameguro-complete-guide | 2025-10-05 | ✅ |
| 224024131147 | hakone-romance-car-booking-guide | 2026-01-10 | ✅ |
| 224019480188 | hakone-travel-guide-day-trip-vs-ryokan | 2025-09-25 | ✅ |
| 224128216969 | tsukishima-monjayaki-street-guide | 2025-12-30 | ✅ |
| 224125943419 | tokyo-3-day-itinerary-landmark-series | 2025-12-29 | ✅ |
| 224124979714 | tokyo-3-day-itinerary-disney-shibuya-sky | 2025-12-28 | ✅ |
| 224123307702 | tokyo-january-1-onsen-spa-24-hours | 2025-12-31 | ✅ |
| 224122259609 | tokyo-sunrise-spots-2026 | 2025-12-25 | ✅ |
| 224121730136 | tokyo-countdown-2026 | 2025-12-24 | ✅ |
| 224114567793 | tokyo-station-ekiben-guide | 2025-12-18 | ✅ |
| 224113027853 | tokyo-station-tokyo-banana-creme-brulee-tart-guide | 2025-12-17 | ✅ |
| 224112740096 | tokyo-station-okashi-land-jagariko-calbee-guide | 2025-12-27 | ✅ |
| 224111977613 | tokyo-station-character-street-guide | 2025-12-16 | ✅ |
| 224110207709 | tokyo-station-year-end-hours-2026 | 2025-12-18 | ✅ |
| 224107954391 | shibuya-station-coin-locker-luggage-storage-guide | 2025-12-13 | ✅ |
| 224106627092 | shibuya-parco-shopping-guide | 2025-12-12 | ✅ |
| 224106448442 | shibuya-parco-nintendo-pokemon-guide | 2025-12-13 | ✅ |
| 224136520145 | tokyo-tokunai-pass-jr-1-day-itinerary-routes | 2026-01-06 | ✅ |
| 224105736326 | shibuya-human-made-offline-store-guide | 2025-12-11 | ✅ |
| 224105333068 | shibuya-parco-kiwamiya-hamburg-waiting-menu | 2025-12-10 | ✅ |
| 224104602398 | tokyo-station-sawamura-lunch | 2025-12-18 | ✅ |
| 224104049826 | shibuya-miyashita-park-yokocho-2025 | 2025-12-15 | ✅ |
| 224102752117 | tokyo-year-end-business-hours-2026 | 2025-12-08 | ✅ |
| 224101626196 | shinjuku-chuo-park | 2025-12-18 | ✅ |
| 224100382618 | shinjuku-hotels-best-10 | 2025-12-06 | ✅ |
| 224099089089 | odaiba-rainbow-fireworks-2025 | 2025-12-06 | ✅ |
| 224098870040 | shibuya-sushi-no-midori-lunch-guide | 2025-12-05 | ✅ |
| 224098592756 | shibuya-blue-cave-illumination-2025 | 2025-12-06 | ✅ |
| 224096781916 | omotesando-illumination-2025 | 2025-12-06 | ✅ |
| 224095124866 | shinjuku-neon-walk-tokyo-illumination-2025-2026 | 2025-12-02 | ✅ |
| 224093593124 | hibiya-park-tokyo-guide | 2025-11-30 | ✅ |
| 224092707353 | jiyugaoka-tokyo-travel-guide | 2025-11-30 | ✅ |
| 224090178080 | shinjuku-gashapon-shops-best-7 | 2025-11-27 | ✅ |
| 224089448937 | shinjuku-station-breakfast-best-8 | 2025-11-27 | ✅ |
| 224086928640 | japan-convenience-store-oden-guide | 2025-11-25 | ✅ |
| 224086214573 | meiji-jingu-gaien-christmas-market-2025 | 2025-11-24 | ✅ |
| 224085512487 | tokyo-node-dining-toranomon-hills-lunch | 2025-11-23 | ✅ |
| 224085358394 | roppongi-hills-christmas-market-2025 | 2025-11-23 | ✅ |
| 224085135200 | azabudai-hills-christmas-market-2025 | 2025-11-23 | ✅ |
| 224084462259 | haneda-amex-centurion-lounge-hours-2025 | 2025-11-22 | ✅ |
| 224084373557 | ueno-christmas-market-2025 | 2025-11-22 | ✅ |
| 224083451617 | tokyo-dome-city-christmas-illumination-2025 | 2025-11-21 | ✅ |
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
| 224046791144 | azabujuban-naniwaya-taiyaki | 2025-10-19 | ✅ |
| 224046408131 | tokyo-transportation-card-guide-2025 | 2025-10-19 | ✅ |
| 224045496649 | tokyo-christmas-markets-guide-2025 | 2025-10-18 | ✅ |
| 224044938913 | shimbashi-shiodome-evening-course | 2025-10-17 | ✅ |
| 224043919463 | odaiba-ariake-toyosu-complete-guide | 2025-10-17 | ✅ |
| 224042431249 | tokyo-christmas-illumination-best-5-2025 | 2025-10-15 | ✅ |
| 224039113760 | japan-travel-discount-coupons-2025 | 2025-10-12 | ✅ |
| 224038568654 | tokyo-halloween-festivals-2025 | 2025-10-12 | ✅ |
| 224038071853 | tokyo-autumn-foliage-best-spots-2025 | 2025-10-12 | ✅ |
| 224037272726 | tsukiji-market-restaurant-guide | 2025-10-11 | ✅ |
| 224037212344 | kichijoji-complete-guide-2025 | 2025-10-11 | ✅ |
| 224035271300 | shinjuku-guide-2025 | 2025-10-09 | ✅ |
| 224034429817 | mitsui-outlet-kisarazu-guide | 2025-12-06 | ✅ |
| 224033964477 | kaldi-coffee-farm-shopping-list | 2024-04-28 | ✅ |
| 224032769630 | yebisu-complete-guide | 2026-01-01 | ✅ |
| 223983589161 | daikanyama-tsutaya-share-lounge-guide | - | pending |
| 224032515713 | daikanyama-complete-guide | 2026-01-01 | ✅ |
| 224031937227 | akihabara-complete-guide | 2025-12-29 | ✅ |
| 224031611221 | tokyo-station-guide | 2025-12-31 | ✅ |
| 224031114514 | shibuya-complete-guide-2025 | 2025-10-03 | ✅ |
| 224030294691 | harajuku-complete-guide-2025 | 2025-10-03 | ✅ |
| 224028694874 | ueno-ameyoko-guide | 2025-10-01 | ✅ |
| 224027835049 | omotesando-guide-2025 | 2025-10-01 | ✅ |
| 224026292057 | tokyo-october-festivals-2025 | 2025-12-31 | ✅ |
| 224026098490 | tokyo-subway-ticket-guide | 2025-09-29 | ✅ |
| 224025699867 | tokyo-subway-pass-vs-jr-tokunai-pass | 2025-09-29 | ✅ |
| 224025044772 | ginza-kuya-monaka-reservation-guide | - | pending |
| 224166818622 | asakusa-food-guide | 2026-01-31 | ✅ |
| 224024819592 | asakusa-complete-guide | 2025-09-28 | ✅ |
| 224024530348 | roppongi-art-night-guide | - | pending |
| 224022065518 | don-quijote-shopping-guide-2025 | 2025-09-26 | ✅ |
| 224010770861 | ginza-hachigo-reservation-guide | 2025-09-16 | ✅ |
| 224010546735 | japanese-whisky-yamazaki-hibiki-price-guide | 2025-09-16 | ✅ |
| 224008430188 | ginza-lotte-duty-free-whisky-guide | - | pending |
| 224007949043 | narita-airport-arrival-guide | 2025-09-14 | ✅ |
| 224004709356 | narita-airport-limousine-budget-bus-guide | 2026-02-15 | ✅ |
| 224003374650 | narita-airport-skyliner-guide | 2025-12-29 | ✅ |
| 223998533494 | visit-japan-web-registration-guide | - | pending |
| 223995074888 | haneda-airport-arrival-guide | 2026-02-15 | ✅ |
| 223992588094 | tokyo-september-festivals-2025 | 2025-09-02 | ✅ |
| 223989943826 | ginza-guide-2025 | 2025-01-06 | ✅ |
| 223988228389 | roppongi-attractions-guide | 2024-09-02 | ✅ |
| 223987954990 | roppongi-hills-observatory-guide | 2026-02-15 | ✅ |
| 223987115708 | iruka-tokyo-roppongi-michelin-ramen-guide | 2026-02-21 | ✅ |
| 223986407872 | tsujihan-midtown-kaisendon-guide | - | pending |
| 223985958480 | imakatsu-roppongi-tonkatsu-guide | - | pending |
| 223980220327 | tokyo-august-festivals-sumida-river | - | pending |
| 223980166231 | harajuku-super-yosakoi-festival-guide | - | pending |
| 223968462793 | azabudai-hills-commen-bakery-review | - | pending |
| 223958175295 | azabudai-hills-summer-festival-review | - | pending |
| 223957316412 | tsurutontan-roppongi-udon-guide | - | pending |
| 223915974358 | tokyo-conveyor-belt-sushi-tabelog-top10 | 2026-02-24 | ✅ |
| 223915389552 | azabudai-hills-series-chinese-restaurant | - | pending |
| 223915132048 | shimbashi-tonkatsu-horiichi | - | pending |
| 223913424029 | iruca-tokyo-roppongi-ramen-guide | - | pending |
| 223912913938 | pain-maison-ginza-salt-bread | - | pending |
| 223716380927 | azabudai-hills-sky-room-cafe-guide | - | pending |
| 223715784445 | ginza-wako-tea-salon | 2026-02-21 | ✅ |
| 223708789355 | azabudai-hills-criollo-chocolate-review | - | pending |
| 224124211319 | tokyo-ramen-street-best-8 | 2025-12-27 | ✅ |
| 223703326263 | ginza-shiseido-parlour-gift-guide | - | pending |
| 223702865232 | sapporo-the-bar-ginza | - | pending |
| 223702371242 | ginza-tenryu-gyoza-restaurant | - | pending |
| 223700200846 | tokyo-skytree-illumination-guide | - | pending |
| 223700095268 | tokyo-skytree-free-observatory | - | pending |
| 223699626846 | tokyo-skytree-gion-tsujiri-matcha | - | pending |
| 223698121379 | ginza-six-imadeya-sake-shopping | - | pending |
| 223697732942 | tokyo-skytree-triton-sushi-guide | - | pending |
| 223696568926 | roppongi-hills-christmas-market-2024 | - | pending |
| 223695518100 | tokyo-skytree-pokemon-center-review | - | pending |
| 223694645793 | ginza-akebono-strawberry-mochi | - | pending |
| 223694057318 | ginza-six-rooftop-garden | - | pending |
| 223693467715 | yamanoue-tempura-omakase-ginza | - | pending |
| 223693165027 | ginza-itoya-stationery-guide | - | pending |
| 223691371517 | tokyo-station-pokemon-store-review | - | pending |
| 223689247336 | miyashita-park-illumination-2024 | 2025-12-31 | ✅ |
| 223687520605 | roppongi-azabujuban-summer-festivals | - | pending |
| 223685676173 | wadakura-fountain-park-starbucks-review | - | pending |
| 223684908680 | shin-marunouchi-building-terrace-dinner | - | pending |
| 223681848151 | kitte-marunouchi-christmas-tree-observatory | 2026-02-25 | ✅ |
| 223681272647 | roppongi-hills-access-coin-locker-guide | - | pending |
| 223680263119 | tokyo-station-nemuro-hanamaru-sushi-guide | 2024-12-02 | ✅ |
| 223678791563 | yebisu-garden-place-access-guide | - | pending |
| 223675952285 | marunouchi-building-free-observatory | - | pending |
| 223675706489 | tokyo-station-breakfast-the-front-room | - | pending |
| 223674804939 | roppongi-hills-summer-festival-doraemon | - | pending |
| 223672616108 | azabudai-hills-teamlab-borderless-guide | 2026-02-20 | ✅ |
| 223670085459 | roppongi-midtown-christmas-review-2024 | - | pending |
| 223668826357 | yebisu-garden-place-illumination-christmas-market-2024 | - | pending |
| 223668328703 | yebisu-garden-place-free-observatory | - | pending |
| 223667593440 | rem-roppongi-hotel-guide | - | pending |
| 223667306537 | streamer-coffee-roppongi-guide | - | pending |
| 223666751487 | st-moritz-roppongi-bakery | - | pending |
| 223664743235 | shinanoya-roppongi-hills-supermarket | 2024-11-18 | ✅ |
| 223979907748 | yokohama-one-day-itinerary | 2025-08-22 | ✅ |
| 223976102621 | yokohama-minato-burari-ticket-guide | 2025-08-19 | ✅ |
---
## Excluded from Migration (Do Not Process)

| Naver ID | Description | Reason |
|----------|-------------|--------|
| 223669458145 | Ueno Museum Monet Exhibition | Outdated content/irrelevant to current project |
The following posts are explicitly excluded from migration (e.g., outdated content, irrelevant links):
---
## Pending Link References

These Naver post IDs are referenced in migrated posts but not yet migrated themselves:

| Naver ID | Referenced In | Description |
|----------|---------------|-------------|
| 224096203397 | shimokitazawa-tokyo-travel-guide | Shimokitazawa Vintage Shopping, Restaurants & Must-Visit Course |
| 224095118118 | - | Demoted from Quick (Filesystem mismatch) |
| 224024530348 | roppongi-art-night-guide | Roppongi Art Night 2025 Detailed Guide with Recommended Lineup |
| 224014619007 | don-quijote-shopping-guide-2025 | Suntory Whisky Official Japan Price Guide |
| 224008430188 | ginza-lotte-duty-free-whisky-guide | Ginza LOTTE Duty Free Whisky Purchase Guide (Yamazaki, Hibiki, Free Tasting) |
| 224007665631 | asakusa-complete-guide | Narita Airport to Asakusa Subway Guide |
| 224002738158 | narita-express-guide | Narita Express (N'EX) Reservation, Price, Timetable |
| 223993881300 | evangelion-30th-roppongi-2025, roppongi-attractions-guide | Tokyo Roppongi Restaurant Map |
| 223991251786 | shinanoya-roppongi-hills-supermarket, roppongi-attractions-guide | Dassai 23, 39, 45 Official Japanese Prices and Brewery Tour Guide |
| 223987115708 | iruka-tokyo-roppongi-michelin-ramen-guide | Iruka Tokyo Roppongi: Michelin Bib Gourmand Ramen Guide |
| 223986407872 | tsujihan-midtown-kaisendon-guide | Tsujihan Midtown: Roppongi Kaisendon Restaurant |
| 223985958480 | imakatsu-roppongi-tonkatsu-guide | Imakatsu Roppongi Main Store: Tokyo Tonkatsu Restaurant |
| 223980220327 | tokyo-august-festivals-sumida-river | August Tokyo Festivals: Sumida River Lantern Floating |
| 223980166231 | harajuku-super-yosakoi-festival-guide | Harajuku Omotesando Super Yosakoi Festival August Guide |
| 223969429024 | roppongi-attractions-guide | Sarashina Horii Main Store: Roppongi Soba Restaurant |
| 223968462793 | azabudai-hills-commen-bakery-review | Comme'N Tokyo Azabudai Hills Bakery Review |
| 223958175295 | azabudai-hills-summer-festival-review | Tokyo Azabudai Hills Summer Festival Review |
| 223957316412 | tsurutontan-roppongi-udon-guide | Tsurutontan Roppongi: Sanuki Udon Restaurant |
| 223915389552 | azabudai-hills-series-chinese-restaurant | Series Michelin 1-Star Chinese Restaurant Review |
| 223915132048 | shimbashi-tonkatsu-horiichi | Tokyo Shimbashi Tonkatsu Restaurant |
| 223914118735 | ueno-ameyoko-guide | Tokyo Ramen Guide (Kangnami's Treasure Box) |
| 223913830951 | toranomon-hills-complete-guide | Yakitori Omakase, Nonotori Gencho Review |
| 223913424029 | iruca-tokyo-roppongi-ramen-guide | Iruca Tokyo Roppongi: Michelin Ramen Restaurant |
| 223912913938 | pain-maison-ginza-salt-bread | Pain Maison Ginza Salt Bread Online Reservation |
| 223716380927 | azabudai-hills-sky-room-cafe-guide | Tokyo Azabudai Hills Observatory Cafe Sky Room Guide |
| 223709608832 | ginza-guide-2025 | Ginza Lotte Duty Free Shopping (Dassai 23, Yamazaki 12 Year) |
| 223708789355 | azabudai-hills-criollo-chocolate-review | Criollo Chocolatier Review |
| 223703326263 | ginza-shiseido-parlour-gift-guide | Ginza Shiseido Parlour Gift Shopping Guide |
| 223702865232 | sapporo-the-bar-ginza | Sapporo The Bar Ginza Perfect Draft Beer |
| 223702371242 | ginza-tenryu-gyoza-restaurant | Ginza Tenryu Grilled Gyoza Restaurant |
| 223700200846 | tokyo-skytree-illumination-guide | Tokyo Skytree Illumination & Christmas Market Detailed Review |
| 223700095268 | tokyo-skytree-free-observatory | Tokyo Skytree Free Observatory: SKYTREE VIEW |
| 223699626846 | tokyo-skytree-gion-tsujiri-matcha | Tokyo Skytree Dessert Spot: Gion Tsujiri Matcha Ice Cream Review |
| 223698121379 | ginza-six-imadeya-sake-shopping | Ginza Six Imadeya Sake & Whisky Shopping |
| 223697732942 | tokyo-skytree-triton-sushi-guide | Tokyo Skytree Conveyor Belt Sushi Restaurant Triton (Queue Number Tips) |
| 223696568926 | roppongi-hills-christmas-market-2024 | Roppongi Hills Christmas Market: A Little Germany in Tokyo |
| 223695518100 | tokyo-skytree-pokemon-center-review | Tokyo Skytree Town Pokemon Center Detailed Review |
| 223694057318 | ginza-six-rooftop-garden | Ginza Six Rooftop Free Observation Deck & Ice Rink |
| 223693467715 | yamanoue-tempura-omakase-ginza | Yamanoue Tempura Omakase Ginza Six Restaurant |
| 223693165027 | ginza-itoya-stationery-guide | Tokyo Ginza Representative Stationery Store: Itoya Main Store |
| 223691772722 | nihonbashi-tokyo-guide | Tokyo Nihonbashi Pokemon Center Tokyo DX & Pokemon Cafe Guide |
| 223691371517 | tokyo-station-pokemon-store-review | Tokyo Station Pokemon Store & Pikachu Card Review |
| 223688700265 | tokyo-christmas-illumination-best-5-2025 | 2024 Tokyo Omotesando Illumination and Harajuku Free Observatory |
| 223687520605 | roppongi-azabujuban-summer-festivals | August Tokyo Festivals: Roppongi Hills Bon Odori & Azabujuban Summer Festival |
| 223685676173 | wadakura-fountain-park-starbucks-review | Wadakura Fountain Park Starbucks Review (Night View) |
| 223684908680 | shin-marunouchi-building-terrace-dinner | Shin-Marunouchi Building Garden Terrace Dinner (Night View) |
| 223681848151 | kitte-marunouchi-christmas-tree-observatory | KITTE Marunouchi Christmas Tree & Free Observatory |
| 223681272647 | roppongi-hills-access-coin-locker-guide | How to Get to Roppongi Hills and Coin Locker Locations |
| 223678791563 | yebisu-garden-place-access-guide | How to Get to Yebisu Garden Place and Coin Locker Locations |
| 223675952285 | marunouchi-building-free-observatory | Marunouchi Building Free Observatory Sunset View |
| 223675706489 | tokyo-station-breakfast-the-front-room | Tokyo Station Breakfast: The Front Room French Toast |
| 223674804939 | roppongi-hills-summer-festival-doraemon | Tokyo Roppongi Hills Summer Festival: Doraemon |
| 223671427079 | azabudai-hills-complete-guide | 2024 Tokyo Azabudai Hills Christmas Market Review |
| 223670085459 | roppongi-midtown-christmas-review-2024 | 2024 Roppongi Tokyo Midtown Christmas Illumination and Santa Tree |
| 223668826357 | yebisu-garden-place-illumination-christmas-market-2024 | 2024 Yebisu Garden Place Christmas Archive |
| 223668328703 | yebisu-garden-place-free-observatory | Yebisu Garden Place Free Observatory Top of Yebisu Guide |
| 223667593440 | rem-roppongi-hotel-guide | rem Roppongi: Best Value Hotel Right in Front of Roppongi Station |
| 223667306537 | streamer-coffee-roppongi-guide | Streamer Coffee Company: Special Roppongi Cafe |
| 223666751487 | st-moritz-roppongi-bakery | St. Moritz: 80-Year-Old Traditional Bakery in Roppongi |
| 224150787671 | tokyo-moheji-monjayaki-marunouchi-guide | Tokyo Moheji Monjayaki Marunouchi: Best Menu & Waiting Guide |
| 224131055243 | shinjuku-department-store-guest-card-discount | Shinjuku Department Store Guest Card 5% Discount Comparison (Isetan vs Takashimaya) |
**Note:** The `tokyo-3-day-christmas-illumination-itinerary` post contains 30+ internal links. Extract them for detailed tracking when updating links.
---
## Statistics

- **Total Posts Migrated:** 175
- **Naver IDs Tracked:** 224
- **Pending References:** 62
- **Posts with Internal Links:** 46+
- **Links Updated:** Verified & Fixed on 2026-02-08
- **Last Migration Date:** 2026-02-25 (KITTE Marunouchi Christmas Tree & Observatory)

---

## Maintenance Notes

- This file is tracked in Git for collaboration
- Update this file EVERY TIME you migrate a new post
- Extract internal links during migration workflow
- Run batch conversion script when ready to update all links
- Keep this file synchronized with actual migrated posts

