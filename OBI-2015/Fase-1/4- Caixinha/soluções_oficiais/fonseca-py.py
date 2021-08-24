#!/usr/bin/env python2.7
# Fernando Fonseca

N,M = [int(n) for n in raw_input().split(" ")]

ans = (N-1)*(N-2)/2
if (N - 1 - M >= 2): ans -= 3*(N - 1 - M)*(N - 2 - M)/2
if (N - 1 - 2*M >= 2): ans += 3*(N - 1 - 2*M)*(N - 2 - 2*M)/2
if (N - 1 - 3*M >= 2): ans -= (N - 1 - 3*M)*(N - 2 - 3*M)/2

print ans
