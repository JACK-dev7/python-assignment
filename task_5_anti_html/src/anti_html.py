
import argparse
import logging

import requests
from bs4 import BeautifulSoup

from src.config import REQUEST_TIMEOUT


logger = logging.getLogger(__name__)


def strip_html(url: str) -> str:
    """
    Download HTML from a URL and return text without HTML tags.

    Args:
        url: URL of the webpage.

    Returns:
        Extracted text from the HTML document.

    Raises:
        ValueError: If the URL is empty.
        requests.RequestException: If the HTTP request fails.
    """
    if not url or not url.strip():
        raise ValueError("URL cannot be empty")

    logger.info("Downloading HTML from %s", url)

    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return soup.get_text(separator="\n", strip=True)


def main() -> None:
    """Parse command-line arguments and print extracted HTML text."""
    parser = argparse.ArgumentParser(
        description="Download HTML and extract text without tags."
    )
    parser.add_argument("url", help="URL of the webpage")

    args = parser.parse_args()

    try:
        text = strip_html(args.url)
        print(text)

    except ValueError as error:
        logger.error("Invalid input: %s", error)
        raise SystemExit(1) from error

    except requests.RequestException as error:
        logger.error("Failed to download webpage: %s", error)
        raise SystemExit(1) from error


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()
