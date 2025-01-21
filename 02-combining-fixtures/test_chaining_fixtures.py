#!/usr/bin/env python3

"""
Show how to set up test conditions by chaining fixtures:

Create empty DB instance in fixture.
Populate with data from second fixture and pass to test.
"""


import pytest


class SimpleDB:
    def __init__(self):
        self.db: list[dict] = []

    def add(self, entry: dict):
        self.db.append(entry)

    def get_latest_entry(self) -> dict | None:
        if not self.db:
            return None

        idx_most_recent = len(self.db) - 1
        return self.db[idx_most_recent]


@pytest.fixture()
def empty_database():
    """
    SimpleDB instance w/o data
    """
    ...


@pytest.fixture()
def test_data():
    """
    Data for testing
    """
    ...


@pytest.fixture()
def initialized_db():
    """
    SimpleDB instance w/ test data
    """
    ...


def test_initialized_db():
    """
    Write test that confirms db contains sample.
    """
    ...
