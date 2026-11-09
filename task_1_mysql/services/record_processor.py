
import logging

import mysql.connector

logger = logging.getLogger(__name__)


def fetch_employees(connection, batch_size=1000):
    """
    Fetch employee records incrementally using a generator.

    Args:
        connection: Active MySQL database connection.
        batch_size: Number of records fetched per batch.

    Yields:
        Individual employee records.
    """
    if (
        isinstance(batch_size, bool)
        or not isinstance(batch_size, int)
        or batch_size <= 0
    ):
        raise ValueError("batch_size must be a positive integer")

    cursor = None
    total_records = 0

    try:
        # Unbuffered cursor avoids buffering the entire result.
        cursor = connection.cursor(buffered=False)

        cursor.execute(
            """
            SELECT emp_no, first_name, last_name, hire_date
            FROM employees
            ORDER BY emp_no
            """
        )

        logger.info("Started fetching employee records")

        while True:
            records = cursor.fetchmany(batch_size)

            if not records:
                break

            for record in records:
                total_records += 1
                yield record

        logger.info(
            "Successfully fetched %d employee records",
            total_records,
        )

    except mysql.connector.Error:
        logger.exception("Error while fetching employee records")
        raise

    finally:
        if cursor is not None:
            cursor.close()
            logger.info("Database cursor closed")
