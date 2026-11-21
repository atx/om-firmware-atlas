# Choose a job

Read only the selected role, any workflow and relevant route shards; routes list each file's size first.

| Job | Role | Workflow / next route |
|---|---|---|
| Find a camera or plan research | [Researcher](roles/researcher.md) | [Cameras](routes/cameras/index.md), then the model/task |
| Add a source or reference fact | [Librarian](roles/librarian.md) | [Ingest](workflows/ingest-source.md), then project/topic routes or [reference policy](../maintenance/reference-policy.md) |
| Update test results or status | [Librarian](roles/librarian.md) | [Status](workflows/update-status.md), then the exact camera/project |
| Refresh sources or add a release | [Librarian](roles/librarian.md) | [Freshness](workflows/review-freshness.md) |
| Explain or improve a human page | [Editor](roles/editor.md) | Relevant [topic](routes/topics/index.md) and records |
| Find discussion spaces | [Researcher](roles/researcher.md) | [Community route](routes/topics/community.md) |

Optional CLI: `python scripts/atlas.py route --job research --camera om5-ii --topic emulation` (intake: `--job ingest --source URL`) prints a reading plan, not an answer. Without it, follow the Markdown routes. [Project routes](routes/projects/index.md) list source shards and contribution homes.
