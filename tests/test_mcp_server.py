import json
import subprocess
import sys
import unittest
from pathlib import Path

from scripts import mcp_server


class McpServerTests(unittest.TestCase):
    def test_only_read_only_scripts_are_exposed(self):
        self.assertIn("render_page.py", mcp_server.SAFE_SCRIPTS)
        self.assertNotIn("gsc_query.py", mcp_server.SAFE_SCRIPTS)
        self.assertNotIn("indexing_notify.py", mcp_server.SAFE_SCRIPTS)
        self.assertNotIn("dataforseo_merchant.py", mcp_server.SAFE_SCRIPTS)

    def test_arguments_remain_separate_process_arguments(self):
        argv = mcp_server.build_run_argv("render_page.py", ["https://example.com", "; whoami"])
        self.assertEqual(argv[-2:], ["https://example.com", "; whoami"])
        self.assertEqual(argv[1], str(Path(mcp_server.ROOT / "scripts" / "runtime.py")))

    def test_unapproved_script_is_rejected(self):
        with self.assertRaises(ValueError):
            mcp_server.build_run_argv("indexing_notify.py", ["https://example.com"])

    def test_file_and_credential_flags_are_rejected(self):
        for flag in ("--output=report.html", "--api-key=secret", "--pairs-file=C:/private.json"):
            with self.subTest(flag=flag), self.assertRaises(ValueError):
                mcp_server.build_run_argv("render_page.py", ["https://example.com", flag])

    def test_stdin_analysis_does_not_accept_a_file_path(self):
        with self.assertRaises(ValueError):
            mcp_server.build_run_argv("content_quality.py", ["C:/Users/private.txt"])

    def test_invalid_tool_arguments_return_invalid_params(self):
        reply = mcp_server.handle(
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "seo_doctor", "arguments": []}}
        )
        self.assertEqual(reply["error"]["code"], -32602)

    def test_stdio_handshake_and_tool_catalog(self):
        requests = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        ]
        result = subprocess.run(
            [sys.executable, str(Path(mcp_server.__file__))],
            input="\n".join(map(json.dumps, requests)) + "\n",
            capture_output=True,
            text=True,
            check=True,
        )
        messages = [json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual(messages[0]["result"]["serverInfo"]["name"], "codex-seo-local")
        self.assertEqual({tool["name"] for tool in messages[1]["result"]["tools"]}, {"seo_doctor", "seo_setup", "seo_analyze"})


if __name__ == "__main__":
    unittest.main()
