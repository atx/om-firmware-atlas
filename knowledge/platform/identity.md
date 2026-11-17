---
schema_version: 1
id: guide.platform.identity
title: Identify the exact input and address space
summary: Separate model/version labels, byte identity and component/runtime mappings.
load_when: [identifying firmware, decoding containers, interpreting addresses]
topics: [platform]
camera_ids: []
project_ids: [project.oly-fw-analysis, project.om-emu]
depends_on: []
source_refs: [source.fishcu.containers, source.fishcu.reproduce, source.emu.container, source.emu.cores]
last_reviewed: '2026-11-17'
---
# Identify the input before using an address

An advertised version is not always a unique file identity. The [PEN-F reproduction guide](../../views/sources/fishcu.reproduce.md) specifically identifies a 3101 build and full digest. Preserve an unknown hash as unknown; do not infer it from a filename.

The examined OE containers package independent components. A container address, decoded payload offset and runtime CPU address are different coordinates. The [container reference](../../views/sources/fishcu.containers.md) explains the shared wrapper and checksum; the [OM-Emu reference](../../views/sources/emu.container.md) covers its broader input handling and acquisition method. A parser's documented scope is not universal coverage.

An address record names the camera, firmware, component/region and address space. Cached/uncached aliases and overlays need explicit mappings. Shared MN103-family code does not describe every processor in a body: see the scoped [OM-1 core analysis](../../views/sources/emu.cores.md).

Vendor download links may expire and an API may only supply the latest file. Record the acquisition method and expected identity rather than preserving a signed URL as a durable download.
