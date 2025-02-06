# pytest tutorial 2025-02-06, day 2

## Intro to mocking

* What is mocking?

* Use cases:
  - Simulate slow parts of code to speed up tests
  - Bypass reliance on external systems
  - Isolate units of code for testing

## Example 1: Mocking simple API using monkeypatch fixture

* Use monkeypatch fixture to test function taht relies on data from external api

## Example 2: Mocking ssh/network calls in bjorn with pytest_mock

* use mocker fixture to bypass ssh/scp calls in bjorn 
* use same fixture to check that subprocess.run has been called with correct args

## Example 3: Mocking MongoDB using mongomock

* Show how mongomock is used in breaxpres

# If time permits:

* Show other built-in fixtures in pytest

## Q/A
