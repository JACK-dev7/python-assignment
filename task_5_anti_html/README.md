
# Program 5 - Anti HTML

## Objective

Download HTML content from a URL, remove HTML tags,
and print the extracted text.

## Features

- HTTP requests using requests.
- HTML parsing using BeautifulSoup.
- Configurable request timeout.
- Logging and exception handling.
- Unit tests using mocked HTTP requests.

## Setup

```bash
python -m venv venv
```

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Execute

```bash
python -m src.anti_html https://example.com
```

## Run Tests

```bash
python -m pytest -v
```

## PEP8 Check

```bash
python -m pycodestyle src tests
```
