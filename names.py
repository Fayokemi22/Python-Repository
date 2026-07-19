# collect 2 input for two names
# use short greeting (hi, name) for short name if the name is ithin  the range of 3 and 5
# use long greetings(hello, name0 for long name if the name is above 5

name = input("Enter a name")

length = len(name)


if   3<=length <=5 :

	print("hi,",name)

elif length >=5 :

	print("hello,",name)

