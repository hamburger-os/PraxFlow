---
name: praxflow-embedded
description: Embedded-systems domain pack for PraxFlow. Use alongside PraxFlow workflows/skills when working on MCU, RTOS, embedded Linux, QNX, device drivers, firmware, hardware protocols, registers, interrupts, DMA, cache, CAN/SPI/UART, or real target devices. Adds embedded evidence authority, review risks, and target-aware verification guidance without replacing project-specific build/deploy/debug skills.
license: MIT
metadata:
  praxflow-type: "pack"
  praxflow-version: "0.1"
  praxflow-domain: "embedded"
---

# PraxFlow Embedded

Apply this pack as an **augmentation** to the active PraxFlow Workflow or Skill. Do not replace the Core method and do not duplicate project-specific capabilities.

Read the relevant references as needed:

- `references/evidence.md` — evidence authority, applicability, Datasheet/Errata/standard/reference-implementation handling.
- `references/review.md` — embedded-specific review dimensions.
- `references/verification.md` — build/target/device verification strategy.
- `references/guidance.md` — recurring embedded reasoning guardrails.

## Core embedded stance

Embedded work frequently combines software inference with external physical facts. Treat the following as high-risk for unsupported guessing:

- registers and bit fields;
- initialization/reset sequences;
- silicon errata;
- interrupt-context behavior;
- DMA and cache coherency;
- memory ownership/alignment/lifetime;
- timing and realtime behavior;
- watchdog/reset behavior;
- protocol fields and wire timing;
- ABI/packing/endian assumptions;
- hardware state that is only observable on a target.

Model memory may suggest what to inspect, but it is not sufficient authority for consequential hardware/protocol facts when applicable references are available.

## Interaction with project capabilities

This pack does not define commands such as:

- build;
- flash/download;
- deploy;
- open serial;
- SSH target;
- run CAN/bus tests;
- JTAG debugger commands.

Those belong to the consuming project.

The pack instead tells the active Workflow **when and why** those capabilities provide stronger evidence.

## Human decision boundaries

Use explicit Decision Gates for consequential choices such as:

- changing a deployed protocol or persistent format;
- altering interrupt/thread ownership;
- accepting data loss or retry semantics;
- changing realtime/resource budgets;
- disabling safety/watchdog behavior;
- operations that can brick, damage, or irreversibly reconfigure hardware.

Do not ask engineers factual questions that code, schematics/project docs, or authoritative references can answer.

## Completion stance

For behavior that depends on hardware or a real target, static reasoning or a successful host build is usually incomplete evidence. Use proportionate target/device verification when the capability exists and the claim depends on real hardware behavior.
