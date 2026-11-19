"""Test module."""

from pathlib import Path

from pyrig_webapp.rig.configs.web_app import WebAppConfigFile


class TestWebAppConfigFile:
    """Test class."""

    def test_content(self) -> None:
        """Test method."""
        assert WebAppConfigFile.I.content()
        assert isinstance(WebAppConfigFile.I.content(), str)
        assert WebAppConfigFile.I.content().startswith(
            '"""Configuration for the web application."""',
        )

    def test_has_config(self) -> None:
        """Test method."""
        assert WebAppConfigFile.I.has_config()

    def test_is_correct(self) -> None:
        """Test method."""
        assert WebAppConfigFile.I.is_correct()

    def test_parent_path(self) -> None:
        """Test method."""
        assert WebAppConfigFile.I.parent_path() == Path()

    def test_stem(self) -> None:
        """Test method."""
        assert WebAppConfigFile.I.stem() == "rxconfig"
