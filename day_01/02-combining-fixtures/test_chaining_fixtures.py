#!/usr/bin/env python3

"""
Show how to set up test conditions by chaining fixtures:

1. Create empty DB instance in fixture.
2. Populate with data from second fixture and pass to test.
3. Show that fixtures can be requested more than once by test.

4. Show simple initialized Flask app fixture in bjornWEB
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
    return SimpleDB()


@pytest.fixture()
def test_data():
    """
    Data for testing
    """
    sample_data = {"sample_id": "foo", "assay": "wgs_hg38", "group_id": "bar"}
    return sample_data


@pytest.fixture()
def initialized_db(empty_database, test_data):
    """
    SimpleDB instance w/ test data
    """
    empty_database.add(test_data)
    assert not empty_database.is_empty()
    return empty_database


def test_get_sample_by_sample_id(initialized_db, test_data):
    """
    Write test that fetches sample by sample id from a SimpleDB instance
    """
    assert initialized_db.get_sample_by_sample_id(test_data["sample_id"]) is not None


def test_get_sample_by_group_id():
    """
    Write test that fetches sample by group id from a SimpleDB instance
    """
