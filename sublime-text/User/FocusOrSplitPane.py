import sublime
import sublime_plugin

class FocusOrSplitPaneCommand(sublime_plugin.WindowCommand):
    def run(self, group=0):
        window = self.window
        
        # If we asked for the 2nd column (group 1) but only 1 exists, split the screen
        if group == 1 and window.num_groups() == 1:
            window.run_command("set_layout", {
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]],
                "cols": [0.0, 0.5, 1.0],
                "rows": [0.0, 1.0]
            })
        
        # Snap keyboard focus to the requested column
        window.focus_group(group)
