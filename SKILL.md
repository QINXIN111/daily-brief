---
name: daily-brief
description: Generate a daily information briefing from global social media platforms. Use when user says "daily brief", "今日汇总", "日报", "热点汇总", or asks for a summary of what's happening on Twitter/X, Reddit, YouTube, etc. Also use during heartbeats when HEARTBEAT.md requests a daily check.
---

# Daily Brief - Global Social Media

Collect and summarize trending topics from major overseas social media platforms.

## Workflow

### Step 1: Collect Data

Run the script to get GitHub trends (the only source that needs scraping):

```bash
python scripts/daily-brief.py --github
```

### Step 2: Search Social Media

Use `web_search` tool to search each platform for hot topics. Search queries (in order):

1. **Twitter/X** — search `site:twitter.com OR site:x.com` for each topic:
   - `crypto Bitcoin today`
   - `AI artificial intelligence today`
   - `"Trump" OR "White House"` (politics)
   - `tech news today`
   
2. **Reddit** — search `site:reddit.com`:
   - `r/cryptocurrency hot today`
   - `r/technology top today`
   - `r/worldnews today`
   - `r/artificial top`

3. **YouTube** — search `site:youtube.com`:
   - `AI news this week`
   - `crypto market today`

4. **Hacker News** — search `site:news.ycombinator.com`:
   - trending topics

Use freshness="day" for all searches to get today's results.

### Step 3: Format Brief

Combine all sources into a structured report:

```
📊 Daily Brief - YYYY-MM-DD (Day)

━━━━━━━━━━━━━━━━━━━━━━━━━

🐦 Twitter/X Hot Topics
  • [topic] - brief summary
  ...

🔴 Reddit Highlights  
  r/subreddit - [title] - brief
  ...

🎬 YouTube Picks
  [channel] - [video title]
  ...

🔥 GitHub Trending
  • owner/repo [lang] ⭐N - description
  ...

📰 Summary (3 bullet points)
  • key trend 1
  • key trend 2
  • key trend 3
```

## Guidelines

- Keep total brief under 2000 characters
- Focus on what's actually trending, not random posts
- Prioritize: crypto/AI > tech > world news (match user interests)
- Skip low-engagement / clickbait content
- Include a 3-point summary at the end
- Use language: Chinese (简中)
