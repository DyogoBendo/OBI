from pathlib import Path
from chocolate import main
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname (os.path.dirname(current_dir)))
sys.path.append(root_dir)

from test_package.test_file import create_test

if __name__ == '__main__':    
    print(current_dir)
    print(os.path.basename(current_dir))
    files =  Path(current_dir, "tests")    
    txt = create_test(main, files, number_tests=19, start_position=2, prefix="test")

    ARQUIVO_FINAL = "resultado_testes.md"

    if os.path.exists(ARQUIVO_FINAL):
        os.remove(ARQUIVO_FINAL)
    f = open(ARQUIVO_FINAL, "w")
    f.write(txt)
    
    