#!/usr/bin/env python3
"""
Update all project CLAUDE.md files with date format guidelines.

This script:
1. Finds all project CLAUDE.md/Claude.md files
2. Checks if they already have date format guidelines
3. Appends guidelines if missing
"""

import os
from pathlib import Path

# Portfolio root directory (script is in _Portfolio/scripts/)
PORTFOLIO_ROOT = Path(__file__).parent.parent.parent

# Date format guidelines to append
DATE_GUIDELINES = """
## Date Format Guidelines

When working with dates in this project:

- **Session filenames**: Use `YYYY-MM-DD-description.md` format (machine-sortable)
- **Frontmatter dates**: Use ISO format `YYYY-MM-DD` (for scripts and queries)
- **Display dates**: Use wiki links `[[DD MMM YYYY]]` (e.g., `[[03 Nov 2025]]`) for human-readable, Obsidian-linked dates
- **Session frontmatter**: Include these fields:
  ```yaml
  ---
  date: YYYY-MM-DD
  project: project-name
  type: session
  claude-generated: true
  tags: [session, planning/implementation/decision]
  ---
  ```

This ensures consistency across the portfolio and enables Obsidian cross-referencing.
"""

def has_date_guidelines(content: str) -> bool:
    """Check if file already has date format guidelines."""
    return '## Date Format Guidelines' in content or 'Date Format Guidelines' in content

def find_claude_files() -> list[Path]:
    """Find all CLAUDE.md and Claude.md files in project folders."""
    claude_files = []

    # Look for .claude folders (skip root portfolio .claude)
    for claude_dir in PORTFOLIO_ROOT.rglob('.claude'):
        if claude_dir == PORTFOLIO_ROOT / '.claude':
            continue  # Skip root portfolio .claude

        # Check for CLAUDE.md or Claude.md
        for variant in ['CLAUDE.md', 'Claude.md']:
            claude_file = claude_dir / variant
            if claude_file.exists():
                claude_files.append(claude_file)
                break  # Only one variant per project

    return claude_files

def update_claude_file(file_path: Path):
    """Append date format guidelines to a CLAUDE.md file."""
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has guidelines
    if has_date_guidelines(content):
        print(f"⏭️  Skipping {file_path.parent.parent.name} (already has date guidelines)")
        return False

    # Append guidelines
    new_content = content.rstrip() + '\n' + DATE_GUIDELINES

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    project_name = file_path.parent.parent.name
    print(f"✅ Updated {project_name}/.claude/{file_path.name}")
    return True

def main():
    print("🔍 Searching for project CLAUDE.md files...")
    claude_files = find_claude_files()

    if not claude_files:
        print("No project CLAUDE.md files found.")
        return

    print(f"Found {len(claude_files)} project CLAUDE.md files.\n")

    updated_count = 0
    for file_path in sorted(claude_files):
        if update_claude_file(file_path):
            updated_count += 1

    print(f"\n✨ Complete! Updated {updated_count}/{len(claude_files)} files.")

if __name__ == '__main__':
    main()
