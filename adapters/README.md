# Client Adapters

PraxFlow uses the open Agent Skills format as its canonical package format. Adapters only decide **where** a package is copied so a particular client can discover it.

Client paths change over time; treat this file and `scripts/install.py` as compatibility code, not methodology.

## Agent Skills format

Normative format:

https://agentskills.io/specification

PraxFlow packages use only portable core frontmatter (`name`, `description`, `license`, `metadata`) and standard supporting directories. Vendor-specific extensions should remain optional.

## Codex

Current repo/project discovery path:

```text
<repo>/.agents/skills/<skill-name>/SKILL.md
```

Current user path:

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

## Claude Code

Current project discovery path:

```text
<repo>/.claude/skills/<skill-name>/SKILL.md
```

Current personal path:

```text
~/.claude/skills/<skill-name>/SKILL.md
```

Anthropic documentation:

https://code.claude.com/docs/en/skills

Install Core into a project:

```bash
python3 scripts/install.py --target claude --scope project --dest /path/to/repo
```

## TRAE

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

## Generic Agent Skills client

For any client that accepts an Agent Skills directory:

```bash
python3 scripts/install.py \
  --target generic \
  --output-dir /path/to/skills
```

## Packs

Core installation includes the four Workflows and five cognitive Skills. Domain Packs are opt-in:

```bash
python3 scripts/install.py \
  --target codex \
  --scope project \
  --dest /path/to/repo \
  --pack praxflow-embedded
```

A Domain Pack is itself packaged as an Agent Skill distribution unit so it can activate alongside a Core Workflow. Conceptually it remains a PraxFlow Pack, not a Core cognitive Skill.

## Copy, don't duplicate source-of-truth

The PraxFlow repository keeps canonical package sources under:

```text
workflows/
skills/
packs/
```

The installer copies them into the client's flat discovery directory. Do not manually maintain duplicate canonical copies under `.agents/skills` and `.claude/skills` in this repository.

## Client-specific enhancements

A client may support extra metadata, UI manifests, invocation policy, or plugin packaging. Add such integrations under `adapters/` only when:

- the portable `SKILL.md` remains valid without them;
- the enhancement solves a demonstrated client problem;
- Core methodology does not depend on the extension.
