# Start from an existing record

Use [the record guide](../maintenance/record-format.md) and [schemas](../schemas/records.schema.json). Copy the smallest relevant canonical row, choose a new stable ID only when needed, and replace every fact and source deliberately. Do not infer compatibility from the example.

| Contribution | Useful example |
|---|---|
| Model/project discovery | [Camera record](../records/cameras/em10-iv.yaml), [project record](../records/projects/caduceus-ep7.yaml) |
| New source | [Pinned repository sources](../records/sources/om3.yaml), [mutable release source](../records/sources/db.yaml) |
| Test or result | [Partial physical and emulator reports](../records/evidence/caduceus-om5.yaml) |
| Scoped feature | [An assertion with incomplete evidence](../records/capabilities/om5-ii/om5-ii-alpha12-overall.yaml) |
| Community venue | [Venue records](../records/community/venues.yaml) |
| Subject explanation | [Topic metadata template](topic.md) |

Unknown is a valid value where the schema permits null. The PR template records sources, changed assertions and rendered human output. Regenerate views rather than copying the example's generated page.
