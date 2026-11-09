
# Program 3 - Remove Duplicates

## Objective

Remove duplicate elements from a list while preserving
the original order of first occurrences.

## Approach

- Use a set to track previously encountered values.
- Use a list to maintain insertion order.
- Skip values that have already been encountered.

## Complexity

- Time: O(n) average
- Space: O(n)

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
