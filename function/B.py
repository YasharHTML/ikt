def findsumofdigits(a):
    sum = 0
    a = str(a)
    for i in range(len(a)):
        sum += int(a[i])
    return sum

def findsumofdigitsv2(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

n = int(input("Enter: "))


print(findsumofdigits(n))
print(findsumofdigitsv2(n))