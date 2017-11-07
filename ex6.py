# assign 10 to types_of_people
types_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

# assigns "binary" to binary
binary = "binary"
# assigns "don't" to do_not
do_not = "don't"

# assigns f-string to y (embedded binary and do_not)
y = f"Those who know {binary} and those who {do_not}."

# prints strings associated with x and y. Then reitterates.
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# assigns False to hilarious and a string to joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# prints string with "hilarious" evaluation
print(joke_evaluation.format(hilarious))

# assigns strings to variables w and e
w = "This is the left side of . . ."
e = "a string with a right side."

# prints w and e's strings one after the other
print(w+e)