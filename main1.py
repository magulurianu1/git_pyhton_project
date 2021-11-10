import math

x = int(input("Enter the Number"))

root = math.sqrt(x)
if int(root + 0.5) ** 2 == x:
    print(x, "is a perfect square")
else:
    print(x, "is not a perfect square")