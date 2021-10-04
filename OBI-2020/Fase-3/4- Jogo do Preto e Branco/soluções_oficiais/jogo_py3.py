#!/usr/bin/env pypy3

from copy import deepcopy

def printboard(board):
    for i in range(1,L+1):
        for j in range(1,C+1):
            if board[i][j]==-1:
                print('*',end=' ')
            else:
                print(board[i][j],end=' ')
        print()

def fill(board,i):
    if i >= len(possiveis):
        return 0;
    lin, col = possiveis[i]
    brancas1,brancas2 = 0,0
    if board[lin][col] == 0:
        # ainda nao foi checado
        # tenta sem colocar peca branca
        oldboard = deepcopy(board)
        brancas1 = fill(board,i+1)
        board = oldboard
        # tenta colocando peca branca
        if board[lin-1][col] != -1 and board[lin][col-1] != -1 and board[lin+1][col] != -1 and board[lin][col+1] != -1:
            oldboard = deepcopy(board)
            board[lin][col] = -1 # peca branca
            brancas2 = 1 + fill(board,i+1)
            board = oldboard
    return(max(brancas1,brancas2))
        
max_num = 0
L,C = [int(i) for i in input().split()]

# constroi tabuleiro com bordas para facilitar
board = []
board.append([2 for i in range(C+2)])
for i in range(L):
    board.append([2] + [0 for i in range(C)] + [2])
board.append([2 for i in range(C+2)])

possiveis = set()
P = int(input())
pretas = []
# coloca pretas
for k in range(P):
    i,j = [int(x) for x in input().split()]
    board[i][j] = 1
    pretas.append((i,j))

# constroi lista de possiveis
for i,j in pretas:
    if board[i+1][j] == 0:
        possiveis.add((i+1,j))
    if board[i-1][j] == 0:
        possiveis.add((i-1,j))
    if board[i][j+1] == 0:
        possiveis.add((i,j+1))
    if board[i][j-1] == 0:
        possiveis.add((i,j-1))

#printboard(board)
possiveis = sorted(list(possiveis))
#print(possiveis)
max_num = fill(board,0)
print(max_num)
