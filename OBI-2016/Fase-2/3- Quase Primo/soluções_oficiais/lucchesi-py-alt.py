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

n, K = map(int, input().split())
k = list(map(int, input().split()))
print("%d\n" % quaseprimo(n, k))
