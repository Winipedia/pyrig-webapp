"""Test module."""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_runtime_dependencies(self) -> None:
        """Test method."""
        assert "reflex" not in Pyrigger().runtime_dependencies()
        assert "reflex" in Pyrigger.I.runtime_dependencies()

    def test_setup_steps(self) -> None:
        """Test method."""
        steps = Pyrigger.I.setup_steps()
        assert steps[2] == (Args("reflex", "compile"), {})

    def test_version_control_ignore_patterns(self) -> None:
        """Test method."""
        patterns = (
            "assets/external/",
            "*.db",
            ".states",
            "*.py[cod]",
            ".web",
        )
        for pattern in patterns:
            assert pattern not in Pyrigger().version_control_ignore_patterns()
            assert pattern in Pyrigger.I.version_control_ignore_patterns()

    def test_web_app_framework(self) -> None:
        """Test method."""
        assert Pyrigger.I.web_app_framework() == "reflex"  # ty: ignore[missing-attribute]
