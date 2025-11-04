#!/usr/bin/env python3
"""
Upgrade existing Notes.md files to new template structure.
Adds Overview, Current Status sections, and tagging convention.
"""

import re
from pathlib import Path

TAGGING_COMMENT = """<!-- Tagging convention for entries below:
Source: #claude (AI-generated) or #user (human-written)
Type: #session (work summary), #reflection (insights), #planning (roadmap), #decision (key choices)
Example: "### [[DD MMM YYYY]] - Planning Session #user #planning"
-->"""

def upgrade_notes_file(notes_path):
    """Upgrade a Notes.md file to new template structure"""
    with open(notes_path, 'r') as f:
        content = f.read()

    # Check if already upgraded
    if "## Overview" in content and "## Current Status" in content:
        return False  # Already upgraded

    # Split into frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"⚠️  Invalid frontmatter in {notes_path}")
        return False

    frontmatter = f"---{parts[1]}---"
    body = parts[2].strip()

    # Extract project name from heading
    match = re.search(r'^# (.+?) - Notes', body, re.MULTILINE)
    project_name = match.group(1) if match else "Project"

    # Build new body with sections
    new_body = f"""# {project_name} - Notes

## Overview
[Brief description of what this project is and why it exists]

## Current Status
[What's working, what's blocked, what's next]

## Running Notes

{TAGGING_COMMENT}

"""

    # Extract existing running notes content (everything after "## Running Notes")
    running_notes_match = re.search(r'## Running Notes\s*(.*)', body, re.DOTALL)
    if running_notes_match:
        existing_notes = running_notes_match.group(1).strip()
        if existing_notes:
            new_body += existing_notes + "\n"

    # Write updated content
    with open(notes_path, 'w') as f:
        f.write(frontmatter + "\n\n" + new_body)

    return True

def main():
    # Get portfolio root directory
    script_dir = Path(__file__).parent
    portfolio_root = script_dir.parent.parent

    # Find all Notes.md files
    upgraded = 0
    skipped = 0

    for project_dir in portfolio_root.iterdir():
        if project_dir.is_dir() and not project_dir.name.startswith('.') and not project_dir.name.startswith('_'):
            notes_path = project_dir / "Notes.md"
            if notes_path.exists():
                if upgrade_notes_file(notes_path):
                    print(f"✅ Upgraded: {project_dir.name}")
                    upgraded += 1
                else:
                    print(f"⏭️  Skipped: {project_dir.name} (already upgraded)")
                    skipped += 1

    print(f"\n✨ Done! Upgraded {upgraded} files, skipped {skipped}.\n")

if __name__ == "__main__":
    main()
