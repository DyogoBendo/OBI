#!/usr/bin/env python2.7

import sys

MAX = 200000

N = int(raw_input())

letra = [0 for i in xrange(MAX+1)]
direita = [0 for i in xrange(MAX+1)]

for i in range(N):
    I = raw_input().split()
    E = int(I[0])          # E
    letra[E] = I[1]        # C
    direita[E] = int(I[2]) # D

E = 0
while( E != 1 ):
    sys.stdout.write("%c" % letra[E])
    E = direita[E]
print
