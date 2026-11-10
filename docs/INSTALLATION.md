# Install Codex SEO

## Requirements

- Codex desktop with local plugin execution enabled
- Python 3.11–3.14 available as `python`
- Git to add the GitHub marketplace source

The Codex skill catalog works as packaged guidance. The local MCP tools also need the Python runtime.

## Install

1. Add the marketplace:

   ```sh
   codex plugin marketplace add CaduR/codex-seo
   ```

2. In Codex desktop, open **Plugins**, select Codex SEO, and install it.
3. Run `$seo_doctor`. It reports whether the isolated runtime is ready.
4. If setup is needed, run `$seo_setup`. The setup tool installs Python packages into the user application-data directory. It does not install Chromium unless requested.

## Verify

Ask Codex to run a public-page workflow such as `$seo-page https://example.com`. The result should identify fetched evidence, limits, and unavailable data sources. Use `$seo_doctor` to check runtime state without making changes.

## What setup changes

Setup creates a virtual environment under the user's application-data directory, installs `requirements.txt`, and stores a runtime state file there. Chromium is an optional separate download for JavaScript-rendered pages and screenshots.

## Limitations

The local MCP server exposes only read-only analysis scripts. Scripts that query account data, spend credits, submit URLs, or write user files are not available through its generic tool. External connectors require their own configuration and authorization.
