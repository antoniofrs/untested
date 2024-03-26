import json
from untested.assertions.response_assertion import ResponseAssertion
from untested.model.request import Request, Response, print_body, print_http_status
from untested.utils.evaluator import evaluate_response_assertion


class PostRequestAction:

    def __init__(self, request: Request , response: Response):
        self.request = request
        self.response = response

    def assert_that(self, *assertions: ResponseAssertion) -> 'PostRequestAction':
        for assertion in assertions:
            evaluate_response_assertion(assertion=assertion, response=self.response)        
        return self

    def get_request(self) -> Request:
        return self.request
    
    def get_response(self) -> Response:
        return self.response
    
    def __str__(self) -> str:
        return f"RESPONSE STATUS: {print_http_status(self.response.status_code)}\n" \
               f"RESPONSE BODY:\n{print_body(self.response.body)}"