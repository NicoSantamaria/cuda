from . import executor

def update(repository_url, branch_name):
    executor.execute('!git fetch')
    executor.execute('!git pull')