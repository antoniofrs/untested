from http import HTTPMethod
from untested.assertions.body_assertion import BodyContains
from untested.assertions.status_code_assertion import StatusCodeIs, StatusCodeTypeIs
from untested.model.status_code import StatusCodeType
from untested.random.random_string import random_str
from untested.sender import send_request


response = send_request(
    method=HTTPMethod.POST,
    url="https://d5045373-edfd-4b19-8951-d15f98c61155.mock.pstmn.io/api/test",
    headers={},
    body={
        "test": random_str()
    }
).assert_that(
    BodyContains("test"),
    StatusCodeIs(200),
    StatusCodeTypeIs(StatusCodeType.SUCCESS)
)