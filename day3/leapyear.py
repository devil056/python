#Leap year check
year = int(input('Enter the year you wish to check: '))

#approach 1
if (year%400==0 or (year%4==0 and year%100!=0)):
	print('Leap year')
else:
	print('Not leap year')

#approach 2
if year%4==0:
	if year%100==0:
		if year%400==0:
			print('Leap year')
		else:
			print('Not leap year')
	else:
		print('Not leap year')
else:
	print('Not leap year')
