"""Test module."""

import reflex as rx

from pyrig_webapp import main
from pyrig_webapp.main import index


def test_docstring() -> None:
    """Test function."""
    assert main.__doc__ == """Project entry point."""


def test_index() -> None:
    """Test function."""
    assert isinstance(index(), rx.Component)
