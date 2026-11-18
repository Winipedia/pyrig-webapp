"""Tool wrapper for the pyrig CLI itself, including new-project initialization."""

from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger


class Pyrigger(BasePyrigger):
    """Customized Pyrigger to integrate webapp functionality."""

    def runtime_dependencies(self) -> tuple[str, ...]:
        """Add reflex as a runtime dependency."""
        return (*super().runtime_dependencies(), "reflex")
