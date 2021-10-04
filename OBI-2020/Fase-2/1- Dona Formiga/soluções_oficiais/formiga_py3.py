#!/usr/bin/env python3

# OBI2020
# dona formiga

alcancados = 0

def busca(k):
    global alcancados
    if not visitado[k]:
        alcancados += 1
        visitado[k] = True
        for q in adj[k]:
            busca(q)

S, T, P = [int(i) for i in input().split()]
altura =  [int(i) for i in input().split()]
visitado =  [False for i in range(S)]

adj = [[] for i in range(S)]

for i in range(T):
    a,b = [int(i) for i in input().split()]
    a -= 1
    b -= 1
    if altura[a] > altura[b]:
        adj[a].append(b)
    elif altura[a] < altura[b]:
        adj[b].append(a)

busca(P-1)
print(alcancados-1)
