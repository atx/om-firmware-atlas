# Review freshness

Start from the open `atlas-update-queue` issue, or run `python scripts/atlas.py freshness --fetch` then `queue` for `.build/update-queue.md`; network access is required. It compares pinned GitHub revisions/releases, each project's newest release and other URLs without running source code.

For a new release, read its notes and add it to the project's `releases` (newest first) and `features` where it adds or changes one, citing a release source. Keep the project's own status words and warnings; test claims stay attributed.

If the GitHub API is unreachable (every GitHub source `check-failed`), compare instead with `git ls-remote` and release pages; report that fallback in the PR. A repository is current when its HEAD is among the pinned revisions; a source tracking a branch or PR compares with that ref, not the default branch. Release-only repositories (every tag on one commit) need their release pages read. Test versions on side branches often carry their notes in the repository; pin those to the tag commit.

Read only changed/overdue source shards. A changed upstream revision queues review; it does not alter a capability. A failed fetch retains the source record and is reported as a failed check. Follow the ingestion workflow for a substantive update.

Update `last_reviewed` only after reviewing facts; link checking alone does not renew it. Historical observations retain their event/report dates. When a maintainer reverses a stated status (an inactive project resumes, a known issue is fixed), treat it as correcting: update the current state and keep the earlier statement as a historical source. Never convert a scheduled job into automatic claim promotion or merging.
