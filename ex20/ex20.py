from sys import argv

script, input_file = argv

# creates function print_all with argument f
# function prints f.read() which reads the file
def print_all(f):
    print(f.read())

# creates function rewind with argument f
# function sets the file's current position to 0 
# f.seek(0) essentially rewinds file f
def rewind(f):
    f.seek(0)

# creates funtion print_a_line with arguments line_count and f
# function prints the line_count followed by f.readline()
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens the file defined in argv
current_file = open(input_file)

# prints "First let's print the whole file"
print("First let's print the whole file:\n")

# prints file contents
print_all(current_file)

# prints "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

# runs function rewind, which rewinds file f
rewind(current_file)

# prints "Let's print three lines:"
print("Let's print three lines:")

# declares variable current line and assigns it a value of 1
# runs function print__a_line which passes variable current_line and current_file.
# prints current line (= 1) which becomes line_count followed by 
# the current file which becomes f and reads the line:
# '1 This is line 1'
current_line = 1
print_a_line(current_line, current_file)

# declares variable current line and assigns it a value of 1
# runs function print__a_line which passes variable current_line and current_file.
# prints current line (= 2) which becomes line_count followed by 
# the current file which becomes f and reads the line:
# '2 This is line 2'
current_line = current_line + 1
print_a_line(current_line, current_file)

# declares variable current line and assigns it a value of 1
# runs function print__a_line which passes variable current_line and current_file.
# prints current line (= 2) which becomes line_count followed by 
# the current file which becomes f and reads the line:
# '3 This is line 3'
current_line = current_line + 1
print_a_line(current_line, current_file)

# Research what the seek  funtion for  file does.

# Seek sets the file's current position
# Syntax: file.seek(offset[,whence])
# The offset is required - offset from the beginning of the file.
# Whence argument is optional and defaults to 0
# Other values are 1 which means seek relative to the current position and
# 2 which means seek relative to the file's end.
# There is no return value

# When you open a file, the system points to the beggining of the file.
# Any read or write will happen from the beginning.
# A seek() operation moves that pointer to some other part of the file


# the readline method is a way to only read in individual line incremental 
# amounts at a time and return them as strings.
# It reads the next line from file f.
# If a complete line is read, it includes the trailing newline character, \n