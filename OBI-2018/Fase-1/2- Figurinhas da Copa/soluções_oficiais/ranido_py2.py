#!/usr/bin/env python
# -*- coding: utf-8 -*-
# album de figurinhas


n,c,m = [int(i) for i in raw_input().split()]

# usando uma lista para as figurinhas carimbadas já compradas
album = []
carimbadas = [int(i) for i in raw_input().split()]
compradas = [int(i) for i in raw_input().split()]

for x in compradas:
    if (x in carimbadas) and (x not in album):
        album.append(x)

# escreve a resposta
print(len(carimbadas) - len(album))
