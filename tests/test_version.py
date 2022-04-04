import re

from tempconv import __version__


def test_version(pyproject_toml):
    """
    GIVEN the project's pyproject.toml file
    WHEN the version field is compared to __version__
    THEN the version strings match
    """
    version_pyproject_toml = (
        re.search(r'\bversion = "(.+)\b', pyproject_toml)
        .group(1)
    )

    assert version_pyproject_toml == __version__
