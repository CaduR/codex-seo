<!-- Updated: 2026-11-10 -->
# Maps and Business Data Sources

Codex SEO does not bundle a Maps or business-data provider. Endpoint names, fields, limits, and prices change, so resolve them from the provider's current documentation before use.

## Optional DataForSEO v3 MCP

Connect the official server using the OAuth steps in [`docs/EXTENSIONS.md`](../../../../docs/EXTENSIONS.md). The current Codex workflow uses `docs_search` to find the Maps SERP, business profile, reviews, questions, or listings endpoint, and `api_request` to call the documented path. Do not use retired endpoint-specific MCP tool names or assume the old v2 MCP contract.

Before any billable request:

1. Confirm the target business, location, language, query, and data depth with the user.
2. Search the current docs for the endpoint, task format, response fields, and current price.
3. Show the task count and estimated cost, including uncertainty if the docs do not provide a precise amount.
4. Wait for explicit approval, then request only the approved data.
5. Report the provider, date, market, method, and any missing data with the result.

For a geo-grid, the task count is `grid_size² × keyword_count`. Do not quote fixed prices from this repository; provider pricing and task behavior can change. Do not infer that a missing response means a business has no profile, reviews, or Q&A.

Without a connected provider, analyze user-supplied exports or provide a collection template. Never fabricate listings, review counts, ranks, or competitor data.
