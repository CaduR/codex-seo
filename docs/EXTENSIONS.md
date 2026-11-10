# Optional provider extensions

Codex SEO carries reference material for nine optional integrations: Ahrefs, Banana/Gemini image generation, Bing Webmaster, DataForSEO, Firecrawl, Matomo, Profound, SE Ranking, and Unlighthouse.

## Current Codex status

Most extension folders in this repository were adapted from Claude SEO. Their installer scripts write Claude Code configuration and are **not** Codex installers. Do not run them to configure this Codex plugin. Unlighthouse is the exception: its pinned runner is available through the bounded `seo_crawl` MCP tool; the other external data providers are not connected by default.

Use a provider only after you add its supported MCP connection to Codex, review the scopes and costs, and explicitly request the relevant workflow. Never commit credentials or paste secrets into chat. The generic local analysis tool intentionally excludes paid-provider queries and account submissions. `seo_crawl` is separately bounded, requests only public pages, and never submits or edits site data.

| Extension | Use | Typical dependency/cost | Default Codex MCP |
|---|---|---|---|
| Ahrefs | Backlinks, organic keywords, content research | Account/API access; plan or usage charges may apply | Not connected |
| Banana / Gemini | Generate or edit SEO images | Google AI account and usage billing may apply | Not connected |
| Bing Webmaster | Site links, indexing data, IndexNow submission | Verified site access; submissions change external state | Not connected |
| DataForSEO | SERPs, keyword metrics, local and backlink datasets | Credit-based API; explicit estimate and approval required | Optional OAuth MCP setup documented below |
| Firecrawl | Crawling and JavaScript-rendered extraction | Provider account, limits and usage billing may apply | Not connected |
| Matomo | Organic analytics reports | Matomo site ID and view-only token; self-hosted or hosted service terms apply | Not connected |
| Profound | AI-search mention and citation monitoring | Provider account and subscription/usage terms | Not connected |
| SE Ranking | Rank and AI share-of-voice analysis | Provider account and subscription terms | Not connected |
| Unlighthouse | Local Lighthouse scans across a site | Node.js and local compute; no API account by default | Available as `seo_crawl`, capped at 50 routes |

Provider plans and pricing change. Confirm current terms and a concrete cost estimate with the provider before enabling a paid call. Keep credentials in the provider's supported local auth store, request only read scopes unless a write is explicitly needed, and never submit URLs or change external data without the user's explicit request.

## Connect DataForSEO to Codex

DataForSEO provides an official remote MCP with OAuth. This adds a separate provider connection to Codex; it does not modify the Codex SEO plugin or require pasting API keys into project files.

```bash
codex mcp add dataforseo --url https://mcp.dataforseo.com/v3/mcp
codex mcp login dataforseo
codex mcp list
```

Start a new Codex session and verify the server's `docs_index`, `docs_list_sections`, `docs_search`, and `api_request` tools. The current server exposes a generic `api_request` rather than the older endpoint-specific tool names. For each workflow, resolve the endpoint and current price with `docs_search`, show the estimate, and wait for approval before a billable request. See [the DataForSEO skill](/codex-seo/skills/seo-dataforseo/) for endpoint patterns and the v3 request flow.
