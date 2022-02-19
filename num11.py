import random

x = random.randint(1000,9999)
t = []
for i in range(0,4):
    t += [x%10]
    x = x//10
p = 1
for i in t:
    print(i ** 2)
    p *= i
print(p)