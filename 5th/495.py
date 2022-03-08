import math

n = int(input("Enter: "))
su = 0
for i in range(n, 0, -1):
    su += (1 / i)
print(su)

n = int(input("Enter: "))
su = 3
for i in range(n, 0, -1):
    su *= (2*(i ** 2) - 1)
print(su)

n, x = int(input("Enter n: ")), float(input("Enter x: "))
su = 0
for i in range(n, 0, -1):
    su += math.sin(i * x * math.pi/180) / i
print(su)