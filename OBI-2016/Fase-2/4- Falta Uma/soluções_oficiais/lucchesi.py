#!/usr/bin/env python2.7

import sys

def resolve(t):
    for j in range(1, len(t)):
        if t[j] < t[1]: return j
    return 1

s = sys.stdin.readline().split()
n = int(s[0])
r = [[0 for j in range(n+1)] for i in range(n)]

while True:
    s = sys.stdin.readline().split()
    if s == []: break
    for i in range(n):
        r[i][int(s.pop(0))] += 1
sep = ""
for i in range(n):
    sys.stdout.write("%s%d" % (sep, resolve(r[i])))
    sep = " "
sys.stdout.write("\n")
