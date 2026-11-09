
from unittest.mock import Mock, patch

import pytest
import requests

from src.anti_html import strip_html


def test_strip_html_success():
    html = """
    <html>
        <body>
            <h1>Hello World</h1>
            <p>Welcome to Python</p>
        </body>
    </html>
    """

    mock_response = Mock()
    mock_response.text = html

    with patch("src.anti_html.requests.get",
               return_value=mock_response) as mock_get:
        result = strip_html("https://example.com")

    assert result == "Hello World\nWelcome to Python"
    mock_get.assert_called_once_with(
        "https://example.com",
        timeout=10
    )


def test_empty_url():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        strip_html("")


def test_whitespace_url():
    with pytest.raises(ValueError, match="URL cannot be empty"):
        strip_html("   ")


def test_http_error():
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = (
        requests.HTTPError("404 Not Found")
    )

    with patch("src.anti_html.requests.get",
               return_value=mock_response):
        with pytest.raises(requests.HTTPError):
            strip_html("https://example.com")


def test_connection_error():
    with patch(
        "src.anti_html.requests.get",
        side_effect=requests.ConnectionError("Connection failed")
    ):
        with pytest.raises(requests.ConnectionError):
            strip_html("https://example.com")
