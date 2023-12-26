import math

def examination(value, name):
    if (value >= 1 and value <= 100):
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

A, B, C = C, A, B

print("A =",A, "B =",B, "C =",C)
