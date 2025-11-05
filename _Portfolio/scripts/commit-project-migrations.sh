#!/bin/bash
# Commit migration changes in all project repositories

PORTFOLIO_ROOT="/Users/bharadwajkulkarni/Documents /Bawa's Lab"
cd "$PORTFOLIO_ROOT"

COMMIT_MSG="Migrate to [project-name].md structure

- Rename Notes.md to [project-name].md for unique Obsidian identification
- Update frontmatter: type: → project_type:
- Add bawa-notes tag for portfolio filtering
- Create Sessions/ folder for development logs
- Update .claude/CLAUDE.md with session tracking instructions

Part of portfolio-wide migration to improve Obsidian UX.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

echo "=============================="
echo "Committing project migrations"
echo "=============================="
echo

# Find all directories with .git folders (project repos)
for project_dir in */; do
    # Remove trailing slash
    project="${project_dir%/}"

    # Skip special directories
    if [[ "$project" == _* ]] || [[ "$project" == .* ]] || [[ "$project" == "node_modules" ]]; then
        continue
    fi

    # Check if it's a git repo
    if [ -d "$project/.git" ]; then
        echo "📦 $project"
        cd "$PORTFOLIO_ROOT/$project"

        # Check if there are changes
        if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git ls-files --others --exclude-standard)" ]; then
            # Add all changes
            git add .

            # Commit
            git commit -m "$COMMIT_MSG"

            if [ $? -eq 0 ]; then
                echo "   ✅ Committed migration changes"
            else
                echo "   ⚠️  Commit failed or no changes"
            fi
        else
            echo "   ⏭️  No changes to commit"
        fi

        echo
        cd "$PORTFOLIO_ROOT"
    fi
done

echo "=============================="
echo "✨ Done!"
echo "=============================="
