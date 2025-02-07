#!/usr/bin/env python3

"""
We've used monkeypatch to simulate data fetch from external api
to isolate get_user_email() for testing.

We're still paranoid though. We want to test that the correct api call is submitted to
requests.get without dispatching the actual request to the api.
"""

import pytest
import logging
import requests


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
            raise RuntimeError()

        json_data = response.json()
        return json_data

    def get_user_email(self, username: str) -> str:
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


def test_get_user_email(patched_user_handler, user_data):
    """
    Test that get_user_email works while bypassing external api call with monkey patch
    """
    assert (
        patched_user_handler.get_user_email(user_data["username"]) == user_data["email"]
    )


def test_user_api_call_is_correct(mocker): ...
