import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillParityTests(unittest.TestCase):
    def test_domain_skills_keep_their_operational_workflows_in_codex(self):
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 26)
        for path in skills:
            if path.parent.name == "seo":
                continue
            text = path.read_text(encoding="utf-8-sig")
            body = re.split(r"\n---\s*\n", text, maxsplit=1)[-1]
            self.assertGreaterEqual(len(body), 3000, path.parent.name)
            self.assertNotIn("CLAUDE_PLUGIN_ROOT", body, path.parent.name)
            self.assertNotRegex(body, r"(?m)^\s*/seo\s", path.parent.name)

    def test_tool_examples_are_codex_mcp_calls_and_roles_are_not_agents(self):
        agentic = (ROOT / "skills" / "seo-agentic" / "SKILL.md").read_text(encoding="utf-8")
        audit = (ROOT / "skills" / "seo-audit" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("seo_analyze", agentic)
        self.assertIn("agentic_check.py", agentic)
        self.assertNotIn("``Codex", agentic)
        self.assertIn("reference cards", audit)
        self.assertIn("inline", audit)


if __name__ == "__main__":
    unittest.main()
