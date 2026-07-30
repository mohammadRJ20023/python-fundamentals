"""
Log Format

This example demonstrates custom log formatting.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Application started.")
logging.warning("Low memory.")