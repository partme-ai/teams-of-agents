#!/usr/bin/env python3
"""
将 claw-agents 从旧「三大分组」迁移为与 agency-agents 一致的一级分类目录。
用法:
  python3 scripts/migrate_to_agency_layout.py --dry-run
  python3 scripts/migrate_to_agency_layout.py
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

# 与 research/agency-agents 一级分类一致（同 agency-agents/scripts/convert.sh 的 AGENT_DIRS，并含 strategy）
AGENT_DIRS = [
    "academic",
    "design",
    "engineering",
    "game-development",
    "marketing",
    "paid-media",
    "sales",
    "product",
    "project-management",
    "testing",
    "support",
    "spatial-computing",
    "specialized",
    "strategy",
]

OLD_PREFIXES = ("1、IM Channels", "2、Digital Workforce", "3、Content Ops")

# 2、Digital Workforce 下二级目录 -> partme 子路径前缀
DW_SUB_TO_PARTME = {
    "10、Web3": "web3",
    # 两个「Customer Service」分组并存，避免 specialized/partme 下路径撞车
    "11、Customer Service": "customer-service-dw11",
    "12、Education": "education",
    "1、Company Manger": "company",
    "1、Customer Service": "customer-service-dw1",
    "2、Sales": "sales",
    "3、Finance & Ops": "finance-ops",
    "4、Game & Media": "game-media",
    "5、XR & Spatial": "xr-spatial",
    "6、Compliance & Risk": "compliance-risk",
    "7、Ad & Creative": "ad-creative",
    "8、Research & Strategy": "research-strategy",
    "9、Software & Delivery": "software-delivery",
    "Software & Ops": "software-ops",
}


def slugify(name: str) -> str:
    """与 convert.sh 中 slugify 一致：小写、非字母数字 -> -，合并重复 -。"""
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def load_slug_to_category(agency_root: Path) -> dict[str, str]:
    """扫描 agency-agents 中带 frontmatter 的 agent .md，建立 slug -> 一级分类。"""
    out: dict[str, str] = {}
    for d in AGENT_DIRS:
        dirpath = agency_root / d
        if not dirpath.is_dir():
            continue
        for md in dirpath.rglob("*.md"):
            try:
                text = md.read_text(encoding="utf-8")
            except OSError:
                continue
            if not text.startswith("---"):
                continue
            m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
            if not m:
                continue
            name = m.group(1).strip().strip("\"'")
            slug = slugify(name)
            out[slug] = d
    return out


def find_agent_roots(claw: Path) -> list[Path]:
    """旧三大分组下，凡存在 AGENTS.md 的智能体根目录（zh-CN 归一到上级）。"""
    roots: set[Path] = set()
    for prefix in OLD_PREFIXES:
        base = claw / prefix
        if not base.is_dir():
            continue
        for p in base.rglob("AGENTS.md"):
            if ".git" in p.parts:
                continue
            parent = p.parent
            if parent.name == "zh-CN":
                parent = parent.parent
            roots.add(parent.resolve())
    return sorted(roots, key=lambda x: str(x))


def slug_candidates(folder_name: str) -> list[str]:
    """文件夹名可能对应的 slug 列表。"""
    base = folder_name.strip()
    out = [base.lower()]
    stripped = re.sub(r"^\d+-", "", base)
    if stripped != base:
        out.append(stripped.lower())
    # 去重保持顺序
    seen: set[str] = set()
    uniq: list[str] = []
    for x in out:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq


def partme_relative(claw: Path, agent_root: Path) -> Path:
    """智能体在 specialized/partme/ 下的相对路径（相对 claw 根）。"""
    rel = agent_root.relative_to(claw)
    parts = rel.parts
    if parts[0] == "1、IM Channels":
        return Path("specialized/partme/im-channels") / Path(*parts[1:])
    if parts[0] == "3、Content Ops":
        return Path("specialized/partme/content-ops") / Path(*parts[1:])
    if parts[0] == "2、Digital Workforce":
        if len(parts) < 2:
            return Path("specialized/partme/digital-workforce") / Path(*parts[1:])
        sub = parts[1]
        if sub in DW_SUB_TO_PARTME:
            key = DW_SUB_TO_PARTME[sub]
            return Path("specialized/partme") / key / Path(*parts[2:])
        return Path("specialized/partme/digital-workforce") / Path(*parts[1:])
    raise ValueError(f"不在旧三大分组下: {rel}")


def resolve_dest(
    claw: Path,
    agent_root: Path,
    slug_map: dict[str, str],
) -> tuple[Path, str]:
    """
    返回目标目录（相对 claw 的 Path，如 engineering/frontend-developer）及原因标签。
    """
    name = agent_root.name
    for cand in slug_candidates(name):
        if cand in slug_map:
            cat = slug_map[cand]
            return Path(cat) / cand, "roster"
    rel = partme_relative(claw, agent_root)
    return rel, "partme"


def collision_fallback_dest(claw: Path, agent_root: Path, slug: str) -> Path:
    """
    当多个源目录映射到同一 roster 目标时，将多余副本放到 partme 下可追溯路径。
    """
    rel = agent_root.relative_to(claw)
    tail = "__".join(rel.parts).replace("、", "_").replace(" ", "_")
    return Path("specialized/partme/roster-collision") / f"{slug}__{tail}"


def plan_moves(
    claw: Path, slug_map: dict[str, str]
) -> list[tuple[Path, Path, str]]:
    """返回 (源目录, 目标相对路径, kind)，并解决 roster 目标冲突。"""
    raw: list[tuple[Path, Path, str]] = []
    for agent_root in find_agent_roots(claw):
        dest_rel, kind = resolve_dest(claw, agent_root, slug_map)
        if (claw / dest_rel).resolve() == agent_root.resolve():
            continue
        raw.append((agent_root, dest_rel, kind))

    # 同一 dest_rel 多个源：保留字典序第一个，其余改到 roster-collision
    from collections import defaultdict

    by_dest: dict[Path, list[tuple[Path, Path, str]]] = defaultdict(list)
    for item in raw:
        by_dest[item[1]].append(item)

    out: list[tuple[Path, Path, str]] = []
    for dest_rel, group in by_dest.items():
        if len(group) == 1:
            out.append(group[0])
            continue
        group_sorted = sorted(group, key=lambda x: str(x[0]))
        first = group_sorted[0]
        out.append(first)
        for agent_root, _old_rel, kind in group_sorted[1:]:
            # 从 folder 名恢复 slug（与 resolve_dest 一致）
            name = agent_root.name
            slug = next((c for c in slug_candidates(name) if c in slug_map), name.lower())
            fb = collision_fallback_dest(claw, agent_root, slug)
            out.append((agent_root, fb, kind + "+collision"))

    return out


def move_agents(
    claw: Path,
    slug_map: dict[str, str],
    dry_run: bool,
) -> None:
    for agent_root, dest_rel, kind in plan_moves(claw, slug_map):
        dest = (claw / dest_rel).resolve()
        if dest.exists():
            raise SystemExit(f"目标已存在，中止: {dest}\n 源: {agent_root}")
        if dry_run:
            print(f"[{kind}] {agent_root.relative_to(claw)} -> {dest_rel}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(agent_root), str(dest))


def merge_openclaw(
    claw: Path,
    openclaw: Path,
    slug_map: dict[str, str],
    dry_run: bool,
) -> None:
    if not openclaw.is_dir():
        print(f"跳过 openclaw 合并（目录不存在）: {openclaw}", file=sys.stderr)
        return
    three = ("AGENTS.md", "IDENTITY.md", "SOUL.md")
    for src_dir in sorted(openclaw.iterdir()):
        if not src_dir.is_dir():
            continue
        slug = src_dir.name
        if slug not in slug_map:
            print(f"警告: openclaw/{slug} 无 roster 映射，跳过", file=sys.stderr)
            continue
        cat = slug_map[slug]
        dest_dir = claw / cat / slug
        if dry_run:
            exists = dest_dir.is_dir()
            print(
                f"[openclaw] {slug} -> {cat}/{slug} "
                f"({'merge 3 files' if exists else 'mkdir + copy 3 files'})"
            )
            continue
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name in three:
            sf = src_dir / name
            if not sf.is_file():
                continue
            shutil.copy2(sf, dest_dir / name)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="仅打印计划，不移动或复制文件",
    )
    args = ap.parse_args()

    claw = Path(__file__).resolve().parent.parent
    # openclaw-agents 与 research/agency-agents 通常同属工作区根目录（workspace-partme-ai/）下
    agency = claw.parent / "research" / "agency-agents"
    if not agency.is_dir():
        agency = Path("/home/wandl/workspaces/workspace-partme-ai/research/agency-agents")
    openclaw = agency / "integrations" / "openclaw"

    slug_map = load_slug_to_category(agency)
    print(f"已加载 roster slug 数: {len(slug_map)}", file=sys.stderr)

    move_agents(claw, slug_map, dry_run=args.dry_run)
    merge_openclaw(claw, openclaw, slug_map, dry_run=args.dry_run)

    if args.dry_run:
        print("Dry-run 完成。", file=sys.stderr)
    else:
        print("迁移与 openclaw 合并完成。", file=sys.stderr)


if __name__ == "__main__":
    main()
