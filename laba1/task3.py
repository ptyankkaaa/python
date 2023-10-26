import math

for i in range(10, 31):
    x = i/10 
    print(x)
    print("f(x) =", 2**(x+1)-(math.sin(x-1)**3))
