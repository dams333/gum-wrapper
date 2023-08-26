import subprocess

def run_program(command, args = []):
	proc = subprocess.Popen([command] + args, stdout=subprocess.PIPE)
	(stdout, stderr) = proc.communicate()
	exit_code = proc.wait()
	return (stdout, exit_code)

def run_program_stdin(command, args=[], stdin_content=""):
	proc = subprocess.Popen([command] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	(stdout, stderr) = proc.communicate(stdin_content)
	exit_code = proc.wait()
	return (stdout, exit_code)
	
def run_program_without_return(command, args = []):
	proc = subprocess.Popen([command] + args)
	proc.wait()