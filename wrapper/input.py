from .program import run_program

def gum_simple_input(placeholder="", prompt="", value="", char_limit=-1, password=False, header=""):
	args = ["input"]
	if placeholder != "":
		args.append('--placeholder=' + placeholder)
	if prompt != "":
		args.append('--prompt=' + prompt)
	if value != "":
		args.append('--value=' + value)
	if char_limit != -1:
		args.append('--char-limit=' + str(char_limit))
	if password:
		args.append('--password')
	if header != "":
		args.append('--header=' + header)

	(stdout, exit_code) = run_program("gum", args)
	return stdout.decode("utf-8").strip()

def gum_multiline_input(height=-1, header="", placeholder="", prompt="", value="", char_limit=-1):
	args = ["write"]
	if height != -1:
		args.append('--height=' + str(height))
	if header != "":
		args.append('--header=' + header)
	if placeholder != "":
		args.append('--placeholder=' + placeholder)
	if prompt != "":
		args.append('--prompt=' + prompt)
	if value != "":
		args.append('--value=' + value)
	if char_limit != -1:
		args.append('--char-limit=' + str(char_limit))

	(stdout, exit_code) = run_program("gum", args)
	return stdout.decode("utf-8").strip()