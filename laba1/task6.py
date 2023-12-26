import math

def examination(value, name):
    if (value >= 1 and value <= 100):
        return True
    else: 
        print("Enter a value in the range from 1 to 100")
        str =name + " = "
        a = int(input(str))
        examination(a, name)
        
stra = 'a'
strb = 'b'

a = int(input("a = "))
examination(a, stra)
b = int(input("b = "))
examination(b, strb)


print(round(pow((a*b),(1/2)),3))

