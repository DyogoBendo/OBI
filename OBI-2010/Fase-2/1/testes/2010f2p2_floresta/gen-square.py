#!/usr/bin/python

import math
import sys

N = int(sys.argv[1])
x = int(math.sqrt(2*N-1))
if x % 2 == 0:
   x -= 1

print (x*x+1) / 2
