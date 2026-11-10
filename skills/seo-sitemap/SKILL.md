---
name: seo-sitemap
description: Review or draft an XML sitemap and its robots.txt discovery reference. Use for sitemap coverage, validity, or generation requests.
---

# XML sitemap

Inspect the sitemap or the user-provided list of canonical URLs. Check XML well-formedness, sitemap index structure, absolute HTTPS URLs, duplicate entries, redirects, non-canonical or noindex URLs, and whether important indexable pages appear. Treat `lastmod` as useful only when it reflects a real content change.

Use `seo_analyze` with `sitemap_discovery.py` when the local MCP runtime is ready. It checks public robots.txt and common sitemap locations. Do not claim a complete site crawl: broad crawling and sitemap file generation are not exposed through the default MCP tools.

When generating a sitemap, use only URLs supplied or verified from the site. Do not claim a sitemap guarantees indexing. Provide a concise validation checklist and point out any URL that needs confirmation.
