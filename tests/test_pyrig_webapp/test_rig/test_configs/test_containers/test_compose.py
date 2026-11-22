"""Test module."""

from pyrig_webapp.rig.configs.containers.compose import ComposeConfigFile


class TestComposeConfigFile:
    """Test class."""

    def test_app_ports(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.app_ports() == ["127.0.0.1:3000:3000"]

    def test_frontend_port(self) -> None:
        """Test method."""
        expected_port = 3000
        assert ComposeConfigFile.I.frontend_port() == expected_port

    def test_loopback_ip(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.loopback_ip() == "127.0.0.1"

    def test_service_app_before(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.service_app_before() == {
            "build": {},
            "ports": ["127.0.0.1:3000:3000"],
        }
