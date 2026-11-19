"""Tool wrapper for the pyrig CLI itself, including new-project initialization."""

from typing import Any

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger

from pyrig_webapp.rig.tools.web_app.framework import WebAppFramework


class Pyrigger(BasePyrigger):
    """Customized Pyrigger to integrate webapp functionality."""

    def setup_steps(self) -> tuple[tuple[Args, dict[str, Any]], ...]:
        """Add web app framework compilation step after sync.

        This creates the ``reflex.lock`` folder, which should be committed to version
        control.
        """
        steps = list(super().setup_steps())
        index = steps.index(self.step_synchronize_project())
        steps.insert(index + 1, (WebAppFramework.I.compile_args(), {}))
        # Keep this workaround until a Reflex release includes the fix from
        # https://github.com/reflex-dev/reflex/pull/7935.
        steps.insert(
            index + 2,
            (
                Args("prek", "run", "mixed-line-ending", "--files", ".gitignore"),
                {"check": False},
            ),
        )
        return tuple(steps)
