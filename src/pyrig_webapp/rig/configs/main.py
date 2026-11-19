"""Scaffold the target project's Reflex app module."""

from types import ModuleType
from typing import override

import reflex as rx
from pyrig.rig.configs.base.copy_module import CopyModuleConfigFile

from pyrig_webapp import main as main_module


class MainConfigFile(CopyModuleConfigFile):
    """Scaffold a Reflex app module."""

    @override
    def copy_module(self) -> ModuleType:
        """Return the starter Reflex app module."""
        return main_module

    @override
    def is_correct(self) -> bool:
        """Return whether the app module contains a Reflex app assignment."""
        return self.has_app()

    def has_app(self) -> bool:
        """Return whether the module contains an ``app = rx.App(`` assignment."""
        return f"app = rx.{rx.App.__name__}(" in self.read_content()
