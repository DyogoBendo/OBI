#!/usr/bin/env python3

MOD = 1000000007

MAXN = 10000
N = int(input())

muro = [None for i in range(MAXN+1)]
# base
muro[0] = 1
muro[1] = 1
muro[2] = 5

#recursao
for i in range(3,N+1):
    muro[i] = (muro[i-1]+4*muro[i-2]+2*muro[i-3])%MOD;

# imprime a  resposta
print(muro[N])

