import math, sys
print("Enter sides of the triangle to find area")
s1 = int(input("Side a: "))
s2 = int(input("Side b: "))
s3 = int(input("Side c: "))
if s1 + s2 < s3 or s1 + s3 < s2 or s2 + s3 < s1:
    sys.exit("not a triangle")
s = (s1 + s2 + s3) / 2
print("Area of the triangle is:", round(math.sqrt(s * (s - s1) * (s - s2) * (s - s3)), 2))