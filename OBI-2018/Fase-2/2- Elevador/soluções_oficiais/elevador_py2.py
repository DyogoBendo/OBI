#!/usr/bin/env python2.7

# Guilherme A. Pinto, OBI-2018, elevador

[N] = [int(c) for c in raw_input().split()]
p = [int(c) for c in raw_input().split()]

p.sort()

# inclui sentinela
p[0:0] = [0]

res = 'S'

for i in xrange(N):
    if ( p[i+1]-p[i] > 8 ):
        res = 'N'
        break

print res
