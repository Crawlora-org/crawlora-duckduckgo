"""Typed DuckDuckGo client for the Crawlora hosted API."""

from .platform import DuckDuckGoClient, AsyncDuckDuckGoClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = DuckDuckGoClient
AsyncClient = AsyncDuckDuckGoClient
__version__ = '0.1.0'
DISPLAY_NAME = 'DuckDuckGo'
PLATFORM = 'duckduckgo'
CONTRACT_REVISION = 'sha256:5c59c5ab37b393d0e018ef034c0638d14301e8a02f310239be2ce08110cd77b9'

__all__ = [
    "DuckDuckGoClient", "AsyncDuckDuckGoClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
