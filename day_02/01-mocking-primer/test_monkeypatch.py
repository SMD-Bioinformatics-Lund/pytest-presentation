#!/usr/bin/env python3

"""
Use built-in monkeypatch fixture to

* Show how to bypass an expensive call by mocking

* Real example 1:
    - Avoiding ssh/scp-calls to hopper in bjorn
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
def fake_user_by_username_response(user_data): ...


@pytest.fixture()
def user_handler(monkeypatch, fake_user_by_username_response):
    """
    Initialized user thingie
    """
    user_handler = UserHandler()
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


def test_get_user_email(user_handler, user_data):
    """
    Test that get_user_email works while bypassing external api call with monkey patch
    """
    assert user_handler.get_user_email(user_data["username"]) == user_data["email"]
