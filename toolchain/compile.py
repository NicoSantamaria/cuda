from IPython import get_ipython


def compile(filename: str, exec_name: str):
    ipython = get_ipython()
    ipython.run_cell_magic('writefile', filename, file_content)
    ipython.run_line_magic('system', f'nvcc {filename} -o {exec_name}')

    # ipython.run_line_magic('system', f'./{exec_name}')

