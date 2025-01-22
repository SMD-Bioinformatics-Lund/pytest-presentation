#!/usr/bin/env python3

"""
Show how to set up test conditions by chaining fixtures:

1. Create empty DB instance in fixture.
2. Populate with data from second fixture and pass to test.
"""


import pytest


class SimpleDB:
    def __init__(self):
        self.db: list[dict] = []

    def add(self, entry: dict):
        self.db.append(entry)

    def get_sample_by_sample_id(self, sample_id) -> dict | None:
        if not self.db:
            return None

        for sample in self.db:
            if sample["sample_id"] == sample_id:
                return sample

    def get_sample_by_group_id(self, group_id) -> dict | None:
        if not self.db:
            return None

        for sample in self.db:
            if sample["group_id"] == group_id:
                return sample

    def is_empty(self) -> bool:
        return len(self.db) == 0


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
    sample_data = {"sample_id": "foo", "assay": "wgs_hg38", "group_id": "bar"}


@pytest.fixture()
def initialized_db():
    """
    SimpleDB instance w/ test data
    """
    ...


def test_get_sample_by_sample_id():
    """
    Write test that fetches sample by sample id from a SimpleDB instance
    """
    ...


def test_get_sample_by_group_id():
    """
    Write test that fetches sample by group id from a SimpleDB instance
    """
