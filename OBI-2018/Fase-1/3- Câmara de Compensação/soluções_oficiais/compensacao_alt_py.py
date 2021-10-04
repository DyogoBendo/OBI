#!/usr/bin/env python2.7

import sys

m, n = [int(x) for x in sys.stdin.readline().split()]

adj = [[0 for i in range(n+1)] for j in range(n+1)]

soma = 0

for i in range(m):
    x, v, y = [int(x) for x in sys.stdin.readline().split()]
    adj[x][y] += v
    soma += v
    
for v in range(1, n+1):
    u = w = 1
    while u <= n and w <= n:
        if adj[u][v] == 0:
            u += 1
            continue
        if adj[v][w] == 0:
            w += 1
            continue
        d = min(adj[u][v], adj[v][w])
        if not u == w: adj[u][w] += d
        adj[u][v] -= d;
        adj[v][w] -= d;

res = 0
for v in range(1, n+1):
    for w in range(1, n+1):
        res += adj[v][w]
        
if res == soma: c = 'N'
else: c = 'S'
sys.stdout.write("%s\n%d\n" % (c, res))
