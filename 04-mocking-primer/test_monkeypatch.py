#!/usr/bin/env python3

import pytest
import logging
import time

"""
Simple example using magickmock to bypass time-consuming function in tests
"""


class Thingie:

    """
    A thingie with a slow data-fetch and process operation
    """

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

    def _some_other_function(self, x, y):
        ...


@pytest.fixture()
def thingie():
    """
    Initialized thingie
    """
    return Thingie()


@pytest.fixture()
def test_case():
    """
    Some test data
    """
    case_obj = {"case_id": "bar", "status": "active", "thing_done": True}
    return case_obj


def test_do_the_thing(thingie):
    """ """
    result = thingie.do_thing_with_some_scout_case()
    assert result["case_id"] == "foo"


def test_raise_exception_if_unable_to_retrieve_data():
    """
    Use monkeypatch on `_fetch_scout_case` to simulate a network error
    """
    ...
    with pytest.raises(RuntimeError, match="Simulated network error"):
        thingie.do_thing_with_some_scout_case()
