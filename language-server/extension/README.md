<img src="https://raw.githubusercontent.com/bradlc/vscode-tailwindcss/master/packages/vscode-tailwindcss/.github/banner-dark.png" alt="" />

Tailwind CSS IntelliSense enhances the Tailwind development experience by providing Visual Studio Code users with advanced features such as autocomplete, syntax highlighting, and linting.

## Installation

**[Install via the Visual Studio Code Marketplace →](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)**

In order for the extension to activate you must have [`tailwindcss` installed](https://tailwindcss.com/docs/installation) and a [Tailwind config file](https://tailwindcss.com/docs/installation#create-your-configuration-file) named `tailwind.config.js` in your workspace.

## Features

### Autocomplete

Intelligent suggestions for class names, as well as [CSS functions and directives](https://tailwindcss.com/docs/functions-and-directives/).

<img src="https://raw.githubusercontent.com/bradlc/vscode-tailwindcss/master/packages/vscode-tailwindcss/.github/autocomplete.png" alt="" />

### Linting

Highlights errors and potential bugs in both your CSS and your markup.

<img src="https://raw.githubusercontent.com/bradlc/vscode-tailwindcss/master/packages/vscode-tailwindcss/.github/linting.png" alt="" />

### Hover Preview

See the complete CSS for a Tailwind class name by hovering over it.

<img src="https://raw.githubusercontent.com/bradlc/vscode-tailwindcss/master/packages/vscode-tailwindcss/.github/hover.png" alt="" />

### CSS Syntax Highlighting

Provides syntax definitions so that Tailwind features are highlighted correctly.

## Recommended VS Code Settings

VS Code has built-in CSS validation which may display errors when using Tailwind-specific syntax, such as `@apply`. You can disable this with the `css.validate` setting:

```
"css.validate": false
```

By default VS Code will not trigger completions when editing "string" content, for example within JSX attribute values. Updating the `editor.quickSuggestions` setting may improve your experience:

```
"editor.quickSuggestions": {
  "strings": true
}
```

## Extension Settings

### `tailwindCSS.includeLanguages`

This setting allows you to add additional language support. The key of each entry is the new language ID and the value is any one of the extensions built-in languages, depending on how you want the new language to be treated (e.g. `html`, `css`, or `javascript`):

```json
{
  "tailwindCSS.includeLanguages": {
    "plaintext": "html"
  }
}
```

### `tailwindCSS.emmetCompletions`

Enable completions when using [Emmet](https://emmet.io/)-style syntax, for example `div.bg-red-500.uppercase`. **Default: `false`**

### `tailwindCSS.colorDecorators`

Controls whether the editor should render inline color decorators for Tailwind CSS classes and helper functions. **Default: `true`**

> Note that `editor.colorDecorators` must be enabled for color decorators to be shown.

### `tailwindCSS.showPixelEquivalents`

Show `px` equivalents for `rem` CSS values in completions and hovers. **Default: `true`**

### `tailwindCSS.rootFontSize`

Root font size in pixels. Used to convert `rem` CSS values to their `px` equivalents. See [`tailwindCSS.showPixelEquivalents`](#tailwindcssshowpixelequivalents). **Default: `16`**

### `tailwindCSS.validate`

Enable linting. Rules can be configured individually using the `tailwindcss.lint` settings:

- `ignore`: disable lint rule entirely
- `warning`: rule violations will be considered "warnings," typically represented by a yellow underline
- `error`: rule violations will be considered "errors," typically represented by a red underline

#### `tailwindCSS.lint.invalidScreen`

Unknown screen name used with the [`@screen` directive](https://tailwindcss.com/docs/functions-and-directives/#screen). **Default: `error`**

#### `tailwindCSS.lint.invalidVariant`

Unknown variant name used with the [`@variants` directive](https://tailwindcss.com/docs/functions-and-directives/#variants). **Default: `error`**

#### `tailwindCSS.lint.invalidTailwindDirective`

Unknown value used with the [`@tailwind` directive](https://tailwindcss.com/docs/functions-and-directives/#tailwind). **Default: `error`**

#### `tailwindCSS.lint.invalidApply`

Unsupported use of the [`@apply` directive](https://tailwindcss.com/docs/functions-and-directives/#apply). **Default: `error`**

#### `tailwindCSS.lint.invalidConfigPath`

Unknown or invalid path used with the [`theme` helper](https://tailwindcss.com/docs/functions-and-directives/#theme). **Default: `error`**

#### `tailwindCSS.lint.cssConflict`

Class names on the same HTML element which apply the same CSS property or properties. **Default: `warning`**

#### `tailwindCSS.lint.recommendedVariantOrder`

Class variants not in the recommended order (applies in [JIT mode](https://tailwindcss.com/docs/just-in-time-mode) only). **Default: `warning`**

### `tailwindCSS.inspectPort`

Enable the Node.js inspector agent for the language server and listen on the specified port. **Default: `null`**

## Troubleshooting

If you’re having issues getting the IntelliSense features to activate, there are a few things you can check:

- Ensure that you have a Tailwind config file in your workspace and that this is named `tailwind.config.js`. Check out the Tailwind documentation for details on [creating a config file](https://tailwindcss.com/docs/installation#create-your-configuration-file).
- Ensure that the `tailwindcss` module is installed in your workspace, via `npm`, `yarn`, or `pnpm`.
- Make sure your VS Code settings aren’t causing your Tailwind config file to be excluded from search, for example via the `search.exclude` setting.
- Take a look at the language server output by running the `Tailwind CSS: Show Output` command from the command palette. This may show errors that are preventing the extension from activating.
