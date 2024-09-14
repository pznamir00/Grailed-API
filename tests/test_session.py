from unittest.mock import MagicMock, patch
import pytest
from grailed_api.exceptions.http_error import HttpError
from grailed_api.session.session import GrailedSession


class TestSession:
    @patch("grailed_api.session.session.Session.request", return_value=MagicMock(status_code=200))
    def test_request_calls_super_request(self, super_request: MagicMock):
        session = GrailedSession()
        session.request("POST", "https://url", verbose=False)
        super_request.assert_called_once()

    @patch("grailed_api.session.session.Session.request", return_value=MagicMock(status_code=200))
    def test_request_adds_headers(self, super_request: MagicMock):
        session = GrailedSession()
        session.request("POST", "https://url", verbose=False)
        assert len(super_request.call_args.kwargs["headers"]) == 11

    @patch("grailed_api.session.session.Session.request", return_value=MagicMock(status_code=200))
    @patch("grailed_api.session.session.pprint")
    def test_request_shows_request_on_verbose(self, _: MagicMock, pprint: MagicMock):
        session = GrailedSession()
        session.request("POST", "https://url", verbose=True)
        pprint.assert_called()

    @patch(
        "grailed_api.session.session.Session.request",
        return_value=MagicMock(status_code=401, json=lambda: {}),
    )
    def test_request_captures_error(self, _: MagicMock):
        with pytest.raises(HttpError):
            session = GrailedSession()
            session.request("POST", "https://url", verbose=False)

    @patch("grailed_api.session.session.Session.request", return_value=MagicMock(status_code=200))
    def test_request_stringifies_data(self, super_request: MagicMock):
        session = GrailedSession()
        session.request("POST", "https://url", data={"data": True}, verbose=False)
        assert super_request.call_args.kwargs["data"] == '{"data": true}'
