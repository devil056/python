import random

names='name1,name2,name3,name4,name5,name6,name7'
list_name = names.split(',')
print(list_name)
print(f'{list_name[random.randint(0,len(list_name)-1)]} will pay the bill')