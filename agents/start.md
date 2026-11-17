# Choose a job

Read only the selected role, workflow when needed, and relevant route shards. Files list bytes and approximate tokens before you open their targets.

| Job | Role | Workflow / next route |
|---|---|---|
| Find a camera or plan research | [Researcher](roles/researcher.md) | [Cameras](routes/cameras/index.md), then the model/task |
| Add a source URL | [Librarian](roles/librarian.md) | [Ingest](workflows/ingest-source.md), then project/topic routes |
| Update test results or status | [Librarian](roles/librarian.md) | [Status](workflows/update-status.md), then the exact camera/project |
| Refresh sources | [Librarian](roles/librarian.md) | [Freshness](workflows/review-freshness.md) |
| Explain or improve a human page | [Editor](roles/editor.md) | Relevant [topic](routes/topics/index.md) and records |
| Find discussion spaces | [Researcher](roles/researcher.md) | [Community route](routes/topics/community.md) |

Optional CLI: `python scripts/atlas.py route --job research --camera om5-ii --topic emulation`. For intake, use `--job ingest --source URL`. It prints a reading plan, not an answer or an automatic change. Without dependencies, follow the Markdown routes directly. [Project routes](routes/projects/index.md) expose source shards and contribution homes.
