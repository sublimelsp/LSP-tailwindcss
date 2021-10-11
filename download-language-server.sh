#!/usr/bin/env bash

GITHUB_REPO_NAME="tailwindlabs/tailwindcss-intellisense"

# download the release
# more info here - https://gist.github.com/steinwaywhw/a4cd19cda655b8249d908261a62687f8

curl -s "https://api.github.com/repos/${GITHUB_REPO_NAME}/releases/latest" \
| grep "browser_download_url.*vsix" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -

# get the zip(.vsix) file
tarball="$(find . -name "*.vsix")"

# clean up
rm -rf ./language-server-temp
rm -rf ./language-server
mkdir ./language-server

# unzip
unzip -a "$tarball" -d ./language-server-temp

# ./language-server/package.json is required for lsp_utils to work. Reuse package.json from the extension folder.
cp ./language-server-temp/extension/package.json ./language-server
cp -R ./language-server-temp/extension/dist/server ./language-server
cp ./resolve_module.js ./language-server # move script to language server dir

# ./language-server/package-lock.json is required. Without it an error will appear when when starting the plugin.
cd language-server && npm i --production && cd ..

# clean up
rm "$tarball"
rm -rf ./language-server-temp
echo "Done"
