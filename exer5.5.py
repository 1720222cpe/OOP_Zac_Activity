prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished?"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int (age)

    if age < 3:
        print(" You get in free!")
    elif age < 12:
        print(" Your ticket is Php10.")
    else:
        print(" Your ticket is Php15.")
