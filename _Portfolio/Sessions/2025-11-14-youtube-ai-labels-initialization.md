---
date: 2025-11-14
project: portfolio-manager
type: session
claude-generated: true
tags: [session, planning, project-init]
---

# Session: youtube-ai-labels Project Initialization

**Date:** [[14 Nov 2025]]
**Focus:** New project initialization and research

## What Happened

User wanted a Firefox extension to make YouTube's "Altered or synthetic content" labels more prominent. These labels exist but are buried in video descriptions - user wants to see them on thumbnails **before** clicking.

### Research Phase
- Searched for existing Firefox extensions - found only AI voice detectors (do their own analysis, not what we need)
- Searched userscript repositories (Greasyfork, OpenUserJS) - nothing targets YouTube's native labels
- Discovered YouTube API has `containsSyntheticMedia` metadata (added Oct 2024)
- Key unknown: Is this metadata available in page data (ytInitialData) or only via API calls?

### Project Initialization
Used `/init-project` to create youtube-ai-labels:
- Type: Personal Tool (userscript)
- Created basic structure, git repo, GitHub integration
- Fixed: Moved project notes file into project directory (was at portfolio root initially)

### Specification Document
User pointed out the init skill didn't think through what a userscript project needs - created comprehensive SPEC.md with:
- Full problem statement and research findings
- Three possible technical approaches (ytInitialData scanning, API calls, or DOM scanning)
- Implementation phases starting with investigation
- Open questions that need answering
- Success criteria and UX goals

Updated CLAUDE.md to point project Claude to SPEC.md for context.

## Key Decisions

1. **Start with userscript, not full extension** - faster to prototype and test
2. **Investigation-first approach** - need to inspect YouTube's DOM structure before choosing implementation path
3. **Project Claude handles implementation** - portfolio manager initialized structure, project Claude does the work

## Repository

https://github.com/bawakul/youtube-ai-labels

## Next Steps

Project Claude will:
1. Create test script to inspect YouTube's ytInitialData structure
2. Determine if containsSyntheticMedia is available at thumbnail level
3. Choose implementation approach based on findings
4. Build the userscript

## Insight

The init-project skill creates generic structure but doesn't have domain knowledge about specific project types (userscripts vs CLI tools vs web apps). SPEC.md compensates by front-loading all the research and context so project Claude knows exactly what's needed.
