# Capability map

Codex SEO splits work between skill instructions and the local MCP server. Skills define the analysis workflow; the server runs only the scripts listed below through an isolated Python environment. A script not listed in the default MCP allowlist is not callable through the plugin's generic analysis tool. The dedicated `seo_crawl` tool is separately bounded and never accepts arbitrary flags or output paths.

| Skill | Local tools exposed by default | Data and limits |
|---|---|---|
| `seo` | `seo_doctor`, `seo_setup` | Routes broad requests; data access follows the selected workflow. |
| `seo-audit` | `seo_crawl` (Unlighthouse; up to 50 routes, Node.js 18+), `render_page.py`, `sitemap_discovery.py`, `agentic_check.py`, `seo_updates.py` | `seo_crawl` runs only when explicitly requested; first use downloads the pinned runner. Always report route cap and actual coverage. |
| `seo-page` | `render_page.py`, `metadata_template.py`, `content_quality.py` | Page findings require accessible page content. |
| `seo-technical` | `seo_crawl` (up to 50 routes), `render_page.py`, `sitemap_discovery.py`, `agentic_check.py` | Full Lighthouse crawling is available through `seo_crawl`; PageSpeed API, CrUX, and account data require a separately authorized tool or supplied report. |
| `seo-content` | `content_quality.py`, `content_verify.py`, `content_humanize.py` (user text via stdin), `metadata_template.py | Human review is needed for claims, expertise, and factual accuracy. |
| `seo-content-brief` | None | Use supplied research or currently connected search tools; do not invent volumes or SERP data. |
| `seo-schema` | `schema_generate.py`, `schema_ecommerce_validate.py` | Validation is limited to rules in the bundled code; Google rich-result eligibility is not guaranteed. |
| `seo-sitemap` | `sitemap_discovery.py` | Reads public robots/sitemap locations. Generation and file writing are not exposed through generic MCP. |
| `seo-images` | `render_page.py` | Image analysis is limited to what the page and available visual tools expose. |
| `seo-geo` | `agentic_check.py`, `agent_ux_check.py`, `seo_updates.py` | AI citation/visibility claims require external evidence and are not ranking metrics. |
| `seo-agentic` | `agentic_check.py`, `agent_ux_check.py`, `agentic_fix.py` (drafts only), `seo_crawl` (multi-page Lighthouse) | Lighthouse Agentic Browsing category fraction still needs PSI or a compatible runner; `seo_crawl` provides general performance/accessibility/SEO Lighthouse scores. |
| `seo-local` | `render_page.py`, `gbp_deprecation_lint.py` | No Google Business Profile, review, or citation account is connected by default. |
| `seo-maps` | None | Map grids and current local rankings require an authorized maps/SERP provider. |
| `seo-hreflang` | `render_page.py` | Check only supplied or accessible language versions; no translation or geo-rank provider is connected. |
| `seo-plan` | None | Recommendations are strategic hypotheses unless backed by supplied business/search data. |
| `seo-programmatic` | `seo_crawl` (up to 50 routes) | Use a bounded crawl for a sample of template URLs; this is not a substitute for a complete inventory of very large sites. |
| `seo-competitor-pages` | None | Competitive evidence requires user-supplied facts or connected search tools. |
| `seo-flow` | None | Workflow framework guidance only; external prompt library sync is not included in default MCP. |
| `seo-backlinks` | None | The scripts are present but not exposed through MCP; no paid backlink index is connected. |
| `seo-google` | None | Google account scripts are not in the default MCP allowlist; use only a separately authorized connection or supplied exports. |
| `seo-cluster` | None | SERP-overlap grouping requires dated search results; semantic grouping alone is labeled as a hypothesis. |
| `seo-drift` | None | No scheduled snapshot store is enabled; compare user-supplied before/after captures. |
| `seo-sxo` | `render_page.py` | Conversion and ranking outcomes must be measured by the site owner. |
| `seo-ecommerce` | `render_page.py`, `schema_ecommerce_validate.py` (user-supplied JSON via stdin), `ucp_check.py` (read-only profile fetch) | No inventory, Merchant Center, marketplace, or pricing feed is connected; UCP endpoint probes are blocked. |
| `seo-dataforseo` | Optional remote DataForSEO v3 MCP (`docs_search`, `api_request`) | Not bundled or connected by default. Use OAuth setup in `EXTENSIONS.md`; every billable request needs a current estimate and approval. |
| `seo-image-gen` | None | Uses an image-generation tool only when one is connected and requested. |

The local MCP allowlist is maintained in `scripts/mcp_server.py`. Scripts that access private accounts, submit URLs, consume provider credits, or write files are excluded. Optional provider extensions are documented separately and must be reviewed and configured by the user.
