"""Test module."""

from pathlib import Path

from pyrig_webapp.rig.configs.web_app.server import WebServerConfigFile


class TestWebServerConfigFile:
    """Test class."""

    def test_content(self) -> None:
        """Test method."""
        expected = """{$SITE_ADDRESS} {
	reverse_proxy app:3000
}
"""
        assert WebServerConfigFile.I.content() == expected

    def test_extension(self) -> None:
        """Test method."""
        assert WebServerConfigFile.I.extension() == ""

    def test_extension_separator(self) -> None:
        """Test method."""
        assert WebServerConfigFile.I.extension_separator() == ""

    def test_parent_path(self) -> None:
        """Test method."""
        assert WebServerConfigFile.I.parent_path() == Path("caddy")

    def test_stem(self) -> None:
        """Test method."""
        assert WebServerConfigFile.I.stem() == "Caddyfile"
