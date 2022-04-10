from lsp_utils import NpmClientHandler
import os


def plugin_loaded():
    LspTailwindcssPlugin.setup()


def plugin_unloaded():
    LspTailwindcssPlugin.cleanup()


class LspTailwindcssPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'node_modules', '.bin', 'tailwindcss-language-server')
