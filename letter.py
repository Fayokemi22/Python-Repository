#collect an input for letter
# if letter is aeiou (print viowel)
# if it is not (print consonant)
# else print Invalid Input


letter=input("Letter is ") 

if  letter == "a" or  letter == "e" or letter == "i" or letter == "o" or letter == "u":

	print("vowel")

elif letter != "a" or  letter != "e" or letter != "i" or letter != "o" or letter != "u":


	print("consonant")

else:
	print("invalid input")