height = int(input('Enter height of the wall you wish to paint: '))
width = int(input('Enter width of the wall you wish to paint: '))
coverage = 5 #using the one paint we can cover 5 sq mts

cans_needed = round((height * width) / coverage)
print(f'you need {cans_needed} to paint the wall')
