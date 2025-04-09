# tests/test_main.py
import pytest
from demo_package.main import greet, add, feature_status

def test_greet():
    """Tests the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Cline") == "Hello, Cline!"

def test_add():
    """Tests the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_feature_status():
    """Tests the initial feature status."""
    # This test might need updating if the feature_status function changes
    assert feature_status() == "Feature v1 is active."

# Example of a test that might fail if a breaking change occurs
# def test_add_strings_fail():
#     """Example test that would fail if 'add' changed unexpectedly."""
#     with pytest.raises(TypeError):
#         add("a", "b") # This assumes add only works with numbers
