from abc import ABC, abstractmethod

from untested.model.request import Response


class ResponseAssertion(ABC):

    @abstractmethod
    def evaluate(self, response: Response) -> bool:
        pass

    

