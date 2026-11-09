
# Program 4 - Squares Using Map and Lambda

## Objective

Generate a list of squares of numbers from 1 to 20
using Python's map() and lambda.

## Implementation

- range() generates numbers from 1 to 20.
- lambda calculates the square of each number.
- map() applies the lambda function.
- list() converts the map iterator into a list.

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

## Run Tests

```bash
python -m pytest -v
```

## PEP8 Check

```bash
python -m pycodestyle src tests
```
