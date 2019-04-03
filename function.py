lang = input("Enter your language ")
def greet(lang):
	if lang == "es":
		return "Hola"
	elif lang == "Hindi":
		return "Namaste!"
	elif lang == "fr":
		return "Bonjour"
	else:
		return "Hello"

print(greet(lang), 'user')

# Addition of two numbers 
def addtwo (a, b):
	return a + b

print(addtwo (7,5))


# Difference between two numbers

def difference (a,b):
	return a-b

print(difference(2,2))
print(difference(0,2))

# Product of two numbers

def multiplication (a,b):
	return a*b

print(multiplication(2,2))

# Print day 

number = int(input("Enter a number "))

def print_day(number):
	if number ==1:
		return("Today is Sunday")
	elif number == 2:
		return("Today is Monday")
	elif number == 3:
		return("Today is Tuesday")
	elif number == 4:
		return("Today is Wednesday")
	elif number == 5:
		return("Today is Thursday")
	elif number ==6:
		return("Today is Friday")
	elif number == 7:
		return("Today is Saturday")
	else:
		return none

print(print_day(number))

# number_compare
def number_compare(a,b):
	if a < b:
		return ("b is greater")
	elif a> b:
	    return ("a is greater")
	else :
	    return ("a and b are equal") 

print(number_compare (5,6))