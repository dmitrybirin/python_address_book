import sys
import datetime
from errors import NotExistError, AlreadyExistError, ValidationError

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False

def print_person(person):
    print '{name:<30}\t{phone:<20}\t{birthday:<20}'.format(**person)

def list(book):
    for person in book.get_list():
        print_person(person)

def add(book):
    print "Please add the info below"
    
    name = raw_input("Name: ")
    phone = raw_input("Phone: ")

    while True:
        birthday_input = raw_input("Date of birth (dd.mm.yyyy): ")
        
        if is_valid_date(birthday_input):
            break
        else:
            raise ValidationError("The date {birthday} is invalid. Format should be dd.mm.yyyy!".format(birthday=birthday_input)) 

    person = {
        "name": name,
        "phone": phone,
        "birthday": birthday_input
    }
    searched_person = book.search_exact(name)
    if searched_person is None:
        book.add_person(person)
    else:
        print_person(searched_person)
        raise AlreadyExistError("You have the '{name}' in your book already. He's info above:".format(**person))

def search(book):
    name_part = raw_input("Enter the part of name of the person you want to search: ")
    searched_persons = book.search_part(name_part)
    if searched_persons is None:
        print "There is no person with '{name_part}' in your book".format(name_part=name_part)
    else:
        for person in searched_persons:
            print_person(person)

def delete(book):
    name = raw_input("Enter the name of the person you want to delete: ")
    if book.search_exact(name) is None:
        raise NotExistError("There is no '{name}' in your book to delete".format(name=name))
    else:
        book.delete_person(name)

def exit(book):
    sys.exit(0)