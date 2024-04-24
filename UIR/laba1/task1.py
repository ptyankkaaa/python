import math

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

print("a = ", float('{:.3f}'.format(pow(x,2)/(8+(pow(x,2)/3)+(pow(y,2)/6)))))
print("b = ", float('{:.3f}'.format(x*(pow(math.cos(x+z), 3)+1))))

