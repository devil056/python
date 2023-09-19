import random

words = ['elephant','mouse','lion']
find = random.choice(words)

word=[]
print(find)
for i in range(len(find)):
	word+='_'

print(word)
while '_' in word:
	guess = input('Enter a character: ').lower()
	for pos in range(len(find)):
		char = find[pos]
		if char == guess:
			word[pos]=guess
	print("".join(word))
print('Game completed')