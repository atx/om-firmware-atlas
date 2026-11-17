# Commit and push identity

Before creating any commit or push, run:

```sh
python scripts/check_identity.py setup
python scripts/check_identity.py effective
python scripts/check_identity.py auth
```

The repository-local policy currently permits `xulfr` with `350797722+xulfr@users.noreply.github.com` as author and committer. GitHub's official web committer is also recognised. The actual push credential must authenticate to GitHub as `xulfr`, including the verified numeric user ID. Global identity and other stored accounts are not changed.

Setup installs the tracked pre-commit and pre-push hooks. The first checks effective author and committer, including environment overrides. The second audits every commit reachable from the pushed tips and verifies the credential returned by Git's own helper against GitHub. Tokens stay in memory and are never logged or stored in the repository.

After committing, run `python scripts/check_identity.py audit HEAD`. Do not bypass hooks, override these fields, push an old checkout/history, or trust an active CLI account alone. Git authentication and commit authorship are separate identities. Do not use a web editor until its selected author email is explicitly verified; browser sign-in alone does not establish no-reply commit metadata.

Other contributors' public identities require an explicit reviewed policy addition. Do not add personal names or private email addresses. CI audits the entire checked-out history as a further check, but a post-push check cannot prevent already published metadata: the local gates must run first.
