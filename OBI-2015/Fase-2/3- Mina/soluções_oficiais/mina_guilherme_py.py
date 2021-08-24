#!/usr/bin/env python2.7

import heapq

MAX = 100
INF = 100000

class Elemento:
    def __init__(self, ai, aj):
        self.i = ai
        self.j = aj
class Quadrado:
    def __init__(self, av, ad, am):
        self.v = av
        self.d = ad
        self.m = am

N = int(raw_input())
mina = [[Quadrado(0,INF,False) for j in xrange(N)] for i in xrange(N)]
for i in xrange(N):
    l = [int(x) for x in raw_input().split()]
    for j in xrange(N):
        mina[i][j].v = l[j]

# Dijkstra

q = [] # fila de prioridades (heap)
d = [0,1,0,-1,0]

mina[0][0].d = 0
heapq.heappush( q, ( 0, Elemento( 0, 0 ) ) )

while q:
    e = heapq.heappop( q )
    f = e[1]
    if ( not mina[f.i][f.j].m ):
        mina[f.i][f.j].m = True
        mina[f.i][f.j].d = e[0]
        if ( f.i == N-1 and f.j == N-1 ): break
        # para cada movimento ortogonal
        for k in xrange(4):
	    a = f.i + d[k]
            b = f.j + d[k+1]
	    if ( a >= 0 and a < N and b >= 0 and b < N and not mina[a][b].m ):
                heapq.heappush( q, ( e[0] + mina[a][b].v, Elemento(  a, b ) ) )

print mina[N-1][N-1].d
