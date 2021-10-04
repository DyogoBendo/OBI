#!/usr/bin/env python2.7

# Guilherme A. Pinto, OBI-2017, arranhaceu

[N, Q] = [int(c) for c in raw_input().split()]

bit = [0]*(N+1)
moradores = [int(c) for c in raw_input().split()]
moradores[:0] = [0]

def update( x, v ):
    while (x <= N):
        bit[x] += v
        x += x&-x

def query( x ):
    r = 0
    while (x > 0):
        r += bit[x]
        x -= x&-x
    return r
        
for i in range(1,N+1):
    update( i, moradores[i] )

while ( Q > 0 ):
    Q -= 1
    q = [int(c) for c in raw_input().split()]
    if ( q[0] == 0 ):
        i, m = q[1], q[2]
        d = m - moradores[i]
        moradores[i] = m
        update( i, d )
    else:
        print query( q[1] )
