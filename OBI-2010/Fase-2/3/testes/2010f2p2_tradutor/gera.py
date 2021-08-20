#!/usr/bin/env python

import os, sys, random

N = int(sys.argv[1])
M = int(sys.argv[2])

def gera_cadeia(size):
    ret = str(random.randint(1, 9))
    for i in range(size-1):
        ret += str(random.randint(0, 9))
    return ret

print gera_cadeia(N)
print gera_cadeia(M)
