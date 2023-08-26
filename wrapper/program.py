import subprocess

def run_program(command, args = []):
	proc = subprocess.Popen([command] + args, stdout=subprocess.PIPE)
	(stdout, stderr) = proc.communicate()
	exit_code = proc.wait()
	return (stdout, exit_code)
	