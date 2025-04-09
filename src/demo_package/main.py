# src/demo_package/main.py

def greet(name: str) -> str:
    """
    Returns a simple greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.
    """
    return a + b

# Example of a function that might change in future versions
def feature_status() -> str:
    """Returns the status of a hypothetical feature."""
    return "Feature v1 is active."
