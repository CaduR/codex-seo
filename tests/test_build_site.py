import subprocess
import sys
import unittest
from pathlib import Path

from scripts.build_site import markdown

ROOT = Path(__file__).resolve().parents[1]


class SiteBuildTests(unittest.TestCase):
    def test_markdown_formats_inline_tokens_and_escapes_html(self):
        self.assertEqual(
            markdown("`code` **bold** *emphasis* <script>"),
            "<p><code>code</code> <strong>bold</strong> <em>emphasis</em> &lt;script&gt;</p>",
        )

    def test_catalog_builds_index_and_one_detail_page_per_skill(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        pages = sorted((ROOT / "docs" / "skills").glob("*/index.html"))
        self.assertEqual(len(skills), 26)
        self.assertEqual(len(pages), len(skills))
        self.assertTrue((ROOT / "docs" / "index.html").is_file())
        self.assertTrue(all("Codex SEO" in page.read_text(encoding="utf-8") for page in pages))
        self.assertIn("<strong>Find:</strong>", (ROOT / "docs" / "skills" / "seo-flow" / "index.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
