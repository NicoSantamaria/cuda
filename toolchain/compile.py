from . import executor

def compile(project_name, executable_name):
    executor.execute(f"!nvcc src/{project_name}.cu -o {executable_name}")