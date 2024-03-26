import ast
from dataclasses import dataclass, field
from http import HTTPMethod, HTTPStatus
import json
from typing import Any, BinaryIO, Dict, Union

import requests


@dataclass
class Request:
    method: HTTPMethod
    url: str
    headers: Dict[str, str] = field(default_factory=dict)
    body: Union[Dict[str, str], str] = ""
    files: Dict[str, BinaryIO] = field(default_factory=dict)


@dataclass
class Response:
    status_code: HTTPStatus
    headers: Any
    body: Union[Dict[str, str], str]



def convert_response(requests_response: requests.Response) -> Response:
    http_response = Response(
        status_code=HTTPStatus(requests_response.status_code),
        headers=requests_response.headers,
        body=convert_body(requests_response.text)
    )
    return http_response


def convert_body(body: str) -> Union[Dict[str, str], str]:
    try:
        dictionary = ast.literal_eval(body)
        if isinstance(dictionary, dict):
            return dictionary
    except (SyntaxError, ValueError):
        pass
    return body


def print_body(body: Union[Dict[str, str], str]) -> str:
    if isinstance(body, dict):
        return json.dumps(body, indent=4)
    else:
        return body
    
def print_http_status(status: HTTPStatus) -> str:
    return f"{status.value} ({status.name.capitalize()})"