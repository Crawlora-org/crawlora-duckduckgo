# Crawlora DuckDuckGo API client for Ruby (`crawlora-duckduckgo`)

This Ruby gem calls Crawlora's hosted DuckDuckGo API at `https://api.crawlora.net/api/v1`. It exposes 6 endpoints covering web, news, image, video, and shopping search plus query suggestions; it does not call or scrape DuckDuckGo directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-duckduckgo"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/duckduckgo"

client = Crawlora::Duckduckgo::Client.new
result = client.request("duckduckgo-search", JSON.parse("{\"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 6 API operations.

```ruby
client = Crawlora::Duckduckgo::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported DuckDuckGo API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/duckduckgo/image` | `duckduckgo-image` | Search DuckDuckGo image results |
| `GET` | `/duckduckgo/news` | `duckduckgo-news` | Search DuckDuckGo news results |
| `GET` | `/duckduckgo/search` | `duckduckgo-search` | Search DuckDuckGo web results |
| `GET` | `/duckduckgo/shopping` | `duckduckgo-shopping` | Search DuckDuckGo shopping results |
| `GET` | `/duckduckgo/suggest` | `duckduckgo-suggest` | Suggest DuckDuckGo search queries |
| `GET` | `/duckduckgo/video` | `duckduckgo-video` | Search DuckDuckGo video results |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-duckduckgo) for account setup, the API operation reference, and release history.
