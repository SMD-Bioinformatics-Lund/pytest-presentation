# pytest-presentation

Presentation given at @SMD-Bioinformatics-Lund on 2025-01-23, and on 2025-02-10

## Install pytest

```
# In yr env of choice:
pip install pytest
```

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
pytest -x            # do not run more tests after first FAIL
pytest --maxfail=3   # stop running tets after three FAILs
pytest --lf          # or --last-failed, only re-reun failed tests from previous run
pytest --ff          # or --failed-first, run the failures first and then the rest of the tests.
```
