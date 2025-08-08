#!/bin/bash

# commandshelf install script

set -e # Exit on error

echo "Installing Commandshelf..."

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed. Please install Python3 and try again."
    exit 1
fi

# Determine the home directory and username of the user who ran the script.
if [ -z "$SUDO_USER" ]; then
    INSTALL_DIR="$HOME/.commandshelf"
    USER_AND_GROUP=$(id -un):$(id -gn)
else
    ORIGINAL_USER_HOME=$(eval echo "~$SUDO_USER")
    INSTALL_DIR="$ORIGINAL_USER_HOME/.commandshelf"
    USER_AND_GROUP="$SUDO_USER:$SUDO_USER"
fi

# IMPORTANT: Set ownership of the directory to the original user
# This allows the user to read and write to the directory and its files.
chown -R "$USER_AND_GROUP" "$INSTALL_DIR"

# copy .py files to install directory
cp shelf.py storage.py executor.py utils.py "$INSTALL_DIR/"

# Create commands.json in install directory
if [ ! -f "$INSTALL_DIR/commands.json" ]; then
    echo "Creating commands.json in $INSTALL_DIR"
    echo '{}' > "$INSTALL_DIR/commands.json"
    chmod 600 "$INSTALL_DIR/commands.json"
else
    echo "commands.json already exists in $INSTALL_DIR"
fi

# Create config.json in install directory
if [ ! -f "$INSTALL_DIR/config.json" ]; then
    echo "Creating config.json in $INSTALL_DIR"
    echo '{}' > "$INSTALL_DIR/config.json"
    chmod 600 "$INSTALL_DIR/config.json"
else
    echo "config.json already exists in $INSTALL_DIR"
fi

# Define the path for the global command wrapper
BIN_PATH="/usr/local/bin/shelf"

# Create global shelf command wrapper
if [ ! -f "$BIN_PATH" ]; then
    echo "Creating shelf command wrapper at $BIN_PATH"
    echo '#!/bin/bash' > "$BIN_PATH"
    echo "python3 $INSTALL_DIR/shelf.py \"\$@\"" >> "$BIN_PATH"
    chmod +x "$BIN_PATH"
else
    echo "shelf command wrapper already exists at $BIN_PATH"
fi

echo "Commandshelf installed successfully!"
echo "You can now use the 'shelf' command to manage your commands."
echo "Configuration files are located at $INSTALL_DIR/commands.json and $INSTALL_DIR/config.json"

# Assisted by YouTube & AI when writing this code.
