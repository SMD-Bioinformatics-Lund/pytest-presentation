# pytest tutorial 2025-02-06, day 2

## Intro to mocking

* What is mocking?

* Use cases:
  - Simulate slow parts of code to speed up tests
  - Bypass reliance on external systems
  - Isolate units of code for testing

## Example 1: Mocking simple external API response using monkeypatch

* `monkeypatch` is a fixture included with pytest -- no installation required.
* Useful for quick and simple replacement of object attributes, system environment variables,
  entries in dictionaries.

## Example 2: Mocking ssh/network calls in bjorn with pytest_mock

* `pytest-mock` is a wrapper around the standard library `unittest.mock`, 
  served through `mocker` fixture.
* More higher-level and feature rich compared to `monkeypatch`:
  - Allows detailed introspection of dependency usage:
      - Was my dependency called at all?
      - Was my dependency called/initialized with the correct arguments?
* Easier to simulate complex behavior or use mocking when chaining multiple calls


## Example 3: Mocking MongoDB using mongomock

* mongomock provides a lightweight in-memory simulation of a MongoDB database
* Simulates the PyMongo API, typically used by replacing a `pymongo.MongoClient` with `mongomock.MongoClient`


# If time permits:

* Show other built-in fixtures in pytest

## Q/A
