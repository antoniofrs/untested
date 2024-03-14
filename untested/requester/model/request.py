from dataclasses import dataclass
from http import HTTPMethod, HTTPStatus
from typing import Any

from requester.validator.request_validator import RequestValidator


@dataclass
class Request:
    method: HTTPMethod
    url: str
    headers: dict[str, Any]
    body: str = ""

    def assert_that(self) -> RequestValidator:
        return RequestValidator(self)


@dataclass
class Response:
    status_code: HTTPStatus
    headers: dict
    body: str