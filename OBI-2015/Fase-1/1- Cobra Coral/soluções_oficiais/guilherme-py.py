#!/usr/bin/env python2.7

A,B,C,D = [int(x) for x in raw_input().split()]

if ( A == C or B == D ): resp = "V"
else: resp = "F"

print resp
