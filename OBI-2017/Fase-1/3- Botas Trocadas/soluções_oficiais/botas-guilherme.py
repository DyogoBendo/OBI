#!/usr/bin/env python2.7

MIN = 30
MAX = 60

N = int(raw_input())

bota = []

for i in range(N):
    tam,pe = raw_input().split()
    bota.append( [int(tam),pe] )

cnt = 0
for i in range(MIN,MAX+1):
    cnt += min(bota.count([i,'E']),bota.count([i,'D']))
    
print cnt
