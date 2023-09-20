def prime_checker(number):
	is_prime=True
	if number==1:
		print('The provided number is not a prime number')
	elif number>1:
		for num in range(2,number):
			if number%num==0:
				is_prime=False
		if is_prime:
			print('Is a prime number')
		else:
			print('Not a prime number')

input_num = int(input('Enter a number you wish to check: '))
prime_checker(input_num)