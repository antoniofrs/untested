from enum import Enum


class StatusCodeType(Enum):
    INFORMATIONAL = 1
    SUCCESS = 2
    REDIRECTION = 3
    CLIENT_ERROR = 4
    SERVER_ERROR = 5

    @classmethod
    def of(self, status_code: int) -> 'StatusCodeType':
        if 100 <= status_code < 200:
            return StatusCodeType.INFORMATIONAL
        elif 200 <= status_code < 300:
            return StatusCodeType.SUCCESS
        elif 300 <= status_code < 400:
            return StatusCodeType.REDIRECTION
        elif 400 <= status_code < 500:
            return StatusCodeType.CLIENT_ERROR
        elif 500 <= status_code < 600:
            return StatusCodeType.SERVER_ERROR
        else:
            raise ValueError("Invalid status code")