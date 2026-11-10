---
name: seo-audit
description: Coordinate a broad review of a website across technical SEO, pages, content, schema, local or international needs, and AI-search readiness. Use when the user asks for a full-site audit or a prioritized SEO baseline.
---

# Full-site SEO audit

Build a site-wide diagnostic from evidence available in the current session. The local MCP tools can inspect individual URLs and discover sitemaps; they do not provide a 500-page crawler or browser farm. The specialist cards in `references/specialists/` can guide parallel Codex subagents when the active Codex surface provides delegation tools.

## Workflow

1. Confirm the target domain and audit depth. Use a URL the user supplied or ask for one only if absent.
2. Check `seo_doctor`. If setup is missing, explain that `seo_setup` installs packages in user data and wait for the user to request that local change; continue with Codex's other available browser and file tools.
3. Use `seo_analyze` with `sitemap_discovery.py` to locate declared public sitemaps and `render_page.py` for the homepage plus a representative set of important pages. Respect robots.txt, avoid high-volume requests, and do not call the same page repeatedly. If broad coverage is not possible, state which URLs were reviewed.
4. Route findings through relevant skills and specialist role cards: technical, page, content, schema, performance, visual, GEO, agent readiness, local or commerce when applicable. Delegate independent reviews in parallel only when Codex exposes subagent tools; otherwise run the passes inline. Do not claim a fixed number of agents.
5. Separate observed evidence, supplied metrics, and assumptions. Never infer ranking position, indexing status, field Core Web Vitals, or traffic without a suitable data source. The default MCP excludes account APIs, paid providers, submissions, and file-writing tools.
6. Prioritize blockers first, then high-impact page issues, then editorial and refinement work. Explain impact without promising a ranking outcome.
7. Return an executive summary, scope and evidence, prioritized findings with URL and fix, missing data, and a short next-step plan. Do not invent a numeric health score.

A full audit is a diagnostic. It does not change the site, submit URLs, or access Search Console/analytics unless the user separately requests and enables those actions. Optional providers may have separate costs; identify and confirm paid calls before using them.

## Specialist role cards

The 19 files in `references/specialists/` define bounded review passes. Read only the cards relevant to the site and requested audit. A card is a prompt resource, not an independently installed Codex agent. Do not claim parallel analysis unless the host actually provided subagents and they returned results.
