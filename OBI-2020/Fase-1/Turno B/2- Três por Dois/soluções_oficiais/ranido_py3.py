#!/usr/bin/env python3

# le entrada
N = int(input())
preco = []
sol = 0
for i in range(N):
    preco.append(int(input()))

# ordena do maior para o menor preco
preco.sort(reverse=True)

# soma precos, sem usar os gratuitos
for i in range(0,len(preco)):
    if i % 3 == 2:
        continue
    sol += preco[i]

print(sol)
