"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.base.copy_module import CopyModuleConfigFile
from pyrig.rig.configs.base.string_ import StringConfigFile
from pyrig.rig.tools.base.hooks import VersionControlHookTool
from pyrig.rig.tools.base.tool import Tool

from pyrig_webapp.rig.configs.web_app.config import WebAppConfigConfigFile
from pyrig_webapp.rig.configs.web_app.main import MainConfigFile

_CONFIG_FILE_OVERRIDES = (
    ConfigFile.is_correct,
    ConfigFile.parent_path,
    ConfigFile.stem,
    CopyModuleConfigFile.copy_module,
    StringConfigFile.content,
)
_CONFIG_FILES = (
    MainConfigFile,
    WebAppConfigConfigFile,
)
_TOOL_OVERRIDES = (
    Tool.dev_dependencies,
    Tool.group,
    Tool.image_url,
    Tool.link_url,
    Tool.runtime_dependencies,
    VersionControlHookTool.hooks,
)
