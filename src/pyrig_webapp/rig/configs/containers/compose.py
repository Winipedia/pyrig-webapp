"""Compose configuration management."""

from typing import Any

from pyrig_containers.rig.configs.containers.compose import (
    ComposeConfigFile as BaseComposeConfigFile,
)
from reflex.constants import DefaultPorts


class ComposeConfigFile(BaseComposeConfigFile):
    """Configure the web application service and its local port mapping."""

    def _configs(self) -> dict[str, Any]:
        """Add the web application port mapping to the base service configuration."""
        configs = super()._configs()
        services = configs["services"]
        app = services["app"]
        app["ports"] = self.app_ports()
        return configs

    def app_ports(self) -> list[str]:
        """Return the loopback port mapping for the Reflex frontend."""
        frontend_port = self.frontend_port()
        return [
            f"{self.loopback_ip()}:{frontend_port}:{frontend_port}",
        ]

    def frontend_port(self) -> int:
        """Return the default Reflex frontend port."""
        return DefaultPorts.FRONTEND_PORT

    def loopback_ip(self) -> str:
        """Return the IPv4 loopback address."""
        return "127.0.0.1"
