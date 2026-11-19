"""Scaffold web application configuration in the target project root."""

from pathlib import Path
from typing import override

import reflex as rx
from pyrig.rig.configs.base.python import PythonConfigFile
from pyrig.rig.tools.packages.manager import PackageManager
from pyrig_runtime.core.introspection.modules import replace_root_module_name

from pyrig_webapp import main


class WebAppConfigConfigFile(PythonConfigFile):
    """Create a Reflex configuration without overwriting user changes."""

    @override
    def content(self) -> str:
        """Configure Reflex to import the target project's app module."""
        package_name = PackageManager.I.package_name()
        main_module = replace_root_module_name(main.__name__, package_name)
        return f'''"""Configuration for the web application."""

import {rx.__name__} as rx

config = rx.{rx.Config.__name__}(
    app_name="{package_name}",
    app_module_import="{main_module}",
)
'''

    @override
    def is_correct(self) -> bool:
        """Return whether the file contains a Reflex config assignment."""
        return self.has_config()

    @override
    def parent_path(self) -> Path:
        """Return the project root."""
        return Path()

    @override
    def stem(self) -> str:
        """Return the Reflex configuration filename stem."""
        return "rxconfig"

    def has_config(self) -> bool:
        """Return whether the file contains a ``config = rx.Config(`` assignment."""
        return f"config = rx.{rx.Config.__name__}(" in self.read_content()
