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

    def test_markdown_renders_tables_links_and_quotes(self):
        rendered = markdown(
            "| Check | Source |\n| --- | --- |\n| Page | [Example](https://example.com) |\n\n> Evidence first."
        )
        self.assertIn("<table>", rendered)
        self.assertIn('<a href="https://example.com" target="_blank" rel="noopener noreferrer">Example</a>', rendered)
        self.assertIn("<blockquote><p>Evidence first.</p></blockquote>", rendered)

    def test_skill_links_resolve_to_pages_or_source(self):
        rendered = markdown(
            "[Capabilities](../../docs/CAPABILITY-MAP.md) [Reference](references/guide.md)",
            "seo-audit",
        )
        self.assertIn('href="/codex-seo/CAPABILITY-MAP.md"', rendered)
        self.assertIn("github.com/CaduR/codex-seo/blob/main/skills/seo-audit/references/guide.md", rendered)

    def test_markdown_keeps_github_pages_subpath_links(self):
        rendered = markdown("[Skills](/codex-seo/skills/)")
        self.assertIn('href="/codex-seo/skills/"', rendered)
        self.assertNotIn("/codex-seo/codex-seo/", rendered)

    def test_catalog_builds_index_and_one_detail_page_per_skill(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        pages = sorted((ROOT / "docs" / "skills").glob("*/index.html"))
        self.assertEqual(len(skills), 26)
        self.assertEqual(len(pages), len(skills))
        self.assertTrue((ROOT / "docs" / "index.html").is_file())
        self.assertTrue(all("Codex SEO" in page.read_text(encoding="utf-8") for page in pages))
        flow_page = (ROOT / "docs" / "skills" / "seo-flow" / "index.html").read_text(encoding="utf-8")
        self.assertIn("<table>", flow_page)
        self.assertIn("<strong>Industry vertical</strong>", flow_page)

    def test_site_builds_install_speed_skills_and_blog_routes(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        for route in ("install", "speed-report", "skills", "blog"):
            with self.subTest(route=route):
                self.assertTrue((ROOT / "docs" / route / "index.html").is_file())
        posts = list((ROOT / "docs" / "blog").glob("*/index.html"))
        self.assertGreaterEqual(len(posts), 3)

    def test_install_page_is_written_in_portuguese(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        install = (ROOT / "docs" / "install" / "index.html").read_text(encoding="utf-8")
        self.assertIn("Requisitos", install)
        self.assertIn("abra <strong>Plugins</strong>", install)
        self.assertNotIn("Requirements", install)

    def test_skill_details_explain_readiness_costs_and_related_workflows(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        audit_page = (ROOT / "docs" / "skills" / "seo-audit" / "index.html").read_text(encoding="utf-8")
        for section in ("PRÉVIA DO WORKFLOW", "O QUE VOCÊ INFORMA", "DADOS E CUSTOS", "Workflows relacionados"):
            with self.subTest(section=section):
                self.assertIn(section, audit_page)
        self.assertIn("/codex-seo/install/", audit_page)

    def test_speed_report_links_live_site_test_without_fabricated_score(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        report = (ROOT / "docs" / "speed-report" / "index.html").read_text(encoding="utf-8")
        self.assertIn("pagespeed.web.dev/analysis?url=https%3A%2F%2Fcadur.github.io%2Fcodex-seo%2F", report)
        self.assertIn("Ainda não publicamos uma medição", report)
        self.assertNotIn("Performance 99", report)
        self.assertNotIn("score 99/100", report)

    def test_home_navigation_exposes_all_main_pages(self):
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py")], cwd=ROOT, check=True)
        home = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        for href in ("/codex-seo/skills/", "/codex-seo/install/", "/codex-seo/speed-report/", "/codex-seo/blog/"):
            with self.subTest(href=href):
                self.assertIn(href, home)


if __name__ == "__main__":
    unittest.main()
