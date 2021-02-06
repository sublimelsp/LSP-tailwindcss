# LSP-tailwindcss

TailwindCSS support for Sublime's LSP.

Provided through [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss), which is open-source on GitHub as [Tailwind Labs](https://github.com/tailwindlabs/tailwindcss-intellisense).

## Installation

This plugin is not published on the official [Package Control](https://packagecontrol.io/).\
We are making the latest adjustments and tests, so that everything works correctly.

**Package Control:**

1. Add a custom repository for Package Control with steps described [here](https://github.com/jfcherng-sublime/ST-my-package-control/blob/master/README.md#usage).
2. Install [LSP](https://packagecontrol.io/packages/LSP) and `LSP-tailwindcss` via Package Control.
3. Restart Sublime.

**Manually:**

1. Download latest release and unzip. it into your Packages folder.
2. Go to `Sublime Text → Preferences → Browse Packages`.
3. Move folder to inside. (folder name should be LSP-tailwindcss)

## Configuration

There are some ways to configure the package and the language server.

- From `Preferences > Package Settings > LSP > Servers > LSP-tailwindcss`
- From the command palette `Preferences: LSP-tailwindcss Settings`

## LSP-html + LSP-tailwindcss

1. Go to [LSP-tailwindcss Settings](#configuration)
2. Paste the following settings:

```diff
  {
      "languageId": "html",
      // ST3
      "scopes": ["text.html.basic",],
      "syntaxes": [
         "Packages/HTML/HTML.sublime-syntax",
         "Packages/PHP/PHP.sublime-syntax",
      ],
      // ST4
      "document_selector": "text.html.basic | embedding.php | text.blade",
-     "feature_selector": "text.html"
+     "feature_selector": "meta.attribute-with-value.class.html"
  },
```
> NOTE: Change the `feature_selector`, it will allow you to use `LSP-html` normally, and you will only use `LSP-tailwindcss` when you write a class.
Since [TailwindCSS](https://tailwindcss.com/) just providing utility classes will work perfectly.
