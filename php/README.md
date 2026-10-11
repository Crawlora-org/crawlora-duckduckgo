# Crawlora DuckDuckGo API client for PHP (`crawlora/duckduckgo`)

This PHP package calls Crawlora's hosted DuckDuckGo API at `https://api.crawlora.net/api/v1`. It exposes 6 endpoints covering web, news, image, video, and shopping search plus query suggestions. It does not call or scrape DuckDuckGo directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/duckduckgo
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Duckduckgo\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("duckduckgo-search", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 6 API operations.

## Supported DuckDuckGo API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/duckduckgo/image` | `duckduckgo-image` | Search DuckDuckGo image results |
| `GET` | `/duckduckgo/news` | `duckduckgo-news` | Search DuckDuckGo news results |
| `GET` | `/duckduckgo/search` | `duckduckgo-search` | Search DuckDuckGo web results |
| `GET` | `/duckduckgo/shopping` | `duckduckgo-shopping` | Search DuckDuckGo shopping results |
| `GET` | `/duckduckgo/suggest` | `duckduckgo-suggest` | Suggest DuckDuckGo search queries |
| `GET` | `/duckduckgo/video` | `duckduckgo-video` | Search DuckDuckGo video results |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-duckduckgo). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md).
