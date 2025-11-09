# Weekly Review Generator

Generate a concise weekly summary of Bawa's project work, optimized for NotebookLM audio overview.

## Purpose

This skill creates a 5-10 minute audio-ready review of the week's work across all portfolio projects. The review is designed for Bawa to listen to during his Tuesday morning commute, helping him reflect on what was accomplished and prepare for the week ahead.

## Process

### 1. Determine Date Range

**Default behavior** (no parameters):
- Generate review for the previous 7 days (Mon-Sun)
- Use current date to calculate range

**With parameter** `/review YYYY-MM-DD`:
- Generate review starting from the specified date
- Cover 7 days from that date

**With parameter** `/review last-month`:
- Generate review for the last 30 days

### 2. Collect Data

Gather information from multiple sources to build a complete picture of the week:

#### A. Session Notes
```bash
# Find all session notes in date range
# 1. Portfolio sessions
find _Portfolio/Sessions -name "*.md" -type f
# 2. CRITICAL: Check EACH project's Sessions/ folder
find */Sessions -name "*.md" -type f 2>/dev/null | grep -v "_Portfolio/Sessions" | grep -v "_Templates"
```

**IMPORTANT:** Project-specific sessions (e.g., `project-norma/Sessions/`) often contain the most substantive work. Always prioritize project sessions over portfolio infrastructure sessions when both exist.

**Extract from sessions**:
- Key decisions made
- Blockers encountered and how they were handled
- "Aha moments" and insights
- What was shipped/accomplished
- Important context for future work

**Skip from sessions**:
- Step-by-step implementation details
- Technical minutiae that won't matter in audio
- Full session transcripts (extract key excerpts only)

#### B. Git Activity
```bash
# Get commits from all projects in date range
for dir in */; do
  if [ -d "$dir/.git" ]; then
    cd "$dir"
    git log --since="YYYY-MM-DD" --until="YYYY-MM-DD" --oneline --no-merges
    cd ..
  fi
done
```

**Extract**:
- What was shipped per project
- Commit frequency (momentum indicator)
- Major feature completions

#### C. Project Frontmatter & Descriptions
```bash
# Read frontmatter from all project notes
for file in */*.md; do
  # Extract YAML frontmatter (status, project_type, last_worked, next_action)
done
# Also read project CLAUDE.md for "Project Vision" section
for file in */.claude/CLAUDE.md; do
  # Extract project description
done
```

**Extract**:
- **Project descriptions** - What is this project? (from notes or CLAUDE.md)
- Status changes (active → paused, etc.)
- Next actions planned
- Project types
- Last worked dates

#### D. GitHub Activity (Optional)
```bash
# Check for issues/PRs in date range if needed
gh issue list --search "created:>=YYYY-MM-DD"
gh pr list --search "created:>=YYYY-MM-DD"
```

### 3. Categorize Projects

Based on collected data, categorize each project:

- **Active**: Had commits or session notes in the date range
- **Paused**: No activity but status is "paused" with reason
- **New**: Initialized during this period
- **Dormant**: No activity and no explicit status

### 4. Generate Review Document

Create the review using this structure:

```markdown
---
NOTEBOOKLM AUDIO OVERVIEW INSTRUCTIONS:

This is a weekly review of Bawa's work for the week of [START DATE] to [END DATE].
Bawa will be listening to this during his Tuesday morning commute to reflect on his work.

CONTEXT: Bawa is vibe-coding - working fluidly across multiple creative projects with Claude
as a thinking partner. He's exploring ideas, making creative decisions, and having breakthroughs.
This is NOT traditional software development - it's creative exploration with code.

When creating the audio overview:
- Focus on the CREATIVE JOURNEY and INSIGHTS, not technical implementation details
- Emphasize WHY decisions were made, WHAT was learned, and AHA MOMENTS
- Each project summary should start with what the project IS and why it matters
- De-emphasize file names, commit messages, and technical specifics
- Highlight: breakthroughs, realizations, creative decisions, interesting problems solved
- Skip: "built X.py", "created Y folder", "updated Z config" unless it reveals insight
- This is about reflection and storytelling, not documentation
- Keep it 5-10 minutes total
- Help him see the through-line and creative momentum

TONE: Conversational and insight-focused. Like discussing creative work with a colleague,
not reading a changelog. The interesting part is the thinking, not the artifacts.
---

# Weekly Review: [START DATE] to [END DATE]

**Generated:** [TIMESTAMP]

## Executive Summary

[2-3 paragraphs: What was the vibe of this week? What themes emerged? What got momentum, what stalled? What's the big picture?]

**Active Projects:** [Number] projects with activity this week
**Key Accomplishments:** [Top 3-5 highlights]

---

## Projects Active This Week

### [Project Name] ([Project Type]) - [Status]

**What it is:** [1-2 sentence project description - what is this project trying to do? Read from project notes or CLAUDE.md]

**Where you're at:** [Current stage - early exploration? building prototype? polishing? paused waiting for X?]

**This week's journey:** [NARRATIVE focused on insights and creative decisions, not technical details. What did you discover? What clicked? What problems did you solve? What decisions did you make and why? Tell the story of the work, not a list of files created.]

**The breakthrough:** [If there was an "aha moment" or key realization, highlight it here]

**What's next:** [Based on momentum and session notes - where is this heading?]

[Repeat for each active project]

---

## Cross-Project Insights

**Themes:** [Common patterns across projects - e.g., "infrastructure week", "exploration phase", "decision-making week"]

**Learnings:** [Key "aha moments" or insights that apply beyond individual projects]

**Energy distribution:** [What kind of work got attention - building vs planning vs experimenting]

---

## Portfolio Status

**Active (building now):**
- [Project names with brief context]

**Paused (waiting for):**
- [Project names with reason - skill gap, decision needed, etc.]

**New (initialized this week):**
- [Project names with vision]

**Momentum indicators:**
- Commits: [Total] across [N] projects
- Sessions: [Total] tracked
- Issues/PRs: [If significant]

---

## The Week Ahead

[Based on next_action frontmatter, momentum indicators, and session notes - what might be worked on next? What's ready to move forward? What decisions need to be made?]

---

**Generated by:** Portfolio Manager
**Purpose:** Weekly reflection audio for Tuesday commute
**Next review:** [Date of next Monday]
```

