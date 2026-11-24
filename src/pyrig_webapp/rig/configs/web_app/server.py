"""Scaffold the web server configuration."""

from pathlib import Path
from typing import override

from pyrig.rig.configs.base.string_ import StringConfigFile

from pyrig_webapp.rig.configs.containers.compose import ComposeConfigFile
from pyrig_webapp.rig.tools.web_app.framework import WebAppFramework
from pyrig_webapp.rig.tools.web_app.server import WebServer


class WebServerConfigFile(StringConfigFile):
    """Create a Caddyfile without overwriting an existing custom configuration."""

    @override
    def content(self) -> str:
        """Return the reverse proxy configuration for the configured site."""
        app_name = ComposeConfigFile.I.service_name(ComposeConfigFile.I.service_app)
        return f"""{{${WebServer.I.site_address_env_var()}}} {{
	reverse_proxy {app_name}:{WebAppFramework.I.frontend_port()}
}}
"""

    @override
    def extension(self) -> str:
        """Return an empty extension for Caddyfile."""
        return ""

    @override
    def extension_separator(self) -> str:
        """Return no extension separator."""
        return ""

    @override
    def parent_path(self) -> Path:
        """Return the directory mounted into the Caddy container."""
        return WebServer.I.config_dir()

    @override
    def stem(self) -> str:
        """Return the Caddy configuration filename."""
        return "Caddyfile"
