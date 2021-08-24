#!/usr/bin/env python2.7
# encoding: utf-8

import sys

def resolve(n, k, t):
    if k == -1: return 0
    res = resolve(n, k-1, t)
    if n >= t[k]: res = max(res, 1 + resolve(n-t[k], k-1, t))
    return res

s = sys.stdin.read().split()

n = int(s.pop(0))
t = [int(s[i]) for i in range(3)]
k = len(s) - 1
print resolve (n, k, t)
