import math

height = int(input('Enter height of the wall you wish to paint: '))
width = int(input('Enter width of the wall you wish to paint: '))
coverage = 5 #using the one paint we can cover 5 sq mts

def can_find(height,width,cover):
	area = height*width
	num_of_cans = math.ceil(area/cover)
	return num_of_cans

cans_needed = can_find(height=height,width=width,cover=coverage)
print(f'you need {cans_needed} to paint the wall')
