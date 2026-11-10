# DataForSEO Cost and Approval Guide

Do not rely on a static cost table. DataForSEO charges by endpoint, request type, task count, location, queue, and result depth; prices can change.

Before a live request:

1. Use the connected `docs_search` tool to check current endpoint documentation and provider pricing.
2. State the endpoint, market, task count/depth, queue, and estimated charge.
3. Wait for explicit user approval. If no concrete estimate is available, do not call the paid endpoint.
4. Make the smallest request that answers the question.
5. When cost auditing matters, use `noAiMode: true` and report the actual `cost` field returned after the call. This is a charge already incurred, not an estimate.

DataForSEO v3 uses `api_request`; this plugin has no spend ledger, budget gate, or cost-approval command. Provider-account limits remain the account owner's responsibility.

Documentation lookups (`docs_index`, `docs_list_sections`, `docs_search`) are distinct from billable API requests. Confirm current provider terms in the [official pricing page](https://dataforseo.com/pricing) and the relevant endpoint documentation.
