"""Test module."""

from pathlib import Path

from pyrig.rig.tools.base.tool import Group

from pyrig_webapp.rig.tools.web_app.server import WebServer


class TestWebServer:
    """Test class."""

    def test_config_dir(self) -> None:
        """Test method."""
        assert WebServer.I.config_dir() == Path("caddy")

    def test_container_image(self) -> None:
        """Test method."""
        assert WebServer.I.container_image() == "docker.io/library/caddy:latest"

    def test_dev_dependencies(self) -> None:
        """Test method."""
        assert WebServer.I.dev_dependencies() == ()

    def test_group(self) -> None:
        """Test method."""
        assert WebServer.I.group() == Group.TOOLING

    def test_healthcheck_url(self) -> None:
        """Test method."""
        assert WebServer.I.healthcheck_url() == "http://localhost:2019/config/"

    def test_http_container_port(self) -> None:
        """Test method."""
        expected = 80
        assert WebServer.I.http_container_port() == expected

    def test_http_host_port(self) -> None:
        """Test method."""
        expected = 8080
        assert WebServer.I.http_host_port() == expected

    def test_https_container_port(self) -> None:
        """Test method."""
        expected = 443
        assert WebServer.I.https_container_port() == expected

    def test_https_host_port(self) -> None:
        """Test method."""
        expected = 8843
        assert WebServer.I.https_host_port() == expected

    def test_image_url(self) -> None:
        """Test method."""
        assert (
            WebServer.I.image_url()
            == "https://img.shields.io/badge/caddy-0059D1?logo=caddy&logoColor=22B638"
        )

    def test_link_url(self) -> None:
        """Test method."""
        assert WebServer.I.link_url() == "https://github.com/caddyserver/caddy"

    def test_name(self) -> None:
        """Test method."""
        assert WebServer.I.name() == "caddy"

    def test_site_address_env_var(self) -> None:
        """Test method."""
        assert WebServer.I.site_address_env_var() == "SITE_ADDRESS"
