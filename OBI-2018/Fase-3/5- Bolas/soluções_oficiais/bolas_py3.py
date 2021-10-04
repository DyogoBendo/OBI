#!/usr/bin/env python3

contador = [0 for i in range(10)]

resposta = 'S'
bolas = [int(c) for c in input().split()]
for b in bolas:
    contador[b] += 1
    if contador[b] > 4:
        resposta = 'N'

print(resposta)
