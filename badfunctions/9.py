def isPrime(n):
    if n == 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

def digitSum(n):
    sum_ = 0
    while n > 0:
        sum_ += n % 10
        n //= 10
    return sum_

def moran(n):
    if isPrime(n / digitSum(n)):
        return True
    return False

n = int(input("Enter a number: "))
print("Moran" if moran(n) else "Not Moran")
