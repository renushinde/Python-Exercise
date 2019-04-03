# Simple If else program using Python. Thiongs learned- input entered by user is always a string. So, we need to convert it into an int or float using int or float function
num = int(input("Enter a number "))

if num % 2 ==0:
    print("You've entered an even number")
else:
	print("num is odd")

# Catching exceptions using try and except
# convert a Fahrenheit temperature to a Celsius temperature:

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
