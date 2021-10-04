#!/usr/bin/env python3

def troca(x):
    '''troca o dígito da posição x com o último dígito'''
    global digito
    tmp = digito[-1]
    digito[-1] = digito[x]
    digito[x] = tmp

N = int(input())
digito = [int(c) for c in input().split()]  # strings são imutáveis, vamos usar uma lista

ze = -1;  # zero mais a esquerda
cd = -1;  # cinco mais a direita
zce = -1; # zero ou cinco, mais a esquerda

for i in range(len(digito)):
    if digito[i] == 0 and ze == -1:
        ze = i
    if digito[i] == 5:
        cd = i
    if (digito[i] == 5 or digito[i] == 0) and zce == -1:
        zce = i 

if zce == -1:         # nenhum digito 0, nem digito 5
    print(-1)
else:
    if digito[N-1] < 5:   # digito da unidade: 1, 2, 3 ou 4
        if ze != -1:
            troca(ze)
        else:
            troca(cd)
    else:                   # digito da unidade: 6, 7, 8 ou 9
        troca(zce)

    for i in range(len(digito)): # cuidado para imprimir apenas os espaços em branco necessários
        print(digito[i], end='')
        if i < N-1: 
            print(end=' ')        
    print()
