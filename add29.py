# convert farhenheit to celcius
def convert(n):
    return (n - 32) * 5 / 9
print("Temperature in Celcius: {}".format(convert(float(input("Enter temperature in farhenheit: ")))))