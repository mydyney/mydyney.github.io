#!/bin/bash

# Download images for Kiwamiya Hamburg Shibuya Parco blog post
# Target directory: static/images/posts

cd "$(dirname "$0")"
mkdir -p static/images/posts

# Image URLs from Naver postfiles
declare -A IMAGES=(
  ["01"]="https://postfiles.pstatic.net/MjAyNTEyMTBfNzIg/MDAxNzY1Mzc1ODY1MDU5.CDPCB-BPHnU-_v5kcIp9bVpx5pfjynPpSai53D_jKKMg.7u5Pi7QEmsLtKs7LlFhYSLVdJPgLoNgtGy6DDZuw-s4g.JPEG/SE-2bff4fde-4134-4807-a73a-7d93c1890040.jpg"
  ["02"]="https://postfiles.pstatic.net/MjAyNTEyMTBfODgg/MDAxNzY1Mzc1ODY2NzQw.XrSqTR9Td9m9i76nCmbfTiY4pUHQt1JhiMzHuBiHcHEg.YEt3M7C11ZRidQkNqZSQkvy6OnhbdssabmtV3q75Chkg.JPEG/SE-70c4f5b9-5aa4-49b6-af3c-7be74a1593be.jpg"
  ["03"]="https://postfiles.pstatic.net/MjAyNTEyMTBfMjMz/MDAxNzY1Mzc1ODY4NzE2.3sxaf4FgwyDlzV-9VEM5PkHfh_DHFOCDSXFfjfPy3-8g.3BhJXCYitT_Dy4mj8shsuQwJUgV5zFzvv2sPjmtiKMEg.JPEG/SE-f607d9fb-e6d4-4411-b753-30363805fcb1.jpg"
  ["04"]="https://postfiles.pstatic.net/MjAyNTEyMTBfNDcg/MDAxNzY1Mzc1ODcwNDcz.2L4ZVp6au1MxRJNVe_obXPCbtZaEU0c5FqzwdEuJjFYg.nkQYGKcdjxGqKBbit09xBNuQIuEnPIKpU7PdgqDT7Bsg.JPEG/SE-de66bf9a-6b16-4bfa-86ab-652ca76e730a.jpg"
  ["05"]="https://postfiles.pstatic.net/MjAyNTEyMTBfMTc4/MDAxNzY1Mzc1ODI3NzAy.lYnPG6Qz_VZQjqPkpRaij4gjmg4aKxaHVlLjk5PwkBYg.lg70bAfxprqavhsos2XSPgRGXP2o7wGYM2neDFF02g8g.PNG/SE-96330c75-474b-4746-8692-9a849b3a2bf6.png"
  ["06"]="https://postfiles.pstatic.net/MjAyNTEyMTBfMTc2/MDAxNzY1Mzc1ODI5MTc1.ubqsWiDry_mqb3z47sw53IC9ocfrC-dPGXzNFgo6OXAg.wKuS0CxG80G2t6NnLW1u-ih0uwug4ypWvaxUznvtwRYg.PNG/SE-9b721c5c-0bc3-4708-b9b5-f57b9a341a9d.png"
  ["07"]="https://postfiles.pstatic.net/MjAyNTEyMTBfMjEw/MDAxNzY1Mzc1ODMwMjY3.UanYuuK7b9O6IYD9NlWNfck_fHNyetsDVbTDFsbK-iQg.JmvXQQyVZGPdFnOl6ASb-3Q6taDYrGeRtY5A3aVKcxgg.PNG/SE-c86027c4-81e2-49e8-869e-a1cf14bf666e.png"
  ["08"]="https://postfiles.pstatic.net/MjAyNTEyMTBfMjkz/MDAxNzY1Mzc1ODcyMzQx.OB0kqYLHxcEkFWXee2uvr2pK3xAV2buxBueDRae8L68g.rptugHdvIMqaGusbmxJp-TkV6yXyDcWiKAxPn8em4O8g.JPEG/SE-7fc3cfed-9ffa-4ff2-892d-4881bd025a4b.jpg"
  ["09"]="https://postfiles.pstatic.net/MjAyNTEyMTBfODEg/MDAxNzY1Mzc1ODc0MjA1.UdxAKHRY0IKp8LijvZN99cfqSiYliIjJjTk26RuWv7Yg.dy3FhNBGZij2_EwGP4uKTlL8DgFkExlLYEhSlhvzFD8g.JPEG/SE-3b6c3bae-4bf0-4661-b24b-dbad7d09494f.jpg"
  ["10"]="https://postfiles.pstatic.net/MjAyNTEyMTBfMTkx/MDAxNzY1MzcxNjc1ODI0.QVSC5bBWG1X2JAK349X3lA6ppIPdrzh8GNc6qxUZ9GIg.1Q_zNrZ-yTLDlQuw3KEn-vCSQuSru3sjkQagXkhYNMog.GIF/KIWAMIWA_HAMBURG.gif"
  ["11"]="https://postfiles.pstatic.net/MjAyNTEyMTBfODkg/MDAxNzY1Mzc1ODc1OTEz.Elua-JAcJDmaDoV8rCoKJTGCCQYO1en0AuByVQzpSQcg.vorIviq4wqi14eyzbZ77o57R1i1wG272huFvh-WOdOcg.JPEG/SE-81521b28-8fea-4d2d-88ea-739b380509e9.jpg"
)

echo "Downloading Kiwamiya Hamburg images..."

for num in "${!IMAGES[@]}"; do
  url="${IMAGES[$num]}"
  # Determine extension from URL
  if [[ $url == *.gif ]]; then
    ext="gif"
  elif [[ $url == *.PNG* ]] || [[ $url == *.png* ]]; then
    ext="jpg"  # Convert PNG to JPG
  else
    ext="jpg"
  fi
  
  output_file="static/images/posts/shibuya-parco-kiwamiya-hamburg-waiting-menu-${num}.${ext}"
  
  echo "Downloading image $num..."
  curl -L "$url" -o "$output_file"
  
  # Convert PNG to JPG if needed
  if [[ $url == *.PNG* ]] || [[ $url == *.png* ]]; then
    echo "Converting PNG to JPG for image $num..."
    sips -s format jpeg "$output_file" --out "${output_file%.jpg}.jpg" 2>/dev/null || convert "$output_file" "${output_file%.jpg}.jpg" 2>/dev/null
  fi
done

echo "Download complete! Downloaded 11 images."
echo "Note: Image 10 is a GIF and may need to be converted to video format for Hugo."
