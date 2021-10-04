#!/usr/bin/env python3

# album de figurinhas

n,c,m = [int(i) for i in input().split()]

# usando um conjunto para as figurinhas carimbadas já compradas
album = set()
carimbadas = [int(i) for i in input().split()]
compradas = [int(i) for i in input().split()]

for x in compradas:
    if (x in carimbadas):
        album.add(x)

# escreve a resposta
print(len(carimbadas) - len(album))
