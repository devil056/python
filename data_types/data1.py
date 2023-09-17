'''
This is a proper way for multi line comment
There are 3 data types
1. String
2. Numbers both integers and float
3. Boolean
'''
import datetime

name = input('Enter your full name: ')
date_of_birth = input('Enter your date of birth(DD/MM/YYYY): ')
year = date_of_birth.split("/")[2]
current_date = datetime.datetime.now()
current_year = current_date.date().strftime('%Y')
if (int(current_year)-int(year)) < 18:
    print("I am sorry you are not allowed in the cafe.")
else:
    print('Please enter the cafe')