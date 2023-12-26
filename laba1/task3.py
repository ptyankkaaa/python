import math

for i in range(10, 31):
    x = i/10 
    print("f(x) =", float('{:.3f}'.format(2**(x+1)-(math.sin(x-1)**3))))
