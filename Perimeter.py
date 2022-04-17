#Perimeter meeasurements of a rectangle......
#Entering Length and width using a float allowing for a decimal if neccessay.....
Length = float(input("Enter the Length of the Rectangle: "))
width = float(input("Enter the Width of the Rectangle: "))
#Below giving Perimeter the value of 2 * (Length + width)
Perimeter = 2 * (Length + width)
#Below you can see code for printing perimeter
print("Perimeter using the following measurements", Length, "and", width, "=", Perimeter)