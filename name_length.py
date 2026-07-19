#collect one input that says enter your name
# length variable as name
# if the length is less than 5 print short string
# if the length is between 5 and 10 print medium
# if the length is greater than 10 print long string

name = str(input("Enter a name "))

length = len(name)



if length < 5:
	print("short string")

elif 5<=length < 10:
	print("medium string")

elif length > 5:
	print("long string")
