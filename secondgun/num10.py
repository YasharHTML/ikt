# days of the week in a list
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
n = int(input('Enter a number between 1 and 7: '))
if n >= 6:
    print(days[n-1])
    print("Rest")
else:
    print(days[n-1])
    print("Work")