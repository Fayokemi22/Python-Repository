# ask users for a number
# check if the number is divisible by 5 and 3

number = int (input("Enter number "))

if number % 5==0 and number % 3 ==0:

	print("divisible")
else:
	print("not divisible")