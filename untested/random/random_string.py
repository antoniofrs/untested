import random
import string
import uuid

dictionary = string.ascii_letters + string.digits + string.punctuation


def random_str(length: int = 10) -> str:
    return ''.join(random.choice(dictionary) for _ in range(length))

def random_email(length: int = 10, url:str = "test.it") -> str:
    return f"{random_str(length)}@{url}" 

def random_uuid() -> str:
    return str(uuid.uuid4())