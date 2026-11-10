import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import runtime


class RuntimeCodexTests(unittest.TestCase):
    def test_codex_plugin_manifest_is_detected_as_plugin(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".codex-plugin").mkdir()
            (root / ".codex-plugin" / "plugin.json").write_text("{}", encoding="utf-8")
            self.assertTrue(runtime._is_plugin(root))

    def test_plugin_data_environment_variable_is_used(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / "plugin-data"
            with patch.dict(os.environ, {"PLUGIN_DATA": str(data)}, clear=False):
                os.environ.pop("CODEX_PLUGIN_DATA", None)
                os.environ.pop("CLAUDE_PLUGIN_DATA", None)
                os.environ.pop("CODEX_SEO_DATA_DIR", None)
                os.environ.pop("CLAUDE_SEO_DATA_DIR", None)
                actual, mode = runtime._data_dir(Path(directory))
            self.assertEqual(actual, data.resolve())
            self.assertEqual(mode, "plugin")


if __name__ == "__main__":
    unittest.main()
