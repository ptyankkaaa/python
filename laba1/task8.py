from cmath import sqrt
import math

def examination(value, name):
    if (value <= -10 and value <= 10):
        return True
    else: 
        print("Enter a value in the range from 1 to 100")
        str =name + " = "
        a = int(input(str))
        examination(a, name)
        
stra = 'A'
strb = 'B'
strc = 'C'

a = int(input("A = "))
examination(a, stra)
b = int(input("B = "))
examination(b, strb)
c = int(input("C = "))
examination(c, strc)

x1 = ((-B-(math.sqrt(abs(pow(B,2)-(4*A*C)))))/(2*A))
x2 = ((-B+(math.sqrt(abs(pow(B,2)-(4*A*C)))))/(2*A))

if x1<x2:
    print("x1 =", "%.4f"%x1)
    print("x2 =", "%.4f"%x2)
else:
    print("x2 =", "%.4f"%x2)
    print("x1 =", "%.4f"%x1)



