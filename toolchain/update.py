def update(repository_url, branch_name):
    with JupyterKernelExecutor(timeout=30) as executor:
        executor.execute('!git fetch')
        executor.execute('!git pull')