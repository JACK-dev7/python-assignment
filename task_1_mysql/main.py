import logging

from database.connection import create_connection
from services.record_processor import fetch_employees

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    connection = create_connection()

    try:
        total_records = 0

        for index, record in enumerate(
            fetch_employees(connection, batch_size=1000),
            start=1,
        ):
            total_records = index

            # Display only the first 5 records.
            if index <= 5:
                print(record)

        print(f"\nTotal records processed: {total_records}")

    finally:
        connection.close()
        logger_message = "Database connection closed"
        logging.info(logger_message)


if __name__ == "__main__":
    main()
