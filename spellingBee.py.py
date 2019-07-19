# Spelling Bee
# Description: Spells out the entered Word
# Author: Vatsal Parmar
# Date: 18th June 2019


wordGiven = input("Please, Enter a word to spell: ")  #gets the input from user and stores it in a variable
length = len(wordGiven); #determines the length of the given word
if length == 0:
	print("Come on! Be serious and Enter a word !")
else:

	number = 0;
	temp = 1;


	while number < len(wordGiven):
		print("Letter " + str(temp) + " is '" + wordGiven[number] + "'")
		temp += 1
		number += 1
	
	print("The word '" + wordGiven + "' has " + str(length) + " letters.")


