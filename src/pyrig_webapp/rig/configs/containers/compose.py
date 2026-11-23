"""Compose configuration management."""

from typing import Any
from urllib import request
from urllib.request import urlopen

from pyrig.rig.tools.programming_language import ProgrammingLanguage
from pyrig_containers.rig.configs.containers.compose import (
    ComposeConfigFile as BaseComposeConfigFile,
)
from reflex.constants import DefaultPorts, Endpoint


class ComposeConfigFile(BaseComposeConfigFile):
    """Configure the web application service, port mapping, and health check."""

    def service_app_before(self) -> dict[str, Any]:
        """Add extra service keys before the defaults."""
        before = super().service_app_before()
        before["ports"] = self.app_ports()
        before["restart"] = "unless-stopped"
        before["healthcheck"] = self.app_healthcheck()
        return before

    def app_healthcheck(self) -> dict[str, Any]:
        """Check the default Reflex production ping endpoint."""
        url = f"http://{self.loopback_ip()}:{self.frontend_port()}{Endpoint.PING}"
        probe = f"""from {request.__name__} import {urlopen.__name__}
{urlopen.__name__}('{url}')"""
        return {
            "test": [
                "CMD",
                *ProgrammingLanguage.I.args(
                    "-c",
                    probe,
                ),
            ],
        }

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
