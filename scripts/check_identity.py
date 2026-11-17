"""Fail closed on unapproved commit metadata and push credentials. Standard library only."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


class IdentityError(Exception):
    pass


def git(*args, root=ROOT, env=None, input=None):
    result = subprocess.run(["git", *args], cwd=root, env=env, input=input,
                            text=True, capture_output=True)
    if result.returncode:
        raise IdentityError("Git identity inspection failed; stop before committing or pushing.")
    return result.stdout.strip()


def policy(root=ROOT):
    return json.loads((root / "maintenance/git-identity.json").read_text(encoding="utf-8"))


def approved(name, email, entries):
    return any(name == item["name"] and email == item["email"] for item in entries)


def effective(config, root=ROOT):
    for variable, key in (("GIT_AUTHOR_IDENT", "authors"), ("GIT_COMMITTER_IDENT", "committers")):
        value = git("var", variable, root=root)
        match = re.match(r"^(.*?) <([^<>]+)> ", value)
        if not match or not approved(match[1], match[2], config[key]):
            raise IdentityError(f"Effective {key[:-1]} identity is not approved. Run python scripts/check_identity.py setup; never rely on inherited identity.")


def audit(config, refs, root=ROOT):
    if not refs:
        raise IdentityError("No commit supplied for metadata audit.")
    text = git("log", "--no-show-signature", "--format=%H%x00%an%x00%ae%x00%cn%x00%ce", *refs, "--", root=root)
    count = 0
    for line in text.splitlines():
        parts = line.split("\0")
        if len(parts) != 5:
            raise IdentityError("Unexpected commit metadata; publication stopped.")
        sha, author, author_email, committer, committer_email = parts
        if not approved(author, author_email, config["authors"]):
            raise IdentityError(f"Commit {sha[:7]} has an unapproved author identity; do not publish this history.")
        if not approved(committer, committer_email, config["committers"]):
            raise IdentityError(f"Commit {sha[:7]} has an unapproved committer identity; do not publish this history.")
        count += 1
    if not count:
        raise IdentityError("No commits were audited; publication stopped.")
    return count


def validate_account(config, account):
    if account.get("login") != config["push_login"] or account.get("id") != config["push_user_id"]:
        raise IdentityError("The actual Git push credential is not the approved account. Stop and authenticate as the repository's approved public account.")


def authenticate(config, root=ROOT, require_workflow=False):
    remote = git("remote", "get-url", "--push", "origin", root=root)
    parsed = urlparse(remote)
    if parsed.scheme != "https" or parsed.hostname != "github.com" or parsed.password or parsed.path.strip("/").removesuffix(".git") != config["repository"] or parsed.username not in (None, config["push_login"]):
        raise IdentityError("Push destination does not match the approved HTTPS repository/account.")
    request = f"protocol=https\nhost=github.com\npath={config['repository']}.git\nusername={config['push_login']}\n\n"
    environment = dict(os.environ, GIT_TERMINAL_PROMPT="0", GH_PROMPT_DISABLED="1", GCM_INTERACTIVE="Never")
    # Capture helper output in memory; never print, save or interpolate credentials into a command.
    result = subprocess.run(["git", "credential", "fill"], cwd=root, input=request,
                            capture_output=True, text=True, env=environment)
    fields = dict(line.split("=", 1) for line in result.stdout.splitlines() if "=" in line)
    token = fields.get("password")
    if result.returncode or not token:
        raise IdentityError("Approved push credentials are unavailable; complete browser authentication as xulfr.")
    api_request = urllib.request.Request("https://api.github.com/user", headers={
        "Authorization": "Bearer " + token,
        "User-Agent": "OM-Firmware-Atlas-identity-check/1",
        "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(api_request, timeout=15) as response:
            account = json.load(response)
            scopes = set(response.headers.get("X-OAuth-Scopes", "").replace(" ", "").split(","))
    except Exception:
        raise IdentityError("Could not verify the actual push credential with GitHub; publication stopped.") from None
    validate_account(config, account)
    if require_workflow and "workflow" not in scopes:
        raise IdentityError("The verified xulfr credential needs workflow scope. Complete gh auth refresh --hostname github.com --scopes workflow as xulfr.")
    return account["login"]


def setup(config, root=ROOT):
    identity = config["authors"][0]
    for key, value in (("user.name", identity["name"]), ("user.email", identity["email"]),
                       ("user.useConfigOnly", "true"), ("core.hooksPath", ".githooks"),
                       ("credential.helper", ""), ("credential.https://github.com.username", config["push_login"])):
        git("config", "--local", "--replace-all", key, value, root=root)
    git("config", "--local", "--add", "credential.helper", "!gh auth git-credential", root=root)
    git("remote", "set-url", "origin", f"https://{config['push_login']}@github.com/{config['repository']}.git", root=root)
    effective(config, root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("setup", "effective", "audit", "auth", "pre-commit", "pre-push"))
    parser.add_argument("refs", nargs="*")
    parser.add_argument("--require-workflow", action="store_true")
    args = parser.parse_args()
    config = policy()
    try:
        if args.mode == "setup":
            setup(config)
            print("Repository-local identity and hooks configured for xulfr; global settings untouched.")
        elif args.mode in ("effective", "pre-commit"):
            effective(config)
            print("Effective author and committer match the approved public identity.")
        elif args.mode == "auth":
            print("Verified actual Git push account:", authenticate(config, require_workflow=args.require_workflow))
        elif args.mode == "audit":
            print(f"Approved author/committer metadata in all {audit(config, args.refs or ['HEAD'])} reachable commits.")
        else:
            if args.refs and args.refs[0] != "origin":
                raise IdentityError("Automatic pushes are restricted to the approved origin.")
            refs = []
            for line in sys.stdin:
                parts = line.split()
                if len(parts) != 4 or parts[1] == "0" * 40:
                    raise IdentityError("Malformed or deletion push; not authorised by this identity guard.")
                refs.append(parts[1])
            count = audit(config, refs)
            login = authenticate(config)
            print(f"Push guard passed: {count} reachable commits; credential verified as {login}.")
    except IdentityError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
