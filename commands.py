import sys

def print_person(person):
    print '{name:<30}\t{phone:<20}\t{birthday:<20}'.format(**person)

def list(book):
    for person in book.get_list():
        print_person(person)

def add(book):
    print("Please add the info below")            
    person = {
        "name":raw_input("Name: "),
        "phone":raw_input("Phone: "),
        "birthday":raw_input("Date of birth: ")
    }
    searched_person = book.search_exact(person["name"])
    if searched_person is None:
        book.add_person(person)
    else:
        print "You have the '{name}' in your book already. He's info below:".format(**person)
        print_person(searched_person)

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
        print "There is no '{name}' in your book to delete".format(name=name)
    else:
        book.delete_person(name)

def exit():
    sys.exit(0)