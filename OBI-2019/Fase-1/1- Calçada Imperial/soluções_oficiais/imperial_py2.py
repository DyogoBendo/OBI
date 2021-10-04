#!/usr/bin/env python2
# OBI2019
# Tarefa Imperial

    
N = int(input())
v = []
for i in range(N):
    v.append(int(input()))

res = 1
visto = set()
for i in range(N):
    if v[i] in visto:
        continue
    visto.add(i)
    for j in range(N):
	atual = 0
	ultimo = -1
	for k in range(N):
	    if (v[k] == v[i] or v[k] == v[j]) and v[k] != ultimo:
		atual += 1
		ultimo = v[k]
	res = max(res,atual)

print(res)
