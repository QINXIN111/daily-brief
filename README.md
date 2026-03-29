# 📊 Daily Brief - 全球社交媒体日报

AI Agent 专用的每日信息汇总 Skill，自动抓取 GitHub 趋势 + 全球主流社交媒体热点，生成一份简洁的中文日报。

## 功能

| 信息源 | 内容 |
|--------|------|
| 🔥 GitHub Trending | 每日热门项目、星标数、语言、描述 |
| 🐦 Twitter/X | 加密货币、AI、科技热点 |
| 🔴 Reddit | r/cryptocurrency、r/technology、r/worldnews 等 |
| 🎬 YouTube | AI、加密市场热门视频 |
| 📰 Hacker News | 前沿科技讨论 |

## 支持的 Agent

- **Claude Code** — 原生支持，放入 `~/.claude/skills/` 即可
- **OpenClaw** — 通过 skill 系统自动加载
- 其他兼容 AgentSkill 规范的系统

## 安装 (Claude Code)

```bash
# 克隆
git clone https://github.com/QINXIN111/daily-brief.git

# 安装
cp -r daily-brief ~/.claude/skills/daily-brief
```

## 使用

在 Agent 对话中说：
- "今日汇总" / "daily brief" / "日报"

Agent 会自动：
1. 运行 `scripts/daily-brief.py` 抓取 GitHub 趋势
2. 用搜索工具拉取 Twitter / Reddit / YouTube / HN 热点
3. 汇总成结构化的中文日报

## 手动运行

```bash
# 获取 GitHub trending (JSON)
python scripts/daily-brief.py

# 仅输出文本摘要
python scripts/daily-brief.py --github
```

## 输出示例

```
📊 Daily Brief - 2026-03-29 (Sunday)

🐦 Twitter/X 热点
  • AI Agent 框架热潮持续...
  ...

🔥 GitHub Trending
  • obra/superpowers [Shell] ⭐2,292 — Agent 技能框架
  • hacksider/Deep-Live-Cam [Python] ⭐1,814 — 实时换脸

📰 速览总结
  • 关键趋势 1
  • 关键趋势 2
```

## 自定义

编辑 `SKILL.md` 中的 `social_search_queries` 部分，修改搜索关键词以匹配你的关注领域。

默认搜索：crypto、AI、tech news。

## License

MIT
