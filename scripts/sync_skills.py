#!/usr/bin/env python3
"""Discover upstream SKILL.md files and generate a searchable catalog.

This script intentionally stores metadata/links rather than copying third-party
skill contents. That keeps upstream attribution/history clear and avoids stale
vendored copies. Run locally or from GitHub Actions.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "upstreams.json"
OUT_JSON = ROOT / "catalog" / "skills.json"
OUT_MD = ROOT / "catalog" / "SKILLS.md"
API = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN", "")


def request_json(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-skill-sync/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def repo_meta(repo: str):
    return request_json(f"{API}/repos/{repo}")


def skill_paths(repo: str, branch: str):
    # Git tree recursive discovery is deterministic and avoids code-search indexing delays.
    branch_data = request_json(f"{API}/repos/{repo}/branches/{urllib.parse.quote(branch, safe='')}")
    commit_sha = branch_data["commit"]["sha"]
    tree = request_json(f"{API}/repos/{repo}/git/trees/{commit_sha}?recursive=1")
    paths = []
    for item in tree.get("tree", []):
        path = item.get("path", "")
        if item.get("type") == "blob" and path.lower().endswith("skill.md"):
            paths.append({"path": path, "blob_sha": item.get("sha")})
    return commit_sha, sorted(paths, key=lambda x: x["path"].lower())


def main():
    cfg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    generated = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    result = {"generated_at": generated, "repositories": [], "skills": []}

    for entry in cfg["repositories"]:
        repo = entry["repo"]
        try:
            meta = repo_meta(repo)
            branch = meta["default_branch"]
            commit, skills = skill_paths(repo, branch)
            rec = {
                **entry,
                "default_branch": branch,
                "head_sha": commit,
                "html_url": meta["html_url"],
                "skill_count": len(skills),
                "status": "ok",
            }
            result["repositories"].append(rec)
            for skill in skills:
                path = skill["path"]
                result["skills"].append({
                    "repo": repo,
                    "path": path,
                    "blob_sha": skill["blob_sha"],
                    "source_url": f"https://github.com/{repo}/blob/{commit}/{path}",
                    "category": entry["category"],
                    "priority": entry["priority"],
                })
        except Exception as exc:
            result["repositories"].append({**entry, "status": "error", "error": str(exc)})

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 自动发现的 Agent Skills",
        "",
        f"> 自动生成时间：{generated}",
        "> 数据来自 `upstreams.json` 中登记的上游仓库。此目录保存来源与版本，不直接复制第三方 Skill 内容。",
        "",
        f"当前发现 **{len(result['skills'])}** 个 `SKILL.md`。",
        "",
        "## 上游状态",
        "",
        "| Repository | Category | Skills | Status | Head |",
        "|---|---|---:|---|---|",
    ]
    for r in result["repositories"]:
        sha = r.get("head_sha", "-")[:12]
        lines.append(f"| [{r['repo']}](https://github.com/{r['repo']}) | {r['category']} | {r.get('skill_count', 0)} | {r['status']} | `{sha}` |")

    lines += ["", "## Skills", ""]
    if result["skills"]:
        for s in result["skills"]:
            lines.append(f"- **{s['repo']}** — [`{s['path']}`]({s['source_url']})")
    else:
        lines.append("暂未发现 SKILL.md。")
    lines += ["", "---", "", "由 `scripts/sync_skills.py` 自动维护。", ""]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
