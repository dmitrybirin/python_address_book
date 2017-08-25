import json
from address_book import AddressBook

def print_person(person):
    print '{name:<30}\t{phone:<20}\t{birthday:<20}'.format(**person)

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
                print_person(person)
        
        if command == "add":
            print("Please add the info below")            
            person = {
                "name":raw_input("Name: "),
                "phone":raw_input("Phone: "),
                "birthday":raw_input("Date of birth: ")
            }
            searched_person = book.search(person["name"])
            if searched_person is None:
                book.add_person(person)
            else:
                print "You have the '{name}' in your book already. He's info below:".format(**person)
                print_person(searched_person)

        # if command == "delete":
        #     name = raw_input("Enter the name of the person you want to delete: ")

        if command == 'exit':
            break