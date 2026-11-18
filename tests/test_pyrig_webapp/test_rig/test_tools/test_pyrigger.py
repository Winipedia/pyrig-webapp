"""Test module."""

from pyrig.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_runtime_dependencies(self) -> None:
        """Test method."""
        assert "reflex" not in Pyrigger().runtime_dependencies()
        assert "reflex" in Pyrigger.I.runtime_dependencies()
