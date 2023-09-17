print("Welcome to the split bill!!!")
bill_amount=float(input('Enter the bill amount:$ '))
new_bill = 0
tip_check=input("Would you like to give a tip ?[yes/no]: ")
if tip_check == 'yes' or tip_check == 'y':
    tip_percentage = int(input('Enter the percentage of the tip you wish to give e.g 10,12,15: '))
    new_bill = bill_amount + (bill_amount*(tip_percentage/100))
else:
    new_bill = bill_amount

members = int(input('Into how many people are splitting the bill: '))
each_bill = round((new_bill/members),2)
#instead of using the round we can also use the inbuilt f string converter f'{:.2f}'
print(f'Each person should pay ${each_bill}')
