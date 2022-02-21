import math
n = int(input()) # amount of sides
s = int(input()) # side length
print(round(n * (s**2/ (4/math.tan(math.pi/n))),2)) # area of the polygon