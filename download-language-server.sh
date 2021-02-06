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

# clean up
rm $tarball
echo "Done"
