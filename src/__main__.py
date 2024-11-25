#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Program entry point."""
import os

from src.main import main


def run() -> None:
    """Run the main function."""
    os.environ["TERM"] = "xterm"
    main()


if __name__ == "__main__":
    # Run with: `bash python -m src`
    run()
