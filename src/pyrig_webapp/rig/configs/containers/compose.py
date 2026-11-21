"""Compose configuration management."""

from pyrig_containers.rig.configs.containers.compose import (
    ComposeConfigFile as BaseComposeConfigFile,
)


class ComposeConfigFile(BaseComposeConfigFile):
    """Use the base container compose configuration for web applications."""
