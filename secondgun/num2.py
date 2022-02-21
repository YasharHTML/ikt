a, b, c = map(int, input().split())
if a == b and b == c:
    print(3 * (a + b + c))
else:
    print(a + b + c)
