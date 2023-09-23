#calculator with funcs

def add(num1,num2):
	"""
	This function is used to provide additions of two numbers
	"""
	return num1+num2

def subtract(num1,num2):
	"""
	This function is used to provide subtracion of two numbers
	"""
	return num1-num2

def multiply(num1,num2):
	"""
	This function is used to provide multiplication of two numbers
	"""
	return num1*num2

def divide(num1,num2):
	"""
	This function is used to provide division of two numbers
	"""
	return num1/num2


funcs = {
	'+':add,
	'-':subtract,
	'*':multiply,
	'/':divide
}

a = float(input('Enter num1: '))
b = float(input('Enter num2: '))
for op in funcs:
	print(op)

func = input('Choose the kind of operation you wish to perform on the provided numbers: ')
res = funcs[func](a,b)

print(f'{a}{func}{b}={res}')