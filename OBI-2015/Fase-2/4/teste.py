from pathlib import Path
from calculo import main
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname (os.path.dirname(current_dir)))
sys.path.append(root_dir)

from test_package.test_file import create_test

if __name__ == '__main__':    
    print(current_dir)
    print(os.path.basename(current_dir))
    files =  Path(current_dir, "testes")    
    create_test(main, files)
    
    