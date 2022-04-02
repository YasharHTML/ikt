#function that reverses a string
def reverse(s):
    return s[::-1] if s.isdecimal() else "error"
n = input("Enter: ")
print("Reversed: ", reverse(n))