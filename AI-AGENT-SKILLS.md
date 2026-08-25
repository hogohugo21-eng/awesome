# AI Agent / Skills / 自动化项目清单

> 用途：收藏值得研究、集成到 Codex / Claude Code / Cursor / 自定义 Agent 工作流中的 GitHub 项目。
> 
> 更新：2026-08-25

## 第一梯队：优先研究

### 1. Anthropic Skills
- GitHub: https://github.com/anthropics/skills
- 方向：Agent Skills / 官方 Skill 示例
- 价值：适合学习标准化 Skill 结构、SKILL.md 组织方式、设计/开发/文档/企业工作流。
- 推荐：★★★★★

### 2. Awesome Agent Skills
- GitHub: https://github.com/VoltAgent/awesome-agent-skills
- 方向：Agent Skill 聚合索引
- 价值：集中收录来自 Google、Vercel、Stripe、Cloudflare、Figma 等团队或生态的 Skills，可继续从这里扩展自己的 Skill 库。
- 推荐：★★★★★

### 3. Browser Use
- GitHub: https://github.com/browser-use/browser-use
- 方向：浏览器 AI Agent / Browser Automation
- 价值：让 Agent 自动打开网页、点击、输入、读取页面、执行网页任务，可与 Codex、MCP、Computer Use 串联。
- 推荐：★★★★★

### 4. ECC
- GitHub: https://github.com/affaan-m/ecc
- 方向：Coding Agent Harness / Skills / Memory / Security
- 价值：适合研究如何给 Codex、Claude Code、Cursor 等 Agent 增加 Skills、记忆、安全、研究优先工作流。
- 推荐：★★★★★

### 5. AgentMemory
- GitHub: https://github.com/rohitg00/agentmemory
- 方向：Agent Persistent Memory
- 价值：给 Coding Agent 增加跨任务、跨 Session 的长期记忆能力，适合作为个人 AI 工作站的 Memory 层。
- 推荐：★★★★☆

## 第二梯队：专项增强

### 6. OpenAgent
- GitHub: https://github.com/the-open-agent/openagent
- 方向：个人 AI Agent / Computer Use / Browser Use / Coding Agent / RAG
- 价值：适合研究“AI 直接完成电脑任务”的整合架构。
- 推荐：★★★★☆

### 7. Last30Days Skill
- GitHub: https://github.com/mvanhorn/last30days-skill
- 方向：互联网研究 Agent
- 价值：自动研究最近一段时间的 Reddit、X、YouTube、Hacker News、Web 等信息，可改造成摄影、AI、设计、GitHub 趋势研究 Skill。
- 推荐：★★★★☆

### 8. Scientific Agent Skills
- GitHub: https://github.com/K-Dense-AI/scientific-agent-skills
- 方向：科研 Agent Skills / 专业知识库
- 价值：适合研究大型专业 Skill Library 如何组织，也可作为构建 Creative / Photography / Design Skill Library 的架构参考。
- 推荐：★★★★★

### 9. Android Skills
- GitHub: https://github.com/android/skills
- 方向：Android Agent Skills
- 价值：面向 Android 开发的模块化 Agent Skills，可研究官方团队如何为 AI Agent 封装开发能力。
- 推荐：★★★★☆

### 10. Awesome Harness Engineering
- GitHub: https://github.com/ai-boost/awesome-harness-engineering
- 方向：Agent Harness / Memory / MCP / 权限 / 评测 / 编排 / Observability
- 价值：适合研究如何把单一模型升级为稳定的长期 Agent 系统。
- 推荐：★★★★☆

## 建议组合架构

```text
个人 AI 工作站
│
├── Agent / Codex
│
├── Skills
│   ├── Photography
│   ├── Photoshop
│   ├── Premiere Pro
│   ├── After Effects
│   ├── Figma
│   ├── 3D
│   └── Coding
│
├── Memory
│   ├── 项目历史
│   ├── 用户偏好
│   ├── 成功方案
│   └── 错误记录
│
├── Browser Use
│
├── Computer Use
│
├── MCP / Tools
│
└── Research Agent
```

## 推荐学习顺序

1. Awesome Agent Skills
2. Anthropic Skills
3. Browser Use
4. ECC
5. AgentMemory
6. OpenAgent
7. Last30Days
8. Scientific Agent Skills

## 后续可以继续扩展的方向

- 摄影 AI / 自动选片 / AI 精修
- Photoshop 自动化
- Premiere Pro / After Effects 自动化
- Blender / 3D / 渲染
- ComfyUI / 图像生成
- 视频生成与视频理解
- Computer Use
- Local AI / 本地模型
- MCP Server
- RAG / 长期记忆
- Figma / UI / Design Agent
- 音乐制作 / DAW 自动化
- OSINT / 数据可视化
- GitHub 自动研究与自动更新

## 安全提醒

第三方 Skill、MCP Server、Agent 插件和自动化脚本不要直接给予高权限。安装前应检查：

- 是否读取系统凭据、浏览器 Cookie、SSH Key、API Key。
- 是否执行未知 Shell / PowerShell 命令。
- 是否向外部服务器上传文件或环境变量。
- 是否修改系统启动项、计划任务或权限。
- 是否包含混淆代码、远程下载执行、隐藏网络请求。
- 是否真的需要管理员权限。

建议优先在沙箱、虚拟机、容器或低权限账户中测试。
