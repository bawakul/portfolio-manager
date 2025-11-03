# Portfolio Manager

A meta-project for managing multiple concurrent creative technology projects using Claude Code and Obsidian.

## Concept

This is **the manager's repo** - it tracks the development and configuration of portfolio management infrastructure itself. The actual projects being managed live in their own folders and repositories.

## How It Works

### Three-Layer System

1. **Claude Code Portfolio Manager** (`.claude/CLAUDE.md`)
   - AI assistant configured as a portfolio-level project manager
   - Operates at meta-level across all projects
   - Helps with prioritization, context switching, and pushing toward completion

2. **Obsidian Vault** (`.obsidian/`)
   - Visual interface for project tracking
   - Each project has a `Notes.md` with metadata and running journal
   - Dashboard views showing portfolio health

3. **Claude Code Skills** (`.claude/skills/`)
   - `/init-project` - Initialize new projects with structure
   - `/status` - Portfolio overview and current states
   - `/sync` - Automatic metadata maintenance via git analysis
   - `/review` - Weekly reflection and stalled project detection

## Project Metadata Schema

Each project folder contains `Notes.md`:

```markdown
---
status: active|paused|blocked|completed
type: product|tool|experiment|design
last_worked: YYYY-MM-DD
next_action: "What to do when resuming"
repo: "https://github.com/..."
---

# Project Name - Notes

[Running notes and session summaries]
```

## Project Types

- **Product** - User-facing apps/services
- **Personal Tool** - Scripts, automation, personal utilities
- **Experiment** - Prototypes, learning projects, quick tests
- **Design** - Creative coding, design systems, visual work

## Philosophy

**Orchestrator, not implementer.** The portfolio manager:
- Tracks status across projects (doesn't write code for them)
- Reduces context switching overhead
- Acts as forcing function toward completion
- Builds tools for itself (skills, dashboards)
- Maintains portfolio-level visibility

Individual projects have their own Claude Code sessions for implementation work.

## Development

This repo contains:
- Portfolio-level Claude Code configuration
- Custom skills for portfolio management
- Documentation of the system architecture

Issues track development of new portfolio management features and tools.
