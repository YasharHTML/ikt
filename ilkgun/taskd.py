import math, sys # import math and sys modules 
print("Enter sides of the triangle to find area") # prompt user to enter sides of the triangle
s1 = int(input("Side a: ")) # side a
s2 = int(input("Side b: ")) # side b
s3 = int(input("Side c: ")) # side c
if s1 + s2 < s3 or s1 + s3 < s2 or s2 + s3 < s1: # if the sum of any two sides is less than the third side, the triangle is invalid
    sys.exit("not a triangle") # exit the program with error message "not a triangle"
s = (s1 + s2 + s3) / 2 # calculate the semi-perimeter
print("Area of the triangle is:", round(math.sqrt(s * (s - s1) * (s - s2) * (s - s3)), 2)) # print the area of the triangle rounded to 2 decimal places