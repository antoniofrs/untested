from typing import Any, Dict

import requests
from untested.requester.model.request import Request

from untested.requester.validator.post_request import PostRequestAction



def send_request(method: str, url: str, headers: Dict[str, Any], body: str = "") -> PostRequestAction:
    return send_request(Request(method=method, url=url, headers=headers, body=body))


def send_request(request:Request) -> PostRequestAction:
    response = requests.request(
        method=request.method.value,
        url=request.url,
        data=request.body
    )
    return PostRequestAction(request , response)