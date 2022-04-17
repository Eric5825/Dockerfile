# converting weight using if statements weight Kilos and Lbs.
weight = float(input("Weight: "))   # Enter weight.
unit = input("(K)g or (L)bs: ")  # K or L will be measured as a UNIT.
if unit.upper() == "K": # using the unit.upper for recognition of the captial "K" for Kilo
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))  #str is concatenated with the word converted
else: 
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))  #str is concatenated with the word converted.

