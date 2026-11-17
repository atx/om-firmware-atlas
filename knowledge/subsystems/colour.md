---
schema_version: 1
id: guide.subsystems.colour
title: Colour, profiles and persistence
summary: Find existing colour work and separate preview, saved output and settings persistence.
load_when: [investigating HSL or film looks, choosing a colour-research home]
topics: [colour, capture]
camera_ids: []
project_ids: [project.caduceus-ep7, project.caduceus-om3, project.caduceus-om5, project.oly-fw-analysis]
depends_on: []
source_refs: [source.ep7.readme, source.om3.readme, source.om5.readme, source.fishcu.readme, source.db.release041]
last_reviewed: '2026-11-17'
---
# Several layers of colour work

The reviewed projects cover HSL, profiles, tone, effects and storing looks. Their feature sets and implementation homes differ. Begin at the camera's project list rather than assuming that a feature in one Caduceus port exists in another.

Live preview, saved JPEG output, movie output and persistence across switching profiles or powering off are separate behaviours. A report that shows a UI control does not establish every downstream effect. Use a separate scoped observation when a test checks one of these paths.

For detailed mechanisms use the original project: [PEN-F research](../../views/projects/oly-fw-analysis.md), [E-P7](../../views/projects/caduceus-ep7.md), [OM-3](../../views/projects/caduceus-om3.md), or [OM-5 generations](../../views/projects/caduceus-om5.md). The [db firmware release](../../views/sources/db.release041.md) is a further research source, with release-level claims and caveats. The Atlas's initial feature entries are starting points, not an exhaustive matrix.
