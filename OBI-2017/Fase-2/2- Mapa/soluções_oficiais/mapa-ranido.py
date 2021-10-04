#!/usr/bin/env python3
# r. anido
# tarefa mapa
# OBI2017

# lê as dimensões do mapa
L,C=input().split()
L=int(L)
C=int(C)
                                          # vamos construir um mapa com uma borda de caracteres '.'
                                          # para não ter que se preocupar com índices fora dos limites
mapa = ['.'*(C+2)]                        # esta é a primeira linha do mapa
for l in range(1,L+1):                    
    mapa.append(list('.'+input()+'.'))    # cada linha inicia e termina com o caractere '.'
    for c in range(1,C+1):
        if mapa[l][c] == 'o':             # marca posição inicial de Hermione
            pos_l = l
            pos_c = c
mapa.append('.'*(C+2))                    # esta é a última linha do mapa

while True:                               # segue Hermione
    if mapa[pos_l+1][pos_c]=='H':
        mapa[pos_l][pos_c]='x'
        pos_l,pos_c=pos_l+1,pos_c
    elif mapa[pos_l-1][pos_c]=='H':
        mapa[pos_l][pos_c]='x'
        pos_l,pos_c=pos_l-1,pos_c
    elif mapa[pos_l][pos_c+1]=='H':
        mapa[pos_l][pos_c]='x'
        pos_l,pos_c=pos_l,pos_c+1
    elif mapa[pos_l][pos_c-1]=='H':
        mapa[pos_l][pos_c]='x'
        pos_l,pos_c=pos_l,pos_c-1
    else:
        break

# imprime o resultado
print(pos_l,pos_c)
