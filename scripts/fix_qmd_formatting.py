#!/usr/bin/env python3
"""Fix QMD formatting - add blank lines before all bullet lists."""

import re
from pathlib import Path

def fix_qmd_formatting(file_path):
    """Add blank line before bullet lists if missing."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check if current line is a bullet point starting with *
        if line.strip().startswith('*   **'):
            # Check if previous line is not empty
            if i > 0 and lines[i-1].strip() != '':
                # Add blank line before this bullet if it doesn't exist
                if not (i > 0 and fixed_lines and fixed_lines[-1] == ''):
                    fixed_lines.append('')
        
        fixed_lines.append(line)
    
    new_content = '\n'.join(fixed_lines)
    
    # Only write if changed
    if new_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Fix all .qmd files in books directory
books_dir = Path('/Users/algimantask/Personal/bookie/books')
fixed_count = 0

for qmd_file in sorted(books_dir.glob('*.qmd')):
    if fix_qmd_formatting(qmd_file):
        print(f"Fixed: {qmd_file.name}")
        fixed_count += 1
    else:
        print(f"No changes needed: {qmd_file.name}")

print(f"\nTotal files fixed: {fixed_count}")
