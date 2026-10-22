# Crawlora DuckDuckGo Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `6`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| duckduckgo | `duckduckgo.image` | `duckduckgo-image` | `GET /duckduckgo/image` | `q` (query String required)<br>`page` (query i64)<br>`region` (query String) | `ApiKeyAuth` | `DuckduckgoImageResponse` |  |
| duckduckgo | `duckduckgo.news` | `duckduckgo-news` | `GET /duckduckgo/news` | `q` (query String required)<br>`page` (query i64)<br>`region` (query String) | `ApiKeyAuth` | `DuckduckgoNewsResponse` |  |
| duckduckgo | `duckduckgo.search` | `duckduckgo-search` | `GET /duckduckgo/search` | `q` (query String required)<br>`page` (query i64)<br>`region` (query String)<br>`time_range` (query String enum{d, w, m, y})<br>`safe_search` (query String enum{strict, moderate, off}) | `ApiKeyAuth` | `DuckduckgoSearchResponse` |  |
| duckduckgo | `duckduckgo.shopping` | `duckduckgo-shopping` | `GET /duckduckgo/shopping` | `q` (query String required)<br>`region` (query String) | `ApiKeyAuth` | `DuckduckgoShoppingResponse` |  |
| duckduckgo | `duckduckgo.suggest` | `duckduckgo-suggest` | `GET /duckduckgo/suggest` | `q` (query String required)<br>`count` (query i64)<br>`region` (query String) | `ApiKeyAuth` | `DuckduckgoSuggestResponse` |  |
| duckduckgo | `duckduckgo.video` | `duckduckgo-video` | `GET /duckduckgo/video` | `q` (query String required)<br>`page` (query i64)<br>`region` (query String) | `ApiKeyAuth` | `DuckduckgoVideoResponse` |  |
