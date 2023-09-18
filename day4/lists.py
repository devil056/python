states = ['Uttar Pradesh','Madhya prades','Telangana','Tamilnadu','Karnataka','Kerala','Andhra Pradesh']
for state in states:
	print(state)

print(states[0])
print(states[0:5])
print(states[-1])
print(states[-3:-1])
print(states[-3:])

#to add a item use append

states.append('Uttarakand') #this is at the very end and -1 will be uttarakand
print(states)