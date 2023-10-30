import math

i=0

while i==0:
    A = int(input("Enter A >= -100. A = "))
    if A < (-100):
        input("Error, try again [Enter]")
        i==0
    else:
        i+=1
        break


B = int(input("Enter B = "))

j=0

while j==0:
    C = int(input("Enter C <= 100. C = "))
    if C > 100:
        input("Error? try again [Enter]")
        j==0
    else:
        j+=1
        break

A, B, C = C, A, B

print("A =",A, "B =",B, "C =",C)
