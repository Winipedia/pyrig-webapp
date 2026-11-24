"""Containerfile configuration management."""

from pathlib import Path
from typing import override

from pyrig.core.subprocesses import Args
from pyrig_containers.rig.configs.containers.file import (
    ContainerfileConfigFile as BaseContainerfileConfigFile,
)

from pyrig_webapp.rig.configs.web_app.config import WebAppConfigFile
from pyrig_webapp.rig.tools.web_app.framework import WebAppFramework


class ContainerfileConfigFile(BaseContainerfileConfigFile):
    """Configure a container image that runs the Reflex application."""

    @override
    def project_command(self) -> Args:
        """Return the Reflex production command for the container entrypoint."""
        return WebAppFramework.I.run_production_args()

    @override
    def required_binaries(self) -> tuple[tuple[str, str, str], ...]:
        """Include Bun alongside the base container binaries."""
        return (
            *super().required_binaries(),
            WebAppFramework.I.package_manager_container_binary_copy_spec(),
        )

    @override
    def required_files(self) -> tuple[Path, ...]:
        """Include the Reflex configuration alongside the base required files."""
        return (*super().required_files(), WebAppConfigFile.I.path())
