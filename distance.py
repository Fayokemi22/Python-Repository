# Collect 3 input for distance miles and price
#Enter the driving distance
# Enter miles per gallon
# Enter the price per gallon
# Find the cost of driving using formula (distance / miles) * price
# print out the result

distance = float(input("Enter the driving distance "))

miles = float(input("Enter miles per gallon "))

price = float(input("Enter the price per gallon "))

cost = (distance / miles) * price

print("The cost of driving is ", round(cost,2))
