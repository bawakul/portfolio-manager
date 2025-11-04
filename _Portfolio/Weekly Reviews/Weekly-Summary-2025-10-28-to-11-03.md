# Weekly Development Summary: October 28 - November 3, 2025

**Generated:** November 3, 2025
**Purpose:** Audio overview via NotebookLM

---

## Executive Summary

This was a pivotal week focused on building portfolio management infrastructure and making critical architectural decisions across multiple projects. The major highlight was establishing a "digital garden" approach to project management, building the `/init-project` skill, and making privacy-first architecture decisions for the expense-splitter project.

**Key Accomplishments:**
- Built complete portfolio manager infrastructure with `/init-project` skill
- Renamed and restructured portfolio from "vibecoding" to "Bawa's Lab"
- Made critical privacy-first backend decision for expense-splitter (paused for skill development)
- Identified iOS limitations for memo-transcriber (discovered Voice Memos API doesn't exist)
- Initialized 3 new projects: personal-site, claude-mode-manager, project-norma, super-productivity-setup

**Active Projects:** 10+ projects across 4 categories (Product, Tool, Experiment, Design)

---

## Part 1: Portfolio Manager Infrastructure

### The Digital Garden Metaphor

This week solidified the "digital garden" approach to managing multiple concurrent projects. Unlike traditional project management tools that assume linear progress, this system recognizes that creative work happens in bursts across many projects simultaneously.

**Key insight:** Traditional PM tools break when you:
- Jump between 10+ projects in a week
- Have wildly different project types (products, tools, experiments, designs)
- Work in bursts of momentum rather than steady sprints
- Start new things while old things are still growing

### The `/init-project` Skill

Built a comprehensive skill that initializes new projects with proper structure:

**What it creates:**
- Project directory with standard structure
- `.claude/CLAUDE.md` with role-specific instructions (Product, Tool, Experiment, or Design)
- Notes.md with frontmatter metadata for Obsidian tracking
- LEARNING.md for experiments
- README.md with project overview
- Proper `.gitignore`
- Local git repository
- GitHub repository with automatic push

**Why this matters:**
- Reduces friction to start new projects
- Ensures consistency across all projects
- Integrates with Obsidian for portfolio visualization
- Automates GitHub setup (no more manual repo creation)

### Infrastructure Evolution

**Major changes this week:**

1. **Folder Rename: "vibecoding" → "Bawa's Lab"**
   - Updated `/init-project` skill to use dynamic paths (no more hardcoded folder names)
   - Tested and validated skill works with new folder structure
   - Portfolio is now folder-name agnostic

2. **Project Rename: "digital-garden" → "knowledge-gardener"**
   - Resolved naming conflict (portfolio IS a digital garden, knowledge-gardener is a tool)
   - Clear separation: portfolio = garden of projects, knowledge-gardener = Obsidian tool

3. **Claude.md Rewrite**
   - Clarified portfolio manager role with "Digital Garden Caretaker" metaphor
   - Defined current vs future phase:
     - Current: Building infrastructure (skills, automation, tools)
     - Future: Using those tools for portfolio management
   - Set clear boundaries:
     - DO: Work on portfolio-manager (build skills, commit code)
     - DON'T: Work inside individual projects (they have their own Claude sessions)

### Session Tracking System

Implemented proper session tracking:
- SESSIONS.md in portfolio-manager root
- Detailed notes for each infrastructure improvement session
- Tracks decisions, changes, and rationale
- Foundation for weekly review automation

**Sessions logged:**
1. Folder rename preparation and path updates
2. Post-rename completion and skill validation
3. Claude.md rewrite and project rename
4. Review planning (this summary is the first output!)

---

## Part 2: Active Projects Overview

### expense-splitter (Product) - PAUSED

**Status:** Paused pending self-hosting skill development
**Type:** Product - Couples expense tracking app
**Repo:** https://github.com/bawakul/expense-splitter

#### The Vision

A privacy-first expense tracking app for couples that splits expenses from bank statement PDFs. Users upload their monthly statements, categorize transactions together, and settle balances.

**Key features:**
- PDF bank statement upload and parsing
- Swipe-based transaction categorization
- Custom split percentages (not just 50/50)
- Monthly settlement cycles
- Partner linking system

#### Session 1: Initial Planning (Oct 31)

**Major discovery:** Banks only provide PDFs, not CSVs - changed entire technical approach.

**Product pivot:** Realized this requires collaborative async workflow:
- Each person can only understand their own transactions
- Both users upload statements independently
- System syncs and calculates settlement
- This is fundamentally a multi-user product requiring backend

**Work completed:**
- Full product specification (SPEC.md)
- Complete technical architecture (React + Vite + Firebase)
- Data models for users, couples, transactions, settlements
- Created 9 GitHub issues (#3-#11) with detailed implementation plans

**Technical stack decided:**
- Frontend: React + TypeScript + Vite + Tailwind CSS
- Backend: Firebase (initial choice)
- PDF Parsing: PDF.js (client-side)
- Deployment: Vercel/Netlify

#### Session 2: Project Setup (Oct 31)

**Fully initialized React + Vite + TypeScript project:**

Dependencies installed:
- React 18.3.1
- Firebase SDK 12.5.0
- React Router 7.9.5
- Tailwind CSS 4.1.16 (v4!)
- pdfjs-dist 5.4.296
- ESLint + Prettier

**Project structure created:**
- Organized folder structure (components, pages, services, types, hooks, utils)
- Firebase configuration with environment variables
- Basic routing (HomePage, LoginPage)
- Code quality tools configured and passing

**Infrastructure decision emerged:**

During collaboration discussion, started questioning Firebase for sensitive financial data:
- Bank transaction data is highly sensitive
- Google has technical access to all data
- Subject to data requests, policy changes
- No control over data location

**Decision framework created:**
- Documented 4 backend options with pros/cons
- Created Decisions/ folder structure
- Decision 001: Backend Service Choice

#### Session 3: Backend Decision & Project Pause (Nov 1)

**Deep privacy analysis performed:**

Analyzed risks of uploading bank statement PDFs to Google servers:

🔴 **Critical concerns:**
1. Direct access to unencrypted financial data
2. Automated data scanning and profiling
3. Government data requests

🟡 **High concerns:**
4. Terms of service changes
5. Third-party data sharing
6. Account lockout risk

🟢 **Moderate concerns:**
7. Data retention after deletion
8. Cross-border transfers
9. Security breach risk
10. Vendor lock-in

**Comparison with Splitwise:**

Key insight: Splitwise is more acceptable because:
- Stores selective manual entries, not complete bank data
- No PDFs or account numbers
- Users choose what to share
- Dedicated business with legal accountability

**This project is MORE invasive:**
- Full bank statement PDFs
- Every transaction (not selective)
- Account numbers and balances
- Complete financial picture for both partners

#### The Decision

**Chosen:** PocketBase (self-hosted)
**Outcome:** Project paused until self-hosting skills developed

**Rationale:**
1. Privacy concerns are too significant for Google servers
2. Self-hosting is the right approach
3. Skill gap needs to be addressed first
4. Better to pause than compromise on privacy

**Skill gap identified:**
- Server deployment and configuration (Fly.io/Railway or Raspberry Pi)
- Database backup and recovery
- Security hardening and monitoring
- Basic DevOps practices

#### Learning Roadmap Created

Comprehensive 4-week learning plan:
- **Week 1:** PocketBase basics + local practice
- **Week 2:** Deployment fundamentals + static site
- **Week 3:** Deploy PocketBase to Fly.io
- **Week 4:** Security, backups, monitoring
- **Week 5+:** Resume expense-splitter development

**Alternative explored:** Local-first architecture (no backend)
- Export/import flow or QR code exchange
- Maximum privacy (data never leaves devices)
- Supports monthly reconciliation workflow
- Could ship immediately without infrastructure learning

**Status:** Issue #15 created to explore local-first options

#### Reflection

This project demonstrated:
- Thoughtful analysis of privacy implications
- Realistic assessment of current capabilities
- Mature decision to prioritize privacy over convenience
- Recognition that some projects require prerequisite skills

**The right call:** Better to pause and build skills than ship something that compromises user privacy for financial data.

---

### memo-transcriber (Personal Tool) - CLOSED

**Status:** Closed - iOS limitation discovered
**Type:** Personal Tool
**Repo:** Not applicable

#### The Vision

Automate extraction of Voice Memo transcripts from iOS 18's native transcription feature and append them to Obsidian daily notes.

**Workflow imagined:**
1. Record voice memo in iOS Voice Memos app
2. iOS 18 auto-transcribes (on-device, private)
3. Apple Shortcut extracts transcript
4. Automatically appends to today's Obsidian daily note

#### What Was Built

**Comprehensive planning documents:**
1. APPLE_SHORTCUTS_PLANNING.md - Three implementation approaches analyzed
2. IMPLEMENTATION_GUIDE.md - Step-by-step technical guide
3. WORKFLOW_DIAGRAM.md - Visual workflow documentation
4. FEASIBILITY_REPORT.md - Critical findings

**Approaches evaluated:**
1. Direct Shortcut (manual trigger)
2. Automated with Personal Automation
3. Hybrid with web service

#### The Critical Discovery

⚠️ **LIMITATION IDENTIFIED:** The original plan is not feasible.

**What works:**
- iOS 18+ includes automatic transcription in Voice Memos app
- Powered by Apple Intelligence (on-device)
- Transcripts visible within Voice Memos app
- Users can manually copy transcripts

**What doesn't work:**
- ❌ No Shortcuts action to access Voice Memo transcripts programmatically
- ❌ Get Voice Memo Transcript - does not exist
- ❌ No API to access transcript text
- ❌ Voice Memos stored in sandboxed location

**Quote from Shortcuts expert Matthew Cassinelli:**
> "I also wish we had access to retrieve the Voice Memos with Shortcuts or via iCloud Drive."

#### Alternative Approaches Evaluated

1. **Manual Copy-Paste** - Defeats automation goal
2. **Third-Party Transcription APIs** - Privacy concern, audio leaves device
3. **Notes App Instead** - iOS 18 Notes has better Shortcuts integration
4. **Custom iOS App** - Requires Swift development skills
5. **Wait for Apple** - No timeline, can't rely on it

#### The Decision

**Project closed** - iOS limitation is a blocker.

**Recommendation:** Test Notes app approach first (if transcription in Notes is accessible via Shortcuts).

**Fallback:** Use third-party APIs (OpenAI Whisper, AssemblyAI) if on-device privacy isn't critical.

**Long-term:** Build custom iOS app with SpeechAnalyzer API (significant investment).

#### Reflection

This project demonstrated:
- Thorough feasibility analysis before building
- Recognition when technical limitations are blockers
- Comprehensive documentation of findings
- Alternative paths identified for future exploration

**The right call:** Close the project when fundamental assumptions are invalidated by platform limitations.

---

### knowledge-gardener (Personal Tool) - Renamed

**Status:** Renamed from "digital-garden" (formerly active)
**Type:** Personal Tool
**Repo:** https://github.com/bawakul/knowledge-gardener

#### What This Is

A tool for managing and maintaining an Obsidian-based digital garden of knowledge notes. Includes automation scripts for:
- Frontmatter standardization
- Content processing (transcripts, citations)
- Batch operations
- Link analysis

**Not to be confused with:** The portfolio itself (which is ALSO a digital garden, but of projects)

#### Recent Activity (6 days ago)

Added YouTube transcript support to transcript processor.

#### The Rename

**Changed:** digital-garden → knowledge-gardener

**Why:** Resolved naming conflict
- Portfolio IS a digital garden (of projects)
- This tool is FOR a digital garden (of knowledge notes)
- "knowledge-gardener" clarifies it's a tool, not the garden itself

**Files updated:**
- Folder renamed
- Notes.md updated with new title and metadata
- GitHub repo renamed

---

### personal-site (Design Project) - NEW

**Status:** Initialized (5 hours ago)
**Type:** Design
**Repo:** https://github.com/bawakul/personal-site

#### The Vision

A unified personal website combining:
- Portfolio work (UX/design projects)
- Digital garden (content from Obsidian vault)
- Data visualizations and diagrams
- Algorithmic art experiments

**Will replace:**
- Current Squarespace-hosted UX portfolio
- Current Obsidian Publish digital garden

#### Tech Stack

- Framework: Next.js (for maximum creative freedom)
- Deployment: Vercel
- Content: Obsidian vault integration (MDX)
- Interactivity: React components, D3.js, p5.js

#### Philosophy

**This is about the journey and craft:**
- Build unified architecture first, content organization evolves
- Support both portfolio showcases and digital garden notes
- Enable creative freedom for data viz and algorithmic art
- Build slowly and thoughtfully - prioritize craft over speed
- Make it vibe-coding friendly
- Experiment, iterate, refine

**Status:** Foundation initialized, ready for development when momentum strikes.

---

### claude-mode-manager (Experiment) - NEW

**Status:** Initialized (3 days ago)
**Type:** Experiment
**Repo:** https://github.com/bawakul/claude-mode-manager

#### The Problem

Context-switching between portfolio management and project development creates friction:
- Need separate Claude Code sessions (one for portfolio manager, one per project)
- Requires closing one IDE window and opening another
- Mental overhead and lost flow state

#### The Experiment

**Question:** What's the simplest way to reduce this context-switching overhead?

**Solutions to explore:**
1. Shell alias + tmux/terminal split (5 min)
2. Simple CLI wrapper script (30 min)
3. VS Code workspace with multiple terminals (10 min)
4. Extend Claude Code CLI with --context-dir or --mode flag (few hours)
5. Fork VS Code for deep IDE integration (substantial effort)

**Recommended first:** VS Code workspace approach (quickest win)

**Status:** Experiment defined, ready for iteration when needed.

---

### project-norma (Experiment) - NEW

**Status:** Initialized (3 days ago)
**Type:** Experiment
**Repo:** https://github.com/bawakul/project-norma

#### The Problem

Super Whisper (voice recording app) forces users to choose between dictation mode (verbatim transcription) or assistant mode (AI processing) BEFORE recording starts. Can't switch mid-session.

#### The Vision

**"The Intercom Button"** - inspired by Michael Scott's intercom in The Office

**How it works:**
1. Start in dictation mode
2. Press button to toggle to assistant mode (ask questions)
3. Press button to toggle back to dictation
4. Record timestamps of all mode switches
5. Post-process: split audio, handle each segment per its mode
6. **Key feature:** Assistant has context of previous dictation

#### Technical Approach

**Available resources:**
- AudioWhisper (MIT license) - menu bar app with Whisper
- OpenSuperWhisper - real-time transcription
- SwiftWhisper/WhisperKit - Swift Whisper libraries
- AVFoundation - native macOS audio (~100-200 lines)

**Estimated effort:** 2-3 days for working prototype

**Questions to explore:**
- Can we reliably split audio at arbitrary timestamps?
- How do we handle mode transitions smoothly in UX?
- Should we fork AudioWhisper or build from scratch?
- What's the latency on real-time transcription?

**Status:** Concept defined, ready to prototype when momentum strikes.

---

### super-productivity-setup (Experiment) - NEW

**Status:** Initialized (4 hours ago)
**Type:** Experiment
**Repo:** https://github.com/bawakul/super-productivity-setup

#### The Experiment

Testing Super Productivity app as a time tracking and task management tool for the portfolio.

**Questions to explore:**
- How does it handle GitHub integration for time tracking per repo?
- Can it integrate with existing portfolio manager?
- What's the workflow for tracking time on multiple projects?
- Does the Pomodoro timer + task description UI work well?
- Can it be used as a floating persistent UI element?
- How does it export time tracking data?
- Can it help reduce context switching?

**Potential future:** Custom tool combining Super Productivity features with portfolio management.

**Status:** Tracking configuration and usage patterns, documenting findings.

---

## Part 3: Key Themes and Insights

### 1. Privacy-First Design Matters

**Lesson from expense-splitter:**
- Financial data deserves higher privacy standards
- Big tech servers are not acceptable for bank statements
- Self-hosting is worth the infrastructure investment
- Sometimes the right decision is to pause and learn

**Broader implication:** Future projects with sensitive data should evaluate privacy trade-offs early in planning.

### 2. Platform Limitations Shape Possibilities

**Lesson from memo-transcriber:**
- iOS Shortcuts limitations are real blockers
- Always verify platform capabilities before detailed planning
- Apple's sandboxing has privacy benefits but limits automation
- Feasibility analysis saves wasted implementation time

**Broader implication:** Test platform assumptions early, especially for iOS/macOS automation projects.

### 3. Infrastructure Investment Pays Off

**Lesson from portfolio-manager:**
- `/init-project` skill dramatically reduces project initialization friction
- Standardization enables portfolio-wide tracking
- Automation tools are worth building even if they take time upfront
- Dynamic paths prevent technical debt (learned from folder rename)

**Broader implication:** Time spent on infrastructure is time invested in all future projects.

### 4. The Digital Garden Metaphor Works

**Why it resonates:**
- Projects grow at different rates (not linear progress)
- Some need attention now, others can rest
- Starting new things doesn't mean abandoning old things
- Momentum and inspiration drive work, not schedules

**Broader implication:** Portfolio management should support fluid work patterns, not force rigid structure.

### 5. Boundaries Enable Focus

**Lesson from claude-mode-manager:**
- Context switching has real costs
- Portfolio manager stays at meta-level
- Individual projects get their own Claude sessions
- Clear boundaries prevent scope creep

**Broader implication:** Separation of concerns applies to AI assistants too.

---

## Part 4: Technical Decisions & Rationale

### Backend Privacy Framework

**Created a decision framework for backend choices:**

For sensitive data (financial, health, personal):
1. **Default:** Self-hosted (PocketBase, Supabase self-hosted)
2. **Why:** Full data control, no big tech access
3. **Trade-off:** Maintenance burden (~30 min/month)
4. **Alternative:** Local-first architecture (no backend at all)

For non-sensitive data (public content, low-risk):
1. **Default:** Managed services (Firebase, Vercel, Netlify)
2. **Why:** Zero maintenance, better reliability
3. **Trade-off:** Less control, vendor lock-in

**Principle:** Match backend choice to data sensitivity.

### Project Type Taxonomy

**4 project types, each with different goals:**

1. **Product** - User-facing apps/services
   - Spec-driven development
   - Full documentation (SPEC.md, user stories, issues)
   - Prioritize user experience

2. **Personal Tool** - Scripts, automation, productivity
   - Pragmatic solutions over perfect code
   - Document usage in USAGE.md
   - Make it work first, optimize later

3. **Experiment** - Prototypes, learning, exploration
   - Document learnings in LEARNING.md
   - Iterate quickly, break things
   - Capture insights and "aha moments"

4. **Design** - Creative coding, visual projects
   - Maintain visual references (INSPIRATION.md)
   - Balance creativity with technical constraints
   - Document design decisions

**Why this matters:** Different project types need different processes and expectations.

---

## Part 5: Portfolio Health Check

### Active Projects by Status

**Active (building now):**
- portfolio-manager (infrastructure)

**Paused (intentional):**
- expense-splitter (skill gap - self-hosting)

**Closed:**
- memo-transcriber (platform limitation)

**Initialized (ready when momentum strikes):**
- personal-site (design)
- claude-mode-manager (experiment)
- project-norma (experiment)
- super-productivity-setup (experiment)

### Projects with Recent Activity (Last 7 Days)

1. **portfolio-manager** - Most active (today)
2. **expense-splitter** - Paused 2 days ago
3. **memo-transcriber** - Closed 3 days ago
4. **personal-site** - Initialized 5 hours ago
5. **super-productivity-setup** - Initialized 4 hours ago
6. **claude-mode-manager** - Initialized 3 days ago
7. **project-norma** - Initialized 3 days ago
8. **knowledge-gardener** - Renamed today, last commit 6 days ago

### Momentum Patterns

**High momentum:** Portfolio infrastructure week
- Built `/init-project` skill
- Renamed and restructured portfolio
- Established session tracking
- Clarified portfolio manager role

**Decision-making week:** Made important architectural decisions
- Privacy-first backend choice (expense-splitter)
- Platform limitation acceptance (memo-transcriber)
- Project taxonomy finalized

**Exploration phase:** Several experiments initialized
- Testing new approaches (claude-mode-manager, super-productivity-setup)
- Exploring creative projects (personal-site, project-norma)

---

## Part 6: What's Next

### Immediate Priorities

1. **Build `/status` skill** - Portfolio-wide overview dashboard
2. **Build `/sync` skill** - Auto-update project metadata
3. **Build `/review` skill** - Automated weekly summaries (like this!)

### Project-Specific Next Actions

**expense-splitter:**
- Begin Week 1 of self-hosting learning roadmap
- Decide: Full PocketBase path vs local-first alternative (Issue #15)

**personal-site:**
- Define initial architecture
- Set up Next.js + MDX integration
- Design visual direction

**claude-mode-manager:**
- Test VS Code workspace approach
- Document findings in LEARNING.md

**project-norma:**
- Prototype audio splitting at arbitrary timestamps
- Test mode transition UX

**super-productivity-setup:**
- Configure GitHub integration
- Test workflow for multi-project tracking

### Portfolio Manager Evolution

**Skills roadmap:**
- `/status` - See portfolio health at a glance
- `/sync` - Keep metadata fresh automatically
- `/review` - Weekly summaries without manual effort

**Infrastructure improvements:**
- Obsidian dataview queries for portfolio dashboard
- Automated Notes.md updates from git activity
- Cross-project analytics and insights

### Learning Goals

**Self-hosting skills (from expense-splitter):**
- Week 1: PocketBase basics + local practice
- Week 2: Deployment fundamentals
- Week 3: Deploy to Fly.io
- Week 4: Security and backups

**iOS development (from project-norma):**
- macOS Swift basics
- AVFoundation audio recording
- WhisperKit integration

---

## Part 7: Reflections and Learnings

### What Worked Well

**Infrastructure focus:** Taking time to build proper foundations pays dividends.
- `/init-project` skill eliminates project setup friction
- Session tracking provides clear history
- Standardized project structure enables automation

**Thoughtful decision-making:** Prioritizing privacy and feasibility over speed.
- Pausing expense-splitter was the right call
- Closing memo-transcriber saved wasted effort
- Decision documentation helps future projects

**Digital garden metaphor:** Accepting that projects grow at different rates.
- Not everything needs to be "in progress"
- Some projects wait for the right momentum
- Portfolio manager enables this flexibility

### Challenges Encountered

**Platform limitations:** iOS Shortcuts API gaps blocked memo-transcriber automation.
- **Lesson:** Verify platform capabilities early
- **Future:** Test platform assumptions before detailed planning

**Skill gaps:** Self-hosting knowledge needed for privacy-first architecture.
- **Lesson:** Identify prerequisite skills upfront
- **Future:** Create learning roadmaps for skill gaps

**Context switching:** Managing portfolio + individual projects creates overhead.
- **Lesson:** Clear boundaries help (portfolio manager vs project Claude)
- **Future:** Experiment with tools to reduce friction (claude-mode-manager)

### Patterns Emerging

**Front-load decisions:**
- Infrastructure choices (backend, hosting, tech stack)
- Privacy implications for sensitive data
- Platform capability verification

**Document everything:**
- Session notes capture reasoning and context
- Decision logs prevent revisiting settled questions
- Learning journals track experiment findings

**Match process to project type:**
- Products need specs and issues
- Tools need usage docs
- Experiments need learning logs
- Design projects need inspiration refs

---

## Conclusion

This week established the **foundation for sustainable portfolio management**. The `/init-project` skill, session tracking, and digital garden philosophy create a system that bends rather than breaks when jumping between projects.

**Major wins:**
- Portfolio infrastructure operational
- Privacy-first principles established
- Platform limitations identified early
- Multiple experiments ready for momentum

**Next phase:** Build remaining skills (`/status`, `/sync`, `/review`) to complete the portfolio manager toolkit.

**Philosophy reinforced:** Better to build slowly and thoughtfully than rush to ship the wrong thing. Privacy, feasibility, and craft matter more than speed.

---

## Appendix: Project Directory

### All Projects in Portfolio

1. **portfolio-manager** - This meta-project
2. **expense-splitter** - Couples expense tracker (paused)
3. **memo-transcriber** - Voice memo automation (closed)
4. **knowledge-gardener** - Obsidian automation tool
5. **personal-site** - Unified personal website (new)
6. **claude-mode-manager** - Context switching experiment (new)
7. **project-norma** - Multi-mode voice recorder (new)
8. **super-productivity-setup** - Time tracking experiment (new)
9. **ai-librarian** - (dormant)
10. **personal-library** - (dormant)
11. **tiny-essay-editor** - (dormant)
12. **Bureaucracy-Tool** - (dormant)
13. **Coaching-example** - (dormant)
14. **Visual coding** - (dormant)
15. **flask-rest-example** - (dormant)
16. **screenshot-transcript-poc** - (dormant)

**Active attention:** 8 projects
**Total in portfolio:** 16 projects

---

## Credits

**Generated by:** Claude (Portfolio Manager)
**Session notes authored by:** Claude (across multiple project sessions)
**Human direction:** Bharadwaj
**Purpose:** Weekly review for NotebookLM audio overview

---

*This document represents one week in the digital garden of projects - tending to what needs attention, letting others rest, and building the tools to make it all sustainable.*
