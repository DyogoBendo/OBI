#!/usr/bin/env python3

resultado = 0
atual = 0
n,k = [int(i) for i in input().split()]
soma = {0:1}

vals = [int(i) for i in input().split()]
i = 0
for x in vals:
    atual += x;
    try:
        resultado += soma[atual - k]
    except:
        pass
    if atual in soma.keys():
        soma[atual] += 1
    else:
        soma[atual] = 1
    i += 1

print(resultado)

