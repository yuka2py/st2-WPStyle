import re
import sublime
import sublime_plugin

class WpstyleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		patterns = (
			(re.compile(r'\((?=\S)', re.M), r'( '),
			(re.compile(r'(?<=\S)\)', re.M), r' )'),
			(re.compile(r'\(\s+\)', re.M), r'()'),
			(re.compile(r'\(\s*(array|bool|boolean|string|integer|object|float|double)\s*\)', re.M), r'(\1)'),
			(re.compile(r'\(\s+$', re.M), r'('),
		)

		regions = self.view.sel()
		if regions[0].size() == 0:
			region = sublime.Region(0, self.view.size())
			regions.add(region)

		for region in regions:
			text = self.view.substr(region)
			for pattern, replace in patterns:
				text = pattern.sub(replace, text)
			self.view.replace(edit, region, text)

class WpFindHookCallCommand(sublime_plugin.WindowCommand):
	def run(self):
		open_find_in_files_with_text(self.window, 
			"""(do_action|apply_filters)(_ref_array)?\([ "']+""")

class WpFindHookRegisteringCommand(sublime_plugin.WindowCommand):
	def run(self):
		open_find_in_files_with_text(self.window, 
			"""(add_action|add_filter)\([ "']+""")

def open_find_in_files_with_text(win, text):
	win.run_command("show_panel", {
		"panel":"find_in_files",
	})
	clipboard = sublime.get_clipboard()
	sublime.set_clipboard(text)
	win.run_command("paste")
	sublime.set_clipboard(clipboard)



