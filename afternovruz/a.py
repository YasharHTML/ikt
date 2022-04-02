n = int(input("Enter"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(n+1-i, end=" ")
    print()