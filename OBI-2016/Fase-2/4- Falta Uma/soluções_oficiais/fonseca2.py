#!/usr/bin/env python2.7

from itertools import permutations

N = int(raw_input())

perms = set(permutations(xrange(1,N+1)))

falta = set()
for i in xrange(len(perms)-1):
        falta.add(tuple(int(x) for x in raw_input().split()))
        
faltando = perms - falta

for e in faltando:
        print ' '.join(map(str,e))
