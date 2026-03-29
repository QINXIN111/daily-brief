#!/usr/bin/env python3
"""
Daily Brief - 全球科技热点数据采集
GitHub trending 抓取 + 社交媒体搜索配置
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

# ─────────────────────────────────────
# 各板块搜索配置
# ─────────────────────────────────────

SECTIONS = {
    "ai": {
        "label": "AI 前沿",
        "queries": [
            "AI new model release announcement site:x.com",
            "LLM GPT Claude Gemini site:news.ycombinator.com",
            "artificial intelligence breakthrough site:reddit.com",
        ],
    },
    "tech": {
        "label": "科技新闻",
        "queries": [
            "tech news today site:theverge.com OR site:techcrunch.com",
            "technology trends today site:reddit.com/r/technology",
        ],
    },
    "product_hunt": {
        "label": "Product Hunt",
        "queries": [
            "site:producthunt.com launched today",
            "site:producthunt.com top product today",
        ],
    },
    "funding": {
        "label": "融资新闻",
        "queries": [
            "startup funding raised Series site:x.com",
            "venture capital investment announcement site:news.ycombinator.com",
        ],
    },
    "security": {
        "label": "安全事件",
        "queries": [
            "data breach security incident today site:x.com",
            "vulnerability CVE critical site:news.ycombinator.com",
            "cybersecurity attack site:reddit.com/r/netsec",
        ],
    },
}


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
        "github": {"trending": fetch_github_trending()},
        "sections": {},
    }

    for key, section in SECTIONS.items():
        result["sections"][key] = {
            "label": section["label"],
            "queries": section["queries"],
        }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    sys.stdout.buffer.write(out.encode("utf-8"))


if __name__ == "__main__":
    main()
