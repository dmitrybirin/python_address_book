from errors import NotExistError


def delete(book):
    name = raw_input("Enter the name of the person you want to delete: ")
    if book.search_exact(name) is None:
        raise NotExistError("There is no '{name}' in your book to delete"
                            .format(name=name))
    else:
        book.delete_person(name)
        print "Person deleted successfully!\n"
        
