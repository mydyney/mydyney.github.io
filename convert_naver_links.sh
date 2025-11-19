#!/bin/bash
# Convert all known Naver links to Hugo links

declare -A MAPPINGS=(
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
  ["223664743235"]="shinanoya-roppongi-hills-supermarket"
)

converted_count=0

for naver_id in "${!MAPPINGS[@]}"; do
  hugo_slug="${MAPPINGS[$naver_id]}"
  echo "Converting $naver_id to $hugo_slug..."

  # English (no language prefix - default language)
  en_count=$(find content/en/posts -name "*.md" -exec grep -l "https://blog.naver.com/tokyomate/$naver_id" {} + | wc -l)
  find content/en/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/posts/$hugo_slug/|g" {} +

  # Japanese (with /ja/ prefix)
  ja_count=$(find content/ja/posts -name "*.md" -exec grep -l "https://blog.naver.com/tokyomate/$naver_id" {} + | wc -l)
  find content/ja/posts -name "*.md" -exec sed -i "s|https://blog.naver.com/tokyomate/$naver_id|/ja/posts/$hugo_slug/|g" {} +

  total=$((en_count + ja_count))
  if [ $total -gt 0 ]; then
    echo "  ✅ Converted in $total files (EN: $en_count, JA: $ja_count)"
    converted_count=$((converted_count + 1))
  fi
done

echo ""
echo "================================================"
echo "Link conversion complete!"
echo "✅ Converted $converted_count different Naver IDs to Hugo URLs"
echo "================================================"
