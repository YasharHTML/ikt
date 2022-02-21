n = int(input("Enter price:"))
if n > 1000:
    print(n * 0.95)
elif n > 500:
    print(n * 0.97)
else:
    print(n)