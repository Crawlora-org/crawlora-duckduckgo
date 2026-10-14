"""Typed DuckDuckGo client for the Crawlora hosted API."""

from .platform import DuckDuckGoClient, AsyncDuckDuckGoClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = DuckDuckGoClient
AsyncClient = AsyncDuckDuckGoClient
__version__ = '0.1.2'
DISPLAY_NAME = 'DuckDuckGo'
PLATFORM = 'duckduckgo'
CONTRACT_REVISION = 'sha256:71470ec99f66e5aa4c627d7f3ca1a3a3597fd90fbe1bb7216ff2acb238bdecf1'

__all__ = [
    "DuckDuckGoClient", "AsyncDuckDuckGoClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
