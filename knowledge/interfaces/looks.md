---
schema_version: 1
id: guide.interfaces.looks
title: Looks and interoperability
summary: Separate shared colour settings from card wrappers, sharing schemes and export targets.
load_when: [moving looks between bodies, adding an exporter, comparing look editors]
topics: [interfaces]
camera_ids: [camera.om3, camera.om5-ii, camera.ep7]
project_ids: [project.caduceus-om3, project.caduceus-om5, project.caduceus-ep7]
depends_on: []
source_refs: [source.om3.formats, source.om5.formats, source.om3.looklab, source.ep7.panel, source.ep7.look-v4]
last_reviewed: '2026-11-17'
---
# A common filename is not a common interface

OM-3 uses an OM3P card wrapper; OM-5 Mark II uses OM5F around a subset of related record fields. Their counts, naming layouts and validation differ. Use the [OM-3 format](../../views/sources/om3.formats.md) and [OM-5 format](../../views/sources/om5.formats.md) for exact details. Do not copy LOOKS.BIN across bodies based on its name.

Also distinguish card binaries from editable look/pack JSON and sharing codes. The [OM-3 LookLab](../../views/sources/om3.looklab.md) documents its own current schema and sharing interfaces. The E-P7 [panel direction](../../views/sources/ep7.panel.md) proposes a shared look model with camera-specific exporters. Its [new-field proposal](../../views/sources/ep7.look-v4.md) discusses additional settings and older consumers.

Record implemented producers/consumers, minimum mod release and fields that an export drops or clamps. A maintainer's consolidation direction is useful but is not proof that every other project has adopted it. Propose changes to an existing interface owner after checking current consumers and policy.
