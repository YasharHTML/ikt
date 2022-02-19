coor1 = list(map(float, input("Enter the first coordinate: ").split()))
coor2 = list(map(float, input("Enter the second coordinate: ").split()))
coor3 = list(map(float, input("Enter the third coordinate: ").split()))

area = abs(coor1[0] * (coor2[1] - coor3[1]) + coor2[0] * (coor3[1] - coor1[1]) + coor3[0] * (coor1[1] - coor2[1])) / 2
print("The area of the triangle is:", area)