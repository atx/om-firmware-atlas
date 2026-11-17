---
schema_version: 1
id: guide.tooling.analysis
title: Analysis tool profiles
summary: Distinguish GNU tools, a specific Ghidra/REA setup and optional IDA configurations.
load_when: [setting up disassembly, choosing decompiler or MCP access]
topics: [tooling]
camera_ids: []
project_ids: [project.caduceus-ep7, project.oly-fw-analysis]
depends_on: [guide.platform.identity]
source_refs: [source.ep7.rea, source.fishcu.reproduce, source.fishcu.ida]
last_reviewed: '2026-11-17'
---
# Pick a documented profile

GNU MN103 binutils underpin assembly/disassembly in the reviewed projects. Begin with the target project's pinned toolchain and exact input. The [reproduction guide](../../views/sources/fishcu.reproduce.md) distinguishes input-free checks from firmware-dependent native probes.

For agent-accessible decompilation, the E-P7 [REA setup](../../views/sources/ep7.rea.md) documents Ghidra, an MN103 module, local fixes, project seeding and an MCP wrapper. This is a specific environment, not a generic promise that installing REA enables MN103. Its decompiler has ABI and coverage limitations, and its displayed assembly has a documented operand-syntax weakness. Check exact instructions with the stated independent disassembler.

The [IDA profile](../../views/sources/fishcu.ida.md) documents a tested historical combination. The REA guide describes different availability/requirements. Keep those configurations attributed rather than declaring a universal IDA requirement. Installation steps and tool/module revisions remain in the pinned upstream profile.
