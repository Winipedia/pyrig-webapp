"""Web server integration for generated web applications."""

from pathlib import Path
from typing import override

from pyrig.rig.tools.base.tool import Group, Tool


class WebServer(Tool):
    """Caddy reverse-proxy integration and container image."""

    @override
    def dev_dependencies(self) -> tuple[str, ...]:
        """Return no Python dependencies for the containerized proxy."""
        return ()

    @override
    def group(self) -> str:
        """Return the tooling badge group."""
        return Group.TOOLING

    @override
    def image_url(self) -> str:
        """Return the web server badge image URL."""
        return f"https://img.shields.io/badge/{self.shield_name()}-0059D1?logo=caddy&logoColor=22B638"

    @override
    def link_url(self) -> str:
        """Return the web server repository URL."""
        return "https://github.com/caddyserver/caddy"

    @override
    def name(self) -> str:
        """Return the web server executable name."""
        return "caddy"

    def config_dir(self) -> Path:
        """Return the project directory containing the Caddy configuration."""
        return Path(self.name())

    def container_image(self) -> str:
        """Return the official Caddy container image."""
        return "docker.io/library/caddy:latest"

    def healthcheck_url(self) -> str:
        """Return the local admin configuration endpoint used for health checks."""
        return "http://localhost:2019/config/"

    def http_container_port(self) -> int:
        """Return Caddy's default HTTP port inside the container."""
        return 80

    def http_host_port(self) -> int:
        """Return the host port published for HTTP."""
        return 8080

    def https_container_port(self) -> int:
        """Return Caddy's default HTTPS and HTTP/3 port inside the container."""
        return 443

    def https_host_port(self) -> int:
        """Return the host port published for HTTPS and HTTP/3."""
        return 8443

    def site_address_env_var(self) -> str:
        """Return the environment variable used for the Caddy site address."""
        return "SITE_ADDRESS"
