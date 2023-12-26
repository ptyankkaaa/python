import math

a = -3
b = -1
c = 0.2
h=1
for i in range(1, 12, h):
    print(float('{:.3f}'.format(((a*i+b)/pow(i,(5/3)))*c+pow(i, a))))


