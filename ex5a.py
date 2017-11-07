# Get rid of my_ in all occurances
# Conversions: in - cm and lbs = kg

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Conversion: 1 Inch = 2.54 Centimeters
height = height * 2.54

# Conversion: 1 Pound = 0.454 Kilograms
weight = weight * 0.454


print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usualy {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")