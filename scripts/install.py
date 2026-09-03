#!/usr/bin/env python3
"""Install PraxFlow Agent Skills packages into client discovery directories."""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

from validate import ROOT, discover_packages, validate_all

PROJECT_PATHS = {
    "codex": Path(".agents/skills"),
    "trae": Path(".agents/skills"),
    "claude": Path(".claude/skills"),
}

USER_PATHS = {
    "codex": Path.home() / ".agents/skills",
    "claude": Path.home() / ".claude/skills",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install PraxFlow workflows, cognitive skills, and optional domain packs."
    )
    parser.add_argument(
        "--target",
        choices=("codex", "claude", "trae", "generic"),
        required=True,
        help="Client whose skill discovery directory should be used.",
    )
    parser.add_argument(
        "--scope",
        choices=("project", "user"),
        default="project",
        help="Install scope for known clients (default: project).",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.cwd(),
        help="Project root for project-scope installs (default: current directory).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Explicit skills directory. Required for --target generic; overrides automatic path resolution.",
    )
    parser.add_argument(
        "--package",
        action="append",
        default=[],
        help="Install only the named package. Repeat to select multiple packages.",
    )
    parser.add_argument(
        "--pack",
        action="append",
        default=[],
        help="Add an optional Domain Pack such as praxflow-embedded. Repeatable.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing destination package directories.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned copies without modifying the destination.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available packages and exit.",
    )
    return parser.parse_args()


def resolve_output_dir(args: argparse.Namespace) -> Path:
    if args.output_dir:
        return args.output_dir.expanduser().resolve()

    if args.target == "generic":
        raise SystemExit("--target generic requires --output-dir")

    if args.scope == "project":
        return (args.dest.expanduser().resolve() / PROJECT_PATHS[args.target]).resolve()

    if args.target == "trae":
        raise SystemExit(
            "TRAE global Skills are product-managed and the public filesystem path may vary. "
            "Use project scope, the TRAE UI, or --target generic --output-dir <known-global-skills-dir>."
        )

    return USER_PATHS[args.target].expanduser().resolve()


def replace_tree(source: Path, target: Path) -> None:
    """Stage a package copy before replacing an existing installation."""
    target.parent.mkdir(parents=True, exist_ok=True)
    staging_root = Path(
        tempfile.mkdtemp(prefix=f".praxflow-{target.name}-", dir=target.parent)
    )
    staged = staging_root / "new"
    backup = staging_root / "old"
    committed = False

    try:
        shutil.copytree(source, staged)
        if target.exists():
            target.rename(backup)
        try:
            staged.rename(target)
            committed = True
        except Exception:
            if target.exists():
                shutil.rmtree(target)
            if backup.exists():
                backup.rename(target)
            raise

        if backup.exists():
            shutil.rmtree(backup)
    finally:
        if not committed and backup.exists() and not target.exists():
            backup.rename(target)
        shutil.rmtree(staging_root, ignore_errors=True)


def main() -> int:
    args = parse_args()
    packages = discover_packages()
    errors, warnings = validate_all(packages)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print("Source packages failed validation; refusing to install.", file=sys.stderr)
        return 1

    index = {p.frontmatter["name"]: p for p in packages}

    if args.list:
        for name in sorted(index):
            package = index[name]
            print(f"{name:24} {package.metadata.get('praxflow-type', '?'):10} {package.root_kind}")
        return 0

    requested = list(args.package)
    if requested:
        selected_names = requested
    else:
        selected_names = sorted(
            name
            for name, package in index.items()
            if package.metadata.get("praxflow-type") in {"workflow", "skill"}
        )

    selected_names.extend(args.pack)

    # Stable de-duplication while preserving explicit order when --package is used.
    selected_names = list(dict.fromkeys(selected_names))

    unknown = [name for name in selected_names if name not in index]
    if unknown:
        print("Unknown package(s): " + ", ".join(unknown), file=sys.stderr)
        print("Run with --list to see available packages.", file=sys.stderr)
        return 2

    output_dir = resolve_output_dir(args)

    canonical_roots = tuple(
        (ROOT / root_name).resolve() for root_name in ("workflows", "skills", "packs")
    )
    if any(
        output_dir == canonical_root or output_dir.is_relative_to(canonical_root)
        for canonical_root in canonical_roots
    ):
        print(
            "Refusing to install into PraxFlow canonical source directories: "
            f"{output_dir}",
            file=sys.stderr,
        )
        return 4

    actions: list[tuple[Path, Path]] = []
    collisions: list[Path] = []

    for name in selected_names:
        source = index[name].directory
        target = output_dir / name
        actions.append((source, target))
        if target.exists() and not args.force:
            collisions.append(target)

    if collisions:
        print("Destination package(s) already exist; use --force to replace them:", file=sys.stderr)
        for path in collisions:
            print(f"  {path}", file=sys.stderr)
        return 3

    print(f"PraxFlow source: {ROOT}")
    print(f"Destination:    {output_dir}")

    for source, target in actions:
        print(f"  {source.relative_to(ROOT)} -> {target}")

    if args.dry_run:
        print("Dry run: no files changed.")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    for source, target in actions:
        replace_tree(source, target)

    print(f"Installed {len(actions)} package(s).")
    if warnings:
        print(f"Source validation produced {len(warnings)} warning(s); run scripts/validate.py for details.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
