n = int(input("Enter: "))
while n % 2 == 0:
    print(2)
    n //= 2
for i in range(3,int(n ** 0.5) + 1,2):
    while n % i == 0:
        print(i)
        n //= i
if n > 2:
    print(n)
