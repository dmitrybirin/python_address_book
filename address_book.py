from file_handler import open_from_file, save_to_file

class AddressBook(object):
    def __init__(self):
        self.book = open_from_file()

    def get_list(self):
        return self.book

    def add_person(self, person):
        self.book.append(person)
        save_to_file(self.book)

    def delete_person(self, name):
        raise NotImplementedError
    
    def search(self, query):
        raise NotImplementedError