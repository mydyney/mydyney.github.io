#!/usr/bin/env python3
"""Resolve merge conflicts in kaldi-coffee-farm-shopping-list.md files"""

import re

def resolve_conflict(filepath):
    """Resolve conflict by keeping HEAD version (with <strong> and Editor's Note)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove conflict markers and keep HEAD version
    # Pattern: <<<<<<< HEAD\n(content)\n=======\n(content)\n>>>>>>> origin/main
    pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> origin/main'
    resolved = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(resolved)
    
    print(f"✓ Resolved: {filepath}")

# Resolve all three conflicted files
files = [
    'content/en/posts/kaldi-coffee-farm-shopping-list.md',
    'content/ja/posts/kaldi-coffee-farm-shopping-list.md',
    'content/zh-cn/posts/kaldi-coffee-farm-shopping-list.md'
]

for filepath in files:
    resolve_conflict(filepath)

print("\n✅ All conflicts resolved!")
print("Kept: <strong> tags + Editor's Note (from HEAD)")
print("Removed: **bold** syntax (from origin/main)")
