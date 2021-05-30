import os
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspTailwindcssPlugin.setup()


def plugin_unloaded():
    LspTailwindcssPlugin.cleanup()


class LspTailwindcssPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(
        server_directory, 'extension', 'dist', 'server', 'index.js'
    )

    @classmethod
    def on_client_configuration_ready(cls, configuration: dict) -> None:
        configuration["initializationOptions"].setdefault("userLanguages", {
            # the server requires the existance of "userLanguages" in initializationOptions
            # userLanguages is a VS Code specific setting
        })

