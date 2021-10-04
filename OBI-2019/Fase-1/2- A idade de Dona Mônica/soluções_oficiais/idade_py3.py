#!/usr/bin/env python3
# idade, OBI-2019
        
M = int(input())
A = int(input())
B = int(input())

res = M-A-B
res = max(res,A,B)

print( res )
