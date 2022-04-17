#enter temperature and get a different response depending of temp that is entered.
temperature = float(input("Input Temperature: "))

if temperature > 70:     # below is the beginning of my (if) block. # The indentations represent a block of code.
    print("It's a hot day") # use double quotes when using a single quote in code here an apostrophe.
    print("Drink plenty of water")  # press shift tab to end if statement below.
elif temperature > 30: # starting a new block of code
    print("It's a nice day") # (temp is greater than 20, and less than or equal to 30)
elif temperature > 10: # ( temp is greater than 10, and less than or equal to 20)
    print("It's freezing cold")
else:
    print("It's damn cold")  


print("Done")



