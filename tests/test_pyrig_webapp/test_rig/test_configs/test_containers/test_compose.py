"""Test module."""

from pyrig_webapp.rig.configs.containers.compose import ComposeConfigFile


class TestComposeConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I._configs() == {  # noqa: SLF001
            "name": ComposeConfigFile.I.name(),
            "services": ComposeConfigFile.I.services_configs(),
            "volumes": {"web-server-data": {}},
        }

    def test_app_healthcheck(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.app_healthcheck() == {
            "test": [
                "CMD",
                "python",
                "-c",
                (
                    "from urllib.request import urlopen\n"
                    "urlopen('http://localhost:3000/ping')"
                ),
            ],
        }

    def test_configs(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.configs() == {
            "name": ComposeConfigFile.I.name(),
            "services": ComposeConfigFile.I.services_configs(),
            "volumes": {"web-server-data": {}},
        }

    def test_service(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.service(
            environment={"MODE": "production"},
        ) == {
            "environment": {"MODE": "production"},
            "restart": "unless-stopped",
            "cap_drop": ["ALL"],
            "security_opt": ["no-new-privileges:true"],
        }
        assert (
            ComposeConfigFile.I.service(
                restart="always",
            )["restart"]
            == "always"
        )

    def test_service_app_settings(self) -> None:
        """Test method."""
        assert "healthcheck" in ComposeConfigFile.I.service_app_settings()

    def test_service_web_server(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.service_web_server() == {
            "image": "docker.io/library/caddy:latest",
            "environment": {
                "SITE_ADDRESS": "${SITE_ADDRESS:-localhost}",
            },
            "ports": ["8080:80", "8443:443", "8443:443/udp"],
            "volumes": ["./caddy:/etc/caddy:ro", "web-server-data:/data"],
            "restart": "unless-stopped",
            "healthcheck": ComposeConfigFile.I.web_server_healthcheck(),
            "cap_drop": ["ALL"],
            "cap_add": ["NET_BIND_SERVICE"],
            "security_opt": ["no-new-privileges:true"],
            "pull_policy": "always",
        }

    def test_service_web_server_settings(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.service_web_server_settings() == {
            "image": "docker.io/library/caddy:latest",
            "pull_policy": "always",
            "environment": {"SITE_ADDRESS": "${SITE_ADDRESS:-localhost}"},
            "ports": ["8080:80", "8443:443", "8443:443/udp"],
            "volumes": ["./caddy:/etc/caddy:ro", "web-server-data:/data"],
            "healthcheck": ComposeConfigFile.I.web_server_healthcheck(),
            "cap_add": ["NET_BIND_SERVICE"],
        }

    def test_services(self) -> None:
        """Test method."""
        compose = ComposeConfigFile.I
        assert compose.services() == (
            compose.service_app,
            compose.service_web_server,
        )
        assert compose.services_configs() == {
            "app": compose.service_app(),
            "web-server": compose.service_web_server(),
        }

    def test_web_server_data_volume(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.web_server_data_volume() == "web-server-data"

    def test_web_server_healthcheck(self) -> None:
        """Test method."""
        assert ComposeConfigFile.I.web_server_healthcheck() == {
            "test": ["CMD", "curl", "--fail", "http://localhost:2019/config/"],
        }
