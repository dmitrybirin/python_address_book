from helpers import print_person

def list(book):
    for person in book.get_list():
        print_person(person)