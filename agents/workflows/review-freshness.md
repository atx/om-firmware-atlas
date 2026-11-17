# Review freshness

Run `python scripts/atlas.py freshness --fetch` to produce an ignored report in `.build/`; network access is required. It compares pinned GitHub revisions/releases and checks other URLs without running source code. Without `--fetch`, it reports dated review needs offline.

Read only changed/overdue source shards. A changed upstream revision queues review; it does not alter a capability. A failed fetch retains the source record and is reported as a failed check. Follow the ingestion workflow for a substantive update.

Update `last_reviewed` only after reviewing facts; link checking alone does not renew it. Historical observations retain their event/report dates. Never convert a scheduled job into automatic claim promotion or merging.
