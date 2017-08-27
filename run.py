from address_book import AddressBook
from commands import list, add, delete, search, exit
from errors import NotExistError, AlreadyExistError, ValidationError

available_commands = {  'list': list,
                        'add': add,
                        'delete': delete,
                        'search': search,
                        'exit': exit }

book = AddressBook()

print "Hello, this is your address book!"
print "Enter the one of commands below"

while True:
    input = raw_input("{}\n".format(', '.join(available_commands.keys())))
    command = input.lower()
    if command not in available_commands.keys():
        print "I don\'t understand your command. Sorry!\n"
    else:
        try:
            available_commands[command](book)
        except (NotExistError, AlreadyExistError, ValidationError) as e:
            print(e)