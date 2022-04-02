def curzon(n):
    return (2**n + 1) % (2*n + 1) == 0
print(curzon(int(input("> "))))