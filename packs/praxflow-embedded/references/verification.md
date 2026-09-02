# Embedded Verification Strategy

Embedded completion claims often depend on behavior outside the development host. This strategy augments the Core Verification Protocol.

## Verification is claim-specific

Do not equate “build succeeded” with “device behavior is correct.”

Choose checks based on what the change claims to establish.

Examples:

- a header-only compile fix may need only targeted build checks;
- a protocol parser may need host/unit vectors plus target integration;
- DMA/cache behavior usually requires target evidence;
- interrupt timing or electrical/bus behavior may require hardware instrumentation.

## Typical ladder

Use the relevant subset, not every step mechanically:

```text
static review / reference check
        ↓
compile / build
        ↓
host unit or simulation test
        ↓
flash / deploy to target
        ↓
target runtime observation
        ↓
interface/bus/device test
        ↓
stress / failure / recovery test
```

## Build

A build is valuable external evidence for:

- syntax/type/link correctness;
- configuration integration;
- generated files/linker constraints;
- ABI or compile-time incompatibilities.

But it does not establish runtime hardware behavior.

## Target execution

Use target execution when correctness depends on:

- peripheral state;
- real interrupt behavior;
- DMA/cache coherency;
- memory map/linker placement;
- RTOS scheduling;
- timing;
- device/board revision;
- actual driver/firmware interaction.

Observe with available capabilities such as serial logs, SSH, debugger/JTAG, counters, trace, device state, or project-specific diagnostics.

## Interface and bus evidence

When a change claims protocol/device behavior, use the strongest practical interface evidence:

- CAN/CAN FD analyzer or peer device;
- SPI/I2C/UART trace;
- protocol conformance/vector tests;
- loopback where meaningful;
- oscilloscope/logic analyzer for timing/electrical claims;
- external device response.

Do not require physical instrumentation for claims that a cheaper deterministic test already establishes.

## Failure and recovery

For reliability changes, test relevant failure conditions when safe and practical:

- timeout;
- unplug/reconnect;
- device reset;
- queue/buffer pressure;
- repeated retry;
- corrupted/invalid frame;
- startup/shutdown cycles;
- watchdog/recovery path.

Avoid destructive testing unless the user/project has explicitly accepted the risk and the environment is suitable.

## Bug fixes

Prefer:

1. reproduce/capture the original device failure when feasible;
2. verify the causal mechanism on target if the cause is hardware/context dependent;
3. verify the repaired path;
4. exercise nearby valid cases and recovery paths proportionately.

## Missing target access

If no target/device capability is available:

- perform the strongest host/static/reference checks available;
- state clearly which hardware-dependent claims remain unverified;
- provide a focused target verification procedure rather than claiming success.

Do not treat lack of target access as permission to convert inference into fact.
