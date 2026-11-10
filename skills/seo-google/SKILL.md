---
name: seo-google
description: Interpret SEO data from Google Search Console, PageSpeed Insights, CrUX, URL Inspection, or GA4 when the user has provided an export or an authorized connection.
---

# Google SEO data

Use only data actually available in the session. Confirm the property, URL scope, date range, search type, filters, and source before interpreting results. Keep Search Console clicks/impressions/position distinct from analytics sessions/conversions; they use different definitions and attribution.

For Search Console, inspect query/page/device/country trends with date comparisons and note anonymized or limited rows. For URL Inspection or Indexing API, use only authorized properties and applicable endpoints; the Indexing API is not a general URL submission route. For PageSpeed, label Lighthouse results as lab data and CrUX as field data, including sample/coverage limits. For GA4, define organic channel grouping and conversion event before calculating results.

Never claim to have called an API without an authorized connector/tool and returned evidence. Do not request secrets in chat or expose tokens. If only a CSV/report is provided, analyze that file and state its limits. API credentials, quotas, and access policies belong to the account owner; this skill provides no Google connector itself.
