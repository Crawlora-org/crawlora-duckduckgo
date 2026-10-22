# DuckDuckGo API endpoint reference and client usage

This reference lists all 6 public DuckDuckGo API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/duckduckgo`, `crawlora-duckduckgo`, and `crawlora-duckduckgo` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape DuckDuckGo locally; Crawlora is independent from and not endorsed by DuckDuckGo or its owners.

The package tracks the public API contract revision `sha256:71470ec99f66e5aa4c627d7f3ca1a3a3597fd90fbe1bb7216ff2acb238bdecf1` bundled with release `0.1.2`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `duckduckgo`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `image` | `image` | `duckduckgo.image` | `GET /duckduckgo/image` | `q` (query, required), `page` (query, optional), `region` (query, optional) | Search DuckDuckGo image results |
| `news` | `news` | `duckduckgo.news` | `GET /duckduckgo/news` | `q` (query, required), `page` (query, optional), `region` (query, optional) | Search DuckDuckGo news results |
| `search` | `search` | `duckduckgo.search` | `GET /duckduckgo/search` | `q` (query, required), `page` (query, optional), `region` (query, optional), `time_range` (query, optional; values: `d`, `w`, `m`, `y`), `safe_search` (query, optional; values: `strict`, `moderate`, `off`) | Search DuckDuckGo web results |
| `shopping` | `shopping` | `duckduckgo.shopping` | `GET /duckduckgo/shopping` | `q` (query, required), `region` (query, optional) | Search DuckDuckGo shopping results |
| `suggest` | `suggest` | `duckduckgo.suggest` | `GET /duckduckgo/suggest` | `q` (query, required), `count` (query, optional), `region` (query, optional) | Suggest DuckDuckGo search queries |
| `video` | `video` | `duckduckgo.video` | `GET /duckduckgo/video` | `q` (query, required), `page` (query, optional), `region` (query, optional) | Search DuckDuckGo video results |

## Client forms

- JavaScript: import `DuckDuckGoClient` (also exported as `Client`) from `@crawlora-org/duckduckgo`; use `new DuckDuckGoClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `DuckDuckGoClient` (also exported as `Client`) from `crawlora_duckduckgo`; use `with DuckDuckGoClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncDuckDuckGoClient`, used with `async with` and `await`.
- Rust: add `crawlora-duckduckgo` with Cargo; import `Client` and the generated operation parameter struct, then call `client.duckduckgo.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
