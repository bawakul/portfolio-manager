#!/usr/bin/env python3
"""
Add session auto-load hooks to existing projects.

This script:
1. Creates .claude/hooks/ directory in each project
2. Copies load-last-session.py hook script
3. Makes the script executable
4. Creates/updates .claude/settings.json with hook configuration
"""

import json
import shutil
from pathlib import Path

# Portfolio root directory
PORTFOLIO_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PORTFOLIO_ROOT / "_Templates"
HOOK_TEMPLATE = TEMPLATES_DIR / "load-last-session.py"

# Excluded directories
EXCLUDED_DIRS = {"_Portfolio", "_Templates", ".git", ".obsidian"}


def find_projects():
    """Find all project directories in the portfolio."""
    projects = []
    for item in PORTFOLIO_ROOT.iterdir():
        if item.is_dir() and item.name not in EXCLUDED_DIRS:
            projects.append(item)
    return sorted(projects)


def has_claude_config(project_path):
    """Check if project has .claude/CLAUDE.md."""
    return (project_path / ".claude" / "CLAUDE.md").exists()


def create_hooks_directory(project_path):
    """Create .claude/hooks/ directory if it doesn't exist."""
    hooks_dir = project_path / ".claude" / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    return hooks_dir


def copy_hook_script(project_path):
    """Copy load-last-session.py to project's hooks directory."""
    hooks_dir = create_hooks_directory(project_path)
    dest_script = hooks_dir / "load-last-session.py"

    if dest_script.exists():
        print(f"  ⚠️  Hook script already exists, overwriting...")

    shutil.copy2(HOOK_TEMPLATE, dest_script)

    # Make executable
    dest_script.chmod(0o755)

    return dest_script


def update_settings_json(project_path):
    """Create or update .claude/settings.json with hook configuration."""
    settings_file = project_path / ".claude" / "settings.json"

    # Hook configuration
    hook_config = {
        "hooks": {
            "UserPromptSubmit": [{
                "hooks": [{
                    "type": "command",
                    "command": "./.claude/hooks/load-last-session.py"
                }]
            }]
        }
    }

    if settings_file.exists():
        # Load existing settings
        with open(settings_file, "r") as f:
            settings = json.load(f)

        # Check if hook already configured
        if "hooks" in settings and "UserPromptSubmit" in settings["hooks"]:
            print(f"  ⚠️  Hooks already configured in settings.json")
            return "exists"

        # Merge configurations
        settings.update(hook_config)
    else:
        settings = hook_config

    # Write settings
    with open(settings_file, "w") as f:
        json.dump(settings, f, indent=2)

    return "updated" if settings_file.exists() else "created"


def migrate_project(project_path):
    """Add hook to a single project."""
    project_name = project_path.name

    print(f"\n📦 {project_name}")

    if not has_claude_config(project_path):
        print(f"  ⚠️  No .claude/CLAUDE.md found, skipping")
        return {
            "project": project_name,
            "status": "skipped",
            "reason": "no_claude_config"
        }

    try:
        # Create hooks directory
        hooks_dir = create_hooks_directory(project_path)
        print(f"  ✓ Created/verified {hooks_dir.relative_to(PORTFOLIO_ROOT)}")

        # Copy hook script
        script_path = copy_hook_script(project_path)
        print(f"  ✓ Copied hook script to {script_path.relative_to(PORTFOLIO_ROOT)}")
        print(f"  ✓ Made script executable")

        # Update settings.json
        settings_status = update_settings_json(project_path)
        if settings_status == "created":
            print(f"  ✓ Created .claude/settings.json with hook config")
        elif settings_status == "updated":
            print(f"  ✓ Updated .claude/settings.json with hook config")

        return {
            "project": project_name,
            "status": "success",
            "settings": settings_status
        }

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return {
            "project": project_name,
            "status": "error",
            "error": str(e)
        }


def main():
    """Run migration on all projects."""
    print("=" * 60)
    print("Session Auto-Load Hook Migration")
    print("=" * 60)

    if not HOOK_TEMPLATE.exists():
        print(f"❌ Hook template not found: {HOOK_TEMPLATE}")
        return

    print(f"\n📂 Scanning for projects in: {PORTFOLIO_ROOT}")

    projects = find_projects()
    print(f"Found {len(projects)} potential projects")

    results = []
    for project in projects:
        result = migrate_project(project)
        results.append(result)

    # Summary
    print("\n" + "=" * 60)
    print("Migration Summary")
    print("=" * 60)

    successful = [r for r in results if r["status"] == "success"]
    skipped = [r for r in results if r["status"] == "skipped"]
    errors = [r for r in results if r["status"] == "error"]

    print(f"\n✅ Successful: {len(successful)}")
    for r in successful:
        print(f"   - {r['project']}")

    if skipped:
        print(f"\n⚠️  Skipped: {len(skipped)}")
        for r in skipped:
            print(f"   - {r['project']} ({r['reason']})")

    if errors:
        print(f"\n❌ Errors: {len(errors)}")
        for r in errors:
            print(f"   - {r['project']}: {r['error']}")

    print(f"\n📊 Total: {len(results)} projects processed")
    print("\n" + "=" * 60)
    print("✓ Migration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
