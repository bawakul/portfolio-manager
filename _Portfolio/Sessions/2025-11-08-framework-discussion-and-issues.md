---
date: 2025-11-08
project: portfolio-manager
type: session
claude-generated: true
tags: [session, planning, discussion]
---

# Framework Discussion and Issue Tracking

**Date:** [[08 Nov 2025]]
**Focus:** Strategic planning and issue management

## What Happened

### Haystack Framework Discussion
- User asked about Haystack (deepset.ai framework for LLM orchestration)
- Explained framework concept in practical terms
- Concluded it's overkill for current project scale
- User's direct API approach is appropriate for personal tools and experiments

### Framework-ifying Portfolio Manager
- User proposed extracting portfolio-manager into a reusable framework
- Discussed what this would entail:
  - Philosophy documentation (digital garden approach)
  - Configurable structure and metadata schemas
  - Skills library (init-project, status, sync, review)
  - Customization points (project types, frontmatter, directory structure)
- **Decision:** Build for personal use first, extract framework later
- Rationale: System still actively developing, needs 1-2 months of real usage to stabilize
- Framework thinking: Keep config separate, document decisions, make scripts parameterized

### Issues Created
1. **#11 - Long-term: Extract portfolio-manager into a reusable framework**
   - Captures vision for making this shareable
   - Lists prerequisites (finish core skills, stabilize through usage)
   - Framework-specific work (setup wizard, config system, multi-tool support)
   - Marked as post-stabilization goal

2. **#12 - Build /close-session skill with SessionEnd hook**
   - Automate session close-out (notes, commit, push)
   - Two phases: manual skill first, then SessionEnd hook
   - Discovered Claude Code has SessionEnd hook that triggers on "exit"
   - Priority: Low - current workflow sufficient

## Decisions Made

1. **Framework timing:** Don't extract too early - finish building personal version first
2. **Issue tracking:** Capture strategic ideas as issues for later consideration
3. **Session automation:** Good idea but not urgent, things working well enough

## Context for Next Time

- Two new strategic issues logged (#11, #12) for future consideration
- Focus remains on building core skills (/status, /sync, /review)
- Framework extraction is a longer-term product opportunity once system stabilizes

## Technical Notes

- Claude Code supports SessionEnd hook for exit automation
- Haystack comparison useful for understanding when frameworks add value vs complexity
- Current issue list: 12 open issues, mix of tactical (core skills) and strategic (framework, automation)
