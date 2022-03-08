n = int(input("Enter: "))
su = 0
for i in range(3, 2 * n, 2):
    su += 1 / i
print(su)

n = int(input("Enter: "))
su = 1
for i in range(2, 2 * n + 1, 2):
    su *= (1 / (i ** 2))
print(su)

n = int(input("Enter: "))
su = 0
for i in range(1, n + 1, 2):
    su += ((2 * n - 1) ** 0.5 / (2 * n))
print(su)
