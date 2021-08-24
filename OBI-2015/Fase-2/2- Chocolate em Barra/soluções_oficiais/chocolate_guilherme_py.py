#!/usr/bin/env python2.7

[N] = [int(x) for x in raw_input().split()]
[X1, Y1] = [int(x) for x in raw_input().split()]
[X2, Y2] = [int(x) for x in raw_input().split()]

if ( (X1 <= N/2 and X2 > N/2 ) or
     (X2 <= N/2 and X1 > N/2 ) or
     (Y1 <= N/2 and Y2 > N/2 ) or
     (Y2 <= N/2 and Y1 > N/2 ) ): print "S"
else: print "N"
