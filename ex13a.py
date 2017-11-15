# Study drill for exercise 13
# Combine  input  with  argv  to make a script that gets more input from the user

from sys import argv
script, first, second = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)

# Combining argv, input()
var1 = input("Can you repeat your first variable? ")
var2 = input("Can you repeat your second variable? ")

print(f"Your first parameter was declared as \"{first}\", you repeated: \"{var1}\"")
print(f"Your second parameter was declared as \"{second}\", you repeated: \"{var2}\"")

# Combining argv, input(), and .format
var3 = input("Are you certain the first is {}? Can you repeat your first variable once more? ".format(var1))
var4 = input("Are you certain the second is {}? Can you repeat your second variable once more? ".format(var2))

print(f"Okay, so you are positive the first is \"{var3}\" and the second is \"{var4}\". Thanks!")

# When to use argv and input()
#   argv: if user gives your script inputs on the command line
#   input(): if you want user to input using the keyboard while the script is running

# Command line arguments are strings unless you use int() to convert them i.e int(input())