# Capability map

Codex SEO splits work between skill instructions and the local MCP server. Skills define the analysis workflow; the server runs only the scripts listed below through an isolated Python environment. A script not listed in the default MCP allowlist is not callable through the plugin's generic analysis tool.

| Skill | Local tools exposed by default | Data and limits |
|---|---|---|
| `seo` | `seo_doctor`, `seo_setup` | Routes broad requests; data access follows the selected workflow. |
| `seo-audit` | `render_page.py`, `sitemap_discovery.py`, `agentic_check.py` | One or more pages can be reviewed; a full 500-page crawler is not exposed. |
| `seo-page` | `render_page.py`, `metadata_template.py`, `content_quality.py` | Page findings require accessible page content. |
| `seo-technical` | `render_page.py`, `sitemap_discovery.py`, `agentic_check.py` | PageSpeed, CrUX, and account data require a separately authorized tool or supplied report. |
| `seo-content` | `content_quality.py`, `content_verify.py`, `metadata_template.py` | Human review is needed for claims, expertise, and factual accuracy. |
| `seo-content-brief` | None | Use supplied research or currently connected search tools; do not invent volumes or SERP data. |
| `seo-schema` | `schema_generate.py`, `schema_ecommerce_validate.py` | Validation is limited to rules in the bundled code; Google rich-result eligibility is not guaranteed. |
| `seo-sitemap` | `sitemap_discovery.py` | Reads public robots/sitemap locations. Generation and file writing are not exposed through generic MCP. |
| `seo-images` | `render_page.py` | Image analysis is limited to what the page and available visual tools expose. |
| `seo-geo` | `agentic_check.py`, `agent_ux_check.py` | AI citation/visibility claims require external evidence and are not ranking metrics. |
| `seo-agentic` | `agentic_check.py`, `agent_ux_check.py` | No Lighthouse Agentic Browsing runner is exposed by the default MCP. |
| `seo-local` | `render_page.py`, `gbp_deprecation_lint.py` | No Google Business Profile, review, or citation account is connected by default. |
| `seo-maps` | None | Map grids and current local rankings require an authorized maps/SERP provider. |
| `seo-international` | `render_page.py` | Check only supplied or accessible language versions; no translation or geo-rank provider is connected. |
| `seo-plan` | None | Recommendations are strategic hypotheses unless backed by supplied business/search data. |
| `seo-programmatic` | None | Quality and indexation risks can be reviewed from supplied templates and examples; no bulk crawler is exposed. |
| `seo-competitor-pages` | None | Competitive evidence requires user-supplied facts or connected search tools. |
| `seo-flow` | None | Workflow framework guidance only; external prompt library sync is not included in default MCP. |
| `seo-backlinks` | None | The scripts are present but not exposed through MCP; no paid backlink index is connected. |
| `seo-google` | None | Google account scripts are not in the default MCP allowlist; use only a separately authorized connection or supplied exports. |
| `seo-cluster` | None | SERP-overlap grouping requires dated search results; semantic grouping alone is labeled as a hypothesis. |
| `seo-drift` | None | No scheduled snapshot store is enabled; compare user-supplied before/after captures. |
| `seo-sxo` | `render_page.py` | Conversion and ranking outcomes must be measured by the site owner. |
| `seo-ecommerce` | `render_page.py`, `schema_ecommerce_validate.py` (user-supplied JSON via stdin) | No inventory, Merchant Center, marketplace, or pricing feed is connected. |
| `seo-dataforseo` | None | Paid API actions are intentionally unavailable through the default MCP server. |
| `seo-image-gen` | None | Uses an image-generation tool only when one is connected and requested. |

The local MCP allowlist is maintained in `scripts/mcp_server.py`. Scripts that access private accounts, submit URLs, consume provider credits, or write files are excluded. Optional provider extensions are documented separately and must be reviewed and configured by the user.
