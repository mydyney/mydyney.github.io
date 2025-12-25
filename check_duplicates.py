#!/usr/bin/env python3
"""Check for duplicate Naver IDs in LINK_MAPPING.md"""

# New mappings to add
new_mappings = {
    "hibiya-park-tokyo-guide": "224093593124",
    "jiyugaoka-tokyo-travel-guide": "224092707353",
    "miyashita-park-illumination-2024": "223689247336",
    "nihonbashi-tokyo-guide": "224042267263",
    "omotesando-guide-2025": "224027835049",
    "shibuya-station-coin-locker-luggage-storage-guide": "224107954391",
    "shimokitazawa-tokyo-travel-guide": "224096203397",
    "shinjuku-gashapon-shops-best-7": "224090178080",
    "shinjuku-neon-walk-tokyo-illumination-2025-2026": "224095124866",
    "tokyo-station-guide": "224031611221",
}

# Read LINK_MAPPING.md
with open('LINK_MAPPING.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("=== 중복 확인 ===\n")

duplicates = []
no_duplicates = []

for slug, naver_id in new_mappings.items():
    if naver_id in content:
        print(f"❌ 중복 발견: {slug} → {naver_id}")
        duplicates.append((slug, naver_id))
    else:
        print(f"✅ 중복 없음: {slug} → {naver_id}")
        no_duplicates.append((slug, naver_id))

print(f"\n총 {len(no_duplicates)}개 추가 가능, {len(duplicates)}개 중복")

if duplicates:
    print("\n⚠️ 중복된 항목:")
    for slug, naver_id in duplicates:
        print(f"  - {slug}: {naver_id}")
