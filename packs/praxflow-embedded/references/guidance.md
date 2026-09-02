# Embedded Reasoning Guidance

These are recurring reasoning guardrails for embedded work. They are not a universal checklist and should be applied only when relevant.

## Hardware facts are externally constrained

Registers, bit fields, electrical limits, reset behavior, protocol timing, and silicon defects are facts about a specific external system. They are not safely invented from general coding patterns.

Use applicable authoritative references and keep revision/version assumptions visible.

## Execution context is part of correctness

A function that is correct in a thread may be invalid in an ISR or realtime-critical path.

When context matters, establish:

- who calls it;
- on which thread/process/interrupt level;
- whether it may block;
- whether shared state is accessed;
- which APIs are legal in that context.

## Resource lifetime crosses software and hardware

DMA, peripherals, interrupts, callbacks, and shared buffers often outlive the lexical scope that configured them.

Trace ownership through:

```text
configure -> start -> active use -> interrupt/callback -> stop -> release/reset
```

Do not treat “function returned” as evidence that hardware no longer uses a resource.

## State machines deserve explicit reasoning

For drivers and protocols, list meaningful states/transitions when behavior depends on sequencing.

Check:

- valid transition source/target;
- events that trigger transitions;
- timeout/error transitions;
- reset/recovery path;
- whether external hardware state and software state can diverge.

## Reference implementation is not a transplant

When adapting Linux/vendor/other-RTOS code:

1. identify the hardware/protocol invariant it is satisfying;
2. identify platform-specific mechanisms it uses;
3. map the invariant into the current project's abstractions;
4. preserve project ownership/error/build conventions unless there is a causal reason not to.

Do not cargo-cult APIs, locking, workqueues, allocation models, or device-framework assumptions across platforms.

## Real target evidence matters when the claim crosses the boundary

Use real hardware/device evidence when correctness depends on conditions that static code cannot establish, such as:

- bus timing;
- interrupt delivery/order;
- peripheral state;
- cache/DMA interaction;
- board wiring/pins/clocks;
- real peer-device behavior.

This does not mean every code change needs hardware testing. Match the evidence to the claim.

## Project-specific mechanics remain project-owned

Do not encode in this pack:

- board IP addresses;
- serial device names;
- flash commands;
- credentials;
- proprietary build paths;
- internal artifact servers;
- specific target aliases.

Capture those as project capabilities in the consuming repository.
