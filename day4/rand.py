import random

num=random.random()
print(num*5)

rand_int=random.randint(1,5)
print(rand_int)

side = random.randint(0,1)
if (side==1):
	print('Heads')
else:
	print('Tails')