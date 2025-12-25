#!/usr/bin/env python3
"""Analyze blog post formats"""

import os
from pathlib import Path

posts_dir = Path("content/en/posts")
posts = list(posts_dir.glob("*.md"))

with_container = 0
without_container = 0
examples_with = []
examples_without = []

for post in posts:
    try:
        content = post.read_text(encoding='utf-8')

        if 'blog-container' in content:
            with_container += 1
            if len(examples_with) < 5:
                examples_with.append(post.name)
        else:
            without_container += 1
            if len(examples_without) < 5:
                examples_without.append(post.name)
    except Exception as e:
        print(f"Error reading {post}: {e}")

print("=" * 70)
print("블로그 포스트 형식 분석")
print("=" * 70)
print(f"\n📊 통계:")
print(f"  전체 포스트: {len(posts)}")
print(f"  blog-container 사용: {with_container} ({with_container/len(posts)*100:.1f}%)")
print(f"  순수 Markdown: {without_container} ({without_container/len(posts)*100:.1f}%)")

print(f"\n✅ blog-container 사용 예시 (최대 5개):")
for ex in examples_with:
    print(f"  - {ex}")

print(f"\n📝 순수 Markdown 예시 (최대 5개):")
for ex in examples_without:
    print(f"  - {ex}")
