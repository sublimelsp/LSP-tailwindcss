import os
import sublime
from LSP.plugin import ClientConfig
from LSP.plugin import WorkspaceFolder
from LSP.plugin.core.typing import List, Optional
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspTailwindcssPlugin.setup()


def plugin_unloaded():
    LspTailwindcssPlugin.cleanup()


class LspTailwindcssPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(
        server_directory, 'extension', 'dist', 'server', 'tailwindServer.js'
    )

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
        path = workspace_folders[0].path
        tailwind_config_file_path = os.path.join(path, 'tailwind.config.js')
        if not os.path.exists(tailwind_config_file_path):
            return "No tailwind.config.js present in {}".format(path)
        return None

    @classmethod
    def on_client_configuration_ready(cls, configuration: dict) -> None:
        configuration["initializationOptions"].setdefault("userLanguages", {
            # the server requires the existance of "userLanguages" in initializationOptions
            # userLanguages is a VS Code specific setting
        })

