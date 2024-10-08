from abc import ABC, abstractmethod
from typing import Any
from requests import Response
from grailed_api.session import GrailedSession


class ApiService(ABC):
    _session = GrailedSession()

    """
    Base Service class that defines http utils
    """

    @abstractmethod
    def send_request(self, *args, verbose: bool, **kwargs) -> Response:
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
