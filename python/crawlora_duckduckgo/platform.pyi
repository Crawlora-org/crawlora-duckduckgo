from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelDuckduckgoVideoResponseDoc = TypedDict('ModelDuckduckgoVideoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDuckduckgoVideoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDuckduckgoVideoResponse = TypedDict('ModelDuckduckgoVideoResponse', {
    'pagination': NotRequired[ModelDuckduckgoSearchPagination],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelDuckduckgoVideoResult]],
}, total=False)

ModelDuckduckgoVideoResult = TypedDict('ModelDuckduckgoVideoResult', {
    'description': NotRequired[str],
    'duration': NotRequired[str],
    'position': NotRequired[int],
    'published_at': NotRequired[str],
    'publisher': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'uploader': NotRequired[str],
    'url': NotRequired[str],
    'view_count': NotRequired[int],
}, total=False)

ModelDuckduckgoSearchPagination = TypedDict('ModelDuckduckgoSearchPagination', {
    'next_page': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

ModelDuckduckgoSuggestResponseDoc = TypedDict('ModelDuckduckgoSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSuggestResponse = TypedDict('ModelSuggestResponse', {
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelSuggestSuggestion]],
}, total=False)

ModelSuggestSuggestion = TypedDict('ModelSuggestSuggestion', {
    'position': NotRequired[int],
    'query': NotRequired[str],
}, total=False)

ModelDuckduckgoShoppingResponseDoc = TypedDict('ModelDuckduckgoShoppingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDuckduckgoShoppingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDuckduckgoShoppingResponse = TypedDict('ModelDuckduckgoShoppingResponse', {
    'page_info': NotRequired[ModelDuckduckgoShoppingPageInfo],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelDuckduckgoShoppingResult]],
}, total=False)

ModelDuckduckgoShoppingResult = TypedDict('ModelDuckduckgoShoppingResult', {
    'brand': NotRequired[str],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'low_price': NotRequired[str],
    'merchant': NotRequired[str],
    'position': NotRequired[int],
    'price': NotRequired[str],
    'rating': NotRequired[float],
    'review_count': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelDuckduckgoShoppingPageInfo = TypedDict('ModelDuckduckgoShoppingPageInfo', {
    'page': NotRequired[int],
    'total_pages': NotRequired[int],
}, total=False)

ModelDuckduckgoSearchResponseDoc = TypedDict('ModelDuckduckgoSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDuckduckgoSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDuckduckgoSearchResponse = TypedDict('ModelDuckduckgoSearchResponse', {
    'pagination': NotRequired[ModelDuckduckgoSearchPagination],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelDuckduckgoSearchResult]],
}, total=False)

ModelDuckduckgoSearchResult = TypedDict('ModelDuckduckgoSearchResult', {
    'description': NotRequired[str],
    'hostname': NotRequired[str],
    'position': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelDuckduckgoNewsResponseDoc = TypedDict('ModelDuckduckgoNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDuckduckgoNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDuckduckgoNewsResponse = TypedDict('ModelDuckduckgoNewsResponse', {
    'pagination': NotRequired[ModelDuckduckgoSearchPagination],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelDuckduckgoNewsResult]],
}, total=False)

ModelDuckduckgoNewsResult = TypedDict('ModelDuckduckgoNewsResult', {
    'excerpt': NotRequired[str],
    'position': NotRequired[int],
    'published_at': NotRequired[int],
    'relative_time': NotRequired[str],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelDuckduckgoImageResponseDoc = TypedDict('ModelDuckduckgoImageResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelDuckduckgoImageResponse],
    'msg': NotRequired[str],
}, total=False)

ModelDuckduckgoImageResponse = TypedDict('ModelDuckduckgoImageResponse', {
    'pagination': NotRequired[ModelDuckduckgoSearchPagination],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelDuckduckgoImageResult]],
}, total=False)

