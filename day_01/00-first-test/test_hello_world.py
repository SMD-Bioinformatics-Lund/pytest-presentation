#!/usr/bin/env python3

# 1. Show simple test
# 2. Show multiple tests per module and how to run specific tests within that module.
# 3. Show how to parametrize tests.


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


# Add test for add below:
def test_add():
    assert add(2, 2) == 4
    assert add(2, 3) == 5
    assert add(3, 3) == 6


# Add test for subtract below
def test_subtract():
    assert subtract(1, 1) == 0
