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

## Release gate

Before a tagged release:

- [ ] `python3 scripts/validate.py` passes.
- [ ] Installer smoke tests pass in CI.
- [ ] README and `README.zh-CN.md` describe the same public surface.
- [ ] `CHANGELOG.md` contains the release changes and known limitations.
- [ ] Each changed Core Workflow/Skill is linked to an observed failure mode, eval, or concrete engineering rationale.
- [ ] Client compatibility claims have been checked against current vendor documentation.
- [ ] Security-sensitive changes have been reviewed.
- [ ] At least one representative end-to-end scenario exercises the release when Core behavior materially changed.

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
- verify the release archive contains expected packages;
- test installation from the tagged checkout;
- keep newly discovered regressions visible in Issues / eval records.
