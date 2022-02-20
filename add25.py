n = int(input()) # time in seconds
# seconds to days, hours, minutes, seconds
days = n // 86400
hours = (n % 86400) // 3600
minutes = (n % 3600) // 60
seconds = n % 60

print("D:HH:MM:SS -> {:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds)) # convert to time
