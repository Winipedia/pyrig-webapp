"""Tool wrapper for the pyrig CLI itself, including new-project initialization."""

from typing import Any

import reflex as rx
from pyrig.core.subprocesses import Args
from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger
from pyrig_runtime.core.strings import snake_to_kebab_case


class Pyrigger(BasePyrigger):
    """Customized Pyrigger to integrate webapp functionality."""

    def runtime_dependencies(self) -> tuple[str, ...]:
        """Add reflex as a runtime dependency."""
        return (*super().runtime_dependencies(), self.web_app_framework())

    def setup_steps(self) -> tuple[tuple[Args, dict[str, Any]], ...]:
        """Add web app framework compilation step after sync.

        This creates the reflex.lock folder which should committed to version control.
        """
        steps = list(super().setup_steps())
        index = steps.index(self.step_synchronize_project())
        steps.insert(index + 1, (Args(self.web_app_framework(), "compile"), {}))
        return tuple(steps)

    def version_control_ignore_patterns(self) -> tuple[str, ...]:
        """Add gitignore patterns required by reflex."""
        return (
            *super().version_control_ignore_patterns(),
            "assets/external/",
            "*.db",
            ".states",
            "*.py[cod]",
            ".web",
        )

    def web_app_framework(self) -> str:
        """Return the web app framework used."""
        return snake_to_kebab_case(rx.__name__)
