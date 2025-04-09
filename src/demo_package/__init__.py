# src/demo_package/__init__.py

# The version is primarily managed in pyproject.toml by semantic-release,
# but defining it here can be useful for runtime access if needed.
# semantic-release does not automatically update this file.
# Consider using a tool like 'importlib.metadata' to get the version
# dynamically from the installed package metadata instead.
__version__ = "0.1.0"

# You can optionally expose functions/classes from submodules here
# from .main import greet

print(f"Initializing demo_package version {__version__}")
