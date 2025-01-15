# pytest-presentation

Presentation given at @SMD-Bioinformatics-Lund on 2025-01-15

## Install pytest

```
# In yr env of choice:
pip install pytest
```

## Yr first test file:

By convention test files should be placed in a `tests/` dir in the project root directory.

### Running tests:

All tests:

```
pytest tests/
```

Specific test module:

```
pytest tests/test_foo.py
```

Specific test inside module:

```
pytest tests/test_foo.py::test_some_thing
```

### Options to pytest:

```
pytest -v            # more verbose output.
pytest -x:           # do not run more tests after first FAIL
pytest --maxfail=3   # stop running tets after three FAILs
```
