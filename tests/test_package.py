import json
import unittest
from pathlib import Path

from scripts import mcp_server, runtime

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_plugin_manifest_and_local_mcp_point_to_packaged_files(self):
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        mcp = json.loads((ROOT / "mcp.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "codex-seo")
        self.assertEqual(manifest["version"], "0.3.0")
        self.assertTrue(manifest["extensions"]["com.openai"]["requires_local_executor"])
        server = mcp["mcpServers"]["codex-seo-local"]
        self.assertEqual(server["type"], "stdio")
        self.assertTrue((ROOT / "scripts" / "mcp_server.py").is_file())

    def test_every_exposed_script_is_bundled_and_allowed_by_runtime(self):
        for script in mcp_server.SAFE_SCRIPTS:
            with self.subTest(script=script):
                self.assertIn(script, runtime.ALLOWED_CORE_SCRIPTS)
                self.assertTrue((ROOT / "scripts" / script).is_file())

    def test_all_specialist_role_cards_are_packaged_with_the_audit_skill(self):
        cards = list((ROOT / "skills" / "seo-audit" / "references" / "specialists").glob("*.md"))
        self.assertEqual(len(cards), 19)


if __name__ == "__main__":
    unittest.main()
