"""
Logging Levels

This example demonstrates different logging levels.
"""

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message.")
logging.info("Information message.")
logging.warning("Warning message.")
logging.error("Error message.")
logging.critical("Critical message.")