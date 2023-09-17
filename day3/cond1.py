# we will be learning the conditional statements in this stage of the python coding

print('Welcome to the rollercoaster')
height=int(input('Enter your height in cms: '))
if height <= 150:
	print('I am afraid that your height does not satisfy the conditions. Please try again later.')
else:
	print('Welcome... Please move ahead and collect your ticket')

#please make sure that the indentation of the code is proper or else you will be able to get the proper output

#checking if a number is even or odd
num = int(input('Enter a number: '))
if num % 2 == 0:
	print('The enetered number is even')
else:
	print('The enetered number is odd')

#Nested if statements
# if age if above 18 pay $12 or else $7
print('Welcome to the rollercoaster ride')
height = int(input('Please enter your height in cms: '))
age = int(input('Please enter your age in yrs: '))
if height >=120:
	if age >= 18:
		print('Your billed amount is $12')
	elif age > 12:
		print('Your billed amount is $7')
	else:
		print('Your billed amount is $5')
else:
	print('I am afraid your height is not upto the mark.Please try again later')