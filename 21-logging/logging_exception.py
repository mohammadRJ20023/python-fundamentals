"""
Logging Exception

This example demonstrates logging an exception.
"""

import logging

logging.basicConfig(level=logging.ERROR)

try:

    result = 10 / 0

except ZeroDivisionError:

    logging.exception("An exception occurred.")