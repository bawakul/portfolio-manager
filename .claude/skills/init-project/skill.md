# Project Initializer

Initialize a new project with proper structure, Claude configuration, and GitHub integration.

## Process

### 1. Gather Project Information

Use the AskUserQuestion tool to collect:

**Project Name:**
- Question: "What is the project name?"
- Header: "Project Name"
- Options: "Use 'Other' to type the name"
- Store as: lowercase-with-hyphens format for folder name

**Project Type:**
- Question: "What type of project is this?"
- Header: "Project Type"
- Options:
  - "Product" - User-facing app/service with spec-driven development
  - "Personal Tool" - Scripts/automation for your own use
  - "Experiment" - Prototype/learning/quick experiment
  - "Design" - Creative coding/design system/visual project

**Project Description:**
- Question: "What is the project vision/description?"
- Header: "Description"
- Options: "Use 'Other' to type the description"

### 2. Create Project Directory

```bash
# Create project in the portfolio directory (current working directory)
mkdir -p "{project-name}"
cd "{project-name}"
```

### 3. Create .claude/Claude.md

Create `.claude/` directory and `Claude.md` with this template:

```markdown
# Development Partner - {Project Name}

You are a **development partner** for this {project-type} project. Your role is to help **design, implement, test, and ship features** while maintaining good practices and project momentum.

## Project Vision

{user-provided-description}

## Your Role

### What You DO:
- Help plan and break down tasks
- Write and implement features
- Maintain project structure and organization
- Manage git workflow (commits, branches, PRs)
- Track progress and push toward completion
- Suggest next steps and priorities
- Keep documentation updated
- Ensure code quality and testing

### What You DON'T Do:
- Over-engineer solutions - prefer simple and pragmatic
- Add unnecessary complexity or abstractions
- Ignore explicit project requirements or constraints

## Project Type: {Project Type}

{type-specific-guidance}

## Communication Style
- Direct and practical
- Focus on shipping and completion
- Ask clarifying questions when ambiguous
- Suggest concrete next actions

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
```

**Type-Specific Guidance:**

**For Product:**
```
This is a product for users. Follow spec-driven development:
1. Write/update SPEC.md before implementing features
2. Ensure features match the spec
3. Think about user experience and edge cases
4. Prioritize shipping and iterating
```

**For Personal Tool:**
```
This is a tool for personal use. Focus on:
1. Pragmatic solutions over perfect code
2. Document usage in USAGE.md
3. Make it work first, optimize later
4. Keep it maintainable for future you
```

**For Experiment:**
```
This is an experimental/learning project. Focus on:
1. Document learnings and findings in LEARNING.md
2. Iterate quickly, break things
3. Capture insights and "aha moments"
4. Don't over-engineer
```

**For Design:**
```
This is a design/creative project. Focus on:
1. Maintain visual references in INSPIRATION.md
2. Balance creativity with technical constraints
3. Document design decisions
4. Iterate on aesthetics
```

### 4. Create README.md

```markdown
# {Project Name}

{user-provided-description}

## Project Type
{Project Type}

## Status
🚧 In Development

## Getting Started

{type-specific-getting-started}

## Project Structure

```
{project-name}/
├── .claude/         # Project manager configuration
├── README.md        # This file
├── Notes.md         # Project notes and portfolio tracking
{type-specific-files}
```

## Development

(Add development instructions as you build)

## License

(Add license if needed)
```

**Type-Specific Getting Started:**

**Product:**
```
1. Read SPEC.md for project requirements
2. Follow spec-driven development workflow
3. Update spec as requirements evolve
```

**Personal Tool:**
```
1. See USAGE.md for how to use this tool
2. Modify and adapt as needed
```

**Experiment:**
```
1. Check LEARNING.md for goals and findings
2. Experiment freely
```

**Design:**
```
1. See INSPIRATION.md for visual references
2. Iterate on design
```

### 5. Create .gitignore

```
# Dependencies
node_modules/
venv/
env/
__pycache__/

# Environment
.env
.env.local

# OS Files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Build outputs
dist/
build/
*.pyc
*.pyo

# Logs
*.log
npm-debug.log*
```

