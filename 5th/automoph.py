n = int(input("Enter: "))
temp = n
leng = 0
while n > 0:
    leng += 1
    n //= 10
print(temp ** 2 % (10 ** leng) == temp)
