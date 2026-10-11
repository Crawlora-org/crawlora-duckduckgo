# crawlora-duckduckgo — DuckDuckGo API client for Python

Python client for Crawlora's hosted DuckDuckGo API. It exposes 6 API endpoints covering web, news, image, video, and shopping search plus query suggestions. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-python-homepage); the package does not run a browser or scrape
DuckDuckGo locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
DuckDuckGo or its owners.

## Install

```sh
python -m pip install crawlora-duckduckgo
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=duckduckgo-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_duckduckgo import DuckDuckGoClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with DuckDuckGoClient(api_key=api_key) as client:
    result_1 = client.search(q='open source web crawler')
    print(result_1)
    result_2 = client.news(q='technology')
    print(result_2)
```

The package also exports `Client` as an alias for `DuckDuckGoClient`. Operation
methods are available directly in snake_case and through the `duckduckgo`
group. The async package client is `AsyncDuckDuckGoClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_duckduckgo import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(q='open source web crawler')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/examples/python.py) for a complete usage example.

## Supported DuckDuckGo API endpoints

This package exposes every route below through direct snake_case methods and the `duckduckgo` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-duckduckgo/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/duckduckgo/image` | `duckduckgo-image` | Search DuckDuckGo image results |
| `GET` | `/duckduckgo/news` | `duckduckgo-news` | Search DuckDuckGo news results |
| `GET` | `/duckduckgo/search` | `duckduckgo-search` | Search DuckDuckGo web results |
| `GET` | `/duckduckgo/shopping` | `duckduckgo-shopping` | Search DuckDuckGo shopping results |
| `GET` | `/duckduckgo/suggest` | `duckduckgo-suggest` | Suggest DuckDuckGo search queries |
| `GET` | `/duckduckgo/video` | `duckduckgo-video` | Search DuckDuckGo video results |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
