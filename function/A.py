def gcd(a,b):
    min_ = a
    if b < a:
        min_ = b
    t = 2
    for i in range(2,min_+1):
        if a%i==0 and b%i==0:
            t = i
    return t
a, b = map(int,input("Enter: ").split())
print(gcd(a, b))