
import os
import configparser
import logging
from pathlib import Path

import mysql.connector

logger = logging.getLogger(__name__)

CONFIG_PATH = (
    Path(__file__).resolve().parent.parent
    / "config"
    / "config.ini"
)


def load_db_config():
    """Load database configuration from config.ini."""
    config = configparser.ConfigParser()

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_PATH}"
        )

    config.read(CONFIG_PATH)

    if not config.has_section("mysql"):
        raise ValueError("Missing [mysql] configuration section")

    return {
        "host": config.get("mysql", "host"),
        "port": config.getint("mysql", "port"),
        "user": config.get("mysql", "user"),
        "password": os.getenv("DB_PASSWORD"),
        "database": config.get("mysql", "database"),
    }


def create_connection():
    """Establish a connection with MySQL."""
    try:
        db_config = load_db_config()
        connection = mysql.connector.connect(**db_config)

        logger.info("MySQL connection established successfully")
        return connection

    except mysql.connector.Error:
        logger.exception("Failed to connect to MySQL")
        raise
