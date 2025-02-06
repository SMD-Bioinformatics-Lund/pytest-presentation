import pytest


@pytest.fixture()
def test_data():
    foo_data = {
        "sample_id": "test_sample",
        "sample_type": "tumor",
        "coverage": 45,
        "contamination": 0.02,
        "insert_size": 150,
    }
    return foo_data
