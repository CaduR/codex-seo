---
name: seo-drift
description: Compare current SEO-critical page elements with a saved baseline or review a proposed site change for regressions. Use for SEO drift, pre/post-deploy checks, and metadata regression reviews.
---

# SEO drift and change review

Compare only fields that have a real prior and current capture. Useful fields include HTTP status, title, description, canonical, robots directives, main heading, hreflang, structured data, Open Graph, and content sections. Record capture dates, URLs, and source. Separate a detected change from its business impact; changes can be intentional and are not proof of ranking loss.

If the user supplies before/after HTML, screenshots, or exports, compare those materials directly. If asked to establish a baseline, summarize the selected fields in a small reviewable Markdown or JSON artifact and write it only in the user-designated workspace. Do not silently persist data elsewhere. For repeated monitoring, state that a scheduled collector and storage are not included in this skill.

Classify findings by urgency and provide evidence plus a validation step. A report is not a CI gate unless a separate tested policy implements that behavior. Do not claim continuous monitoring or historical drift analysis without stored captures. Optional performance data needs a real authorized source.
