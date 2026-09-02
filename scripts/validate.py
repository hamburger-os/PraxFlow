#!/usr/bin/env python3
"""Validate PraxFlow Agent Skills packages without third-party dependencies."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOTS = {
    "workflows": "workflow",
    "skills": "skill",
    "packs": "pack",
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_RE = re.compile(r"(?:`|\()((?:references|scripts|assets)/[^`)\s]+)")


@dataclass
class Package:
    root_kind: str
    directory: Path
    skill_file: Path
    frontmatter: dict[str, str]
    metadata: dict[str, str]
    body: str


def parse_frontmatter(path: Path) -> tuple[dict[str, str], dict[str, str], str, list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, {}, text, ["SKILL.md must start with YAML frontmatter delimiter '---'"]

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, {}, text, ["SKILL.md frontmatter is missing closing '---'"]

    top: dict[str, str] = {}
    metadata: dict[str, str] = {}
    section: str | None = None

    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        if raw.startswith("  "):
            if section == "metadata" and ":" in raw:
                key, value = raw.strip().split(":", 1)
                metadata[key.strip()] = unquote(value.strip())
            continue

        if ":" not in raw:
            errors.append(f"unrecognized frontmatter line: {raw!r}")
            continue

        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            section = key
            continue
        section = None
        top[key] = unquote(value)

    body = "\n".join(lines[end + 1 :])
    return top, metadata, body, errors


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def discover_packages() -> list[Package]:
    packages: list[Package] = []
    for root_name, conceptual_type in PACKAGE_ROOTS.items():
        base = ROOT / root_name
        if not base.exists():
            continue
        for skill_file in sorted(base.glob("*/SKILL.md")):
            top, metadata, body, parse_errors = parse_frontmatter(skill_file)
            package = Package(root_name, skill_file.parent, skill_file, top, metadata, body)
            package._parse_errors = parse_errors  # type: ignore[attr-defined]
            packages.append(package)
    return packages


def validate_package(package: Package) -> tuple[list[str], list[str]]:
    errors: list[str] = list(getattr(package, "_parse_errors", []))
    warnings: list[str] = []
    rel = package.skill_file.relative_to(ROOT)
    name = package.frontmatter.get("name", "")
    description = package.frontmatter.get("description", "")

    if not name:
        errors.append("missing required frontmatter field: name")
    else:
        if len(name) > 64:
            errors.append("name exceeds 64 characters")
        if not NAME_RE.fullmatch(name):
            errors.append("name must contain lowercase ASCII letters, digits, and single hyphens only")
        if name != package.directory.name:
            errors.append(f"name {name!r} does not match parent directory {package.directory.name!r}")

    if not description:
        errors.append("missing required frontmatter field: description")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    elif len(description) < 40:
        warnings.append("description may be too vague for reliable implicit discovery")

    expected_type = PACKAGE_ROOTS[package.root_kind]
    actual_type = package.metadata.get("praxflow-type")
    if actual_type != expected_type:
        errors.append(
            f"metadata.praxflow-type must be {expected_type!r} for packages under {package.root_kind}/"
        )

    if not package.metadata.get("praxflow-version"):
        errors.append("metadata.praxflow-version is required")

    line_count = len(package.skill_file.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        warnings.append(f"SKILL.md has {line_count} lines; Agent Skills recommends keeping it under 500")

    for ref in sorted(set(REFERENCE_RE.findall(package.body))):
        candidate = package.directory / ref
        if not candidate.exists():
            errors.append(f"referenced file does not exist: {ref}")

    # Keep supporting content reasonably shallow for progressive disclosure.
    for support_dir in ("references", "scripts", "assets"):
        base = package.directory / support_dir
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and len(p.relative_to(package.directory).parts) > 2:
                warnings.append(f"deep supporting-file nesting: {p.relative_to(package.directory)}")

    if not package.body.strip():
        errors.append("SKILL.md body is empty")

    return [f"{rel}: {e}" for e in errors], [f"{rel}: {w}" for w in warnings]


def validate_all(packages: Iterable[Package]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    names: dict[str, Path] = {}

    packages = list(packages)
    if not packages:
        errors.append("no PraxFlow packages found")
        return errors, warnings

    for package in packages:
        pkg_errors, pkg_warnings = validate_package(package)
        errors.extend(pkg_errors)
        warnings.extend(pkg_warnings)

        name = package.frontmatter.get("name")
        if name:
            if name in names:
                errors.append(
                    f"duplicate package name {name!r}: {names[name].relative_to(ROOT)} and "
                    f"{package.directory.relative_to(ROOT)}"
                )
            else:
                names[name] = package.directory

    expected_core = {
        "develop-feature",
        "fix-bug",
        "understand-project",
        "review-change",
        "survey",
        "trace",
        "grill",
        "diagnose",
        "plan-change",
    }
    missing = sorted(expected_core - set(names))
    if missing:
        errors.append("missing expected v0.1 Core packages: " + ", ".join(missing))

    return errors, warnings


def main() -> int:
    packages = discover_packages()
    errors, warnings = validate_all(packages)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"\nValidation failed: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(packages)} package(s): 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
