#!/usr/bin/env python

import sys

def quaseprimo(n, k):
    if k == []: res = n
    else:
        p = k.pop()
        res = quaseprimo(n, k)
        if n >= p: res -= quaseprimo(n / p, k) 
        k.append(p)
    return res

s = sys.stdin.read().split()
n = int(s.pop(0))
K = int(s.pop(0))
k = []
for i in range(K):
    k.append(int(s.pop(0)))
sys.stdout.write("%d\n" % quaseprimo(n, k))
