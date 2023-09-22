#checking the validity of the while loop

run = False
while not run:
	print('Inside loop')
	status = input('Wanna continue with the loop? [yes/no]: ')
	if status == 'yes':
		run=False
	else:
		run=True


