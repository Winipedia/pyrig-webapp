"""Web application framework integration for generated web applications."""

from typing import Any, override

import reflex as rx
from pyrig.core.subprocesses import Args
from pyrig.rig.tools.base.hooks import VersionControlHookTool
from pyrig.rig.tools.base.tool import Group
from pyrig.rig.tools.linting.python import PythonLinter
from pyrig.rig.tools.packages.manager import PackageManager
from pyrig.rig.tools.version_control.hooks.manager import (
    VersionControlHookManager,
)
from pyrig_runtime.core.strings import snake_to_kebab_case
from reflex.constants import DefaultPorts


class WebAppFramework(VersionControlHookTool):
    """Web application framework CLI integration and project metadata."""

    @override
    def dev_dependencies(self) -> tuple[str, ...]:
        """Return no dev dependencies because the framework is a runtime dependency."""
        return ()

    @override
    def group(self) -> str:
        """Return `Group.TOOLING`."""
        return Group.TOOLING

    @override
    def hooks(self) -> tuple[dict[str, Any], ...]:
        """Return the framework compile hook."""
        return (self.compile_web_app_hook(),)

    @override
    def image_url(self) -> str:
        """Return the web framework badge image URL."""
        return f"https://img.shields.io/badge/{self.shield_name()}-1C1C1E?logo=reflex&logoColor=white"

    @override
    def link_url(self) -> str:
        """Return the web framework website URL."""
        return "https://github.com/reflex-dev/reflex"

    @override
    def runtime_dependencies(self) -> tuple[str, ...]:
        """Return the framework as a runtime dependency for generated projects."""
        return (self.name(),)

    @override
    def version_control_ignore_patterns(self) -> tuple[str, ...]:
        """Return files and directories generated or used by the framework."""
        return (
            *super().version_control_ignore_patterns(),
            "assets/external/",
            "*.db",
            ".states",
            "*.py[cod]",
            ".web",
        )

    @override
    def name(self) -> str:
        """Return the framework CLI name."""
        return snake_to_kebab_case(rx.__name__)

    def frontend_port(self) -> int:
        """Return the default frontend port for the application service."""
        return DefaultPorts.FRONTEND_PORT

    def package_manager_container_binary_copy_spec(self) -> tuple[str, str, str]:
        """Return the Bun image and paths used to copy its binary into a container."""
        return ("docker.io/oven/bun:slim", "/usr/local/bin/bun", "/usr/local/bin/bun")

    def run_production_args(self, *args: str) -> Args:
        """Return arguments to run the web application in production."""
        return self.run_args("--env=prod", *args)

    def compile_web_app_hook(self) -> dict[str, Any]:
        """Return the framework compile hook, ordered after dependency checks."""
        return VersionControlHookManager.I.local_hook(
            self.compile_web_app,
            priority=VersionControlHookManager.I.deprioritize(
                PythonLinter.I.format_hook(),
            ),
            stages=["pre-push"],
            pass_filenames=False,
            always_run=True,
        )

    def run_args(self, *args: str) -> Args:
        """Return arguments to run the web application."""
        return self.args("run", *args)

    def compile_web_app(self) -> Args:
        """Return the command compiling the app within the project environment."""
        return PackageManager.I.run_args(*self.compile_args())

    def compile_args(self, *args: str) -> Args:
        """Return arguments to compile the web application."""
        return self.args("compile", *args)
