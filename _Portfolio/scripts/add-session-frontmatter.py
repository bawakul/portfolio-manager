#!/usr/bin/env python3
"""
Add frontmatter and wiki link dates to existing session notes.

This script:
1. Finds all session note markdown files
2. Extracts date from filename (YYYY-MM-DD format)
3. Detects project name from folder path
4. Adds frontmatter with metadata
5. Inserts wiki link date [[DD MMM YYYY]] at top of content
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Portfolio root directory (script is in _Portfolio/scripts/)
PORTFOLIO_ROOT = Path(__file__).parent.parent.parent

def parse_date_from_filename(filename: str) -> datetime | None:
    """Extract date from filename in YYYY-MM-DD format."""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    if match:
        try:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        except ValueError:
            return None
    return None

def format_wiki_link_date(date: datetime) -> str:
    """Format date as wiki link: [[DD MMM YYYY]]"""
    return f"[[{date.strftime('%d %b %Y')}]]"

def infer_tags(filename: str, content: str) -> list[str]:
    """Infer tags from filename and content."""
    tags = ['session']

    # Check filename for keywords
    filename_lower = filename.lower()
    if 'planning' in filename_lower or 'plan' in filename_lower:
        tags.append('planning')
    elif 'decision' in filename_lower:
        tags.append('decision')
    elif 'implementation' in filename_lower or 'setup' in filename_lower:
        tags.append('implementation')
    elif 'initial' in filename_lower:
        tags.append('planning')

    # Check content for keywords if no tag found yet
    if len(tags) == 1:
        content_lower = content.lower()
        if 'decision' in content_lower or 'architecture' in content_lower:
            tags.append('decision')
        elif 'setup' in content_lower or 'initialize' in content_lower:
            tags.append('implementation')
        else:
            tags.append('planning')

    return tags

def has_frontmatter(content: str) -> bool:
    """Check if file already has frontmatter."""
    return content.strip().startswith('---')

def add_frontmatter_to_file(file_path: Path):
    """Add frontmatter and wiki link date to a session note file."""
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has frontmatter
    if has_frontmatter(content):
        print(f"⏭️  Skipping {file_path.name} (already has frontmatter)")
        return False

    # Extract date from filename
    date = parse_date_from_filename(file_path.name)
    if not date:
        print(f"⚠️  Skipping {file_path.name} (couldn't parse date)")
        return False

    # Detect project from path
    # Path structure: portfolio-root/project-name/Sessions/file.md
    parts = file_path.parts
    try:
        sessions_idx = parts.index('Sessions')
        project_name = parts[sessions_idx - 1]
    except (ValueError, IndexError):
        # Fallback: try to find project folder
        project_name = file_path.parent.parent.name

    # Infer tags
    tags = infer_tags(file_path.name, content)

    # Format frontmatter
    iso_date = date.strftime('%Y-%m-%d')
    wiki_date = format_wiki_link_date(date)

    frontmatter = f"""---
date: {iso_date}
project: {project_name}
type: session
claude-generated: true
tags: {tags}
---

# Session: {wiki_date}

"""

    # Combine frontmatter with existing content
    new_content = frontmatter + content

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Updated {file_path.name} (project: {project_name}, tags: {tags})")
    return True

def find_session_files() -> list[Path]:
    """Find all session note files in the portfolio."""
    session_files = []

    # Look for Sessions/ folders
    for sessions_dir in PORTFOLIO_ROOT.rglob('Sessions'):
        if sessions_dir.is_dir():
            # Find all .md files in Sessions folder
            for md_file in sessions_dir.glob('*.md'):
                session_files.append(md_file)

    return session_files

def main():
    print("🔍 Searching for session notes...")
    session_files = find_session_files()

    if not session_files:
        print("No session files found.")
        return

    print(f"Found {len(session_files)} session files.\n")

    updated_count = 0
    for file_path in sorted(session_files):
        if add_frontmatter_to_file(file_path):
            updated_count += 1

    print(f"\n✨ Complete! Updated {updated_count}/{len(session_files)} files.")

if __name__ == '__main__':
    main()
