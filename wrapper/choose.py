from .program import run_program

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
	