### 6. Create Type-Specific File

**For Product** - Create `SPEC.md`:
```markdown
# {Project Name} - Specification

## Overview
{user-provided-description}

## User Stories

(Add user stories here)

## Features

### MVP
- [ ] (Define minimum viable features)

### Future
- (Nice-to-have features)

## Technical Approach

(Add technical decisions here)

## Open Questions

(Track unresolved questions)
```

**For Personal Tool** - Create `USAGE.md`:
```markdown
# Usage Guide - {Project Name}

## What It Does
{user-provided-description}

## How to Use

(Add usage instructions)

## Configuration

(Add configuration options)

## Examples

(Add example usage)
```

**For Experiment** - Create `LEARNING.md`:
```markdown
# Learning Journal - {Project Name}

## Goal
{user-provided-description}

## Questions to Explore
- (What do you want to learn?)

## Findings

### [Date]
(Document learnings as you go)

## Resources
- (Links and references)
```

**For Design** - Create `INSPIRATION.md`:
```markdown
# Design Inspiration - {Project Name}

## Vision
{user-provided-description}

## Visual References
- (Add links to inspiring designs)

## Color Palette
(Define colors)

## Typography
(Define fonts)

## Design Decisions

### [Date]
(Document design choices)
```

### 7. Create Notes.md

Create `Notes.md` with frontmatter for portfolio tracking. **Content sections should be left empty as placeholders for the user to fill in.**

```markdown
---
status: active
type: {project-type}
last_worked: {YYYY-MM-DD}
next_action: "{type-specific-next-action}"
repo: "https://github.com/{username}/{project-name}"
---

# {Project Name} - Notes

## Overview
[Brief description of what this project is and why it exists]

## Current Status
[What's working, what's blocked, what's next]

## Running Notes
[Your running notes, session summaries, and project context go here]
```

**Type-Specific Next Actions:**
- **Product**: "Refine SPEC.md with user requirements"
- **Personal Tool**: "Define usage patterns in USAGE.md"
- **Experiment**: "Set learning goals in LEARNING.md"
- **Design**: "Gather visual inspiration in INSPIRATION.md"

**Important:** Only fill in the frontmatter. Leave the content sections (Overview, Current Status, Running Notes) as placeholder text in brackets for the user to write themselves.

### 8. Initialize Git and Push to GitHub

```bash
git init
git add .
git commit -m "Initial project setup

- Initialize project structure
- Add Claude manager configuration
- Add project documentation
- Add Notes.md for portfolio tracking

🤖 Generated with Claude Code"

# Create GitHub repo (auto-creates on personal account)
gh repo create {project-name} --private --source=. --remote=origin --push
```

If `gh` is not available or fails, provide manual instructions:
```
GitHub setup required:
1. Create a new repository at https://github.com/new
2. Name it: {project-name}
3. Run: git remote add origin git@github.com:{username}/{project-name}.git
4. Run: git push -u origin main
```

### 9. Confirmation

After setup completes, provide a summary:

```
✓ Project initialized: {project-name}
✓ Type: {project-type}
✓ Claude manager configured
✓ Notes.md created for portfolio tracking
✓ Git repository created
✓ Pushed to GitHub: https://github.com/{username}/{project-name}

Next steps:
1. cd "{project-name}"
2. Fill in Notes.md with your project context
3. Open in Cursor/Claude Code
4. {type-specific-next-step}

Your project is ready to build!
```

**Type-Specific Next Steps:**
- **Product**: "Start by refining SPEC.md with your requirements"
- **Personal Tool**: "Define usage patterns in USAGE.md"
- **Experiment**: "Set learning goals in LEARNING.md"
- **Design**: "Gather inspiration in INSPIRATION.md"

## Implementation Notes

- Use relative paths from current working directory (portfolio root)
- Quote all paths in bash commands
- Create all files in a single session
- Ensure GitHub integration works or provide fallback
- Keep templates minimal but useful
- Focus on consistency across projects
