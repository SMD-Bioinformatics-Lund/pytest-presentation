#!/usr/bin/env python3

"""
We've used monkeypatch to simulate data fetch from external api
to isolate get_user_email() for testing.

We're still paranoid though. We want to test that the correct api call is submitted to
requests.get without dispatching the actual request to the api.

1. Replace monkeypatch patches with mocker equivalent
2. Use mocker to check if requests.get inside fetch_user_by_username is called
   with correct api call
3. Use mocked response from response.get to simulate RuntimeError
"""

import pytest
import logging
import requests


# Custom Exception to signal api errors:
class ApiError(Exception): ...


class UserHandler:
    """
    A thingie that fetches some user data from external api and processes it
    """

    API_URL = "http://localhost:666"

    def __init__(self) -> None: ...

    def fetch_user_by_username(self, username: str) -> list[dict]:
        """
        Fetch and process a case from external api.
        """
        api_call = f"{self.API_URL}/users?username={username}"
        response = requests.get(api_call)

        if not response.ok:
            error_msg = "Unexpected error when fetching API data"
            logging.error(error_msg)
            raise ApiError(error_msg)

        json_data = response.json()
        return json_data

    def get_user_email(self, username: str) -> str:
        """
        fetch user email from external db
        """
        user_data = self.fetch_user_by_username(username).pop()
        return user_data["email"]


@pytest.fixture()
def fake_user_by_username_response(user_data):
    """
    Mock fetch_user_by_username response()
    """
    return lambda _: [user_data]


@pytest.fixture()
def user_handler():
    """
    Initialized user thingie
    """
    user_handler = UserHandler()
    return user_handler


@pytest.fixture()
def patched_user_handler(user_handler, monkeypatch, fake_user_by_username_response):
    monkeypatch.setattr(
        target=user_handler,
        name="fetch_user_by_username",
        value=fake_user_by_username_response,
    )
    return user_handler


@pytest.fixture()
def user_data():
    """
    Test user data
    """
    return {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {"lat": "-37.3159", "lng": "81.1496"},
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
    }


@pytest.fixture()
def api_url():
    return "http://localhost:666"


@pytest.fixture()
def user_api_call(api_url, user_data):
    return f"{api_url}/users?username={user_data['username']}"


def test_get_user_email(patched_user_handler, user_data):
    """
    Test that get_user_email works while bypassing external api call with monkey patch
    """
    assert (
        patched_user_handler.get_user_email(user_data["username"]) == user_data["email"]
    )


def test_check_if_correct_api_call_dispatched(
    user_handler, user_data, mocker, user_api_call
):

    class FakeResponse:
        ok = True

        def json(self):
            return [user_data]

    # 1. user mocker to mock requests.get
    patch_requests_get = mocker.patch("requests.get", return_value=FakeResponse())

    result = user_handler.get_user_email(user_data["username"])
    assert result == user_data["email"]
    patch_requests_get.assert_called_once_with(user_api_call)


def test_get_user_email_raises_error(user_handler, user_data, mocker, caplog):
    """
    Test that our function behaves as expected when api is unreachable
    """

    expected_error_msg = "Unexpected error when fetching API data"

    # Simulate failed api call:
    class FakeResponse:
        ok = False

        def json(self):
            return {}

    # Patch in FakeResponse as a returned value from requests.get()

    # 1. Ensure that ApiError exception is raised
    # 2. Ensure that correct error msg is logged
    # Ensure that correct msg is logged and that correct exception is raised

    # Is the  exception message as expected?

    # Is the correct err msg logged?
