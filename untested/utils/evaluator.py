from untested.assertions.response_assertion import ResponseAssertion
from untested.model.request import Response


def evaluate_response_assertion(response: Response, assertion: ResponseAssertion) -> None:
    if (not assertion.evaluate(response)):
        print(f"\033[91mAssertion Failed: {assertion}\033[0m")
        exit(1)
    else:
        print(f"\033[92mAssertion Passed: {assertion}\033[0m")
