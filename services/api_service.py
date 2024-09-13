from abc import ABC, abstractmethod
from typing import Any
from requests import Response


class ApiService(ABC):
    """
    Base Service class that defines http utils
    """

    @abstractmethod
    def send_request(self, *args, **kwargs) -> Response:
        """Sends http requests and returns Response object

        Returns:
            Response: request result
        """

    @abstractmethod
    def parse_response(self, response: Response) -> Any:
        """Converts http response object to final data

        Args:
            response (Response): http response object

        Returns:
            Unknown: data
        """
        return response.json()
