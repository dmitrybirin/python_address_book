import json
from address_book import AddressBook

available_commands = ['list', 'add', 'delete', 'search', 'remind', 'exit']

print "Hello, this is your address book!"
book = AddressBook()

while True:
    input = raw_input("Enter the one of commands below\n{}\n".format(', '.join(available_commands)))
    command = input.lower()
    if command not in available_commands:
        print "I don\'t understand your command. Sorry!\n"
    else:
        
        if command == "list":
            list = book.get_list()
            print(json.dumps(list, indent=4))
        
        if command == "add":
            print("Please add the info below")            
            person = {
                "name":raw_input("Name: "),
                "phone":raw_input("Phone: "),
                "birth_date":raw_input("Date of birth: ")
            }
            book.add_person(person)

        if command == "add":
            print("Please add the info below")            
            person = {
                "name":raw_input("Name: "),
                "phone":raw_input("Phone: "),
                "birth_date":raw_input("Date of birth: ")
            }
            book.add_person(person)

        if command == 'exit':
            break

        print('Your command is not implemented yet. Sorry\n')