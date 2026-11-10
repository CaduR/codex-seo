---
name: seo-agentic
description: Review whether a public website is understandable and usable by browser-based AI agents and assistive technologies. Use for agent readiness, WebMCP, llms.txt, or accessibility-tree discovery questions.
---

# Agent readiness review

Treat agent readiness as a usability and discoverability review, not a ranking metric. Inspect only what the available browser, source, and network tools can actually retrieve. Check whether primary content and actions have clear accessible names, links and controls are discoverable, important content depends on inaccessible client-only behavior, and navigation exposes a coherent structure.

If local tools are ready, use `seo_analyze` with `agentic_check.py` and `agent_ux_check.py`. The default MCP does not expose the Lighthouse report reader or an agentic-browser runner. Do not represent heuristic checks as an agentic-browsing benchmark.

When in scope, review robots.txt and named crawler policies against the relevant provider's current documentation; distinguish search, user-triggered browsing, and model-training purposes. Check for `llms.txt`, Markdown alternatives, discovery files, and WebMCP support as optional capabilities, not universal requirements. Do not interpret absence of any one convention as an indexing failure.

If Lighthouse Agentic Browsing or a compatible agent/browser test is actually run, report its exact fraction, tool/version, page, and test conditions. Do not estimate the score or imply that it is a Google ranking signal. WebMCP/browser APIs can change; consult current primary documentation before giving implementation advice.

Return tested pages, observed accessibility/discovery issues, evidence, limitations, and prioritized fixes. Do not change bot policies or production actions without approval. This skill does not bundle a browser test runner or WebMCP server.
