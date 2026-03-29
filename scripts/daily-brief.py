#!/usr/bin/env python3
"""
Daily Brief - Global Social Media & GitHub Trends
Scrapes GitHub trending, outputs structured JSON for agent to format.
Social media searches (Twitter/Reddit/YouTube/HN) are done by agent via web_search.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

def fetch_github_trending() -> list:
    """Scrape GitHub trending repos (daily)"""
    try:
        url = "https://github.com/trending?since=daily"
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        repos = []
        seen = set()
        articles = html.split("<article")

        for article in articles[1:]:
            h2_match = re.search(r"<h2[^>]*>(.*?)</h2>", article, re.DOTALL)
            if not h2_match:
                continue
            raw = re.sub(r"<[^>]+>", "", h2_match.group(1))
            raw = "".join(raw.split())
            if "/" not in raw or raw in seen:
                continue
            seen.add(raw)
            if len(repos) >= 15:
                break

            info = {"repo": raw, "url": f"https://github.com/{raw}"}

            desc_match = re.search(r'<p[^>]*color-fg-muted[^>]*>(.*?)</p>', article, re.DOTALL)
            if desc_match:
                desc = re.sub(r"<[^>]+>", "", desc_match.group(1)).strip()
                if desc:
                    info["description"] = desc[:150]

            stars_match = re.search(r"([\d,]+)\s+stars?\s*today", article)
            if stars_match:
                info["stars_today"] = stars_match.group(1)

            lang_match = re.search(r'itemprop="programmingLanguage">([^<]+)<', article)
            if lang_match:
                info["language"] = lang_match.group(1)

            repos.append(info)

        return repos
    except Exception as e:
        return [{"error": str(e)}]


def main():
    now = datetime.now(CST)
    result = {
        "timestamp": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "day": now.strftime("%A"),
        "github": {
            "trending": fetch_github_trending(),
        },
        "social_search_queries": {
            "twitter": [
                "crypto Bitcoin today site:twitter.com OR site:x.com",
                "AI artificial intelligence today site:x.com",
                "tech news today site:x.com",
            ],
            "reddit": [
                "cryptoocurrency hot today site:reddit.com",
                "technology top today site:reddit.com",
                "worldnews today site:reddit.com",
                "artificial top today site:reddit.com",
            ],
            "youtube": [
                "AI news this week site:youtube.com",
                "crypto market today site:youtube.com",
            ],
            "hacker_news": [
                "trending site:news.ycombinator.com",
            ],
        },
        "_note": "social_search_queries are for agent to use web_search with freshness=day"
    }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    sys.stdout.buffer.write(out.encode("utf-8"))


if __name__ == "__main__":
    main()
