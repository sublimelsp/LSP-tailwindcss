from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing_extensions import override


def plugin_loaded():
    LspTailwindcssPlugin.register()


def plugin_unloaded():
    LspTailwindcssPlugin.unregister()


class LspTailwindcssPlugin(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath('Packages', package_name, 'language-server'),
            Path('node_modules', '@tailwindcss', 'language-server', 'bin', 'tailwindcss-language-server'),
            node_version_requirement='>=18.17.0',
        )
