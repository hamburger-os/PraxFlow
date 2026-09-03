# Client Adapters

PraxFlow uses the open Agent Skills format as its canonical package format.

The Agent Skills specification defines what belongs **inside an individual Skill directory**. PraxFlow separately chooses a flat canonical source catalog for this repository:

```text
skills/<package-name>/SKILL.md
```

This repository layout is a PraxFlow interoperability convention, not a universal filesystem requirement of the Agent Skills specification. PraxFlow conceptual types (`workflow`, `skill`, and `pack`) are recorded in `metadata.praxflow-type`; they are not encoded as separate repository roots.

Client adapters decide **where** an installed package is placed. They must not redefine package content or create duplicate canonical source copies.

For the user-facing installation and usage guide, see [`../docs/getting-started.md`](../docs/getting-started.md) or [`../docs/getting-started.zh-CN.md`](../docs/getting-started.zh-CN.md).

## Recommended installation

For most users, use an Agent Skills ecosystem installer rather than cloning PraxFlow first:

```bash
npx skills@latest add hamburger-os/PraxFlow
```

PraxFlow deliberately publishes each package as an immediate child of `skills/`, so the supported repository-install path does not require PraxFlow-specific recursive discovery.

Install selected packages directly when needed:

```bash
npx skills@latest add hamburger-os/PraxFlow \
  --skill develop-feature \
  --skill diagnose \
  --agent codex \
  --yes
```

GitHub CLI can also discover the repository's Skill catalog:

```bash
gh skill install hamburger-os/PraxFlow
```

The external installer is the preferred first-run path because it handles client discovery and selection without requiring a PraxFlow clone or Python runtime.

## Agent Skills format

Normative format:

https://agentskills.io/specification

At minimum, an Agent Skill directory contains `SKILL.md`. The specification also defines optional/conventional supporting directories such as `scripts/`, `references/`, and `assets/`, while allowing additional files.

PraxFlow packages use portable core frontmatter (`name`, `description`, `license`, `metadata`) and package-local supporting resources. Vendor-specific extensions must remain optional.

The package directory name must match `name` in `SKILL.md`. Supporting material should remain package-local (`references/`, `scripts/`, `assets/`) so each package stays self-contained.

PraxFlow does not add `README.md` to every package by default. Human tutorials and conceptual explanations belong under `docs/`; package-local documentation should exist because the agent needs it during execution, normally under `references/`.

## Discovery locations are client conventions

The Agent Skills specification does **not** mandate one universal installation path. Client implementations choose where to scan for Skill directories.

The cross-client `.agents/skills/` location is a widely adopted interoperability convention, while some clients also have native locations such as `.claude/skills/`. Treat these as client/ecosystem conventions rather than package-format requirements.

## Built-in deterministic installer

PraxFlow keeps `scripts/install.py` as an advanced compatibility and development tool. It is useful when you need:

- deterministic Core installation without interactive package selection;
- explicit Domain Pack installation;
- custom output directories;
- project vs user scope control for known clients;
- dry-run / collision behavior;
- local source validation before copying.

The built-in installer and validator require **Python 3.10 or newer**.

### Codex

Current repo/project discovery path used by PraxFlow's adapter:

```text
<repo>/.agents/skills/<skill-name>/SKILL.md
```

Current user path used by PraxFlow's adapter:

```text
~/.agents/skills/<skill-name>/SKILL.md
```

OpenAI documentation:

https://learn.chatgpt.com/docs/build-skills

Install Core into a project:

```bash
python3 scripts/install.py --target codex --scope project --dest /path/to/repo
```

Install selected packages for the current user:

```bash
python3 scripts/install.py --target codex --scope user --package diagnose --package trace
```

### Claude Code

Current project discovery path used by PraxFlow's adapter:

```text
<repo>/.claude/skills/<skill-name>/SKILL.md
```

Current personal path used by PraxFlow's adapter:

```text
~/.claude/skills/<skill-name>/SKILL.md
```

Anthropic documentation:

https://code.claude.com/docs/en/skills

Install Core into a project:

```bash
python3 scripts/install.py --target claude --scope project --dest /path/to/repo
```

### TRAE

TRAE supports Agent Skills and project Skill loading from:

```text
<repo>/.agents/skills/<skill-name>/SKILL.md
```

The public TRAE changelog documents `.agents/skills` project loading:

https://www.trae.ai/changelog

Install into a project:

```bash
python3 scripts/install.py --target trae --scope project --dest /path/to/repo
```

TRAE also provides global Skills through product UI. PraxFlow does not hard-code a filesystem global path because public client behavior can change. Use the UI or `--target generic --output-dir ...` if you know the target directory for your installation.

### Generic Agent Skills client

For any client that accepts an Agent Skills directory:

```bash
python3 scripts/install.py \
  --target generic \
  --output-dir /path/to/skills
```

## Domain Packs

Core installation through the built-in installer includes the four Workflows and five cognitive Skills. Domain Packs are opt-in:

```bash
python3 scripts/install.py \
  --target codex \
  --scope project \
  --dest /path/to/repo \
  --pack praxflow-embedded
```

A Domain Pack is technically an Agent Skills package and therefore lives under `skills/` like every other installable PraxFlow unit. Conceptually it remains a PraxFlow Pack, not a Core cognitive Skill.

## One canonical distribution tree

Do not maintain duplicate source trees under client-specific paths such as `.agents/skills/`, `.claude/skills/`, or a generated `workflows/` / `packs/` hierarchy.

Canonical PraxFlow source:

```text
skills/
```

Client-specific copies are installation output only.

This separation gives PraxFlow one portable source of truth while allowing multiple clients and installers to map packages into their own discovery paths.

## Client-specific enhancements

A client may support extra metadata, UI manifests, invocation policy, plugin packaging, or managed update channels. Add such integrations only when:

- the canonical package remains valid without them;
- the enhancement solves a demonstrated client problem;
- Core methodology does not depend on the extension;
- generated or managed distributions are derived from canonical `skills/`, never maintained as a second methodology source.

Native plugins can be useful as a managed distribution layer, especially when they provide automatic updates or bundle multiple capabilities. They should remain adapters over the canonical catalog rather than a replacement for it.
