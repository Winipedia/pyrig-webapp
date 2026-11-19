"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.base.copy_module import CopyModuleConfigFile
from pyrig.rig.configs.base.string_ import StringConfigFile

from pyrig_webapp.rig.configs.main import MainConfigFile
from pyrig_webapp.rig.configs.web_app import WebAppConfigFile

_CONFIG_FILE_OVERRIDES = (
    ConfigFile.is_correct,
    ConfigFile.parent_path,
    ConfigFile.stem,
    CopyModuleConfigFile.copy_module,
    StringConfigFile.content,
)
_CONFIG_FILES = (
    MainConfigFile,
    WebAppConfigFile,
)
