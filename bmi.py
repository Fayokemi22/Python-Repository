weight = float(input("The weight is "))

height = float(input("The height is "))

bmi = (weight / (height * height))

if bmi < 18.5:

	print("underweight")

elif bmi >= 18.5 and bmi <= 24.9:

	print("Normal")

elif bmi >= 25 and bmi<= 29.9:
	
	print("overweight")

elif bmi >= 30:

	print ("obese")

print("BMI is: ", round(bmi,2))