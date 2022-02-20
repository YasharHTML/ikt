n = int(input()) # time in seconds
print("HH:MM:SS -> {0}:{1}:{2}".format(n // 3600, n // 60 % 60, n % 60)) # convert to time
