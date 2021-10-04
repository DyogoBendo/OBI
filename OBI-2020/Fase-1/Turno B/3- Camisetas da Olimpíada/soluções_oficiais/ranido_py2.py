#!/usr/bin/env python2

N = input()
tamanhos = [int(i) for i in raw_input().split()]
prod_peq = input()
prod_med = input()

for i in tamanhos:
    if i == 1:
        prod_peq -= 1
    else:
        prod_med -= 1

if prod_peq < 0 or prod_med < 0:
    print('N')
else:
    print('S')
