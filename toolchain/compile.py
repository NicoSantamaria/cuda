from .__init__ import executor


def compile(project_name, executable_name):
    executor.execute("!git fetch")
    executor.execute("!git pull")