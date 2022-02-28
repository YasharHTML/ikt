n = int(input("Binary: "))
new = 0
i = 0
while n > 0:
    new += 2 ** i * n % 10
    i += 1
    n //= 10
print("To decimal: ", new)
new1 = 0
i = 0
while new > 0:
    new1 += 10 ** i * (new % 2)
    new //= 2
    i += 1
print("To Bin again: ", new1)
