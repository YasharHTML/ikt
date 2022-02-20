def euclidian_distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5 # calculate the distance between two points

A = list(map(float, input("Enter the coordinate of A: ").split())) # coordinate of A
B = list(map(float, input("Enter the coordinate of B: ").split())) # coordinate of B

print(euclidian_distance(*A, *B)) # *A, *B is the same as A[0], A[1], A[2], B[0], B[1], B[2]