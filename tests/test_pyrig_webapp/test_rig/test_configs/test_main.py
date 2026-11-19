"""Test module."""

from pyrig_webapp import main
from pyrig_webapp.rig.configs.main import MainConfigFile


class TestMainConfigFile:
    """Test class."""

    def test_copy_module(self) -> None:
        """Test method."""
        assert MainConfigFile.I.copy_module() is main

    def test_has_app(self) -> None:
        """Test method."""
        assert MainConfigFile.I.has_app()

    def test_is_correct(self) -> None:
        """Test method."""
        assert MainConfigFile.I.is_correct()
