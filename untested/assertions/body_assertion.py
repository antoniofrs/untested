import json
from typing import Any, Union

from untested.assertions.response_assertion import ResponseAssertion

from untested.model.request import Response


class BodyAssertion(ResponseAssertion):

    def __init__(self, expected: Union[str, dict[str, Any]]) -> None:
        if isinstance(expected, str):
            self.expected = expected
        elif isinstance(expected, dict):
            self.expected = json.dumps(expected)
        else:
            raise ValueError(
                "Unsupported type for 'body'. Expected str or dict[str, Any].")
        
    def __str__(self) -> str:
        return "Body assertion"


class BodyContains(BodyAssertion):

    def __init__(self, expected: Union[str, dict[str, Any]]) -> None:
        super().__init__(expected)

    def evaluate(self, response: Response) -> bool:
        return self.expected in response.body


class BodyIsExactly(BodyAssertion):

    def __init__(self, expected: Union[str, dict[str, Any]]) -> None:
        super().__init__(expected)

    def evaluate(self, response: Response) -> bool:
        return response.body == self.expected
    