# Study Drill
# Use only  input and try the script that way. 
# Why is one way of getting the filename better than another?

filename = input(f"Type the file name please: ")

txt = open(filename)

print(txt.read())
