"""
Log To File

This example demonstrates writing logs to a file.
"""

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application started.")
logging.warning("Low disk space.")
logging.error("Connection failed.")