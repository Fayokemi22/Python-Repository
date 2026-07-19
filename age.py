
# collect one input for age
# if age is less than 5, make price to be free
# if age is less than 12, make price to be $5
# if age is less than 64, make price to be $12
# else make price to be $8
# print price

age = int(input("Age is "))

if age<5:
	price = "free"

elif age<12:
	price = "$5"

elif age<64:
	price = "$12"

else:
	price = "$8"

print("The Price" , price)