import json
from address_book import AddressBook
from config import BOOK_FILE

available_commands = ['list', 'add', 'delete', 'search', 'exit']

print "Hello, this is your address book!"
book = AddressBook()
book.load_file(BOOK_FILE)

while True:
    input = raw_input("Enter the one of commands below\n{}\n".format(', '.join(available_commands)))
    command = input.lower()
    if command not in available_commands:
        print "I don\'t understand your command. Sorry!\n"
    else:
        
        if command == "list":
            for person in book.get_list():
                print('{name:<30}\t{phone:<20}\t{birthday:<20}'.format(**person))
        
        if command == "add":
            print("Please add the info below")            
            person = {
                "name":raw_input("Name: "),
                "phone":raw_input("Phone: "),
                "birthday":raw_input("Date of birth: ")
            }
            book.add_person(person)

        if command == 'exit':
            break