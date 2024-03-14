from untested.requester.model.request import Request
from untested.requester.validator.request_validator import RequestAssertions


class PostRequestAction:

    def __init__(self, request: Request , response: ) -> None:
        self.request = request
        pass

    def and_than_assert(self) -> RequestAssertions:
        return RequestAssertions(self.request)