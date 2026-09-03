# Releasing PraxFlow

PraxFlow releases should reflect tested methodology, not calendar pressure.

## Versioning

PraxFlow is pre-1.0. Until the conceptual model stabilizes, use SemVer pre-releases such as:

```text
v0.1.0-alpha.1
v0.1.0-alpha.2
v0.1.0-beta.1
```

Breaking methodology changes are acceptable during pre-release, but they must be documented.

Tagged releases are also part of the distribution contract: standards-compatible installers can resolve or pin repository versions, so package layout and installability must be verified from the release commit rather than assumed from the default branch.

## Release gate

Before a tagged release:

- [ ] `python3 scripts/validate.py` passes on the supported Python floor.
- [ ] Every package under `skills/*` passes the pinned Agent Skills reference validator used by CI.
- [ ] Every installable package is directly discoverable as `skills/<name>/SKILL.md`; no first-class package depends on deep-search flags or client-specific source directories.
- [ ] External Agent Skills CLI distribution smoke tests pass from the release checkout.
- [ ] Built-in installer smoke tests pass across supported targets and failure modes.
- [ ] No top-level Protocol change is left without a synchronized installable package change under `skills/`.
- [ ] The final `Validate PraxFlow` CI gate is green on the release commit.
- [ ] README and `README.zh-CN.md` describe the same public surface.
- [ ] `CHANGELOG.md` contains the release changes and known limitations.
- [ ] Each changed Core Workflow/Skill is linked to an observed failure mode, eval, or concrete engineering rationale.
- [ ] Client compatibility claims have been checked against current vendor documentation.
- [ ] Security-sensitive changes have been reviewed.
- [ ] At least one representative end-to-end scenario exercises the release when Core behavior materially changed.

Because `gh skill publish` is currently a preview feature, use `gh skill publish --dry-run` as an additional release validation when the available GitHub CLI version supports it; do not make preview-only behavior the sole release gate.

## Distribution invariants

A release must preserve these invariants:

1. `skills/` is the only canonical installable source root.
2. Each immediate child of `skills/` is a self-contained Agent Skills package whose directory matches its `name`.
3. PraxFlow conceptual type is carried by `metadata.praxflow-type`, not path depth.
4. `skills.sh.json` is presentation metadata only; deleting it must not make the packages undiscoverable.
5. Client-specific or managed plugin bundles, when added, are derived distribution layers rather than duplicate methodology sources.

## Alpha release criterion

The first `v0.1.0-alpha.1` should not be cut merely because the repository structure exists.

Recommended minimum evidence:

1. one real `develop-feature` run;
2. one real `fix-bug` run;
3. one unfamiliar-project understanding run;
4. one real change review;
5. at least one embedded-domain run that uses authoritative references and environment verification;
6. documented failures or limitations discovered during those runs.

## Release notes

Release notes should answer:

- what changed in agent behavior?
- what problem motivated the change?
- which packages changed?
- what evidence supports the change?
- what remains experimental?
- are there installation or compatibility changes?

Avoid release notes that are only a commit list.

## After release

After publishing:

- link the release from `CHANGELOG.md`;
- verify the release archive contains the expected `skills/*` packages;
- test installation from the tagged release through at least one standards-compatible external installer;
- test the built-in installer from the tagged checkout;
- verify a specific skill can be previewed/selected by name where the client supports that capability;
- keep newly discovered regressions visible in Issues / eval records.
