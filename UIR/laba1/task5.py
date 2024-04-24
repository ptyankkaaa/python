import math

def examination(value, name):
    if (value >= 1 and value <= 100):
        return True
    else: 
        print("Enter a value in the range from 1 to 100")
        str =name + " = "
        a = int(input(str))
        examination(a, name)
        
strv1 = 'v1'
strv2 = 'v2'
strs = 's'
strt = 't'
v1 = int(input("V1 = "))
examination(v1, strv1)
v2 = int(input("V2 = "))
examination(v2, strv2)
s = int(input("S = "))
examination(s, strs)
t = int(input("T = "))
examination(t, strt)

print("S =", abs(s-t*(v1+v2)))