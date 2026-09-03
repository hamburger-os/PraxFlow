# Embedded Review Policy

Apply these dimensions in addition to the Core `review-change` Workflow. Use only the checks relevant to the changed code and hardware path; do not dump this list into every review.

## Concurrency and execution context

Check where code executes and whether that context permits the operations used:

- ISR versus thread/task/process context;
- shared data races;
- lock ordering and deadlock;
- blocking calls from interrupt or realtime-sensitive context;
- atomicity and visibility assumptions;
- callbacks crossing ownership/lifetime boundaries;
- scheduler or priority-inversion effects.

Do not assume an API is ISR-safe, thread-safe, or blocking-safe without applicable evidence.

## Memory and lifetime

Check:

- bounds and buffer lengths;
- stack use and large local allocations;
- heap allocation policy where constrained;
- use-after-free/double free/leaks;
- ownership transfer;
- alignment and packing;
- DMA buffer lifetime;
- signed/unsigned conversion and integer overflow;
- aliasing/undefined behavior relevant to C/C++.

## DMA, cache, and memory ordering

When DMA or shared memory is involved, inspect:

- cache clean/invalidate requirements;
- coherency assumptions;
- buffer ownership while DMA is active;
- descriptor/data ordering;
- memory barriers/volatile semantics where hardware requires them;
- alignment/region constraints.

`volatile` is not a substitute for synchronization or cache maintenance.

## Register and hardware access

Check consequential register/bit values against applicable references rather than model memory.

Review:

- reset/default-state assumptions;
- read-modify-write hazards;
- write-one-to-clear / side-effect reads;
- reserved bits;
- required delays or sequencing;
- peripheral clock/reset dependencies;
- silicon revision/Errata effects.

## Protocol and binary compatibility

Check:

- field sizes/order;
- endian;
- packing/alignment;
- CRC/checksum rules;
- timeout/retry semantics;
- sequence/state rules;
- ABI or wire-format compatibility;
- CAN/SPI/UART/etc. timing or frame assumptions where relevant.

## Reliability and failure paths

Review behavior under:

- timeout;
- partial transfer;
- bus/device unavailable;
- reset/restart;
- repeated retry;
- queue full / buffer exhausted;
- watchdog interaction;
- error-state recovery;
- resource release after failed initialization.

Do not accept an error path that merely logs and leaves hardware/software state inconsistent.

## Realtime/resource constraints

Check whether the change alters:

- worst-case blocking time;
- interrupt latency;
- polling frequency;
- CPU load;
- memory use;
- queue depth;
- startup time;
- watchdog margin;
- bus bandwidth.

Escalate only when the effect is plausible and material to the system constraints.

## Review evidence standard

For an important embedded finding, identify:

- changed code/path;
- execution/hardware condition needed for the issue;
- applicable reference or observed behavior when external facts are involved;
- impact on the target system.

Attempt to falsify the finding by checking guards, context, revision applicability, and real project behavior before reporting it as Blocker/Major.
