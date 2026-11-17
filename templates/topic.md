# Topic metadata template

Create a subject file only for a durable topic. Replace example values with existing IDs or deliberately add the required taxonomy/records. This fenced template is not an active guide.

```yaml
---
schema_version: 1
id: guide.domain.specific-topic
title: A concrete topic
summary: Why a reader would open it.
load_when: [a particular task]
topics: [an-existing-topic]
camera_ids: []
project_ids: []
depends_on: []
source_refs: [source.existing-source]
last_reviewed: YYYY-MM-DD
---
```

Explain the useful delta, exact scope and practical implications. Link canonical records for changing status and the detailed upstream sections. Keep dependencies shallow and avoid repeating their content.
