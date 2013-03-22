import re, sublime, sublime_plugin

class WpstyleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		patterns = (
			(re.compile(r'\(\s+'), '('),
			(re.compile(r'\s+\)'), ')'),
			(re.compile(r'\('), '( '),
			(re.compile(r'\)'), ' )'), 
			(re.compile(r'\(\s+\)'), '()'),
			(re.compile(r'\(\s*(array|bool|boolean|string|integer|object|float|double)\s*\)'), r'(\1)'),
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
