# Example: Project Capabilities for an Embedded Repository

This file demonstrates the kind of environment-specific knowledge that belongs to a **consuming project**, not PraxFlow Core or the embedded Domain Pack.

It is illustrative only. Replace every command/path with the real project's supported workflow.

## Build

Purpose: compile/link the firmware using the project's supported configuration.

```bash
scons -j8
```

Success evidence:

- command exits successfully;
- expected firmware artifact exists;
- no linker overflow or generated-code failure is hidden.

## Focused test

Purpose: run host-side protocol/parser tests when the changed behavior is covered there.

```bash
python3 -m pytest tests/protocol
```

## Flash / download

Purpose: program the current development target.

```text
Use the project's approved flash tool/IDE command here.
```

Safety notes should live beside the capability when relevant, for example:

- target must be externally powered;
- do not erase calibration partition;
- bootloader region is protected;
- physical operator approval required for production units.

## Serial observation

Purpose: observe runtime logs/status from the development target.

```text
port: project-specific
baud: project-specific
```

Do not commit credentials, private network addresses, or personal machine device names if the repository is shared.

## Device test

Purpose: verify the externally observable behavior that the feature/fix claims to change.

Example contract:

```text
Given: target is booted and CAN peer is available
When: test frame sequence X is sent
Then: expected frames Y are observed and error counters remain within the accepted range
```

The exact command/tool can be a project-specific Skill, script, test harness, debugger procedure, or documented manual step.

## Why this is outside PraxFlow Core

PraxFlow Core defines reasoning such as:

```text
The changed driver behavior depends on real interrupt/DMA/device state.
Therefore target verification is stronger relevant evidence than static review alone.
```

The consuming project defines:

```text
How to build this firmware.
How to flash this board.
How to read this target.
How to execute the accepted device test safely.
```

This separation keeps methodology portable while allowing real environments to remain specific, auditable, and secure.
