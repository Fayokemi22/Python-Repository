# collect input for weight
# collect input for height
# use the formula (weight / (height * height)) to get BMI
# if bmi is less than 18.5 (print underweight)
# if bmi is greater than or equal to 18.5 and bmi is bmi is lessthan or equal to 24.9 (normal)
# if bmi greater than or equal to 25 and bmi is less than or equal to 29.9 (print overweight)
# bmi is greater than or equal to 30 (print obese)
# print the result

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