# Codex SEO

A small, focused set of SEO skills packaged as a Codex plugin. The skills cover general audits, technical SEO, individual pages, content, structured data, local SEO, international SEO, and XML sitemaps.

## Install from GitHub

In Codex, add this repository as a plugin marketplace source:

```text
https://github.com/CaduR/codex-seo
```

The repository includes `.agents/plugins/marketplace.json` for marketplace discovery and `.codex-plugin/plugin.json` for the plugin package. In Codex CLI, the equivalent command is:

```sh
codex plugin marketplace add CaduR/codex-seo
```

Restart/refresh the plugin directory and install **Codex SEO**. Availability can vary by Codex client and account settings.

## Skills

- `seo`: route broad requests and coordinate focused findings
- `seo-technical`: crawlability and indexability checks
- `seo-page`: one-page search and conversion review
- `seo-content`: content quality and editorial briefs
- `seo-schema`: structured data inspection and drafting
- `seo-local`: local business search
- `seo-international`: multilingual and hreflang review
- `seo-sitemap`: XML sitemap validation and drafting

Core workflows use the page/source material and tools available in the current Codex environment. They do not require paid SEO APIs. Search Console, analytics, commercial keyword/backlink datasets, and performance field data are optional inputs; the plugin never claims to have queried them without access.

## Marketplace directory submission

This repository is installable as a Git-backed Codex marketplace source. Inclusion in the universal public plugin directory is a separate submission and review step through the OpenAI developer portal; publishing this GitHub repository alone does not list it there.
