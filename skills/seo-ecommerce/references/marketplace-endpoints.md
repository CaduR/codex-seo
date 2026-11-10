# DataForSEO Marketplace Endpoint Reference

Use the optional official DataForSEO v3 MCP only when the user requests live marketplace evidence and a DataForSEO connection is available.

The provider's current server exposes a generic `api_request` tool, not separate merchant MCP tools. Resolve product, seller, or marketplace endpoint paths, required task fields, market/language codes, queue options, and current prices with `docs_search` before any call. Treat price examples in older Claude SEO materials as obsolete.

## Safe request flow

1. Ask which target country and marketplace matter.
2. Search the current official DataForSEO documentation for the matching Google Shopping or Amazon API endpoint.
3. Explain the exact request scope, result depth, queue, and current estimated cost.
4. Wait for explicit approval.
5. Call `api_request` with the documented method/path and a one-task `data` array.
6. Label provider-reported price, stock, seller, currency, and freshness. Do not infer missing values.

DataForSEO marketplace requests are paid. Codex SEO does not include a spend ledger, connector, or installer. Never assume a US location, 100-result depth, a fixed price, or that a query is free.
