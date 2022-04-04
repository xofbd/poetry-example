import pytest


@pytest.fixture
def pyproject_toml():
    with open("pyproject.toml", "r") as f:
        return f.read()
