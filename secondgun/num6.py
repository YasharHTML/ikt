import math
a, b, c = map(float, input("a b c").split())
D = b ** 2 - 4 * a * c
if D > 0:
    print("2 roots")
    print((-b + math.sqrt(D))/(2*a))
    print((-b - math.sqrt(D))/(2*a))
if D == 0:
    print("1 root")
    print(-b/(2*a))
if D < 0:
    print("No real roots")