# Optional provider extensions

Codex SEO carries reference material for nine optional integrations: Ahrefs, Banana/Gemini image generation, Bing Webmaster, DataForSEO, Firecrawl, Matomo, Profound, SE Ranking, and Unlighthouse.

## Current Codex status

The extension folders in this repository were adapted from Claude SEO. Their installer scripts write Claude Code configuration and are **not** Codex installers. Do not run them to configure this Codex plugin. The default MCP server does not connect to these providers.

Use a provider only after you add its supported MCP connection to Codex, review the scopes and costs, and explicitly request the relevant workflow. Never commit credentials or paste secrets into chat. The local analysis tool intentionally excludes paid-provider queries and account submissions.

| Extension | Use | Typical dependency/cost | Default Codex MCP |
|---|---|---|---|
| Ahrefs | Backlinks, organic keywords, content research | Account/API access; plan or usage charges may apply | Not connected |
| Banana / Gemini | Generate or edit SEO images | Google AI account and usage billing may apply | Not connected |
| Bing Webmaster | Site links, indexing data, IndexNow submission | Verified site access; submissions change external state | Not connected |
| DataForSEO | SERPs, keyword metrics, local and backlink datasets | Credit-based API; check per-request estimate before calling | Not connected |
| Firecrawl | Crawling and JavaScript-rendered extraction | Provider account, limits and usage billing may apply | Not connected |
| Matomo | Organic analytics reports | Matomo site ID and view-only token; self-hosted or hosted service terms apply | Not connected |
| Profound | AI-search mention and citation monitoring | Provider account and subscription/usage terms | Not connected |
| SE Ranking | Rank and AI share-of-voice analysis | Provider account and subscription terms | Not connected |
| Unlighthouse | Local Lighthouse scans across a site | Node.js and local compute; no API account by default | Not connected |

Provider plans and pricing change. Confirm current terms and a concrete cost estimate with the provider before enabling a paid call. Keep credentials in the provider's supported local auth store, request only read scopes unless a write is explicitly needed, and never submit URLs or change external data without the user's explicit request.
