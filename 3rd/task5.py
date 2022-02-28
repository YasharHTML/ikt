a, b = map(int, input().split())
t = [0,0]
for i in range(a, b + 1):
    t[i % 2] += 1
print("Even: {}\nOdd: {}".format(t[0], t[1]))