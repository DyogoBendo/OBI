#!/usr/bin/python

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

assert len(primes) == 24

def dfs(p, n, d):
   print d, (n+1)/2
   if p >= len(primes):
      return
   for e in range(1, 19):
      m = n * primes[p]**e
      if m > 2*10**4 - 1:
         return
      dfs(p+1, m, d * (e+1))

dfs(0, 1, 1)
