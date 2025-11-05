#!/usr/bin/env python3
"""
Populate [project-name].md files for all projects in the portfolio.
Reads git activity to set initial metadata intelligently.
"""

import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Project type inference based on name patterns
TYPE_PATTERNS = {
    'tool': ['tool', 'setup', 'manager', 'poc'],
    'experiment': ['example', 'poc', 'transcript'],
    'design': ['visual', 'essay'],
    'product': []  # default
}

def run_git_command(project_dir, command):
    """Run a git command in the project directory"""
    try:
        result = subprocess.run(
            command,
            cwd=project_dir,
            capture_output=True,
            text=True,
            shell=True
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None

def get_last_commit_date(project_dir):
    """Get the date of the last commit"""
    date_str = run_git_command(project_dir, "git log -1 --format=%ci")
    if date_str:
        # Parse git date format: "YYYY-MM-DD HH:MM:SS +ZZZZ"
        return datetime.fromisoformat(date_str.split()[0])
    return None

def get_repo_url(project_dir):
    """Get the remote repository URL"""
    url = run_git_command(project_dir, "git remote get-url origin")
    return url if url else ""

def infer_project_type(project_name):
    """Infer project type from name"""
    name_lower = project_name.lower()
    for ptype, patterns in TYPE_PATTERNS.items():
        if any(pattern in name_lower for pattern in patterns):
            return ptype
    return 'product'  # default

def determine_status(last_commit_date):
    """Determine project status based on last commit date"""
    if not last_commit_date:
        return 'paused'

    days_ago = (datetime.now() - last_commit_date).days

    if days_ago < 7:
        return 'active'
    elif days_ago < 30:
        return 'paused'
    else:
        return 'paused'

def create_notes_file(project_dir, project_name, template_path):
    """Create [project-name].md file from template with populated metadata"""
    notes_path = project_dir / f"{project_name}.md"

    # Skip if [project-name].md already exists
    if notes_path.exists():
        print(f"⏭️  {project_name}: {project_name}.md already exists, skipping")
        return

    # Read template
    with open(template_path, 'r') as f:
        content = f.read()

    # Get git data
    last_commit = get_last_commit_date(project_dir)
    repo_url = get_repo_url(project_dir)

    # Populate metadata
    status = determine_status(last_commit)
    project_type = infer_project_type(project_name)
    last_worked = last_commit.strftime("%Y-%m-%d") if last_commit else "YYYY-MM-DD"

    # Replace template placeholders
    content = content.replace("Project Name", project_name)
    content = content.replace("status: active", f"status: {status}")
    content = content.replace("project_type: product", f"project_type: {project_type}")
    content = content.replace("last_worked: YYYY-MM-DD", f"last_worked: {last_worked}")
    content = content.replace('repo: "https://github.com/..."', f'repo: "{repo_url}"')

    # Write [project-name].md
    with open(notes_path, 'w') as f:
        f.write(content)

    print(f"✅ {project_name}: Created {project_name}.md (status={status}, project_type={project_type}, last_worked={last_worked})")

def main():
    # Get portfolio root directory (parent of _Portfolio)
    script_dir = Path(__file__).parent
    portfolio_root = script_dir.parent.parent

    # Template path
    template_path = portfolio_root / "_Templates" / "Notes-Template.md"

    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        return

    # Find all project directories (exclude hidden, _Portfolio, _Templates, node_modules)
    project_dirs = []
    for item in portfolio_root.iterdir():
        if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_') and item.name != 'node_modules':
            project_dirs.append(item)

    project_dirs.sort()

    print(f"\n📝 Creating [project-name].md files for {len(project_dirs)} projects...\n")

    for project_dir in project_dirs:
        create_notes_file(project_dir, project_dir.name, template_path)

    print(f"\n✨ Done! Check your projects for new [project-name].md files.\n")

if __name__ == "__main__":
    main()
