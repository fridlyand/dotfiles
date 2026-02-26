import sublime
import sublime_plugin
import os

class IdoFindFileCommand(sublime_plugin.WindowCommand):
    def run(self, current_dir=None, other_pane=False):
        self.other_pane = other_pane
        
        # 1. Determine starting directory
        if not current_dir:
            view = self.window.active_view()
            if view and view.file_name():
                current_dir = os.path.dirname(view.file_name())
            else:
                current_dir = os.path.expanduser("~")
                
        self.current_dir = current_dir
        
        # 2. Read the hard drive
        try:
            items = os.listdir(current_dir)
        except Exception:
            items = []
            
        folders = [".. (Parent Directory)"]
        files = []
        
        for item in items:
            # Hide invisible files (like .git or .DS_Store) to keep it clean
            if item.startswith('.'): continue 
                
            full_path = os.path.join(current_dir, item)
            if os.path.isdir(full_path):
                folders.append(item + "/")
            else:
                files.append(item)
                
        folders.sort()
        files.sort()
        
        # Folders at the top, files at the bottom
        self.display_list = folders + files
        
        # 3. Show the visual, fuzzy-searchable Quick Panel
        self.window.show_quick_panel(self.display_list, self.on_done)

    def on_done(self, index):
        if index == -1: return # User pressed Escape
        
        selected = self.display_list[index]
        
        # 4. Handle navigation up a folder
        if selected == ".. (Parent Directory)":
            parent = os.path.dirname(self.current_dir)
            self.window.run_command("ido_find_file", {"current_dir": parent, "other_pane": self.other_pane})
            return
            
        target_path = os.path.join(self.current_dir, selected.replace("/", ""))
        
        # 5. If it's a folder, drill down into it and open the panel again
        if os.path.isdir(target_path):
            self.window.run_command("ido_find_file", {"current_dir": target_path, "other_pane": self.other_pane})
        else:
            # 6. If it's a file, open it using your established pane logic
            self.open_file(target_path)
            
    def open_file(self, target_path):
        if self.other_pane:
            if self.window.num_groups() == 1:
                self.window.run_command("set_layout", {
                    "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
                    "cols": [0.0, 0.5, 1.0],
                    "rows": [0.0, 1.0]
                })
                sublime.set_timeout(lambda: self._open_in_group(target_path, 1), 50)
            else:
                next_grp = 1 if self.window.active_group() == 0 else 0
                self._open_in_group(target_path, next_grp)
        else:
            self.window.open_file(target_path)

    def _open_in_group(self, target_path, group):
        self.window.open_file(target_path, flags=sublime.FORCE_GROUP, group=group)
        self.window.focus_group(group)
