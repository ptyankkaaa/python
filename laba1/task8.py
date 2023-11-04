from cmath import sqrt
import math

i=0
while i==0:
    A = int(input("Enter A != 0 and A >= (-10) : A = "))
    if (A == 0 or A <(-10)):
        print("Error, try again")
        i=0
    else:
        i+=1
        break

B = int(input("Enter B = "))

i=0
while i==0:
    C = int(input("Enter C <= 10 : C = "))
    if (C > 10):
        print("Error, try again")
        i=0
    else:
        i+=1
        break

x1 = ((-B-(math.sqrt(abs(pow(B,2)-(4*A*C)))))/(2*A))
x2 = ((-B+(math.sqrt(abs(pow(B,2)-(4*A*C)))))/(2*A))

if x1<x2:
    print("x1 =", "%.4f"%x1)
    print("x2 =", "%.4f"%x2)
else:
    print("x2 =", "%.4f"%x2)
    print("x1 =", "%.4f"%x1)



