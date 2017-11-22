# Function is called w/ 2 arguments: a and b
# Return the addition of a + b
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b 

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# add(age, subtract(height, multiply(weight, divide(iq, 2))))
# add(35, subtract(74, multiply(180, divide(50, 2))))
# 50 / 2 = 25
# add(35, subtract(74, multiply(180, 25)))
# 180 * 25 = 4500
# add(35, subtract(74, 4500))
# 74 - 4500 = -4426
# add(35, -4426)
# -4,391
#
# Normal formula:
# *35 + 74 - 180 * 50 / 2