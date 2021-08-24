#!/usr/bin/env python2.7

from itertools import permutations, izip_longest

def fat(n):
	r = 1
	while n:
		r *= n
		n -= 1
	return r

N = int(raw_input())
perms = []

for linha in xrange(fat(N)-1):
	perms.append( tuple(int(x) for x in raw_input().split()) )

for entrada, perm in izip_longest(sorted(perms), permutations(range(1,N+1))):
	if entrada != perm:
		print ' '.join(map(str,perm))
		break