#!/usr/bin/python
# encoding=utf-8

#####
#  r. anido
#  tarefa Calculo, OBI2015, Fase 2
####

n, m = [int(x) for x in raw_input().split()]
first = [int(x) for x in raw_input().split()]
second = [int(x) for x in raw_input().split()]

first.extend([0] * m)
second.extend([0] * n)
l = len(first)
result=[0 for i in xrange(l)]

# calcula resultado
carry=0
for i in xrange(l-1,-1,-1):
    r = first[i]+second[i]+carry
    if r <= 1:
        carry=0
        result[i]=r
    elif r==2:
        carry=1
        result[i]=0
    else:
        carry=1
        result[i]=1

# descarta digitos 0 do final, tomando o cuidado de não descartar todos
# se o resultado for zero
discard=0
for i in xrange(l-1,0,-1):
    if result[i] != 0:
        break
    discard+=1

# escreve resultado
print " ".join(str(i) for i in result[:-discard])
