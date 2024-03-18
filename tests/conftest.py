"""PyTest configuration module. Defines useful fixtures, command line args."""

import logging
from pathlib import Path

import pytest
from etoolbox.utils.pudl import setup_access_key_for_ci

logger = logging.getLogger(__name__)


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add package-specific command line options to pytest.

    This is slightly magical -- pytest has a hook that will run this function
    automatically, adding any options defined here to the internal pytest options that
    already exist.
    """
    parser.addoption(
        "--sandbox",
        action="store_true",
        default=False,
        help="Flag to indicate that the tests should use a sandbox.",
    )


@pytest.fixture(scope="session")
def test_dir() -> Path:
    """Return the path to the top-level directory containing the tests.

    This might be useful if there's test data stored under the tests directory that
    you need to be able to access from elsewhere within the tests.

    Mostly this is meant as an example of a fixture.
    """
    return Path(__file__).parent


@pytest.fixture(scope="session")
def pudl_access_key_setup():  # noqa: PT004
    """Set up PUDL access key for testing.

    This is required for any test that requires access to the PUDL GCS bucket
    that runs in CI.
    """
    # disable the PUDL tests if etoolbox is not installed
    setup_access_key_for_ci()
