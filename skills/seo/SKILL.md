---
name: seo
description: Route a general SEO request to a focused workflow or coordinate a site review. Use when the user asks broadly for SEO help without specifying a narrower task.
---

# SEO workflow router

Identify the user's outcome and route to the most specific skill:

- Broad site review: `seo-audit`
- Technical, page, content or brief, schema, image: `seo-technical`, `seo-page`, `seo-content`, `seo-content-brief`, `seo-schema`, `seo-images`
- AI search, agents, local/maps, international, sitemap: `seo-geo`, `seo-agentic`, `seo-local`, `seo-maps`, `seo-international`, `seo-sitemap`
- Strategy, programmatic, comparison pages, clusters, FLOW, SXO: `seo-plan`, `seo-programmatic`, `seo-competitor-pages`, `seo-cluster`, `seo-flow`, `seo-sxo`
- Backlinks, Google data, DataForSEO, drift, commerce, image creation: `seo-backlinks`, `seo-google`, `seo-dataforseo`, `seo-drift`, `seo-ecommerce`, `seo-image-gen`

## Working rules

- Ask for a URL, target market, or dataset only when the request cannot be addressed without it.
- Inspect the live page or supplied source before stating that an issue exists. If access is unavailable, label advice as a checklist or hypothesis.
- For each finding, provide evidence, user/search impact, priority, and a concrete next step. Keep verified observations separate from suggestions.
- Prioritize indexing blockers and broken experiences, then high-impact page and content fixes, then refinements. Never invent ranking guarantees or numerical scores.
- Do not change a site, submit URLs, access analytics, or spend provider credits unless the user requests the action and access is available.
- Paid SEO data is optional. State when a recommendation depends on an unavailable source and continue with free evidence where useful.
