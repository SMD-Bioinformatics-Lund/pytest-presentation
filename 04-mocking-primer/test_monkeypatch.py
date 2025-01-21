#!/usr/bin/env python3

import pytest
import logging
import time

"""
Simple example using magickmock to bypass time-consuming function in tests
"""


class ThingieThatDoesThing:
    def __init__(self) -> None:
        pass

    def do_thing_with_some_scout_case(self):
        """
        Fetch and process a case.
        """
        result = self._fetch_scout_case()

        if not result:
            raise RuntimeError

        result["thing_done"] = True
        return result

    def _fetch_scout_case(self) -> dict:
        """
        Slow network call. We don't want this to run in our tests.
        """
        logging.info("Fetching case...")
        time.sleep(15)

        case_obj = {"case_id": "foo", "status": "archived"}

        return case_obj


@pytest.fixture()
def thingie():
    return ThingieThatDoesThing()


@pytest.fixture()
def test_case():
    case_obj = {"case_id": "bar", "status": "active", "thing_done": True}
    return case_obj


@pytest.fixture()
def patched_thingie():
    ...


def test_do_the_thing(patched_thingie):
    result = patched_thingie.do_thing_with_some_scout_case()
    assert result["case_id"] == "foo"
    assert result["thing_done"]


def test_fetch_scout_case_called_only_once():
    ...


def test_raise_exception_if_unable_to_retrieve_data():
    ...
    with pytest.raises(RuntimeError, match="Simulated network error"):
        thingie.do_thing_with_some_scout_case()
