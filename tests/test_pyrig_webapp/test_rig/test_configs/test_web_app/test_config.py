"""Test module."""

from pathlib import Path

from pyrig_webapp.rig.configs.web_app.config import WebAppConfigConfigFile


class TestWebAppConfigConfigFile:
    """Test class."""

    def test_content(self) -> None:
        """Test method."""
        assert WebAppConfigConfigFile.I.content()
        assert isinstance(WebAppConfigConfigFile.I.content(), str)
        assert WebAppConfigConfigFile.I.content().startswith(
            '"""Configuration for the web application."""',
        )

    def test_has_config(self) -> None:
        """Test method."""
        assert WebAppConfigConfigFile.I.has_config()

    def test_is_correct(self) -> None:
        """Test method."""
        assert WebAppConfigConfigFile.I.is_correct()

    def test_parent_path(self) -> None:
        """Test method."""
        assert WebAppConfigConfigFile.I.parent_path() == Path()

    def test_stem(self) -> None:
        """Test method."""
        assert WebAppConfigConfigFile.I.stem() == "rxconfig"
