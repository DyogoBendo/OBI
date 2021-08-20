from pathlib import Path
import os

# Apesar de passar em todos os casos de testes, no site da OBI dá como incorreto

if __name__ == '__main__':

    files =  Path("OBI-2009", "Fase-2", "Atividade-4", "testes")                   

    for l in range(1, 11):
        print(l)
        files_folder = Path(files, "test" + str(l))
        for i in range(1, (len(os.listdir(files_folder)) // 2) + 1):
            input_filename = Path(files_folder, 'in' + str(i))        
            input_file = open(input_filename, 'r')
            n, m = map(int, input_file.readline().split())        
            paises = [[0, 0, 0, k + 1] for k in range(n)]
            for j in range(m):
                o, p, b = map(int, input_file.readline().split())
                paises[o - 1][0] += 1
                paises[p - 1][1] += 1
                paises[b - 1][2] += 1        
            paises = sorted(paises, key=lambda pais:(pais[0], pais[1], pais[2]), reverse=True)            
            
            s = ''
            for j in range(n):
                s += str(paises[j][3])
                if j < n - 1:
                    s+= ' '   
                else:
                    s += '\n' 
            output_filename = Path(files_folder, 'out' + str(i))
            output_file = open(output_filename, 'r')
            r = output_file.readline()
            print(i, s == r)        
        print()
    