#!/usr/bin/env python2.7
 ############################################################################
 # Arthur Pratti Dadalto
 # OBI 2015 - Macaco
 # Convex hull com line sweep
 ############################################################################

class point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __lt__(self, other):
		return self.x < other.x or (self.x == other.x and self.y < other.y)

def cross (p0, p1, p2):
	return (p1.x - p0.x)*(p2.y - p0.y) - (p2.x - p0.x)*(p1.y - p0.y)

n = int(raw_input())
p = [point(0,0) for i in range(n)]
ch = [0 for i in range(n)]

for i in range(n):
	l = [int(x) for x in raw_input().split()]
	p[i].x, p[i].y = l[0], l[1]

p.sort()
nch = 0

for i in range(n):
	while (nch > 1 and cross(p[ch[nch-2]], p[ch[nch-1]], p[i]) >= 0):
		nch -= 1;
	ch[nch] = i
	nch += 1;

print nch - 1
