def euclidian_distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

A = list(map(float, input("Enter the coordinate of A: ").split()))
B = list(map(float, input("Enter the coordinate of B: ").split()))

print(euclidian_distance(*A, *B))