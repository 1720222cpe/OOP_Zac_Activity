prompt = "\nPlease enter your age to see the price for a ticket. \nEnter 'quit' when done: "

age = ""

while True:
    age = input(prompt)
    

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <=12:
        print("Your ticket is $10.")
    elif 12 < age:
        print("Your ticket is $15.")
    else:
        print("Please enter a valid age.")