numbers = []

for x in range (1, 1001):

   numSplit = [int(d) for d in str(x)]

   odd = False

   for y in range (0, len(numSplit)):

       if numSplit[y] % 2 != 0:

           odd = True

   if (odd == False):

       numbers.append(x)

print (numbers)