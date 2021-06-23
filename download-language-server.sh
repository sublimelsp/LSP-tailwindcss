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
rm -rf ./language-server
mkdir ./language-server

# unzip
unzip -a $tarball -d ./language-server

# ./language-server/package.json is requrired for lsp_utils to work. Reuse pacakge.json from extenison folder.
cp ./language-server/extension/package.json ./language-server

# ./language-server/package-lock.json is required. Without it an error will apear when when starting the plugin.
cd language-server && npm i && cd ..

# clean up
rm $tarball
echo "Done"
