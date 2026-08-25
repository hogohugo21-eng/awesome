# AI Agent / Skills / 自动化项目中心

> 更新：2026-08-25
>
> 本仓库现已从“项目收藏清单”升级为 **可自动追踪上游版本的 Agent Skill Catalog**。

## 自动同步系统

核心文件：

- `upstreams.json` — 登记需要追踪的上游 GitHub 仓库。
- `scripts/sync_skills.py` — 自动读取上游最新 commit，并递归发现 `SKILL.md`。
- `catalog/skills.json` — 自动生成的机器可读 Skill 数据库。
- `catalog/SKILLS.md` — 自动生成的 Skill 浏览目录。
- `.github/workflows/sync-agent-skills.yml` — 每日自动检查上游变化。

自动同步不会盲目执行第三方 Skill，也不会默认复制第三方完整源码。它记录来源仓库、精确 commit、Skill 路径和 blob SHA；这样既能追踪更新，也能降低供应链和许可证风险。

## 当前追踪的 10 个上游

1. https://github.com/anthropics/skills — 官方/通用 Agent Skills
2. https://github.com/VoltAgent/awesome-agent-skills — Skill 聚合索引
3. https://github.com/browser-use/browser-use — Browser Agent + Browser Skills
4. https://github.com/affaan-m/ECC — Agent Harness + 大量 Skills
5. https://github.com/rohitg00/agentmemory — Persistent Agent Memory
6. https://github.com/the-open-agent/openagent — Computer/Browser/Coding Agent
7. https://github.com/mvanhorn/last30days-skill — Web Research Skill
8. https://github.com/K-Dense-AI/scientific-agent-skills — Scientific Skill Library
9. https://github.com/android/skills — Android Agent Skills
10. https://github.com/ai-boost/awesome-harness-engineering — Harness Engineering Index

## 已确认存在真实 Skill 的项目示例

### Browser Use

上游 `browser-use/browser-use` 当前存在多个 Skill 目录，包括：

- `skills/browser-use/`
- `skills/cloud/`
- `skills/open-source/`
- `skills/qa/`
- `skills/remote-browser/`
- `skills/x402/`

### ECC

已确认包含大量真实 `SKILL.md`，例如：

- `skills/ecc-guide/SKILL.md`
- `skills/skill-scout/SKILL.md`
- `skills/skill-comply/SKILL.md`
- `skills/react-testing/SKILL.md`
- `skills/react-patterns/SKILL.md`
- `skills/orch-fix-defect/SKILL.md`
- `skills/orch-refine-code/SKILL.md`
- `skills/orch-add-feature/SKILL.md`
- `skills/orch-change-feature/SKILL.md`
- `skills/blueprint/SKILL.md`
- `skills/orch-build-mvp/SKILL.md`

完整数量和路径由自动同步脚本生成，不在这里手工维护。

## 目标架构

```text
awesome/
├── AI-AGENT-SKILLS.md
├── upstreams.json
├── catalog/
│   ├── README.md
│   ├── SKILLS.md          # 自动生成
│   └── skills.json        # 自动生成
├── scripts/
│   └── sync_skills.py
└── .github/workflows/
    └── sync-agent-skills.yml
```

## 更新逻辑

```text
上游 GitHub 项目更新
        ↓
GitHub Actions 每日检查
        ↓
读取最新 commit SHA
        ↓
递归发现 SKILL.md
        ↓
记录 Skill path + blob SHA + source URL
        ↓
与当前 catalog 比较
        ↓
有变化 → 自动 commit
无变化 → 不产生提交
```

## 安全原则

第三方 Skill、MCP Server、Agent 插件和自动化脚本不能因为被发现就自动执行。安装/运行前至少检查：凭据读取、Shell/PowerShell 命令、外部网络请求、环境变量上传、启动项/计划任务、管理员权限以及混淆或远程下载执行代码。

后续可以在此基础上继续增加：摄影、Photoshop、Premiere Pro、After Effects、Figma、Blender、ComfyUI、视频生成、本地 AI、MCP、RAG、音乐制作、OSINT 等方向的 Skill 上游。
