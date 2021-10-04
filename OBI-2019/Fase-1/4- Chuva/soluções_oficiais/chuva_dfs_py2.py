#!/usr/bin/env python2.7
# chuva, dfs, OBI-2019

def dfs( i, j ):
    # molha
    p[i][j] = 'o'

    # base
    if ( i == N-1 ): return

    # recusao
    if ( p[i+1][j] == '.' ): dfs( i+1, j )
    if ( p[i+1][j] == '#' ):
        if ( p[i][j-1] == '.' ): dfs( i, j-1 )
        if ( p[i][j+1] == '.' ): dfs( i, j+1 )
        
import sys
f = sys.stdin
sys.setrecursionlimit(5000)

N,M = [int(i) for i in f.readline()[:-1].split(" ")]
        
p = []
for i in xrange(N):
    p.append(list(f.readline()[:-1]))

dfs( 0, p[0].index('o') )

for i in xrange(N):
    print "".join(p[i])
    
