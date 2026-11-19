"""Test module."""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_setup_steps(self) -> None:
        """Test method."""
        steps = Pyrigger.I.setup_steps()
        assert steps[2] == (Args("reflex", "compile"), {})
