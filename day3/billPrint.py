#Rollercoaster bill

print('Welcome to the rollercoaster ride')
height = int(input('Enter your height in cms: '))
age = int(input('Enter your age in yrs: '))
photo =input('Do you want to click a photo?[yes/no]: ')
bill=0
if height > 120 :
	print("You can ride the rollercoaster")
	if age < 12:
		bill+=5
	elif age <= 18:
		bill+=7
	else:
		bill+=12

	if photo=='yes':
		bill+=3

	print(f'The total bill amount is ${bill}')
else:
	print('Sorry we cannot allow you to ride')

