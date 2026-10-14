# DuckDuckGo clients for Crawlora

Official Crawlora client packages for the hosted DuckDuckGo API. Access 6 API endpoints covering web, news, image, video, and shopping search plus query suggestions from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape DuckDuckGo locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by DuckDuckGo or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/duckduckgo`](javascript/README.md)
- Python: [`crawlora-duckduckgo`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-duckduckgo`](go.mod)
- Ruby: [`crawlora-duckduckgo`](ruby/README.md)
- Java: [`net.crawlora:crawlora-duckduckgo:0.1.2`](java/README.md)
- PHP: [`crawlora/duckduckgo`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 6 selected public DuckDuckGo API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/duckduckgo/image` | `duckduckgo-image` | Search DuckDuckGo image results |
| `GET` | `/duckduckgo/news` | `duckduckgo-news` | Search DuckDuckGo news results |
| `GET` | `/duckduckgo/search` | `duckduckgo-search` | Search DuckDuckGo web results |
| `GET` | `/duckduckgo/shopping` | `duckduckgo-shopping` | Search DuckDuckGo shopping results |
| `GET` | `/duckduckgo/suggest` | `duckduckgo-suggest` | Suggest DuckDuckGo search queries |
| `GET` | `/duckduckgo/video` | `duckduckgo-video` | Search DuckDuckGo video results |

## License

MIT. See [LICENSE](LICENSE).
