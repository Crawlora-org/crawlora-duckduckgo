# Crawlora DuckDuckGo JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `6`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| duckduckgo | `duckduckgo.image` | `duckduckgo-image` | `GET /duckduckgo/image` | `q` (query string required)<br>`page` (query number)<br>`region` (query string) | `ApiKeyAuth` | `DuckduckgoImageResponse` |  |
| duckduckgo | `duckduckgo.news` | `duckduckgo-news` | `GET /duckduckgo/news` | `q` (query string required)<br>`page` (query number)<br>`region` (query string) | `ApiKeyAuth` | `DuckduckgoNewsResponse` |  |
| duckduckgo | `duckduckgo.search` | `duckduckgo-search` | `GET /duckduckgo/search` | `q` (query string required)<br>`page` (query number)<br>`region` (query string)<br>`time_range` (query "d" \| "w" \| "m" \| "y")<br>`safe_search` (query "strict" \| "moderate" \| "off") | `ApiKeyAuth` | `DuckduckgoSearchResponse` |  |
| duckduckgo | `duckduckgo.shopping` | `duckduckgo-shopping` | `GET /duckduckgo/shopping` | `q` (query string required)<br>`region` (query string) | `ApiKeyAuth` | `DuckduckgoShoppingResponse` |  |
| duckduckgo | `duckduckgo.suggest` | `duckduckgo-suggest` | `GET /duckduckgo/suggest` | `q` (query string required)<br>`count` (query number)<br>`region` (query string) | `ApiKeyAuth` | `DuckduckgoSuggestResponse` |  |
| duckduckgo | `duckduckgo.video` | `duckduckgo-video` | `GET /duckduckgo/video` | `q` (query string required)<br>`page` (query number)<br>`region` (query string) | `ApiKeyAuth` | `DuckduckgoVideoResponse` |  |
