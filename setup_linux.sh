#!/bin/bash
# setup_linux.sh - Bootstraps the Linux environment

SUBLIME_DIR="$HOME/.config/sublime-text/Packages"

echo "Setting up Linux Sublime Text symlinks..."

# Ensure the Packages directory exists, then remove the default User folder
mkdir -p "$SUBLIME_DIR"
rm -rf "$SUBLIME_DIR/User"

# Create the symlink pointing to our dotfiles
ln -s "$HOME/dotfiles/sublime-text/User" "$SUBLIME_DIR/User"

echo "Linux setup complete!"
