import random, math
x, y = random.random(), random.random()
print(round(math.sqrt(1 + y ** 2) * math.sin(x ** 2 / (1 + abs(y))), 3))