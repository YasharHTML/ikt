import random
li = [random.randint(1,6) for i in range(10)]
print(li)
max_ = li[0]
max_idx = 0
max_2 = li[0]
max_2_idx = 0
for i in range(len(li)):
    if li[i] > max_:
        max_2 = max_
        max_ = li[i]
        max_2_idx = max_idx
        max_idx = i
    if li[i] < max_ and li[i] > max_2:
        max_2 = li[i]
        max_2_idx = i

print(max_ , max_idx)
print(max_2 , max_2_idx)
