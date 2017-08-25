from file_handler import yield_dicts_from_file, save_to_file
from person import Person

class AddressBook(object):
    def __init__(self):
        self.book = []

    def load_file(self, file_path):
        for person in yield_dicts_from_file(file_path):
            self.book.append(person)

    def save_file(self, file_path):
        save_to_file(self.book, file_path)

    def get_list(self):
        return self.book

    def add_person(self, person):
        self.book.append(person)
        
    def delete_person(self, name):
        raise NotImplementedError
    
    def search(self, query):
        raise NotImplementedError