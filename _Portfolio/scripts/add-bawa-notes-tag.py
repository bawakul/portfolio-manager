#!/usr/bin/env python3
"""
Add 'bawa-notes' tag to all project notes files.
"""

import re
from pathlib import Path

def add_tag_to_frontmatter(notes_path):
    """Add bawa-notes tag to a project notes file"""
    with open(notes_path, 'r') as f:
        content = f.read()

    # Split into frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"⚠️  Invalid frontmatter in {notes_path}")
        return False

    frontmatter = parts[1]

    # Check if tags already exist
    if 'tags:' in frontmatter:
        # Check if bawa-notes is already in tags
        if 'bawa-notes' in frontmatter:
            return False  # Already has the tag

        # Add bawa-notes to existing tags
        # Handle both list format and array format
        if re.search(r'tags:\s*\[', frontmatter):
            # Array format: tags: [tag1, tag2]
            frontmatter = re.sub(
                r'(tags:\s*\[)([^\]]*)',
                r'\1bawa-notes, \2',
                frontmatter
            )
        else:
            # List format: tags:\n  - tag1
            frontmatter = re.sub(
                r'(tags:)',
                r'\1\n  - bawa-notes',
                frontmatter
            )
    else:
        # No tags field exists, add it
        frontmatter = frontmatter.rstrip() + '\ntags: [bawa-notes]'

    # Reconstruct content
    new_content = f"---{frontmatter}---{parts[2]}"

    with open(notes_path, 'w') as f:
        f.write(new_content)

    return True

def main():
    # Get portfolio root directory
    script_dir = Path(__file__).parent
    portfolio_root = script_dir.parent.parent

    print("=" * 60)
    print("Adding 'bawa-notes' tag to all project notes files")
    print("=" * 60)
    print()

    updated = 0
    skipped = 0

    # Find all project directories
    for project_dir in sorted(portfolio_root.iterdir()):
        if project_dir.is_dir() and not project_dir.name.startswith('.') and not project_dir.name.startswith('_') and project_dir.name != 'node_modules':
            notes_path = project_dir / f"{project_dir.name}.md"

            if notes_path.exists():
                if add_tag_to_frontmatter(notes_path):
                    print(f"✅ {project_dir.name}: Added bawa-notes tag")
                    updated += 1
                else:
                    print(f"⏭️  {project_dir.name}: Already has bawa-notes tag")
                    skipped += 1
            else:
                print(f"⚠️  {project_dir.name}: No notes file found")

    print()
    print("=" * 60)
    print(f"✨ Done! Updated {updated} files, skipped {skipped}")
    print("=" * 60)

if __name__ == "__main__":
    main()
