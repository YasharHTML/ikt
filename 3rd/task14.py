n = int(input("Enter: "))
new = 0
i = 0
while n > 0:
    new += 10 ** i * (n % 2)
    n //= 2
    i += 1
print(new)