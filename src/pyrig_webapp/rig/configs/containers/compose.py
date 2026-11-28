"""Compose configuration management."""

from collections.abc import Callable
from typing import Any, override
from urllib import request
from urllib.request import urlopen

from pyrig.rig.tools.programming_language import ProgrammingLanguage
from pyrig_containers.rig.configs.containers.compose import (
    ComposeConfigFile as BaseComposeConfigFile,
)
from reflex.constants import Endpoint

from pyrig_webapp.rig.tools.web_app.framework import WebAppFramework
from pyrig_webapp.rig.tools.web_app.server import WebServer


class ComposeConfigFile(BaseComposeConfigFile):
    """Configure the web app and its public HTTPS reverse proxy."""

    @override
    def service_app_settings(self) -> dict[str, Any]:
        """Return the app service's health check settings."""
        settings = super().service_app_settings()
        settings["healthcheck"] = self.app_healthcheck()
        return settings

    @override
    def services(self) -> tuple[Callable[[], dict[str, Any]], ...]:
        """Include the web server alongside the application."""
        return (*super().services(), self.service_web_server)

    @override
    def _configs(self) -> dict[str, Any]:
        """Include persistent storage for Caddy's data."""
        return {
            **super()._configs(),
            "volumes": {
                self.web_server_data_volume(): {},
            },
        }

    @override
    def service(
        self,
        *,
        restart: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Return a service using the web app's default restart policy.

        Args:
            restart: Container restart policy; defaults to `unless-stopped`.
            **kwargs: Additional settings forwarded to the base service builder.

        Returns:
            The service configuration.
        """
        return super().service(
            restart="unless-stopped" if restart is None else restart,
            **kwargs,
        )

    def app_healthcheck(self) -> dict[str, Any]:
        """Return a health check that requests the default Reflex ping endpoint."""
        url = f"http://localhost:{WebAppFramework.I.frontend_port()}{Endpoint.PING}"
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

    def service_web_server(self) -> dict[str, Any]:
        """Return the Caddy service with the app as its upstream."""
        return self.service(
            **self.service_web_server_settings(),
        )

    def service_web_server_settings(self) -> dict[str, Any]:
        """Return the settings for the web server service."""
        return {
            "image": WebServer.I.container_image(),
            "pull_policy": "always",
            "environment": {
                WebServer.I.site_address_env_var(): (
                    f"${{{WebServer.I.site_address_env_var()}:-localhost}}"
                ),
            },
            "ports": [
                f"{WebServer.I.http_host_port()}:{WebServer.I.http_container_port()}",
                f"{WebServer.I.https_host_port()}:{WebServer.I.https_container_port()}",
                (
                    f"{WebServer.I.https_host_port()}:"
                    f"{WebServer.I.https_container_port()}/udp"
                ),
            ],
            "volumes": [
                f"./{WebServer.I.config_dir().as_posix()}:/etc/caddy:ro",
                f"{self.web_server_data_volume()}:/data",
            ],
            "healthcheck": self.web_server_healthcheck(),
            "cap_add": ["NET_BIND_SERVICE"],
        }

    def web_server_data_volume(self) -> str:
        """Return the web server's persistent data volume name."""
        return "web-server-data"

    def web_server_healthcheck(self) -> dict[str, Any]:
        """Check that the web server's admin API responds."""
        return {
            "test": [
                "CMD",
                "curl",
                "--fail",
                WebServer.I.healthcheck_url(),
            ],
        }
