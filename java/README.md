# Crawlora DuckDuckGo API client for Java

The official Java client for Crawlora's hosted DuckDuckGo API. It exposes 6 endpoints covering web, news, image, video, and shopping search plus query suggestions. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-duckduckgo</artifactId>
  <version>0.1.2</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-java-console) to get an API key.

```java
import net.crawlora.duckduckgo.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.search(Map.ofEntries(Map.entry("q", "open source web crawler")));
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported DuckDuckGo API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md) also lists parameters and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/duckduckgo/image` | `duckduckgo-image` | Search DuckDuckGo image results |
| `GET` | `/duckduckgo/news` | `duckduckgo-news` | Search DuckDuckGo news results |
| `GET` | `/duckduckgo/search` | `duckduckgo-search` | Search DuckDuckGo web results |
| `GET` | `/duckduckgo/shopping` | `duckduckgo-shopping` | Search DuckDuckGo shopping results |
| `GET` | `/duckduckgo/suggest` | `duckduckgo-suggest` | Suggest DuckDuckGo search queries |
| `GET` | `/duckduckgo/video` | `duckduckgo-video` | Search DuckDuckGo video results |

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-duckduckgo)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-java-api-docs)
