def isPronic(n):
    for i in range(1, n):
        if n == i * (i + 1):
            return True
    return False

n = int(input("Enter a number: "))
if isPronic(n):
    print("{} is a pronic number".format(n))
else:
    print("{} is not a pronic number".format(n))
    