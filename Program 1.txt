x = int(input("Enter any number \n"))
print("The factors of",x,"are:")
for i in range(1, x + 1):
    if x % i == 0:
        if i % 2 == 0:
            print(i," Even")
        else:
            print(i," Odd")