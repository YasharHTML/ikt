import random
t = random.randint(1,101),random.randint(1,101),random.randint(1,101)
max_ = 0
min_ = 10000000000000000
for i in t:
    if max_ < i:
        max_ = i
    if min_ > i:
        min_ = i
print(t)
print(t[0] + t[1] + t[2] - max_ - min_)
