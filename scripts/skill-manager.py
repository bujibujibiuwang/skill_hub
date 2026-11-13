#!/usr/bin/env python3
"""Small, dependency-free Skill Hub manager."""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.yaml"


def read_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*[\"']?(.*?)[\"']?$", line)
        if match:
            result[match.group(1)] = match.group(2)
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def discover(roots: list[Path]) -> list[dict[str, str]]:
    found = []
    for root in roots:
        if not root.exists():
            continue
        for skill_file in sorted(root.rglob("SKILL.md")):
            meta = read_frontmatter(skill_file)
            found.append({
                "name": meta.get("name", skill_file.parent.name),
                "description": meta.get("description", ""),
                "path": str(skill_file.parent),
                "sha256": sha256(skill_file),
            })
    return found


def catalog_text() -> str:
    return CATALOG.read_text(encoding="utf-8")


def names_in_catalog() -> set[str]:
    return set(re.findall(r"^  - name:\s*([^\s#]+)", catalog_text(), re.M))


def cmd_scan(args: argparse.Namespace) -> int:
    roots = [Path(p).expanduser() for p in args.roots]
    for item in discover(roots):
        print(f"{item['name']}\t{item['path']}\t{item['sha256']}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    needle = args.query.lower()
    for item in discover([ROOT / "skills"]):
        if needle in (item["name"] + " " + item["description"]).lower():
            print(f"{item['name']}\t{item['description']}\t{item['path']}")
    return 0


def cmd_validate(_: argparse.Namespace) -> int:
    errors = []
    names = names_in_catalog()
    for name in names:
        skill = ROOT / "skills" / name / "SKILL.md"
        if not skill.is_file():
            errors.append(f"missing managed Skill: {skill}")
        elif not read_frontmatter(skill).get("name"):
            errors.append(f"missing frontmatter name: {skill}")
    if not names:
        errors.append("catalog.yaml contains no Skills")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"validated {len(names)} Skill(s)")
    return 0


def cmd_conflicts(args: argparse.Namespace) -> int:
    items = discover([Path(p).expanduser() for p in args.roots])
    by_name: dict[str, list[dict[str, str]]] = {}
    for item in items:
        by_name.setdefault(item["name"], []).append(item)
    conflicts = 0
    for name, group in sorted(by_name.items()):
        if len({item["sha256"] for item in group}) > 1:
            conflicts += 1
            print(f"CONFLICT {name}")
            for item in group:
                print(f"  {item['sha256']} {item['path']}")
    print(f"conflicts: {conflicts}")
    return 1 if conflicts else 0


def cmd_install(args: argparse.Namespace) -> int:
    source = ROOT / "skills" / args.name
    if not (source / "SKILL.md").is_file():
        print(f"unknown managed Skill: {args.name}", file=sys.stderr)
        return 1
    target_root = Path(args.global_root).expanduser()
    target = target_root / args.name
    if target.exists() or target.is_symlink():
        if target.is_symlink() and target.resolve() == source.resolve():
            print(f"already linked: {target}")
            return 0
        print(f"refusing to overwrite existing path: {target}", file=sys.stderr)
        return 2
    target_root.mkdir(parents=True, exist_ok=True)
    target.symlink_to(source, target_is_directory=True)
    print(f"linked {target} -> {source}")
    return 0


def cmd_upgrade(args: argparse.Namespace) -> int:
    source = Path(args.source).expanduser().resolve()
    target = ROOT / "skills" / args.name
    if not (source / "SKILL.md").is_file():
        print(f"source is not a Skill directory: {source}", file=sys.stderr)
        return 1
    target.mkdir(parents=True, exist_ok=True)
    for item in source.rglob("*"):
        relative = item.relative_to(source)
        destination = target / relative
        if item.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, destination)
    print(f"upgraded {args.name} from {source}; original source unchanged")
    return 0


def cmd_deprecate(args: argparse.Namespace) -> int:
    text = catalog_text()
    pattern = rf"(^  - name: {re.escape(args.name)}$.*?^    status:) active$"
    updated, count = re.subn(pattern, r"\1 deprecated", text, flags=re.M | re.S)
    if not count:
        print(f"active Skill not found in catalog: {args.name}", file=sys.stderr)
        return 1
    CATALOG.write_text(updated, encoding="utf-8")
    print(f"marked deprecated: {args.name}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="skill-manager")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("scan"); p.add_argument("roots", nargs="+", help="directories to scan"); p.set_defaults(func=cmd_scan)
    p = sub.add_parser("search"); p.add_argument("query"); p.set_defaults(func=cmd_search)
    p = sub.add_parser("validate"); p.set_defaults(func=cmd_validate)
    p = sub.add_parser("conflicts"); p.add_argument("roots", nargs="+", help="directories to compare"); p.set_defaults(func=cmd_conflicts)
    p = sub.add_parser("install"); p.add_argument("name"); p.add_argument("--global-root", default="~/.codex/skills"); p.set_defaults(func=cmd_install)
    p = sub.add_parser("upgrade"); p.add_argument("name"); p.add_argument("--source", required=True); p.set_defaults(func=cmd_upgrade)
    p = sub.add_parser("deprecate"); p.add_argument("name"); p.set_defaults(func=cmd_deprecate)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
