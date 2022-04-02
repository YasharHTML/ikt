def mod(a, b):
    return (a // b) % 2 == 0


n, m = map(int, input("> ").split())

print("Even" if mod(n, m) else "Odd")
