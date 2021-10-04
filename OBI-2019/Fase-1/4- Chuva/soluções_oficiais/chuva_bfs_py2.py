#!/usr/bin/env python2.7
# chuva, bfs, OBI-2019

def molha( a, b ):
    p[a][b] = 'o'
    q.append( [a,b] )
    

def bfs( i, j ):

    q.append( [i,j] )

    while( len(q) > 0 ):
        a, b = q.pop(0)
    
        if ( a == N-1 ): continue

        if ( p[a+1][b] == '.' ): molha( a+1, b )
        if ( p[a+1][b] == '#' ):
            if ( p[a][b-1] == '.' ): molha( a, b-1 )
            if ( p[a][b+1] == '.' ): molha( a, b+1 )

import sys
f = sys.stdin

N,M = [int(i) for i in f.readline()[:-1].split(" ")]
        
p = []
for i in xrange(N):
    p.append(list(f.readline()[:-1]))

# fila
q = []

bfs( 0, p[0].index('o') )

for i in xrange(N):
    print "".join(p[i])
    
