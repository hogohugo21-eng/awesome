# Skill Catalog

本目录由自动同步系统维护。

## 工作方式

1. `upstreams.json` 保存需要追踪的 GitHub 上游仓库。
2. `scripts/sync_skills.py` 读取每个仓库默认分支的最新 commit。
3. 脚本递归扫描所有以 `SKILL.md` 结尾的文件。
4. `catalog/skills.json` 保存机器可读的仓库、Skill 路径、blob SHA、上游 commit 和来源地址。
5. `catalog/SKILLS.md` 生成人类可读索引。
6. `.github/workflows/sync-agent-skills.yml` 每天运行一次；只有上游版本或 Skill 目录发生变化时才提交更新。

## 为什么不直接复制第三方源码

自动复制完整第三方项目会带来许可证、历史丢失、冲突和供应链风险。本仓库默认采用“来源 + 精确 commit + blob SHA”的方式追踪，因此既能知道上游什么时候变化，也能定位到当时的确切 Skill 版本。

如果以后确定某个 Skill 需要本地安装，再针对该 Skill 增加经过审核的 vendor/install 流程。

## 添加新项目

编辑根目录 `upstreams.json`，增加：

```json
{"repo": "owner/repository", "category": "your-category", "priority": 5}
```

然后手动运行 GitHub Actions 的 `Sync Agent Skills Catalog`，或等待每日自动同步。
