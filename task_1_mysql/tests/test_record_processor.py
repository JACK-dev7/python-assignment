
import mysql.connector
import pytest
from unittest.mock import MagicMock, call

from services.record_processor import fetch_employees


def test_fetch_employees():
    """Test fetching records in multiple batches."""

    connection = MagicMock()
    cursor = MagicMock()

    connection.cursor.return_value = cursor

    cursor.fetchmany.side_effect = [
        [(10001, "Georgi"), (10002, "Bezalel")],
        [(10003, "Parto")],
        [],
    ]

    records = list(fetch_employees(connection, batch_size=2))

    assert records == [
        (10001, "Georgi"),
        (10002, "Bezalel"),
        (10003, "Parto"),
    ]

    cursor.fetchmany.assert_has_calls([
        call(2),
        call(2),
        call(2),
    ])

    cursor.close.assert_called_once()


@pytest.mark.parametrize(
    "batch_size",
    [0, -1, 1.5, True, "100"],
)
def test_invalid_batch_size(batch_size):
    """Test rejection of invalid batch sizes."""

    connection = MagicMock()

    with pytest.raises(ValueError):
        list(fetch_employees(connection, batch_size))

    connection.cursor.assert_not_called()


def test_database_error():
    """Test database error handling and cursor cleanup."""

    connection = MagicMock()
    cursor = MagicMock()

    connection.cursor.return_value = cursor
    cursor.fetchmany.side_effect = mysql.connector.Error(
        "Database error"
    )

    with pytest.raises(mysql.connector.Error):
        list(fetch_employees(connection))

    cursor.close.assert_called_once()
