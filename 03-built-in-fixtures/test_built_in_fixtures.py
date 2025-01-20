#!/usr/bin/env python3
import pytest
import logging
from pathlib import Path


def write_hello_world_to_file(path: Path) -> None:
    path.write_text("Hello world!")


def test_write_hello_world():
    """
    Use tmp_dir
    """
    ...


def log_hello_world():
    logging.error("Hello world!")


def test_caplog():
    """
    Test that log_hello_world logs correct message
    """
    log_hello_world()
