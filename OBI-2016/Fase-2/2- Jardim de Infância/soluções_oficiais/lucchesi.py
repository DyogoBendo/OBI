#!/usr/bin/env python
# coding: utf-8
# solução para o problema "jardim"

import sys

def dist2(i, j):
    return  (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
    
def delta_alpha(i, j, k):
    return (x[j]-x[i])*(y[k]-y[i]) - (x[k]-x[i])*(y[j]-y[i])


x = [0]
y = [0]
s = sys.stdin.read().split()
for i in range(7):
    x.append(int(s.pop(0)))
    y.append(int(s.pop(0)))

# ângulo p2p1p3 deve ser agudo
if dist2(1,2) + dist2(1,3) <= dist2(2, 3): print 'N'

# p1p2 e p1p3 têm o mesmo comprimento
elif dist2(1,2) != dist2(1,3): print 'N'

# p2, p3, p4 e p5 são colineares
elif delta_alpha(2,3,4) != 0 or delta_alpha(2,3,5) != 0: print 'N'

# os pontos médios de p2p3 e de p4p5 coincidem
elif x[2]+x[3] != x[4] + x[5] or y[2]+y[3] != y[4] + y[5]: print 'N'

# p2p3 > p4p5
elif dist2(2, 3) <= dist2(4,5): print 'N'

# p4p6 e p5p7 perpendiculares a p2p3
elif dist2(2,4) + dist2(4,6) != dist2(2,6) or \
     dist2(3,5) + dist2(5,7) != dist2(3,7): print 'N'

# p4p6 e p5p7 têm o mesmo comprimento
elif dist2(4,6) != dist2(5,7): print 'N'

# p1 e p6 separados pela reta que contém p2p3
elif delta_alpha(2, 3, 1) * delta_alpha(2,3,6) >= 0: print 'N'

else: print 'S'
