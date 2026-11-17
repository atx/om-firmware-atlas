"""Identity gates test complete history, overrides and the actual credential principal."""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_identity as identity


class IdentityTests(unittest.TestCase):
    def setUp(self):
        self.policy = identity.policy(ROOT)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, env=self.env)

    def commit(self, author="xulfr", committer="xulfr", author_email=None):
        mail = self.policy["authors"][0]["email"]
        env = dict(self.env, GIT_AUTHOR_NAME=author, GIT_AUTHOR_EMAIL=author_email or mail,
                   GIT_COMMITTER_NAME=committer, GIT_COMMITTER_EMAIL=mail)
        subprocess.run(["git", "-c", "commit.gpgsign=false", "commit", "--allow-empty", "-qm", "Synthetic identity fixture"],
                       cwd=self.root, env=env, check=True, capture_output=True)

    def test_approved_root_passes(self):
        self.commit()
        self.assertEqual(identity.audit(self.policy, ["HEAD"], self.root), 1)

    def test_unapproved_author_is_blocked(self):
        self.commit(author="Unapproved Synthetic Author")
        with self.assertRaisesRegex(identity.IdentityError, "unapproved author"):
            identity.audit(self.policy, ["HEAD"], self.root)

    def test_unapproved_committer_is_blocked(self):
        self.commit(committer="Unapproved Synthetic Committer")
        with self.assertRaisesRegex(identity.IdentityError, "unapproved committer"):
            identity.audit(self.policy, ["HEAD"], self.root)

    def test_private_email_is_blocked_even_with_correct_name(self):
        self.commit(author_email="synthetic-private@example.invalid")
        with self.assertRaisesRegex(identity.IdentityError, "unapproved author"):
            identity.audit(self.policy, ["HEAD"], self.root)

    def test_good_tip_does_not_hide_bad_ancestor(self):
        self.commit(author="Unapproved Synthetic Author")
        self.commit()
        with self.assertRaises(identity.IdentityError):
            identity.audit(self.policy, ["HEAD"], self.root)

    def test_wrong_authenticated_login_or_id_is_blocked(self):
        valid = dict(login="xulfr", id=self.policy["push_user_id"])
        identity.validate_account(self.policy, valid)
        for invalid in (dict(valid, login="unapproved-synthetic-login"), dict(valid, id=1)):
            with self.assertRaisesRegex(identity.IdentityError, "actual Git push credential"):
                identity.validate_account(self.policy, invalid)

    def test_diagnostics_do_not_repeat_rejected_identity(self):
        name = "Unapproved Synthetic Author"
        self.commit(author=name)
        with self.assertRaises(identity.IdentityError) as error:
            identity.audit(self.policy, ["HEAD"], self.root)
        self.assertNotIn(name, str(error.exception))


if __name__ == "__main__":
    unittest.main()
