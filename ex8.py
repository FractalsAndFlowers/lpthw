# declares new variable "formatter" and assigns value
formatter = "{} {} {} {}"

# prints: 1 2 3 4
print(formatter.format(1, 2, 3, 4))
# prints: one two three four
print(formatter.format("one", "two", "three", "four"))
# prints: True False False True
print(formatter.format(True, False, False, True))
# prints {} x16
print(formatter.format(formatter, formatter, formatter, formatter))
# prints: Try your Own text here Maybe a poem Or a song about fear
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# formatter.format(. . .) is telling python to do the following:
#   - take the formatter string defined on line 1
#   - call its format function, which is similar to telling it to do a command
#     line command named format.
#   - pass to format four arguments, which match up with the four {}s in the
#     formatter variable. This is like passing arguments to the command line
#     command fomat.
#   - the result of calling format on formatter is a new string that has the {}
#     replaced with the four variables. This is what print is now printing out.