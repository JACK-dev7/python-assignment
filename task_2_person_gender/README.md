
# Program 2 - Person Gender

## Objective

Implement an abstract Person class with Male and Female
subclasses that implement get_gender().

## Features

- Abstract base class using abc.
- Abstract method get_gender().
- Male and Female child classes.
- Type hints and docstrings.
- Unit testing using pytest.

## Project Structure

```text
task_2_person_gender/
├── src/
│   ├── __init__.py
│   └── person.py
├── tests/
│   ├── __init__.py
│   └── test_person.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

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

## Run

```bash
python -c "from src.person import Male, Female; print(Male().get_gender()); print(Female().get_gender())"
```

## Run Tests

```bash
python -m pytest -v
```

## PEP8 Check

```bash
python -m pycodestyle src tests
```
