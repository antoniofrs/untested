from http import HTTPStatus
from typing import Any

from untested.requester.model.request import Request
from untested.requester.validator.body_validator import ValidationStrategy, test_body

class RequestAssertions:

    def __init__(self, request: Request) -> None:
        self.request=request
        pass

    def body_contains(self, expected: Any) -> None:
        test_body(
            strategy = ValidationStrategy.CONTAINS,
            actual=self.request.body,
            expected=expected
        )

    def status_code_is(self, expected_status_code: HTTPStatus) -> None:
        print("status_code_is")
