#!/usr/bin/env python3
import pytest
import logging
from pathlib import Path


def write_hello_world_to_file(path: Path) -> None:
    """
    Write hello world to file at `path`
    """
    path.write_text("Hello world!")


def test_write_hello_world():
    """
    Use `tmp_dir` fixture to create a temp_file,
    log the path with the logging module
    Test that 'Hello world!' is written to file.
    """
    ...


def log_hello_world():
    logging.error("Hello world!")


def test_log_hello_world():
    """
    Use `caplog` fixture to check that log_hello_world logs
    correct message
    """
    log_hello_world()
