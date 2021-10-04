#!/usr/bin/env python2.7

import sys

m, n = [int(x) for x in sys.stdin.readline().split()]

net_degree = [0 for i in range(n+1)]
soma = 0

for i in range(m):
    x, v, y = [int(x) for x in sys.stdin.readline().split()]
    net_degree[x] += v
    net_degree[y] -= v
    soma += v
    
res = 0
for i in range(1,n+1):
    if net_degree[i] > 0: res += net_degree[i]

if res == soma: c = 'N'
else: c = 'S'
sys.stdout.write("%s\n%d\n" % (c, res))
