<!-- Updated: 2026-11-10 -->
# Geo-Grid Rank Tracking Algorithm

## Concept

Geo-grid rank tracking samples local search visibility from coordinates around a business. The result is a grid of observed positions, not a ranking guarantee or a complete measure of local visibility.

## Grid generation

Choose a center coordinate, an odd grid size (3–13), and a radius appropriate to the service area. For each row `i` and column `j`, with `center = (grid_size - 1) / 2` and `step = 2 * radius_km / (grid_size - 1)`:

```
dy = (i - center) * step
dx = (j - center) * step
lat = center_lat + dy / 111.32
lng = center_lng + dx / (111.32 * cos(center_lat * pi / 180))
```

Use a smaller radius for dense urban areas and a wider radius for rural service areas. Ask the user for the business location and target area when they are not known; do not assume a country, language, or default city.

## Collecting positions

If the official DataForSEO v3 MCP is connected, use `docs_search` to resolve the current Google Maps SERP endpoint, required request fields, limits, and price. Present the number of tasks (`grid_size² × keywords`), the current estimate, and wait for approval before calling `api_request`. Submit only the approved number of tasks and use the user's market, language, and device. The Codex plugin does not provide this provider or pricing data itself.

If no provider is connected, provide the grid coordinates and a collection template for the user to fill from an authorized source. Never invent rankings or cost estimates. Do not launch large grids by default; start with the smallest grid that answers the question.

## Share of Local Voice

When positions were actually collected, calculate:

```
SoLV = (grid points ranking in the top 3 / grid points checked) * 100
```

Label this as a sample-specific metric. Also report average observed rank, missing results, the weakest quadrant, the exact query, date, provider, market, and grid radius. Do not imply that the metric is an official Google score.

## Heatmap

Use ranks 1–3 for strong visibility, 4–10 for visible results, `+` for lower positions, and `-` for not found in the checked depth. Mark the center point and include the query and collection context. Treat uncollected points as unknown, not as `-`.
