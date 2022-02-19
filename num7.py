import math
n = float(input("A=")) # side
m = float(input("B=")) # side
angle = float(input("alpha=").split()[0]) # angle
print("Area of the triangle is:", n * m * round(math.sin(angle / (180/math.pi)),3)/2)