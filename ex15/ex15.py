from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())



# Lines 1-3 use argv to get a filename.'
# Line 5 introduces the command  open. It takes a parameter and returns a value you can set to your own variable.
# You can give a file a command by using the  ., the name of the command, and parameters.
# Line 8 we call a function on  txt  named  read. -> txt.read() says, "Hey txt! Do your read command with no parameters!"