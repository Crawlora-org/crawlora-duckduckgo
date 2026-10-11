# DuckDuckGo client usage

The `@crawlora-org/duckduckgo` and `crawlora-duckduckgo` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape DuckDuckGo locally; Crawlora is independent from and not endorsed by DuckDuckGo or its owners.

The package tracks the public API contract revision `sha256:5c59c5ab37b393d0e018ef034c0638d14301e8a02f310239be2ce08110cd77b9` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 6 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `duckduckgo` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `image` / `image` | `GET /duckduckgo/image` | `q` (query, required), `page` (query, optional), `region` (query, optional) | Search DuckDuckGo image results |
| `news` / `news` | `GET /duckduckgo/news` | `q` (query, required), `page` (query, optional), `region` (query, optional) | Search DuckDuckGo news results |
| `search` / `search` | `GET /duckduckgo/search` | `q` (query, required), `page` (query, optional), `region` (query, optional), `time_range` (query, optional; values: `d`, `w`, `m`, `y`), `safe_search` (query, optional; values: `strict`, `moderate`, `off`) | Search DuckDuckGo web results |
| `shopping` / `shopping` | `GET /duckduckgo/shopping` | `q` (query, required), `region` (query, optional) | Search DuckDuckGo shopping results |
| `suggest` / `suggest` | `GET /duckduckgo/suggest` | `q` (query, required), `count` (query, optional), `region` (query, optional) | Suggest DuckDuckGo search queries |
| `video` / `video` | `GET /duckduckgo/video` | `q` (query, required), `page` (query, optional), `region` (query, optional) | Search DuckDuckGo video results |

## Client forms

- JavaScript: import `DuckDuckGoClient` (also exported as `Client`) from `@crawlora-org/duckduckgo`; use `new DuckDuckGoClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `DuckDuckGoClient` (also exported as `Client`) from `crawlora_duckduckgo`; use `with DuckDuckGoClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncDuckDuckGoClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
