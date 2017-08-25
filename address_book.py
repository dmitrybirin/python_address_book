from config import BOOK_FILE
from file_handler import get_list_from_file, save_to_file
from person import Person

class AddressBook(object):
    def __init__(self):
        self.book = get_list_from_file(BOOK_FILE)

    def get_list(self):
        return self.book

    def add_person(self, person):
        self.book.append(person)
        save_to_file(self.book, BOOK_FILE)
        
    def delete_person(self, name):
        raise NotImplementedError
    
    def search(self, name):
        for person in self.book:
            if person["name"] == name:
                return person
        return None