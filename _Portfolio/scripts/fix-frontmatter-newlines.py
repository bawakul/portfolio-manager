#!/usr/bin/env python3
"""
Fix frontmatter formatting issues where closing --- is on same line as last field.
Ensures proper newline before closing ---.
"""

import re
from pathlib import Path

def fix_frontmatter_newline(notes_path):
    """Fix frontmatter closing newline"""
    with open(notes_path, 'r') as f:
        content = f.read()

    # Check if frontmatter has the issue: ]--- pattern
    if re.search(r'\]---', content):
        # Fix: add newline before closing ---
        fixed_content = re.sub(r'\]---', r']\n---', content)

        with open(notes_path, 'w') as f:
            f.write(fixed_content)

        return True

    return False

def main():
    # Get portfolio root directory
    script_dir = Path(__file__).parent
    portfolio_root = script_dir.parent.parent

    print("=" * 60)
    print("Fixing frontmatter newline issues")
    print("=" * 60)
    print()

    fixed = 0
    ok = 0

    # Find all project directories
    for project_dir in sorted(portfolio_root.iterdir()):
        if project_dir.is_dir() and not project_dir.name.startswith('.') and not project_dir.name.startswith('_') and project_dir.name != 'node_modules':
            notes_path = project_dir / f"{project_dir.name}.md"

            if notes_path.exists():
                if fix_frontmatter_newline(notes_path):
                    print(f"✅ {project_dir.name}: Fixed frontmatter newline")
                    fixed += 1
                else:
                    print(f"⏭️  {project_dir.name}: Already correct")
                    ok += 1
            else:
                print(f"⚠️  {project_dir.name}: No notes file found")

    print()
    print("=" * 60)
    print(f"✨ Done! Fixed {fixed} files, {ok} were already correct")
    print("=" * 60)

if __name__ == "__main__":
    main()
