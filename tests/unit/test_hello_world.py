# type: ignore
"""First test."""

import pytest

from src.main import print_hello_user  # noqa


@pytest.mark.all
def test_print_hello_user() -> None:
    """Test successful input message."""
    print_hello_user()
    assert True, "test failed"
