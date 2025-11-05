#!/usr/bin/env python3
"""
Migrate all projects to new structure:
1. Rename Notes.md to [project-name].md
2. Update frontmatter: type: -> project_type:
3. Create Sessions/ folders in each project
4. Update project .claude/CLAUDE.md files to:
   - Reference new [project-name].md filename
   - Add session tracking instructions
"""

import re
from pathlib import Path

SESSION_TRACKING_SECTION = """
## Session Tracking

After each session, write session notes in `Sessions/YYYY-MM-DD-description.md`. **Ask for permission** before writing session notes to avoid overdoing it. Session notes help track progress and maintain context across sessions.
"""

def update_claude_md(claude_md_path, project_name):
    """Update a project's .claude/CLAUDE.md file"""
    if not claude_md_path.exists():
        return False

    with open(claude_md_path, 'r') as f:
        content = f.read()

    # Check if already has session tracking
    if "## Session Tracking" in content:
        print(f"  ⏭️  CLAUDE.md already has session tracking")
        return False

    # Add session tracking section before "## Date Format Guidelines" if it exists
    if "## Date Format Guidelines" in content:
        content = content.replace(
            "## Date Format Guidelines",
            SESSION_TRACKING_SECTION + "\n## Date Format Guidelines"
        )
    else:
        # Otherwise add before the end
        content = content.rstrip() + "\n" + SESSION_TRACKING_SECTION

    # Update any references to Notes.md -> [project-name].md
    content = content.replace("Notes.md", f"{project_name}.md")

    with open(claude_md_path, 'w') as f:
        f.write(content)

    return True

def rename_notes_file(project_dir, project_name):
    """Rename Notes.md to [project-name].md and update frontmatter"""
    notes_path = project_dir / "Notes.md"
    new_path = project_dir / f"{project_name}.md"

    if not notes_path.exists():
        return "no-notes"

    if new_path.exists():
        return "already-renamed"

    # Read and update content
    with open(notes_path, 'r') as f:
        content = f.read()

    # Update frontmatter: type: -> project_type:
    content = re.sub(r'\ntype:', '\nproject_type:', content)

    # Write to new filename
    with open(new_path, 'w') as f:
        f.write(content)

    # Remove old file
    notes_path.unlink()

    return "renamed"

def create_sessions_folder(project_dir):
    """Create Sessions/ folder if it doesn't exist"""
    sessions_dir = project_dir / "Sessions"

    if sessions_dir.exists():
        return "exists"

    sessions_dir.mkdir()
    return "created"

def migrate_project(project_dir):
    """Migrate a single project to new structure"""
    project_name = project_dir.name
    print(f"\n📦 {project_name}")

    actions = []

    # 1. Rename Notes.md
    rename_result = rename_notes_file(project_dir, project_name)
    if rename_result == "renamed":
        actions.append(f"✅ Renamed Notes.md -> {project_name}.md")
    elif rename_result == "already-renamed":
        actions.append(f"⏭️  Already using {project_name}.md")
    else:
        actions.append("⚠️  No Notes.md found")

    # 2. Create Sessions/ folder
    sessions_result = create_sessions_folder(project_dir)
    if sessions_result == "created":
        actions.append("✅ Created Sessions/ folder")
    else:
        actions.append("⏭️  Sessions/ folder already exists")

    # 3. Update .claude/CLAUDE.md
    claude_md_path = project_dir / ".claude" / "CLAUDE.md"
    if update_claude_md(claude_md_path, project_name):
        actions.append("✅ Updated CLAUDE.md with session tracking")
    elif claude_md_path.exists():
        actions.append("⏭️  CLAUDE.md already up to date")
    else:
        actions.append("⚠️  No .claude/CLAUDE.md found")

    for action in actions:
        print(f"  {action}")

    return len([a for a in actions if a.startswith("✅")])

def main():
    # Get portfolio root directory
    script_dir = Path(__file__).parent
    portfolio_root = script_dir.parent.parent

    print("=" * 60)
    print("PORTFOLIO MIGRATION: Notes.md -> [project-name].md")
    print("=" * 60)

    # Find all project directories
    project_dirs = []
    for item in portfolio_root.iterdir():
        if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_') and item.name != 'node_modules':
            project_dirs.append(item)

    project_dirs.sort()

    print(f"\nFound {len(project_dirs)} projects to migrate\n")

    total_changes = 0
    for project_dir in project_dirs:
        changes = migrate_project(project_dir)
        total_changes += changes

    print("\n" + "=" * 60)
    print(f"✨ Migration complete! Made {total_changes} changes across {len(project_dirs)} projects")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review changes in your projects")
    print("2. Commit the migration")
    print("3. Update any external references to Notes.md\n")

if __name__ == "__main__":
    main()
