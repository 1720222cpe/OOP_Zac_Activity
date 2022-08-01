def show_magicians(messages):
   
    for message in messages:
        print(message)

def make_great(messages, show_magicians):
    
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        show_magicians.append(current_message)

messages = ["Dan", "Aaron", "Zac"]
show_magicians(messages)

show_magicians = []
make_great(messages, show_magicians)

print("\nFinal lists:")
print(messages)
print(show_magicians)