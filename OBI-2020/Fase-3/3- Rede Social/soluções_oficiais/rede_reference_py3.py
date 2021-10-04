#!/usr/bin/env pypy3

n = int(input())
repostagens = []
for i in range(n):
    repostagens.append(int(input()))

repostagens.sort(reverse=True)
fi = 0
while fi < n and repostagens[fi] >= fi + 1:
    fi += 1
print(fi)
