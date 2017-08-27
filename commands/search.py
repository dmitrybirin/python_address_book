from errors import NotExistError
from helpers import print_person


def search(book):
    name_part = raw_input("Enter the part of name of the person "
                          "you want to search: ")
    searched_persons = book.search_part(name_part)
    if searched_persons is None:
        raise NotExistError("There is no person with '{name_part}'"
                            " in your book".format(name_part=name_part))
    else:
        for person in searched_persons:
            print_person(person)
