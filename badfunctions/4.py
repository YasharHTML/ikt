def check(n, m):
    return m ** m == n


n, m = map(int, input("> ").split())

print(check(n, m))
