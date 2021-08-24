#!/usr/bin/env python

codigo = raw_input().strip()

mensagem=''

i=0
while i<len(codigo):
    if codigo[i]==' ':
        mensagem=mensagem+' '
    else:
        i=i+1
        mensagem=mensagem+codigo[i]
    i=i+1

print mensagem
