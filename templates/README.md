# Start from an existing record

Use [the record guide](../maintenance/record-format.md) and [schemas](../schemas/records.schema.json). Copy the smallest relevant canonical row, choose a new stable ID only when needed, and replace every fact and source deliberately. Do not infer compatibility from the example.

| Contribution | Useful example |
|---|---|
| Model/project discovery | [Camera record](../records/cameras/em10-iv.yaml), [project record](../records/projects/caduceus-ep7.yaml) |
| New source | [Pinned repository sources](../records/sources/om3.yaml), [mutable release source](../records/sources/db.yaml) |
| Test or result | [Partial physical and emulator reports](../records/evidence/caduceus-om5.yaml) |
| Scoped feature | [An assertion with incomplete evidence](../records/capabilities/om5-ii/om5-ii-alpha12-overall.yaml) |
| Project showcase and releases | [Features, releases and goals](../records/projects/om10mi-mods.yaml) |
| Camera result with a reported hash | [Owner test of a pinned build](../records/evidence/epm2mod.yaml) |
| Address, hazard or free space | [Technical reference entries](../records/reference/om5-ii-1100.yaml), with the [reference policy](../maintenance/reference-policy.md) |
| Platform fact or built-in feature | [Per-build platform entries](../records/reference/om5-ii-1100-platform.yaml) |
| Community venue | [Venue records](../records/community/venues.yaml) |
| Subject explanation | [Topic metadata template](topic.md) |

Unknown is a valid value where the schema permits null. The PR template records sources, changed assertions and rendered human output. Regenerate views rather than copying the example's generated page.
