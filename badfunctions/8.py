def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

def kempner(n):
    for i in range(1, n+1):
        if fac(i) % n == 0:
            return i
    
print(kempner(int(input("Enter a number: "))))