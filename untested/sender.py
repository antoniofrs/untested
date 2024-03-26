from http import HTTPMethod
from typing import Any, BinaryIO, Dict, List, Mapping, Optional, Union

import requests
from untested.assertions.post_request import PostRequestAction

from untested.model.request import Request,  convert_response


def send_request(
        method: HTTPMethod = HTTPMethod.GET, 
        url: str = "", 
        headers: Dict[str, str] = {} , 
        body: Dict[str, str] = {},
        files:Dict[str, BinaryIO] = {}
    ) -> PostRequestAction:
    request = Request(method=method, url=url, headers=headers,body=body,files=files)
    return send(request)
    

def send(request: Request) -> PostRequestAction:
    response = requests.request(
            method=request.method,
            url=request.url,
            headers=request.headers,
            data=request.body,
            files=request.files
        )
    return PostRequestAction(request , convert_response(response))

