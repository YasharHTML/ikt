k = 0
su = 0
while True:
    n = int(input(">"))
    if n == -1:
        break 
    su += n
    k += 1
print(su / k)