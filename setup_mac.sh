#!/bin/bash
# setup_mac.sh - Bootstraps the Mac environment

SUBLIME_DIR="$HOME/Library/Application Support/Sublime Text/Packages"

echo "Setting up macOS Sublime Text symlinks..."

# Remove default User folder if it exists
rm -rf "$SUBLIME_DIR/User"

# Create the symlink pointing to our dotfiles
ln -s "$HOME/dotfiles/sublime-text/User" "$SUBLIME_DIR/User"

echo "Setting up Kitty symlinks..."
mkdir -p ~/.config/kitty
ln -s ~/dotfiles/terminal/kitty.conf ~/.config/kitty/kitty.conf

echo "macOS setup complete!"
