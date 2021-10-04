#!/usr/bin/env python3

a = int(input())
b = int(input())


achou = False
for x in range(1,b+1):
    if b % x != 0:
        continue
    larg = b//x + 2
    compr = x + 2
    if a == 2*(compr+larg) - 4:
        achou = True
        break

if achou:
    print(compr,larg)
else:
    print(-1,-1)
