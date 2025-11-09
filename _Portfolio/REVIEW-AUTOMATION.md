# Weekly Review Automation

## Overview

The `/review` skill automatically generates weekly summaries of portfolio work every Monday evening at 7 PM. Reviews are saved to `_Portfolio/Weekly Reviews/` and optimized for NotebookLM audio playback.

## Usage

### Manual Trigger (RECOMMENDED)
Run anytime within Claude Code:
```bash
/review              # Last 7 days (Mon-Sun)
/review 2025-11-03   # Specific week from date
/review last-month   # Last 30 days
```

**For now, use the manual trigger.** The skill works perfectly when run manually in Claude Code sessions.

### Automated Schedule (EXPERIMENTAL - NOT YET TESTED)
The automation is configured but not yet confirmed working:
- **When:** Every Monday at 7:00 PM
- **What:** Should generate review for previous Mon-Sun week
- **Output:** `_Portfolio/Weekly Reviews/YYYY-MM-DD-to-YYYY-MM-DD.md`
- **Status:** Needs testing - `claude -p` command behavior in non-interactive mode is unclear

**To use automation:** Test the setup (see Testing section) and verify it works before relying on it.

## Setup (Already Done)

The launchd service is configured at:
```
~/Library/LaunchAgents/com.bawa.portfolio-review.plist
```

To load the service:
```bash
launchctl load ~/Library/LaunchAgents/com.bawa.portfolio-review.plist
```

To unload (disable automation):
```bash
launchctl unload ~/Library/LaunchAgents/com.bawa.portfolio-review.plist
```

## Testing the Automation

### Test the CLI Command
Run this manually to verify it works:
```bash
cd "/Users/bharadwajkulkarni/Documents /Bawa's Lab"
claude -p "/review"
```

This should generate a review file in `_Portfolio/Weekly Reviews/`.

### Test the Launchd Service
To test without waiting for Monday 10pm:

1. Run immediately:
```bash
launchctl start com.bawa.portfolio-review
```

2. Check the logs:
```bash
tail -f /tmp/portfolio-review.log
tail -f /tmp/portfolio-review-stdout.log
tail -f /tmp/portfolio-review-stderr.log
```

3. Verify the review file was created:
```bash
ls -lt "_Portfolio/Weekly Reviews/" | head -5
```

### Check Service Status
```bash
# List all loaded launch agents
launchctl list | grep portfolio-review

# Get detailed info
launchctl print gui/$(id -u)/com.bawa.portfolio-review
```

## Troubleshooting

### Review Not Generated
1. Check logs in `/tmp/portfolio-review*.log`
2. Verify claude CLI works: `which claude`
3. Test manual command (see Testing section)
4. Ensure laptop is awake/on at 10 PM Mondays

### Permission Issues
If launchd can't run the command:
```bash
# Reload the service
launchctl unload ~/Library/LaunchAgents/com.bawa.portfolio-review.plist
launchctl load ~/Library/LaunchAgents/com.bawa.portfolio-review.plist
```

### macOS Sleep/Power
- Laptop must be awake at scheduled time (7 PM Monday)
- Scheduled for 7 PM so laptop is likely to be on
- If you're typically not using laptop at this time, adjust schedule in the plist

## Output Format

Generated reviews are optimized for NotebookLM:
- **Length:** 750-1500 words (~5-10 min audio)
- **Format:** Markdown with NotebookLM instructions header
- **Content:** Key decisions, insights, what was shipped
- **Tone:** Conversational, for personal reflection

## Upload to NotebookLM

After the review is generated:
1. Open `_Portfolio/Weekly Reviews/` folder
2. Find the latest review (YYYY-MM-DD-to-YYYY-MM-DD.md)
3. Upload to NotebookLM: https://notebooklm.google.com
4. Generate Audio Overview
5. Listen on Tuesday morning commute!

## Customization

### Change Schedule
Edit `~/Library/LaunchAgents/com.bawa.portfolio-review.plist`:

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Weekday</key>
    <integer>1</integer>  <!-- 1=Monday, 2=Tuesday, etc. -->
    <key>Hour</key>
    <integer>22</integer>  <!-- 24-hour format -->
    <key>Minute</key>
    <integer>0</integer>
</dict>
```

Then reload:
```bash
launchctl unload ~/Library/LaunchAgents/com.bawa.portfolio-review.plist
launchctl load ~/Library/LaunchAgents/com.bawa.portfolio-review.plist
```

### Change Review Length/Format
Edit `.claude/skills/review/skill.md` and adjust:
- Target word count (default: 750-1500)
- Section structure
- NotebookLM instructions
- Content filtering rules
