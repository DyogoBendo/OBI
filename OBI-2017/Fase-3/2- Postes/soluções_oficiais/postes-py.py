#!/usr/bin/env python2.7

# Guilherme A. Pinto, OBI-2017, postes

[N] = [int(c) for c in raw_input().split()]

substituidos = 0
consertados = 0

X = [int(c) for c in raw_input().split()]

for i in range(N):
    if ( X[i] < 50 ):
        substituidos += 1
    if ( 50 <= X[i] < 85 ):
        consertados += 1

print substituidos, consertados
