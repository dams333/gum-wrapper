from .program import *

def gum_choose(items, height=-1, cursor="", header="", limit=1, selected=[]):
	args = ["choose"]
	if height != -1:
		args.append('--height=' + str(height))
	if cursor != "":
		args.append('--cursor=' + cursor)
	if header != "":
		args.append('--header=' + header)
	if limit > 1:
		args.append('--limit=' + str(limit))
	elif limit == -1:
		args.append('--no-limit')
	if len(selected) > 0:
		args.append('--selected=' + ",".join(selected))

	for item in items:
		args.append(item)

	(stdout, exit_code) = run_program("gum", args)
	if (limit == 1):
		return stdout.decode("utf-8").split("\n")[0]
	return stdout.decode("utf-8").split("\n")[0:-1]

def gum_confirm(question="", affirmative="", negative=""):
	args = ["confirm"]
	if question != "":
		args.append(question)
	if affirmative != "":
		args.append('--affirmative=' + affirmative)
	if negative != "":
		args.append('--negative=' + negative)

	(stdout, exit_code) = run_program("gum", args)
	return exit_code == 0

class FileType:
	FILE = 1
	DIRECTORY = 2

def gum_file(directory="", cursor="", all_file=False, type=FileType.FILE, height=-1):
	args = ["file"]
	if directory != "":
		args.append(directory)
	if cursor != "":
		args.append('--cursor=' + cursor)
	if all_file:
		args.append('--all')
	if type == FileType.FILE:
		args.append('--file')
	if type == FileType.DIRECTORY:
		args.append('--directory')
	if height != -1:
		args.append('--height=' + str(height))

	(stdout, exit_code) = run_program("gum", args)
	return stdout.decode("utf-8").split("\n")[0]
	
def gum_filter(values, indicator="", selected_prefix="", unselected_prefix="", header="", placeholder="", width=-1, height=-1, value="", reverse=False):
	args = ["filter"]
	if indicator != "":
		args.append('--indicator=' + indicator)
	if selected_prefix != "":
		args.append('--selected-prefix=' + selected_prefix)
	if unselected_prefix != "":
		args.append('--unselected-prefix=' + unselected_prefix)
	if header != "":
		args.append('--header=' + header)
	if placeholder != "":
		args.append('--placeholder=' + placeholder)
	if width != -1:
		args.append('--width=' + str(width))
	if height != -1:
		args.append('--height=' + str(height))
	if value != "":
		args.append('--value=' + value)
	if reverse:
		args.append('--reverse')

	(stdout, exit_code) = run_program_stdin("gum", args, "\n".join(values).encode("utf-8"))
	return stdout.decode("utf-8").split("\n")[0]