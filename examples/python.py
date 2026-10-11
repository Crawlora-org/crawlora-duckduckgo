import os

from crawlora_duckduckgo import DuckDuckGoClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with DuckDuckGoClient(api_key=api_key) as client:
    search = client.search(q='open source web crawler')
    print('search', search)
    news = client.news(q='technology')
    print('news', news)
