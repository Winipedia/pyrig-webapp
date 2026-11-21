"""Test module."""

from pathlib import Path

from pyrig.core.subprocesses import Args

from pyrig_webapp.rig.configs.containers.file import ContainerfileConfigFile


class TestContainerfileConfigFile:
    """Test class."""

    def test_project_command(self) -> None:
        """Test method."""
        assert ContainerfileConfigFile.I.project_command() == Args(
            "reflex",
            "run",
            "--env=prod",
        )

    def test_required_binaries(self) -> None:
        """Test method."""
        assert (
            "docker.io/oven/bun:slim",
            "/usr/local/bin/bun",
            "/usr/local/bin/bun",
        ) in ContainerfileConfigFile.I.required_binaries()

    def test_required_files(self) -> None:
        """Test method."""
        assert Path("rxconfig.py") in ContainerfileConfigFile.I.required_files()
