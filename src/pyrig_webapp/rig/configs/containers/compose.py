"""Compose configuration management."""

from types import MethodType
from typing import Any
from urllib import request
from urllib.request import urlopen

from pyrig.rig.tools.programming_language import ProgrammingLanguage
from pyrig_containers.rig.configs.containers.compose import (
    ComposeConfigFile as BaseComposeConfigFile,
)
from reflex.constants import DefaultPorts, Endpoint


class ComposeConfigFile(BaseComposeConfigFile):
    """Configure the web app service, restart policy, port mapping, and health check."""

    def service(
        self,
        method: MethodType,
        *,
        restart: str | None = None,
        **kwargs: Any,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a service using the web app's default restart policy.

        Args:
            method: The service method used to derive the service name.
            restart: Container restart policy; defaults to `unless-stopped`.
            **kwargs: Additional settings forwarded to the base service builder.

        Returns:
            The named service configuration.
        """
        return super().service(
            method,
            restart="unless-stopped" if restart is None else restart,
            **kwargs,
        )

    def service_app_settings(self) -> dict[str, Any]:
        """Return the app service's build, port mapping, and health check settings."""
        settings = super().service_app_settings()
        settings["ports"] = self.app_ports()
        settings["healthcheck"] = self.app_healthcheck()
        return settings

    def app_healthcheck(self) -> dict[str, Any]:
        """Return a health check that requests the default Reflex ping endpoint."""
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
