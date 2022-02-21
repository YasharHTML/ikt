a, b, c = map(int, input().split())
if a == b or a == c or b == c:
    print(0)
else:
    print(a + b + c)