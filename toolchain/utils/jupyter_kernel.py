from IPython import get_ipython
from dataclasses import dataclass


@dataclass
class CellExecutor:
    ipyhon: any = get_ipython()
    
    def execute(self, code):        
        result = self.ipython.run_cell(code)
        if result.error_in_exec:
            raise RuntimeError(result.error_in_exec)
        return result