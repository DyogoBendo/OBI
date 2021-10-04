#!/usr/bin/env python2.7

# Guilherme A. Pinto, OBI-2017, imperio

import sys

def dfs( i, pai ):
    global res
    peso = 1
    for p in g[i]:
        if ( p != pai ):
            peso += dfs( p, i )
    dif = abs(N-2*peso)
    if ( dif < res ):
        res = dif
    return peso

[N] = [int(c) for c in raw_input().split()]

g = [[] for _ in range(N+1)]

for i in range(1,N):
    [A, B] = [int(c) for c in raw_input().split()]
    g[A].append( B )
    g[B].append( A )

res = N

sys.setrecursionlimit(10**5)

dfs( 1, -1 )

print res
