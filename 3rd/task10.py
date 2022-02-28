engineerPi = 3
t = 0
for i in range(2, 30, 2):
    if t == 0:
        engineerPi += 4 / (i * (i + 1) * (i + 2))
        t = 1
    else:
        engineerPi -= 4 / (i * (i + 1) * (i + 2))
        t = 0
print(engineerPi)