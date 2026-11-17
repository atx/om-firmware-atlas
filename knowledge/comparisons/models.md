---
schema_version: 1
id: guide.comparisons.models
title: Reason across models without inventing compatibility
summary: Use shared code as a research lead while retaining model, build and method boundaries.
load_when: [planning a port, comparing firmware families]
topics: [platform]
camera_ids: []
project_ids: [project.caduceus-ep7, project.caduceus-om5, project.om-emu]
depends_on: [guide.platform.identity]
source_refs: [source.ep7.bodies, source.emu.cores, source.om5.readme]
last_reviewed: '2026-11-17'
---
# Similarity is a set of observations

A shared container, processor family, matching instruction sequence, common UI subsystem and compatible physical device are different kinds of similarity. Do not collapse them into a single port score.

The E-P7 [body survey](../../views/sources/ep7.bodies.md) reports signature matches under its particular method and revision, while retaining missing screens/hooks and camera-testing gaps. Those percentages do not measure how safe or complete a port is.

The original OM-5 and Mark II have separate identities and projects can take different approaches to them. Follow the exact [camera record](../../views/cameras/index.md), not the broad “OM-5” family label. Processor-role observations are also model-specific; the [OM-1 analysis](../../views/sources/emu.cores.md) is not a universal hardware specification.
