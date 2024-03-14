from enum import Enum
from typing import Any

class ValidationStrategy(Enum):
    CONTAINS = 1
    IS_EXACTLY = 2
    

def test_body(strategy: ValidationStrategy, actual: Any, expected: Any) -> None:

    if(type(actual) != type(expected)):
        error_and_exit("'actual' and 'expected' must have the same type")

    if isinstance(actual, str):
        test_str_body(strategy, actual, expected)
    elif isinstance(actual, dict):
        error_and_exit("Unsupported")


def test_str_body(strategy: ValidationStrategy, actual:str, expected:str) -> None:
    if strategy == ValidationStrategy.CONTAINS:
        true_or_exit(actual in expected)
    elif strategy == ValidationStrategy.IS_EXACTLY:
        true_or_exit(actual == expected)


def true_or_exit(expression: bool) -> None:
    if(not expression):
       exit(0)

def error_and_exit(error:str) -> None:
    print(error)
    exit(0)