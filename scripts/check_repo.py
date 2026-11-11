#!/usr/bin/env python3
"""仓库结构自检：技能 frontmatter、登记册模板、站点文章、相对链接。
只做结构检查，不判断内容质量。失败返回非零退出码。"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def check_skills() -> None:
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if len(skills) != 18:
        errors.append(f"skills 目录应为 18 个技能，实际 {len(skills)}")
    for d in skills:
        f = d / "SKILL.md"
        if not f.is_file():
            errors.append(f"{d.name}: 缺少 SKILL.md")
            continue
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append(f"{d.name}: frontmatter 缺失或未闭合")
            continue
        fm = yaml.safe_load(m.group(1))
        if fm.get("name") != d.name:
            errors.append(f"{d.name}: name 与目录名不一致（{fm.get('name')}）")
        if not str(fm.get("description", "")).strip():
            errors.append(f"{d.name}: description 为空")


def check_templates() -> None:
    tdir = ROOT / "templates" / "paper"
    files = sorted(tdir.glob("*.yml"))
    if len(files) != 12:
        errors.append(f"登记册模板应为 12 个，实际 {len(files)}")
    for f in files:
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{f.name}: YAML 解析失败 {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{f.name}: 顶层应为映射")
    wf = yaml.safe_load((tdir / "workflow.yml").read_text(encoding="utf-8"))
    gates = {g["id"] for g in wf.get("gates", [])}
    if gates != {"G1", "G2", "G3", "G4", "G5", "G6"}:
        errors.append(f"workflow.yml 门控应为 G1–G6，实际 {sorted(gates)}")
    for stage in wf.get("stages", []):
        for dep in stage.get("blocked_by", []):
            if dep not in gates:
                errors.append(f"stage {stage['id']}: blocked_by 引用了未知门 {dep}")


def check_scope() -> None:
    """本仓库只承载技能与模板；博客站点已迁到 keyd164.github.io 仓库。"""
    if (ROOT / "site").exists():
        errors.append("site/ 应已迁出本仓库，博客站点在 keyd164.github.io 仓库维护")
    if (ROOT / ".github" / "workflows" / "pages.yml").exists():
        errors.append("pages.yml 应已移除，本仓库不再负责站点部署")


def check_links() -> None:
    for md in ROOT.rglob("*.md"):
        parts = set(md.parts)
        if ".git" in parts or "third_party" in parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\]\((?!https?:|mailto:|#)([^)]+)\)", text):
            target = m.group(1).split("#")[0].strip()
            if not target:
                continue
            if not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: 断链 {target}")


def check_workflows() -> None:
    for wf in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        try:
            yaml.safe_load(wf.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{wf.name}: workflow YAML 解析失败 {exc}")


def main() -> int:
    for fn in (check_skills, check_templates, check_scope, check_links, check_workflows):
        fn()
    if errors:
        print("结构自检失败：")
        for e in errors:
            print(" -", e)
        return 1
    print("结构自检通过：18 个技能、12 个模板、仓库边界与相对链接均正常")
    return 0


if __name__ == "__main__":
    sys.exit(main())