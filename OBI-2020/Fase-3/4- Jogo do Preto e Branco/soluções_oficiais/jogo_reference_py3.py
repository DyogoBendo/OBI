#!/usr/bin/env pypy3

def fill(tabuleiro,i):
    if i >= len(possiveis):
        return 0
    lin, col = possiveis[i]
    brancas1,brancas2 = 0,0
    if tabuleiro[lin][col] == 0:
        # continua sem colocar peca branca
        brancas1 = fill(tabuleiro,i+1)
        # continua colocando peca branca
        if tabuleiro[lin-1][col] != -1 and tabuleiro[lin][col-1] != -1 and tabuleiro[lin+1][col] != -1 and tabuleiro[lin][col+1] != -1:
            tabuleiro[lin][col] = -1 # peca branca
            brancas2 = 1 + fill(tabuleiro,i+1)
            tabuleiro[lin][col] = 0 # restaura
    return max(brancas1,brancas2)
        
max_num = 0
L,C = [int(i) for i in input().split()]

# constroi tabuleiro com bordas de valor 2 para facilitar
tabuleiro = []
tabuleiro.append([2 for i in range(C+2)])
for i in range(L):
    tabuleiro.append([2] + [0 for i in range(C)] + [2])
tabuleiro.append([2 for i in range(C+2)])

possiveis = set()
P = int(input())
pretas = []
# coloca pretas
for k in range(P):
    i,j = [int(x) for x in input().split()]
    tabuleiro[i][j] = 1
    pretas.append((i,j))

# constroi lista de possiveis
for i,j in pretas:
    if tabuleiro[i+1][j] == 0:
        possiveis.add((i+1,j))
    if tabuleiro[i-1][j] == 0:
        possiveis.add((i-1,j))
    if tabuleiro[i][j+1] == 0:
        possiveis.add((i,j+1))
    if tabuleiro[i][j-1] == 0:
        possiveis.add((i,j-1))

# transforma possiveis em lista para poder percorrer com índice
possiveis = list(possiveis) 
max_num = fill(tabuleiro,0)
print(max_num)
