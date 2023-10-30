import math

i=0
while i==0:
    a = int(input("Enter a = "))
    if (a < 1):
        input("Error, a>=1 try again [Enter]")
        i=0
    else:
        i+=1
        break

i=0
while i==0:
    b = int(input("Enter b = "))
    if (b > 100):
        input("Error, b<=100 try again [Enter]")
        i=0
    else:
        i+=1
        break

print(round(pow((a*b),(1/2)),3))

