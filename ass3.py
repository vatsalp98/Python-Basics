# ASCII converter
# Description: Return the ASCII value of the entered letter
# Author: Vatsal Parmar
# Date: 18th June 2019

import re

temp = range(0, 10);
for x in temp:

	###################### Asking for user Input ######################
	print("Please, enter a letter and I will tell you what its ASCII numerical value is: ");
	charGiven = input();

	###################### Checking if input is valid or not ######################
	length = len(charGiven);
	string = bool(length==1);
	digit = charGiven.isdigit();
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]');
	specialChar = bool(regex.search(charGiven));

	###################### Conversion to ASCII if valid Input ######################

	if string == True and digit == False and specialChar == False:
		minAlpha = 97;
		majAlpha = 65;

		###################### Printing Upper Case Alphabets ######################

		if charGiven == "a":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha) + ".");
		
		elif charGiven == "b":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+1) + ".");
	
		elif charGiven == "c":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+2) + ".");

		elif charGiven == "d":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+3) + ".");

		elif charGiven == "e":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+4) + ".");

		elif charGiven == "f":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+5) + ".");	

		elif charGiven == "g":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+6) + ".");

		elif charGiven == "h":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+7) + ".");

		elif charGiven == "i":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+8) + ".");

		elif charGiven == "j":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+9) + ".");		
	
		elif charGiven == "k":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+10) + ".");	

		elif charGiven == "l":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+11) + ".");	

		elif charGiven == "m":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+12) + ".");

		elif charGiven == "n":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+13) + ".");	

		elif charGiven == "o":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+14) + ".");

		elif charGiven	== "p":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+15) + ".");	

		elif charGiven == "q":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+16) + ".");	
	
		elif charGiven == "r":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+17) + ".");

		elif charGiven == "s":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+18) + ".");
		
		elif charGiven == "t":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+19) + ".");

		elif charGiven == "u":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+20) + ".");	

		elif charGiven == "v":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+21) + ".");
			
		elif charGiven == "w":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+22) + ".");

		elif charGiven == "x":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+23) + ".");

		elif charGiven == "y":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+24) + ".");

		elif charGiven == "z":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+25) + ".");

		###################### Printing Upper Case Alphabets ######################

		elif charGiven == "A":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha) + ".");

		elif charGiven == "B":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+1) + ".");
	
		elif charGiven == "C":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+2) + ".");

		elif charGiven == "D":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+3) + ".");

		elif charGiven == "E":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+4) + ".");

		elif charGiven == "F":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(minAlpha+5) + ".");	

		elif charGiven == "G":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+6) + ".");

		elif charGiven == "H":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+7) + ".");

		elif charGiven == "I":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+8) + ".");

		elif charGiven == "J":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+9) + ".");		
	
		elif charGiven == "K":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+10) + ".");	

		elif charGiven == "L":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+11) + ".");	

		elif charGiven == "M":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+12) + ".");

		elif charGiven == "N":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+13) + ".");	

		elif charGiven == "O":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+14) + ".");

		elif charGiven	== "P":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+15) + ".");	

		elif charGiven == "Q":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+16) + ".");	
	
		elif charGiven == "R":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+17) + ".");

		elif charGiven == "S":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+18) + ".");
		
		elif charGiven == "T":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+19) + ".");

		elif charGiven == "U":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+20) + ".");	

		elif charGiven == "V":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+21) + ".");
			
		elif charGiven == "W":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+22) + ".");

		elif charGiven == "X":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+23) + ".");

		elif charGiven == "Y":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+24) + ".");

		elif charGiven == "Z":
			print("Your letter '" + charGiven + "' has the ASCII numerical value " + str(majAlpha+25) + ".");	


	###################### Building Robustness for Invalid Inputs ######################	

	elif digit == True:
		print("Your letter '" + charGiven + "' is actually a number so, please, try again!");
	elif string == False:
		print("Your letter '" + charGiven + "' is actually a string so, please, try again!");
	elif specialChar == True:	
		print("Your letter '" + charGiven + "' is actually not a letter so, please, try again!");

###################### Final Word ######################
print("Wow! That was fun!");
