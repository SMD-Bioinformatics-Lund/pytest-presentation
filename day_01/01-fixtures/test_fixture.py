"""
 1. Show how to make a fixture:
 2. Show how to pass a fixture to a test
 3. Move test_data fixtures and move to conftest.py
"""

import pytest


def check_coverage(test_data: dict, min_coverage: float):
    return test_data["coverage"] >= min_coverage


def check_contamination(test_data: dict, max_contamination: float):
    return test_data["contamination"] <= max_contamination


def check_insert_length(test_data: dict, min_insert_length: int):
    return test_data["insert_size"] >= min_insert_length


def test_check_coverage(test_data):
    assert check_coverage(test_data, 30) == True


def test_check_contamination(test_data):
    assert check_contamination(test_data, 0.01) == False


def test_check_fixture(test_data):
    assert type(test_data) == dict


# def test_check_insert_length(): ...
