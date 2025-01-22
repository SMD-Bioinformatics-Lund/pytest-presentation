"""
 1. Show how to make a fixture:
 2. Show how to pass a fixture to a test
 3. Move test_data fixtures and move to conftest.py
 (4. Use requests fixture to fetch multiple test cases?)
"""


def check_coverage(test_data: dict, min_coverage: float):
    return test_data["coverage"] >= min_coverage


def check_contamination(test_data: dict, max_contamination: float):
    return test_data["contamination"] <= max_contamination


def check_insert_length(test_data: dict, min_insert_length: int):
    return test_data["insert_size"] >= min_insert_length


# def test_check_coverage():
#     test_data = {
#         "sample_id": "test_sample",
#         "sample_type": "tumor",
#         "coverage": 45,
#         "contamination": 0.02,
#         "insert_size": 150,
#     }
#     ...


# def test_check_coverage(): ...

# def test_check_contamination(): ...

# def test_check_insert_length(): ...
