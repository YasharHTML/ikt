a, b, c = map(int, input().split())
if a == b and a == c:
    print('ALL equal')
elif a == b or a == c or b == c:
    print('2 of 3 equal')
else:
    print('NOT equal')