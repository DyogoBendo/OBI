#!/usr/bin/env python3

# OBI2020
# estrada

t = int(input())
n = int(input())
cidades = []
for i in range(n):
    cidades.append(int(input()))

cidades.sort()

compr_oeste,compr_leste = 0,0

# inicia com a extensao do primeiro trecho a oeste
compr_min = cidades[0] + (cidades[1] - cidades[0])/2
for i in range(1,n-1):
    dif_oeste = cidades[i] - cidades[i-1]
    dif_leste = cidades[i+1] - cidades[i]
    compr = dif_oeste/2 + dif_leste/2
    if compr < compr_min:
        compr_min = compr
# extensao do ultimo trecho a leste
compr = (cidades[n-1] - cidades[n-2])/2 + (t - cidades[n-1])
if compr < compr_min:
    compr_min = compr
print("{:.2f}".format(compr_min))
