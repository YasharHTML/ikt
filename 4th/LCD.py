a, b = map(int, input().split())
x_, y_ = list(), list()
while True:
    if a % 2 == 0:
        x_ += [2]
        a //= 2
    else:
        break

while True:
    if b % 2 == 0:
        y_ += [2]
        b //= 2
    else:
        break

for i in range(3, int(a ** 0.5) + 2, 2):
    while a % i == 0:
        x_ += [i]
        a //= i
if a > 2:
    x_ += [a]


for i in range(3, int(b ** 0.5) + 2, 2):
    while b % i == 0:
        y_ += [i]
        b //= i
if b > 2:
    y_ += [b]


print(x_)
print(y_)
# function to intersect two lists


def intersect(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def subtract_list(a, b):
    return [i for i in a if not i in b or b.remove(i)]


z_ = subtract_list(x_ + y_, intersect(x_, y_))
p = 1
for i in z_:
    p *= i
print(p)
