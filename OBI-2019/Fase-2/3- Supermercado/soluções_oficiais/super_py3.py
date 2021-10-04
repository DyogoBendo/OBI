#!/usr/bin/env python3

N = int(input())

p,g = input().split()
p = float(p)
g = int(g)
preco_grama = p / g;

for i in range(N-1):
    p,g = input().split()
    p = float(p)
    g = int(g)
    if p/g < preco_grama:
        preco_grama = p / g;

print('{:.2f}'.format(1000*preco_grama))
