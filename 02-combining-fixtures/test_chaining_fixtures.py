#!/usr/bin/env python3

import pytest

# 1. Show how to chain fixtures


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
    ...


@pytest.fixture()
def test_data():
    ...


@pytest.fixture()
def initialized_db():
    ...


def test_db_add():
    ...
