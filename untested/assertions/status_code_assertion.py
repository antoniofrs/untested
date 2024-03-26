from http import HTTPStatus
from typing import Union
from untested.assertions.response_assertion import ResponseAssertion

from untested.model.request import Response
from untested.model.status_code import StatusCodeType


class StatusCodeAssertion(ResponseAssertion):

    def __init__(self, expected: Union[int, HTTPStatus, str]) -> None:
        if isinstance(expected, int):
            self.expected = HTTPStatus(expected)
        elif isinstance(expected, HTTPStatus):
            self.expected = expected
        elif isinstance(expected, str):
            self.expected = HTTPStatus(int(expected))
        else:
            raise ValueError(
                "Unsupported type for 'status_code'. Expected str,int or HTTPStatus.")
        
    def __str__(self) -> str:
        return "Status code assertion"

class StatusCodeIs(StatusCodeAssertion):

    def __init__(self, expected: Union[int, HTTPStatus, str]) -> None:
        super().__init__(expected)

    def evaluate(self, response: Response) -> bool:
        return self.expected == response.status_code


class StatusCodeTypeIs(StatusCodeAssertion):

    def __init__(self, status_code_type: StatusCodeType) -> None:
        self.status_code_type = status_code_type

    def evaluate(self, response: Response) -> bool:
        return StatusCodeType.of(response.status_code) == self.status_code_type


