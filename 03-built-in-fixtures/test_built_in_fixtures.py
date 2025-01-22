#!/usr/bin/env python3
import pytest
import logging
from pathlib import Path

LOG = logging.getLogger(__name__)

# Show some examples of built-in fixtures:

def write_hello_world_to_file(path: Path) -> None:
    """
    Write hello world to file at `path`
    """
    path.write_text("Hello world!")


def test_write_hello_world():
    """
    Use `tmp_path` fixture to create a temp_file,
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


# Show autouse, scope, teardown

@pytest.fixture(autouse=True)
def setup_db():
    LOG.info("Connecting to the test database...")
    # yield
    # LOG.info("This is a teardown.")

def test_query():
    LOG.info("Running a query.")
    assert True

def test_other_query():
    LOG.error("Running another query.")
    assert True
