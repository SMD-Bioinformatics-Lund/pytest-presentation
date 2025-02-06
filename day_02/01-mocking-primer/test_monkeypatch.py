#!/usr/bin/env python3

"""
Use built-in monkeypatch fixture to

* Show how to bypass an expensive call by mocking
* Show how to simulate runtime errors using mocking.

* Real example 1:
    - Avoiding ssh/scp-calls to hopper in bjorn
* Real example 2:
    - Mocking pymongo connections in flask apps (simplest example in bjornWeb)
"""

import pytest
import logging
import time


class Thingie:

    """
    A thingie with a slow data-fetch and process operation
    """

    def __init__(self) -> None:
        ...

    def do_thing_with_some_scout_case(self):
        """
        Fetch and process a case.
        """
        result = self._slow_api_call()

        # Raise error if case cannot be fetched:
        if not result:
            raise RuntimeError

        result["thing_done"] = True
        return result

    def _slow_api_call(self) -> dict:
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
def example_case():
    """
    Some test data
    """
    case_obj = {"case_id": "bar", "status": "active", "thing_done": True}
    return case_obj


def test_do_the_thing(thingie):
    """
    Test that do_thing works, but bypass the expensive _fetch_scout_case function
    """
    result = thingie.do_thing_with_some_scout_case()
    assert result["case_id"] == "foo"


def test_raise_exception_if_unable_to_retrieve_data():
    """
    Use monkeypatch on `_fetch_scout_case` to simulate a network error
    """
    ...
    with pytest.raises(RuntimeError, match="Simulated network error"):
        thingie.do_thing_with_some_scout_case()
