"""Tests for the web application framework tool."""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.base.hooks import VersionControlHookTool
from pyrig.rig.tools.base.tool import Group

from pyrig_webapp.rig.tools.web_app.framework import WebAppFramework


class TestWebAppFramework:
    """Test the web application framework metadata and commands."""

    def test_compile_args(self) -> None:
        """Test the framework compile command."""
        assert WebAppFramework.I.compile_args() == Args("reflex", "compile")

    def test_compile_web_app(self) -> None:
        """Test the project-environment compile command."""
        assert WebAppFramework.I.compile_web_app() == Args(
            "uv",
            "run",
            "reflex",
            "compile",
        )

    def test_compile_web_app_hook(self) -> None:
        """Test the framework compile hook runs on pre-push through uv."""
        hook = WebAppFramework.I.compile_web_app_hook()
        assert hook["id"] == "compile-web-app"
        assert hook["entry"] == "uv run reflex compile"
        assert hook["stages"] == ["pre-push"]
        assert hook["always_run"] is True
        assert hook["pass_filenames"] is False
        assert hook in VersionControlHookTool.subclasses_hooks()

    def test_dev_dependencies(self) -> None:
        """Test the framework does not add a dev dependency."""
        assert WebAppFramework.I.dev_dependencies() == ()

    def test_group(self) -> None:
        """Test the framework badge group."""
        assert WebAppFramework.I.group() == Group.TOOLING

    def test_hooks(self) -> None:
        """Test the framework contributes the compile hook."""
        assert WebAppFramework.I.hooks() == (WebAppFramework.I.compile_web_app_hook(),)

    def test_image_url(self) -> None:
        """Test the framework badge image URL."""
        assert (
            WebAppFramework.I.image_url()
            == "https://img.shields.io/badge/web--framework-reflex-1C1C1E"
        )

    def test_link_url(self) -> None:
        """Test the framework website."""
        assert WebAppFramework.I.link_url() == "https://github.com/reflex-dev/reflex"

    def test_name(self) -> None:
        """Test the framework CLI name."""
        assert WebAppFramework.I.name() == "reflex"

    def test_runtime_dependencies(self) -> None:
        """Test the framework is declared as a runtime dependency."""
        assert WebAppFramework.I.runtime_dependencies() == ("reflex",)

    def test_version_control_ignore_patterns(self) -> None:
        """Test framework-specific ignore patterns."""
        assert WebAppFramework.I.version_control_ignore_patterns() == (
            "assets/external/",
            "*.db",
            ".states",
            "*.py[cod]",
            ".web",
        )
