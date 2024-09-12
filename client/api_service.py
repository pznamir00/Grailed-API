from abc import ABC, abstractmethod
from typing import Any
from requests import Response


class ApiService(ABC):
    @abstractmethod
    def send_request(self, *args, **kwargs) -> Response:
        pass

    @abstractmethod
    def parse_response(self, response: Response) -> Any:
        return response.json()
