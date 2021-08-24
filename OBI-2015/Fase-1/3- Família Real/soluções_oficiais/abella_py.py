#!/usr/bin/python

import sys

n, m = [int(x) for x in raw_input().split()]

children = [[] for x in range(n+1)]
parent = [int(x) for x in raw_input().split()]
for childid, parentid in enumerate(parent, 1):
    children[parentid].append(childid)

came = [False] * (n+1)
camelist = [int(x) for x in raw_input().split()]
for id in camelist:
    came[id] = True

genmany, gencame = [0] * (n+1), [0] * (n+1)

def dfs(v, dist):
    genmany[dist] += 1
    if came[v]:
        gencame[dist] += 1

    for son in children[v]:
        dfs(son, dist+1)

dfs(0, 0)

for d in range(1, n+1):
    if genmany[d] == 0:
        break
    if d > 1:
        sys.stdout.write(" ")
    sys.stdout.write("%.2f" % (100.0 * gencame[d] / genmany[d]) )
print
