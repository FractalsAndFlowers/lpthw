# Study Drill
# Write a script similar to the last exercise that uses read and argv to read
# the file you just created
# Use strings, formats, and escapes to print out line1-3 with just one target.write() command instead of six.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

txt = open(filename)

# Read file
print(f"Here's your file {filename}:")
print(txt.read())

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the files.")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()
