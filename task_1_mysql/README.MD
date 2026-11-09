# MySQL Employee Record Processor

A Python application that efficiently processes large volumes of employee records from a MySQL database using generators, batch fetching, and unbuffered cursors to minimize memory consumption.

## Features

- MySQL connectivity using `mysql-connector-python`.
- Generator-based record processing using `yield`.
- Configurable batch fetching using `fetchmany()`.
- Unbuffered database cursor (`buffered=False`).
- INI-based configuration management.
- Environment-based database credentials.
- Logging and exception handling.
- Unit testing using pytest and unittest.mock.

## Project Structure

```text
task_1_mysql/
├── config/
│   └── config.ini
├── database/
│   └── connection.py
├── services/
│   ├── __init__.py
│   └── record_processor.py
├── sample_data/
├── tests/
│   └── test_record_processor.py
├── main.py
├── requirements.txt
└── README.md
```

## Tech Stack

Python | MySQL | mysql-connector-python | Pytest | unittest.mock | ConfigParser

## Setup

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd task_1_mysql
```

**2. Create and activate a virtual environment**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

## Database Configuration

Configure `config/config.ini`:

```ini
[mysql]
host = localhost
port = 3306
user = root
database = employees
```

Set your database password in PowerShell:

```powershell
$env:DB_PASSWORD = "your_mysql_password"
```

**Sample Database:** [MySQL Employees Database](https://github.com/datacharmer/test_db)

Import the sample database into your local MySQL server before running the application.

## Run the Application

From the project root directory:

```bash
python main.py
```

The application connects to MySQL, fetches employee records in batches of 1,000, processes them incrementally, displays the first five records, and reports the total number of processed records.

## Run Tests

```bash
python -m pytest -v
```

Tests use mocked database connections, so a live MySQL connection is not required.

**Test coverage:**
- Successful fetching across multiple batches.
- Invalid batch-size validation.
- Database exception handling.
- Cursor cleanup.
- Verification of repeated `fetchmany()` calls.

## Key Concepts

| Concept | Purpose |
|---|---|
| Generators (`yield`) | Process records one at a time. |
| `fetchmany()` | Retrieve records in batches. |
| Unbuffered Cursor | Avoid full-result client-side buffering. |
| ConfigParser | Externalize database configuration. |
| Environment Variables | Protect database credentials. |
| pytest & MagicMock | Test database logic independently. |
| Logging & Exceptions | Improve debugging and reliability. |