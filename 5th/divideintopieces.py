a = int(input("Enter: "))
x_ = []
while True:
    if a % 2 == 0:
        x_ += [2]
        a //= 2
    else:
        break
for i in range(3, int(a ** 0.5) + 2, 2):
    while a % i == 0:
        x_ += [i]
        a //= i
if a > 2:
    x_ += [a]


print(x_)