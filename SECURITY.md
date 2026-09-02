# Security Policy

PraxFlow primarily distributes methodology, Markdown-based Agent Skills, and small installation/validation scripts. Security reports are still welcome, especially when they involve installer behavior, path handling, unsafe execution guidance, prompt/package supply-chain risks, or instructions that could cause unintended destructive actions.

## Supported versions

PraxFlow is currently pre-1.0. Security fixes are applied to the latest `main` branch and the most recent published pre-release when practical.

## Reporting a vulnerability

**Do not publish vulnerability details in a public issue.**

Preferred channel:

1. Open the repository's **Security** tab.
2. Use **Report a vulnerability** / private vulnerability reporting when available.
3. Include the affected file/package, impact, reproduction steps, and any proposed mitigation.

If private vulnerability reporting is not yet available, open a public issue titled **Security contact request** **without vulnerability details**. A maintainer can then establish a private channel before technical details are shared.

## What to include

A useful report contains:

- affected PraxFlow version or commit;
- affected package/script/path;
- realistic impact;
- minimal reproduction or proof of concept when safe;
- environmental assumptions;
- suggested mitigation, if known.

## Scope notes

Project-specific commands installed alongside PraxFlow remain owned by the consuming project. Reports about a project's credentials, infrastructure, or private deployment should be sent to that project's security channel rather than disclosed here.

We will distinguish between:

- a confirmed vulnerability;
- unsafe methodology or guardrail behavior;
- a downstream project configuration issue;
- a client/platform vulnerability outside PraxFlow's control.

Please preserve this distinction in reports when possible.
