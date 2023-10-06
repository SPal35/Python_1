alpha,string=0,"Sourav"
for i in string:
	if (i.isalpha()):
		alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of Alphabets is", alpha)
