#!/usr/bin/env python3

N = int(input())
tamanhos = [int(i) for i in input().split()]
prod_peq = int(input())
prod_med = int(input())

pref_peq = tamanhos.count(1)
pref_med = tamanhos.count(2)

if prod_peq < pref_peq or prod_med < pref_med:
    print('N')
else:
    print('S')