### 5. Save the Review

```bash
# Save to Weekly Reviews folder
OUTPUT_FILE="_Portfolio/Weekly Reviews/YYYY-MM-DD-to-YYYY-MM-DD.md"
# Write content to file
# Confirm location to user
```

### 6. Output Confirmation

After generating the review, provide:
- File path where review was saved
- Word count (target: 750-1500 words)
- Estimated audio length (word count ÷ 150 ≈ minutes)
- Next steps: "Upload to NotebookLM for audio generation"

## Content Guidelines

### Keep It Concise
- **Target**: 750-1500 words total
- **Per project**: 150-250 words (more for highly active projects)
- **Executive summary**: 150-250 words
- **Focus on what matters**: Creative journey, insights, breakthroughs

### Narrative & Insight-Focused
- **This is vibe-coding** - creative exploration with Claude as thinking partner
- Tell the story of discovery and creative decisions
- Emphasize WHY over HOW
- Write for reflection, not documentation
- Use conversational language (like discussing with a colleague)
- Start each project with context (what IS this project?)

### What to Include
✅ **Project context** - What is this? Why does it matter? What stage are you at?
✅ **Creative breakthroughs** - "Aha moments", realizations, things that clicked
✅ **Interesting decisions** - Why you chose X over Y (not just that you did)
✅ **Problems solved** - The challenge and the insight, not the implementation
✅ **Learning moments** - What you discovered or figured out
✅ **Momentum indicators** - What's energized? What's stuck? Why?
✅ **Cross-project themes** - Patterns in your creative process

### What to De-emphasize or Skip
⚠️ File names, folder structures, commit messages (unless they reveal insight)
⚠️ "Built X.py, created Y.md, updated Z config" (boring!)
⚠️ Technical implementation details (how you wrote the code)
⚠️ Step-by-step chronology (unless it tells a story)
❌ Code snippets or command syntax
❌ Minor bug fixes, formatting changes, infrastructure tweaks
❌ Jargon without context

### Example Transformations

**❌ Technical/boring:**
"Built consolidate.py script with Claude API integration. Created test_segments.json with mode labels. Tested with three segments and generated consolidated_output.txt."

**✅ Insight/narrative:**
"Had the breakthrough that this is really a two-stage problem: Whisper just transcribes, but the magic happens when Claude weaves inline responses into the dictation. Built a quick prototype to test it - and it worked perfectly. The responses flow naturally, like having a conversation mid-thought."

**❌ Technical/boring:**
"Installed ffmpeg via Homebrew (89 dependencies). Tested base vs tiny Whisper model. Base model took 38 seconds on CPU, tiny took 25 seconds on GPU."

**✅ Insight/narrative:**
"Discovered that Whisper's 'base' model is actually way better at understanding context - it got 'limbic capitalism' right where the tiny model mangled it. The extra 13 seconds of processing is totally worth it for quality. Also confirmed ffmpeg can split audio at exact timestamps, which is perfect for the Intercom Button concept."

## Error Handling

- If no session notes found: Generate review from git commits only
- If no git activity: Generate from session notes only
- If neither: Output message "No activity in this date range"
- If date parsing fails: Show clear error with expected format

## Success Criteria

- Review generates in under 30 seconds
- Output is consistently 750-1500 words
- Captures key moments from the week
- Reads naturally when spoken aloud (test by reading to yourself)
- File saved to correct location with correct naming

## Future Enhancements

- Auto-open NotebookLM upload URL after generation
- Integration with NotebookLM API (if/when available)
- Smart excerpt extraction (ML-based key phrase detection)
- Trend analysis across multiple weeks
- Audio length estimation based on NotebookLM's actual output
