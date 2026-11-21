"""Test module."""

from pyrig_webapp.rig.configs.containers.compose import ComposeConfigFile


class TestComposeConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.configs() == {
            "services": {
                "app": {
                    "build": {},
                    "ports": ["127.0.0.1:3000:3000"],
                },
            },
        }
        assert ComposeConfigFile.I.load() == ComposeConfigFile.I.configs()

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
