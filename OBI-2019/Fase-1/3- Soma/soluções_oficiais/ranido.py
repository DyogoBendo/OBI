#!/usr/bin/env python3

MAX = 500000


N,K = [int(i) for i in input().split()]

o = [int(i) for i in input().split()]

  # remove zeros do vetor original o[] e cria vetor auxiliar z[]
  # contendo o numero de zeros a esquerda de cada nao-zero
  #
  # entrada, o[]: 2 0 1 1 0 0 8 4 1 3, produz:
  #
  #          q[]: 2 1 1 8 4 1 3
  #          z[]: 0 1 0 2 0 0 0 0
    
cnt = 0
k = 0
q = []
z = []
for i in range(N):
    if o[i] == 0:
        cnt += 1
    else:
        q.append(o[i])
        z.append(cnt)
        cnt = 0

z.append(cnt)
N = len(q);
q.append(0) # sentinela

count = 0

if K == 0:
    # sequencia de z[i] zeros possui combinacao de z[i]+1, 2 a 2, retangulos
    for i in range(len(z)):
        count += ((z[i]+1)*z[i])/2
else:
        # dois ponteiros sobre o vetor de nao-zeros
        l = 0
        r = 0 
        soma = q[0] 
    
        while r < N:
            if soma <= K:
                if soma == K:
                    count += (z[l]+1)*(z[r+1]+1)
                r += 1
                soma += q[r] # move ponteiro direito
            else:
                soma -= q[l] # move ponteiro esquerdo
                l += 1
                if l > r:
                    r = l
                    soma = q[r] # reinicia janela

print(int(count))
