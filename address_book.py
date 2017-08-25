from config import BOOK_FILE
from file_handler import get_list_from_file, save_to_file

class AddressBook(object):
    def __init__(self):
        self.book = get_list_from_file(BOOK_FILE)

    def get_list(self):
        return self.book

    def add_person(self, person):
        self.book.append(person)
        save_to_file(self.book, BOOK_FILE)

    def delete_person(self, name):
        for i, person in enumerate(self.book):
            if person["name"] == name:
                del self.book[i]
        save_to_file(self.book, BOOK_FILE)
    
    def search_exact(self, name):
        for person in self.book:
            if person["name"] == name:
                return person
        return None

    def search_part(self, query):
        return [person for person in self.book if query.lower() in person["name"].lower()]