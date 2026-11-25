"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.base.copy_module import CopyModuleConfigFile
from pyrig.rig.configs.base.shell import ShellConfigFile
from pyrig.rig.configs.base.string_ import StringConfigFile
from pyrig.rig.tools.base.hooks import VersionControlHookTool
from pyrig.rig.tools.base.tool import Tool
from pyrig_containers.rig.configs.containers.file import ContainerfileConfigFile

from pyrig_webapp.rig.configs.web_app.config import WebAppConfigFile
from pyrig_webapp.rig.configs.web_app.forward_ports import ForwardPortsConfigFile
from pyrig_webapp.rig.configs.web_app.main import MainConfigFile
from pyrig_webapp.rig.configs.web_app.server import WebServerConfigFile

_CONFIG_FILE_OVERRIDES = (
    ConfigFile.extension,
    ConfigFile.extension_separator,
    ConfigFile.is_correct,
    ConfigFile.parent_path,
    ConfigFile.stem,
    ContainerfileConfigFile.project_command,
    CopyModuleConfigFile.copy_module,
    ShellConfigFile.script,
    StringConfigFile.content,
)
_CONFIG_FILES = (
    ForwardPortsConfigFile,
    MainConfigFile,
    WebAppConfigFile,
    WebServerConfigFile,
)
_TOOL_OVERRIDES = (
    Tool.dev_dependencies,
    Tool.group,
    Tool.image_url,
    Tool.link_url,
    Tool.runtime_dependencies,
    VersionControlHookTool.hooks,
)
