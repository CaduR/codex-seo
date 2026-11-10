# DataForSEO v3 API endpoint guide

The current official server exposes documentation tools and one generic request tool; it does not expose one MCP tool per endpoint.

## Tool flow

1. `docs_list_sections` or `docs_index` to find the relevant API family.
2. `docs_search` for the current endpoint's required fields, method, prices, queue, limits, and response schema.
3. After the user approves the estimate, call `api_request` with `method`, `path`, and `data` as a JSON array containing one task object.

The server defaults to its `.ai` response format. That format may omit fields such as actual `cost`. Set `noAiMode: true` only when the raw response or actual cost field is required. Do not mistake a post-request actual cost for a pre-request estimate.

## Common endpoint families

| Workflow | v3 endpoint family |
|---|---|
| Organic, images, Maps, news, YouTube SERPs | `/v3/serp/{engine}/...` |
| Keyword volume and trends | `/v3/keywords_data/{source}/...` |
| Keyword ideas, rankings, competitors, intersections | `/v3/dataforseo_labs/{source}/...` |
| Backlink summaries, links, anchors, referring domains | `/v3/backlinks/...` |
| On-page parsing, instant checks, Lighthouse | `/v3/on_page/...` |
| Domain technology and WHOIS | `/v3/domain_analytics/...` |
| Business listings and reviews | `/v3/business_data/...` |
| Content search, summaries, phrase trends | `/v3/content_analysis/...` |
| AI visibility, LLM responses and mentions | `/v3/ai_optimization/...` |
| Shopping and marketplace data | `/v3/merchant/...` |

These are families, not complete paths. Confirm every path and body through `docs_search`; DataForSEO can change endpoints and pricing.

## Verified examples

- Google organic SERP: `POST /v3/serp/google/organic/live/regular`
- Google Images SERP: resolve the current `google/images/live` endpoint using `docs_search`
- Backlink summary: `POST /v3/backlinks/summary/live`

Use the market-specific location and language codes. The examples in this file are endpoint patterns; they are not approval to make a paid API request.
