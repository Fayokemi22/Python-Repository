total_bill = int(input("The total balance is "))

is_member = int(input("The member is "))

if total_bill >= 1000 and is_member == "yes":

	print("10% off")

if total_bill >= 1000 and is_member != "no":
	
	print ("5% off")

else:
	print("No discount Print final amount and discount message")
