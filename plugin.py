import fnmatch
import os
import re
import sublime
from LSP.plugin import ClientConfig
from LSP.plugin import WorkspaceFolder
from LSP.plugin.core.typing import List, Optional, Set
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspTailwindcssPlugin.setup()


def plugin_unloaded():
    LspTailwindcssPlugin.cleanup()


class LspTailwindcssPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'server', 'tailwindServer.js')

    @classmethod
    def is_allowed_to_start(
        cls,
        window: sublime.Window,
        initiating_view: Optional[sublime.View] = None,
        workspace_folders: Optional[List[WorkspaceFolder]] = None,
        configuration: Optional[ClientConfig] = None
    ) -> Optional[str]:
        if not workspace_folders:
            return "Requires a folder to start."

        # Config pattern is found here:
        # https://github.com/tailwindlabs/tailwindcss-intellisense/blob/766a5d533dcb68640ce6b3270488f6701dd1173d/packages/vscode-tailwindcss/src/extension.ts#L40
        config_file_pattern = r'^(tailwind|tailwind\.config)\.(js|cjs)$'
        folder_exclude_patterns = set(sublime.load_settings('Preferences.sublime-settings').get("folder_exclude_patterns", [])) # type: Set[str]
        folder_exclude_patterns.add('node_modules') # definitely exclude node_modules
        config_file = find_file_in_workspace(config_file_pattern, workspace_folders[0].path, folder_exclude_patterns)
        if config_file:
            return None # config found, return None to start the session
        return "No tailwind configuration file present in the workspace folder."


def find_file_in_workspace(file_pattern: str, root_folder: str, folder_exclude_patterns: Set[str] = None) -> Optional[str]:
    for path, directories, files in os.walk(root_folder):
        for folder_exclude_pattern in folder_exclude_patterns or []:
            # skip ignored folders
            directories[:] = [d for d in directories if not fnmatch.fnmatch(d, folder_exclude_pattern)]

        for file in files:
            if re.match(file_pattern, file):
                return os.path.join(path, file)
    return None
