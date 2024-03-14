from http import HTTPMethod
from untested.requester.sender import send_request


send_request(
    method=HTTPMethod.POST,
    url="test",
    headers={},
    body="test"
)

