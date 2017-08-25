import json
from address_book import AddressBook

available_commands = ['list', 'add', 'delete', 'search', 'exit']

book = AddressBook()

print "Hello, this is your address book!"
print "Enter the one of commands below"

while True:
    input = raw_input("{}\n".format(', '.join(available_commands)))
    command = input.lower()
    if command not in available_commands:
        print "I don\'t understand your command. Sorry!\n"
    else:
        if command == "list":
            for person in book.get_list():
                print '{name:<30}\t{phone:<20}\t{birthday:<20}'.format(**person)
        
        if command == "add":
            print("Please add the info below")            
            person = {
                "name":raw_input("Name: "),
                "phone":raw_input("Phone: "),
                "birthday":raw_input("Date of birth: ")
            }
            book.add_person(person)
            

        # if command == "delete":
        #     name = raw_input("Enter the name of the person you want to delete: ")

        if command == 'exit':
            break