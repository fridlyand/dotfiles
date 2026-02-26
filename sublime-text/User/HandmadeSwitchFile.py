import sublime
import sublime_plugin
import os

def get_target_file(original_file):
    base_name, ext = os.path.splitext(original_file)
    ext = ext.lower()
    if ext in ['.c', '.cpp', '.cc', '.cxx']:
        return base_name + '.h'
    elif ext in ['.h', '.hpp', '.inl', '.cin', '.hin']:
        return base_name + '.cpp'
    return None

class SwitchFileCurrentPaneCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        if not view or not view.file_name():
            return

        target = get_target_file(view.file_name())
        if target:
            self.window.open_file(target)

class SwitchFileOtherPaneCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        if not view or not view.file_name():
            return

        target = get_target_file(view.file_name())
        if not target:
            return

        if self.window.num_groups() == 1:
            self.window.run_command("set_layout", {
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 1.0]
            })
            sublime.set_timeout(lambda: self.open_it(target, 1), 50)
        else:
            next_grp = 1 if self.window.active_group() == 0 else 0
            self.open_it(target, next_grp)

    def open_it(self, target, group):
        self.window.open_file(target, flags=sublime.FORCE_GROUP, group=group)
        self.window.focus_group(group)
