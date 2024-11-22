#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""
import logging
import sys

from src.console_core.console import ConsoleRunner
from src.console_core.utils.front import make_front_console

logger = logging.getLogger(__name__)


def main():
    """Entrypoint."""
    try:
        utility = ConsoleRunner(console=make_front_console())
        utility.run()
    except KeyboardInterrupt:
        logger.debug("main menu exit code: 1")
        sys.exit(1)
    except Exception as e:
        logger.exception("main menu exception:", e)
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
