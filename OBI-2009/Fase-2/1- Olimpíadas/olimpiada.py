from pathlib import Path
import os

# Apesar de passar em todos os casos de testes, no site da OBI dá como incorreto

def main(entrada=input, test=False):
    n, m = map(int, entrada().split())        
    paises = [[0, 0, 0, k + 1] for k in range(n)]
    for j in range(m):
        o, p, b = map(int, entrada().split())
        paises[o - 1][0] += 1
        paises[p - 1][1] += 1
        paises[b - 1][2] += 1        
    paises = sorted(paises, key=lambda pais:(pais[0], pais[1], pais[2]), reverse=True)                
    s = ''
    for j in range(n):
        s += str(paises[j][3])
        if j < n - 1:
            s+= ' '     
    if not test:
        print(s)
    else:
        return [s]

if __name__ == '__main__':
    main()
