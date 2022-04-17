#Using the Print Functon w/ end=" " and sep=" "!!!!!
name = input("what is your name?: ")
color = input("What is your favorite color?: ")
age = int(input("What is your age?: "))

print(name, end=" ") #To keep all text on one line add end=" "
print("is " + str(age) + "years old", end=" ")
print("and loves the color " +color+ ".", end=" ")

#using sep: below - allows user to put full  statement on one line (working with line above) as evidenced by duplicate portion of ouput below.
print(name, 'is', age, 'years old and loves the color', color, '.', sep=" ")