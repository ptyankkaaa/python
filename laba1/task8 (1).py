import math

i=0
while i==0:
    A = int(input("Enter A != 0 and A >= (-10). A = "))
    if (A == 0 or A <(-10)):
        print("Error, try again")
        i=0
    else:
        i+=1
        break

B = int(input("Enter B = "))

i=0
while i==0:
    C = int(input("Enter C != 0 and C >= (-10). C = "))
    if (C == 0 or C <(-10)):
        print("Error, try again")
        i=0
    else:
        i+=1
        break

def d():
