x, y = map(int, input("GCD: ").split())
while(y):
    x, y = y, x % y
print(x)