# @crawlora-org/duckduckgo — DuckDuckGo API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted DuckDuckGo API.
It exposes 6 API endpoints for web, news, image, video, and shopping search plus query suggestions through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-javascript-homepage). It does not run a browser or scrape DuckDuckGo locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by DuckDuckGo or its owners.

## Install

```sh
npm install @crawlora-org/duckduckgo
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { DuckDuckGoClient } from "@crawlora-org/duckduckgo";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new DuckDuckGoClient({ apiKey });
const result1 = await client.search({ q: "open source web crawler" });
console.log(result1);
const result2 = await client.news({ q: "technology" });
console.log(result2);
```

The client also exports `Client` as an alias for `DuckDuckGoClient`. Operation
methods are available directly in camelCase and through the `duckduckgo`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported DuckDuckGo API endpoints

This package exposes each route below as a direct method and through the `duckduckgo` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/duckduckgo/image` | `duckduckgo-image` | Search DuckDuckGo image results |
| `GET` | `/duckduckgo/news` | `duckduckgo-news` | Search DuckDuckGo news results |
| `GET` | `/duckduckgo/search` | `duckduckgo-search` | Search DuckDuckGo web results |
| `GET` | `/duckduckgo/shopping` | `duckduckgo-shopping` | Search DuckDuckGo shopping results |
| `GET` | `/duckduckgo/suggest` | `duckduckgo-suggest` | Suggest DuckDuckGo search queries |
| `GET` | `/duckduckgo/video` | `duckduckgo-video` | Search DuckDuckGo video results |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
