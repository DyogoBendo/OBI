from pathlib import Path
from floresta import main
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname (os.path.dirname(current_dir)))
sys.path.append(root_dir)

from test_package.test_file import create_test

if __name__ == '__main__':    
    print(current_dir)
    print(os.path.basename(current_dir))
    files =  Path(current_dir, "tests")    
    txt = create_test(main, files, number_tests=11, start_position=0)

    ARQUIVO_FINAL = "resultado_testes.md"

    path_atual = current_dir + "/" + ARQUIVO_FINAL
    if os.path.exists(path_atual):
        os.remove(path_atual)
    f = open(path_atual, "w")
    f.write(txt)
    
    
    