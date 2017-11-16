# Study Drill
# Change the  prompt  variable to something else entirely.
# Add another argument and use it in your script
# Understand how to combine """ style multiline string w/ the {} format activator

from sys import argv

script, user_name, pet_choice = argv
prompt = f'{user_name} nyaa ~(=^-^): '

print(f"Welcome {user_name}! I am the {script} script.")
print(f"I see you have indicated that your choice pet is {pet_choice}. Me too!")
print("What is another pet you would love to own?")
pet_choice2 = input(prompt)

print(f"Would you prefer to own {pet_choice} or {pet_choice2}?")
prefer = input(prompt)

print(f"What would you name your {prefer}?")
name = input(prompt)

print(f"""
Thank you for all of your input!
I think it's wonderful that your choice of pet is {pet_choice}. I feel the same way!
Better yet, you even love {pet_choice2}! Brilliant!
However, naming your prefered animal, {prefer}, {name} is a little odd.
I would suggest naming it "Yatza Dratsa Fooji Fooji Frohni." Much more unique.
""")

