#!/usr/bin/env python3

# OBI2020 - Fase 2
# fotografia

foto = [int(i) for i in input().split()]
N = int(input())

foto.sort()
melhor_moldura = -1
menor_area = 200 * 200
area = foto[0] * foto[1]
for i in range(N):
    moldura = [int(i) for i in input().split()]
    moldura.sort()
    if moldura[0] >= foto[0] and moldura[1] >= foto[1]:
        # moldura serve
        if moldura[0] * moldura[1] - area < menor_area:
            melhor_moldura = i+1
            menor_area = moldura[0] * moldura[1] - area

print(melhor_moldura)
