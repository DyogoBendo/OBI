#!/usr/bin/env python2.7

N = int(raw_input())

nD = 0
for i in range(N):
    rodada = raw_input().split()
    D,X = int(rodada[0]),int(rodada[1])
    if ((X==(D+1)%5) or (X==(D+2)%5)):
        nD += 1

if ( nD > (N-nD) ):
    print "dario"
else:
    print "xerxes"
