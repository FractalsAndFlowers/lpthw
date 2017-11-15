# An import - add features to script from Python feature set.
# argv is the "argument variable"
from sys import argv
# read the WYSS section for how to run this
# Unpacks argv so that it gets assigned to four variables
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Run: python ex13.py first second third
# Can be run with different arguments, i.e. apple, cherry, orange
# Just make sure you give it enough parameters else ValueError
# ValueError: not enough values to unpack (expected 4, got _)