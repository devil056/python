#BMI calculator 2.0
print('Welcome to the BMI calculator 2.0')
height=float(input('Please enter your height in m: '))
weight=float(input('Please eneter your weight in kg: '))

bmi=round((weight/(height**2)),0)
if bmi > 35:
	print(f'Your BMI is {bmi}, you are clinically obese')
elif bmi>30:
	print(f'Your BMI is {bmi}, you are obese')
elif bmi>25:
	print(f'Your BMI is {bmi}, you are slightly overweight')
elif bmi>18.5:
	print(f'Your BMI is {bmi}, you are normal weight')
else:
	print(f'Your BMI is {bmi}, you are underweight')