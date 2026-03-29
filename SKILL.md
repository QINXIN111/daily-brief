---
name: daily-brief
description: Generate a daily information briefing from global social media and tech platforms. Use when user says "daily brief", "今日汇总", "日报", "热点汇总", or asks for a summary of what's happening on Twitter/X, Reddit, YouTube, Hacker News, Product Hunt, AI news, etc. Also use during heartbeats when HEARTBEAT.md requests a daily check.
---

# Daily Brief - 全球科技热点汇总

收集全球主流社交媒体和科技平台的热门内容，生成简洁的中文日报。

## Workflow

### Step 1: 运行数据采集脚本

```bash
python scripts/daily-brief.py
```

脚本输出 JSON，包含：
- GitHub Trending 项目列表
- 各板块的搜索关键词配置

### Step 2: 按板块搜索（用 web_search 工具）

按以下顺序搜索，每个搜索加 `freshness="day"`：

**1. 🤖 AI 前沿**
- `AI new model release announcement site:x.com`
- `LLM GPT Claude Gemini site:news.ycombinator.com`
- `artificial intelligence breakthrough site:reddit.com`

**2. 🔥 科技新闻**
- `tech news today site:theverge.com OR site:techcrunch.com`
- `科技新闻 today site:reddit.com/r/technology`

**3. 📱 Product Hunt**
- `site:producthunt.com launched today`
- `site:producthunt.com top product today`

**4. 💰 融资新闻**
- `startup funding raised Series site:x.com`
- `venture capital investment announcement site:news.ycombinator.com`

**5. 🛡️ 安全事件**
- `data breach security incident today site:x.com`
- `vulnerability CVE critical site:news.ycombinator.com`
- `hacker attack cybersecurity site:reddit.com/r/netsec`

**6. 🔥 GitHub Trending**（脚本已抓取，直接用）

### Step 3: 汇总格式

```
📊 Daily Brief - YYYY-MM-DD (星期X)

━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 AI 前沿
  • [标题] — 一句话摘要
  ...

📰 科技新闻
  • [标题] — 一句话摘要
  ...

📱 Product Hunt 精选
  • [产品名] — 功能描述 [今日第X]
  ...

💰 融资动态
  • [公司] 融资$XXM [轮次] — 投资方
  ...

🛡️ 安全事件
  • [事件] — 影响范围
  ...

🔥 GitHub Trending
  • owner/repo [语言] ⭐今日+数 — 描述
  ...

━━━━━━━━━━━━━━━━━━━━━━━━━

📰 今日速览（3要点）
  • 关键趋势 1
  • 关键趋势 2
  • 关键趋势 3
```

## Guidelines

- 总量控制在 2500 字符以内
- 每板块 3-5 条精选，跳过低质量/标题党
- 优先级：AI > 科技 > 融资 > 安全 > Product Hunt
- 描述用中文，项目/产品名保留英文
- 结尾 3 条速览总结当天最重要的趋势
