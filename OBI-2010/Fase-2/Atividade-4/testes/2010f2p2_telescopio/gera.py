import sys
from random import *

max_n = int(sys.argv[1])


n = randint(1,max_n)
a = randint(1,10000)

print a
print n

for i in xrange(n):
	print randint(1,20000)

