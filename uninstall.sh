#!/bin/bash

# commandshelf uninstall script

set -e # Exit on error

INSTALL_DIR="$HOME/.commandshelf"
BIN_PATH="/usr/local/bin/shelf"

echo "Uninstalling Commandshelf..."

# Remove install directory if it exists
if [ -d "$INSTALL_DIR" ]; then
    echo "Removing installation directory: $INSTALL_DIR"
    rm -rf "$INSTALL_DIR"
else
    echo "Installation directory $INSTALL_DIR does not exist. Nothing to remove."
fi

# Remove global shelf command wrapper if it exists
if [ -f "$BIN_PATH" ]; then
    echo "Removing shelf command wrapper at $BIN_PATH"
    rm -f "$BIN_PATH"
else
    echo "shelf command wrapper at $BIN_PATH does not exist. Nothing to remove."
fi

echo "Commandshelf uninstalled successfully!"
echo "All files and configurations have been removed from your system."
echo "You can now safely delete any remaining files related to Commandshelf if you wish."

# Assisted by YouTube & AI when writing this code.