# 📊 Daily Brief - 全球科技热点汇总

AI Agent 专用的每日信息汇总 Skill，自动抓取 GitHub 趋势 + 全球主流社交媒体热点，生成一份简洁的中文日报。

## 功能

覆盖 6 大内容板块：

| 板块 | 来源 | 内容 |
|------|------|------|
| 🤖 **AI 前沿** | Twitter/X、HN、Reddit | 新模型发布、LLM 动态、突破性进展 |
| 📰 **科技新闻** | TheVerge、TechCrunch、Reddit | 科技行业热点、趋势 |
| 📱 **Product Hunt** | Product Hunt | 今日新上线产品、热门项目 |
| 💰 **融资新闻** | Twitter/X、HN | 创投、融资公告、Series A/B/C |
| 🛡️ **安全事件** | Twitter/X、HN、Reddit | 数据泄露、CVE 漏洞、网络攻击 |
| 🔥 **GitHub Trending** | GitHub（自动抓取） | 每日热门项目、星标数、语言 |

## 支持的 Agent

- **Claude Code** — 原生支持，放入 `~/.claude/skills/` 即可
- **OpenClaw** — 通过 skill 系统自动加载
- 其他兼容 AgentSkill 规范的系统

## 安装 (Claude Code)

```bash
# 克隆
git clone https://github.com/QINXIN111/daily-brief.git

# 安装
mkdir -p ~/.claude/skills
cp -r daily-brief ~/.claude/skills/daily-brief
```

## 使用

在 Agent 对话中说：
- "今日汇总" / "daily brief" / "日报"

Agent 会自动：
1. 运行 `scripts/daily-brief.py` 抓取 GitHub 趋势
2. 按 5 个板块分别搜索社交媒体热点
3. 汇总成结构化的中文日报

### 手动运行

```bash
# 获取数据配置 (JSON)
python scripts/daily-brief.py
```

## 输出示例

```
📊 Daily Brief - 2026-03-29 (Sunday)

🤖 AI 前沿
  • [Claude 4] Anthropic 发布新一代模型...
  ...

📰 科技新闻
  • [Apple] WWDC 2026 公布新功能...
  ...

📱 Product Hunt 精选
  • [产品名] — 功能描述 [今日第1]
  ...

💰 融资动态
  • [公司] 融资$50M Series B — a16z 领投
  ...

🛡️ 安全事件
  • [CVE-2026-xxxx] XX 组件高危漏洞...
  ...

🔥 GitHub Trending
  • owner/repo [Python] ⭐1,234 — 项目描述
  ...

📰 今日速览（3 要点）
  • 关键趋势 1
  • 关键趋势 2
  • 关键趋势 3
```

## 自定义

编辑 `scripts/daily-brief.py` 中的 `SECTIONS` 字典，修改搜索关键词以匹配你的关注领域。

## License

MIT
