#!/bin/bash
# setup_mac.sh - Bootstraps the Mac environment

SUBLIME_DIR="$HOME/Library/Application Support/Sublime Text/Packages"

echo "Setting up macOS Sublime Text symlinks..."

# Remove default User folder if it exists
rm -rf "$SUBLIME_DIR/User"

# Create the symlink pointing to our dotfiles
ln -s "$HOME/dotfiles/sublime-text/User" "$SUBLIME_DIR/User"

echo "macOS setup complete!"
