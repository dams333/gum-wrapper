from .program import *

class BorderType:
	NONE = 'none'
	NORMAL = 'normal'
	ROUNDED = 'rounded'
	DOUBLE = 'double'

class AlignmentType:
	LEFT = 'left'
	CENTER = 'center'
	RIGHT = 'right'
	MIDDLE = 'middle'
	TOP = 'top'
	BOTTOM = 'bottom'

class GumStyle:
	def __init__(self, lines, background_color="", text_color="", border=BorderType.NONE, border_background_color="", border_character_color="", align=AlignmentType.MIDDLE, padding=[0, 0], margin=[0, 0], height=-1, width=-1, bold=False, faint=False, italic=False, strikethrough=False, undeline=False):
		self.lines = lines
		self.background_color = background_color
		self.text_color = text_color
		self.border = border
		self.border_background_color = border_background_color
		self.border_character_color = border_character_color
		self.align = align
		self.padding = str(padding[0]) + " " + str(padding[1])
		self.margin = str(margin[0]) + " " +str( margin[1])
		self.height = height
		self.width = width
		self.bold = bold
		self.faint = faint
		self.italic = italic
		self.strikethrough = strikethrough
		self.undeline = undeline

	def export(self):
		args = []
		for line in self.lines:
			args.append(line)
		if self.background_color != "":
			args.append('--background=' + self.background_color)
		if self.text_color != "":
			args.append('--foreground=' + self.text_color)
		if self.border != BorderType.NONE:
			args.append('--border=' + self.border)
		if self.border_background_color != "":
			args.append('--border-background=' + self.border_background_color)
		if self.border_character_color != "":
			args.append('--border-foreground=' + self.border_character_color)
		args.append('--align=' + self.align)
		if self.width != -1:
			args.append('--width=' + str(self.width))
		if self.height != -1:
			args.append('--height=' + str(self.height))
		args.append('--padding=' + self.padding)	
		args.append('--margin=' + self.margin)
		if self.bold:
			args.append('--bold')
		if self.faint:
			args.append('--faint')
		if self.italic:
			args.append('--italic')
		if self.strikethrough:
			args.append('--strikethrough')
		if self.undeline:
			args.append('--underline')
		return args

def gum_style(style):
	args = ["style"]
	args.extend(style.export())
	run_program_without_return("gum", args)

def gum_join_horizontal(styles):
	res = []
	for style in styles:
		args = ["style"]
		args.extend(style.export())
		(stdout, exit_code) = run_program("gum", args)
		res.append(stdout.decode("utf-8"))

	args = ["join", "--horizontal"]
	args.extend(res)
	run_program_without_return("gum", args)

def gum_join_vertical(styles, align=AlignmentType.CENTER):
	res = []
	for style in styles:
		args = ["style"]
		args.extend(style.export())
		(stdout, exit_code) = run_program("gum", args)
		res.append(stdout.decode("utf-8"))

	args = ["join", "--vertical"]
	args.append('--align=' + align)
	args.extend(res)
	run_program_without_return("gum", args)

def gum_join_table(styles, align=AlignmentType.CENTER):
	res = []
	for line_styles in styles:
		line = []
		for style in line_styles:
			args = ["style"]
			args.extend(style.export())
			(stdout, exit_code) = run_program("gum", args)
			line.append(stdout.decode("utf-8"))
		args = ["join", "--horizontal"]
		args.extend(line)
		(stdout, exit_code) = run_program("gum", args)
		res.append(stdout.decode("utf-8"))

	args = ["join", "--vertical"]
	args.append('--align=' + align)
	args.extend(res)
	run_program_without_return("gum", args)