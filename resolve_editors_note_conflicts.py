#!/usr/bin/env python3
"""Resolve Editor's Note merge conflicts automatically"""

import os
import re
from pathlib import Path

def resolve_conflict(filepath):
    """Resolve conflict by keeping only one Editor's Note"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the conflict structure:
    # <<<<<<< HEAD
    # =======
    # (editor's note from origin/main)
    # >>>>>>> origin/main
    # (editor's note we want to keep)
    
    # Remove the conflict markers and origin/main's version
    # Keep only our version (after >>>>>>>)
    pattern = r'<<<<<<< HEAD\n=======\n.*?>>>>>>> origin/main\n+'
    
    resolved = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Check if content changed
    if resolved != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(resolved)
        return True
    return False

def main():
    """Resolve all conflicts in blog posts"""
    
    # Get all conflicted files from git status
    import subprocess
    result = subprocess.run(
        ['git', 'diff', '--name-only', '--diff-filter=U'],
        capture_output=True,
        text=True
    )
    
    conflicted_files = result.stdout.strip().split('\n')
    conflicted_files = [f for f in conflicted_files if f.endswith('.md')]
    
    fixed_count = 0
    
    for filepath in conflicted_files:
        if os.path.exists(filepath):
            if resolve_conflict(filepath):
                fixed_count += 1
                print(f"✓ Resolved: {filepath}")
    
    print(f"\n{'='*60}")
    print(f"Total conflicts resolved: {fixed_count}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