ModelDuckduckgoImageResult = TypedDict('ModelDuckduckgoImageResult', {
    'height': NotRequired[int],
    'hostname': NotRequired[str],
    'image_url': NotRequired[str],
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

DuckduckgoImageResponse = ModelDuckduckgoImageResponseDoc
DuckduckgoImageParams = TypedDict('DuckduckgoImageParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoNewsResponse = ModelDuckduckgoNewsResponseDoc
DuckduckgoNewsParams = TypedDict('DuckduckgoNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoSearchResponse = ModelDuckduckgoSearchResponseDoc
DuckduckgoSearchParams = TypedDict('DuckduckgoSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
    'time_range': NotRequired[Literal['d', 'w', 'm', 'y']],
    'safe_search': NotRequired[Literal['strict', 'moderate', 'off']],
}, total=False)

DuckduckgoShoppingResponse = ModelDuckduckgoShoppingResponseDoc
DuckduckgoShoppingParams = TypedDict('DuckduckgoShoppingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'region': NotRequired[str],
}, total=False)

DuckduckgoSuggestResponse = ModelDuckduckgoSuggestResponseDoc
DuckduckgoSuggestParams = TypedDict('DuckduckgoSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoVideoResponse = ModelDuckduckgoVideoResponseDoc
DuckduckgoVideoParams = TypedDict('DuckduckgoVideoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

class DuckduckgoGroup:
    @overload
    def image(self, **params: Unpack[DuckduckgoImageStreamParams]) -> BinaryIO: ...
    @overload
    def image(self, **params: Unpack[DuckduckgoImageTextResponseParams]) -> str: ...
    @overload
    def image(self, **params: Unpack[DuckduckgoImageDefaultParams]) -> DuckduckgoImageResponse: ...
    @overload
    def news(self, **params: Unpack[DuckduckgoNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[DuckduckgoNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[DuckduckgoNewsDefaultParams]) -> DuckduckgoNewsResponse: ...
    @overload
    def search(self, **params: Unpack[DuckduckgoSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[DuckduckgoSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[DuckduckgoSearchDefaultParams]) -> DuckduckgoSearchResponse: ...
    @overload
    def shopping(self, **params: Unpack[DuckduckgoShoppingStreamParams]) -> BinaryIO: ...
    @overload
    def shopping(self, **params: Unpack[DuckduckgoShoppingTextResponseParams]) -> str: ...
    @overload
    def shopping(self, **params: Unpack[DuckduckgoShoppingDefaultParams]) -> DuckduckgoShoppingResponse: ...
    @overload
    def suggest(self, **params: Unpack[DuckduckgoSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[DuckduckgoSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[DuckduckgoSuggestDefaultParams]) -> DuckduckgoSuggestResponse: ...
    @overload
    def video(self, **params: Unpack[DuckduckgoVideoStreamParams]) -> BinaryIO: ...
    @overload
    def video(self, **params: Unpack[DuckduckgoVideoTextResponseParams]) -> str: ...
    @overload
    def video(self, **params: Unpack[DuckduckgoVideoDefaultParams]) -> DuckduckgoVideoResponse: ...

OperationId = Literal[
    'duckduckgo-image',
    'duckduckgo-news',
    'duckduckgo-search',
    'duckduckgo-shopping',
    'duckduckgo-suggest',
    'duckduckgo-video',
]

class CrawloraClient:
    duckduckgo: DuckduckgoGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['duckduckgo-image'],
        params: DuckduckgoImageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoImageResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['duckduckgo-news'],
        params: DuckduckgoNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['duckduckgo-search'],
        params: DuckduckgoSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['duckduckgo-shopping'],
        params: DuckduckgoShoppingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoShoppingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['duckduckgo-suggest'],
        params: DuckduckgoSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['duckduckgo-video'],
        params: DuckduckgoVideoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoVideoResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['duckduckgo-image'],
        params: DuckduckgoImageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoImageResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['duckduckgo-news'],
        params: DuckduckgoNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['duckduckgo-search'],
        params: DuckduckgoSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['duckduckgo-shopping'],
        params: DuckduckgoShoppingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoShoppingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['duckduckgo-suggest'],
        params: DuckduckgoSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['duckduckgo-video'],
        params: DuckduckgoVideoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> DuckduckgoVideoResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class DuckDuckGoClient(CrawloraClient):
    def __enter__(self) -> DuckDuckGoClient: ...
    @overload
    def image(self, **params: Unpack[DuckduckgoImageStreamParams]) -> BinaryIO: ...
    @overload
    def image(self, **params: Unpack[DuckduckgoImageTextResponseParams]) -> str: ...
    @overload
    def image(self, **params: Unpack[DuckduckgoImageDefaultParams]) -> DuckduckgoImageResponse: ...
    @overload
    def news(self, **params: Unpack[DuckduckgoNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[DuckduckgoNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[DuckduckgoNewsDefaultParams]) -> DuckduckgoNewsResponse: ...
    @overload
    def search(self, **params: Unpack[DuckduckgoSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[DuckduckgoSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[DuckduckgoSearchDefaultParams]) -> DuckduckgoSearchResponse: ...
    @overload
    def shopping(self, **params: Unpack[DuckduckgoShoppingStreamParams]) -> BinaryIO: ...
    @overload
    def shopping(self, **params: Unpack[DuckduckgoShoppingTextResponseParams]) -> str: ...
    @overload
    def shopping(self, **params: Unpack[DuckduckgoShoppingDefaultParams]) -> DuckduckgoShoppingResponse: ...
    @overload
    def suggest(self, **params: Unpack[DuckduckgoSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[DuckduckgoSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[DuckduckgoSuggestDefaultParams]) -> DuckduckgoSuggestResponse: ...
    @overload
    def video(self, **params: Unpack[DuckduckgoVideoStreamParams]) -> BinaryIO: ...
    @overload
    def video(self, **params: Unpack[DuckduckgoVideoTextResponseParams]) -> str: ...
    @overload
    def video(self, **params: Unpack[DuckduckgoVideoDefaultParams]) -> DuckduckgoVideoResponse: ...

class AsyncDuckDuckGoClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncDuckDuckGoClient: ...
    duckduckgo: _AsyncDuckduckgoGroup
    @overload
    async def image(self, **params: Unpack[DuckduckgoImageStreamParams]) -> BinaryIO: ...
    @overload
    async def image(self, **params: Unpack[DuckduckgoImageTextResponseParams]) -> str: ...
    @overload
    async def image(self, **params: Unpack[DuckduckgoImageDefaultParams]) -> DuckduckgoImageResponse: ...
    @overload
    async def news(self, **params: Unpack[DuckduckgoNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[DuckduckgoNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[DuckduckgoNewsDefaultParams]) -> DuckduckgoNewsResponse: ...
    @overload
    async def search(self, **params: Unpack[DuckduckgoSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[DuckduckgoSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[DuckduckgoSearchDefaultParams]) -> DuckduckgoSearchResponse: ...
    @overload
    async def shopping(self, **params: Unpack[DuckduckgoShoppingStreamParams]) -> BinaryIO: ...
    @overload
    async def shopping(self, **params: Unpack[DuckduckgoShoppingTextResponseParams]) -> str: ...
    @overload
    async def shopping(self, **params: Unpack[DuckduckgoShoppingDefaultParams]) -> DuckduckgoShoppingResponse: ...
    @overload
    async def suggest(self, **params: Unpack[DuckduckgoSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[DuckduckgoSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[DuckduckgoSuggestDefaultParams]) -> DuckduckgoSuggestResponse: ...
    @overload
    async def video(self, **params: Unpack[DuckduckgoVideoStreamParams]) -> BinaryIO: ...
    @overload
    async def video(self, **params: Unpack[DuckduckgoVideoTextResponseParams]) -> str: ...
    @overload
    async def video(self, **params: Unpack[DuckduckgoVideoDefaultParams]) -> DuckduckgoVideoResponse: ...

class _AsyncDuckduckgoGroup:
    @overload
    async def image(self, **params: Unpack[DuckduckgoImageStreamParams]) -> BinaryIO: ...
    @overload
    async def image(self, **params: Unpack[DuckduckgoImageTextResponseParams]) -> str: ...
    @overload
    async def image(self, **params: Unpack[DuckduckgoImageDefaultParams]) -> DuckduckgoImageResponse: ...
    @overload
    async def news(self, **params: Unpack[DuckduckgoNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[DuckduckgoNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[DuckduckgoNewsDefaultParams]) -> DuckduckgoNewsResponse: ...
    @overload
    async def search(self, **params: Unpack[DuckduckgoSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[DuckduckgoSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[DuckduckgoSearchDefaultParams]) -> DuckduckgoSearchResponse: ...
    @overload
    async def shopping(self, **params: Unpack[DuckduckgoShoppingStreamParams]) -> BinaryIO: ...
    @overload
    async def shopping(self, **params: Unpack[DuckduckgoShoppingTextResponseParams]) -> str: ...
    @overload
    async def shopping(self, **params: Unpack[DuckduckgoShoppingDefaultParams]) -> DuckduckgoShoppingResponse: ...
    @overload
    async def suggest(self, **params: Unpack[DuckduckgoSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[DuckduckgoSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[DuckduckgoSuggestDefaultParams]) -> DuckduckgoSuggestResponse: ...
    @overload
    async def video(self, **params: Unpack[DuckduckgoVideoStreamParams]) -> BinaryIO: ...
    @overload
    async def video(self, **params: Unpack[DuckduckgoVideoTextResponseParams]) -> str: ...
    @overload
    async def video(self, **params: Unpack[DuckduckgoVideoDefaultParams]) -> DuckduckgoVideoResponse: ...

DuckduckgoImageDefaultParams = TypedDict('DuckduckgoImageDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoImageTextResponseParams = TypedDict('DuckduckgoImageTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoImageStreamParams = TypedDict('DuckduckgoImageStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoNewsDefaultParams = TypedDict('DuckduckgoNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoNewsTextResponseParams = TypedDict('DuckduckgoNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoNewsStreamParams = TypedDict('DuckduckgoNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoSearchDefaultParams = TypedDict('DuckduckgoSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
    'time_range': NotRequired[Literal['d', 'w', 'm', 'y']],
    'safe_search': NotRequired[Literal['strict', 'moderate', 'off']],
}, total=False)

DuckduckgoSearchTextResponseParams = TypedDict('DuckduckgoSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
    'time_range': NotRequired[Literal['d', 'w', 'm', 'y']],
    'safe_search': NotRequired[Literal['strict', 'moderate', 'off']],
}, total=False)

DuckduckgoSearchStreamParams = TypedDict('DuckduckgoSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
    'time_range': NotRequired[Literal['d', 'w', 'm', 'y']],
    'safe_search': NotRequired[Literal['strict', 'moderate', 'off']],
}, total=False)

DuckduckgoShoppingDefaultParams = TypedDict('DuckduckgoShoppingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'region': NotRequired[str],
}, total=False)

DuckduckgoShoppingTextResponseParams = TypedDict('DuckduckgoShoppingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'region': NotRequired[str],
}, total=False)

DuckduckgoShoppingStreamParams = TypedDict('DuckduckgoShoppingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'region': NotRequired[str],
}, total=False)

DuckduckgoSuggestDefaultParams = TypedDict('DuckduckgoSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'count': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoSuggestTextResponseParams = TypedDict('DuckduckgoSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'count': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoSuggestStreamParams = TypedDict('DuckduckgoSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'count': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoVideoDefaultParams = TypedDict('DuckduckgoVideoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoVideoTextResponseParams = TypedDict('DuckduckgoVideoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)

DuckduckgoVideoStreamParams = TypedDict('DuckduckgoVideoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'region': NotRequired[str],
}, total=False)
