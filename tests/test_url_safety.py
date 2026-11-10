import os
import unittest
from unittest.mock import patch

from scripts.url_safety import _local_targets


class LocalTargetEnvironmentTests(unittest.TestCase):
    def test_codex_environment_name_is_supported(self):
        with patch.dict(os.environ, {"CODEX_SEO_LOCAL_TARGETS": "localhost:3000"}, clear=True):
            self.assertEqual(_local_targets(), (("localhost", 3000),))

    def test_legacy_environment_name_remains_supported(self):
        with patch.dict(os.environ, {"CLAUDE_SEO_LOCAL_TARGETS": "127.0.0.1:8080"}, clear=True):
            self.assertEqual(_local_targets(), (("127.0.0.1", 8080),))

    def test_codex_environment_takes_precedence(self):
        values = {"CODEX_SEO_LOCAL_TARGETS": "localhost:3000", "CLAUDE_SEO_LOCAL_TARGETS": "127.0.0.1:8080"}
        with patch.dict(os.environ, values, clear=True):
            self.assertEqual(_local_targets(), (("localhost", 3000),))


if __name__ == "__main__":
    unittest.main()
