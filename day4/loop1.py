# for loop

list1=['item1','item2','item3','item4','item5','item6']

#one form of for loop
for item in list1:
	print(item)

print('-----completed one iteration-------')

#second approach
for item in range(0,len(list1)-1):
	print(list1[item])

print('---completed 2nd iteration-------')

def while_loop():
	i=0
	while i<=(len(list1)-1):
		print(list1[i])
		i+=1

print('function defining and using no args')
while_loop()
#completed