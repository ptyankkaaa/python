import math

i=0
while i==0:
    v1 = int(input("V1 = "))
    if (v1>=1 and v1<=100):
        i+=1
    else:
        print("Enter a value in the range from 1 to 100")
        i==0

i=0
while i==0:
    v2 = int(input("V2 = "))
    if (v2>=1 and v2<=100):
        i+=1
    else:
        print("Enter a value in the range from 1 to 100")
        i==0

i=0
while i==0:
    s = int(input("S = "))
    if (s>=1 and s<=100):
        i+=1
    else:
        print("Enter a value in the range from 1 to 100")
        i==0

i=0
while i==0:
    t = int(input("T = "))
    if (t>=1 and t<=100):
        i+=1
    else:
        print("Enter a value in the range from 1 to 100")
        i==0

print("S =", abs(s-t*(v1+v2)))