import random
for i in random.sample(range(1,101), 10):
    if i % 2 == 0:
        print(f"Even: {i}")
    else:
        print(f"Odd: {i}")