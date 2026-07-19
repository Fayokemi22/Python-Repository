#collect input for x
# collect input for y
# if x is greater 0 and y is less than 0 print (print("Q1")
#elif x is less than 0 and y is greater than 0: (print("Q2")
#elif x is greater 0 and y is less than  0:   print("Q3")
#elif x is greater 0 and y is less than 0: print("Q4")
# elif x and y is equal to 0: print("Origin")
# elif elif y is equal to 0 and x is not equal to 0: print("X-axis")
# elif x is equal to 0 and y is not equal to 0: print("Y-axis")


x = int(input("first integer is "))

y = int(input("second integer is "))

if x > 0 and y >0:
	print("Q1")

elif x < 0 and y >0:
	print("Q2")

elif x < 0 and y < 0:
	print("Q3")

elif x > 0 and y < 0:
	print("Q4")

elif x and y ==0:
	print("Origin")

elif y ==0 and x != 0:
	print("X-axis")

elif x==0 and y !=0:
	print("Y-axis")




