from errors import AlreadyExistError, ValidationError
from helpers import print_person, is_valid_date


def add(book):
    print "Please add the info below"
    
    name = raw_input("Name: ")
    phone = raw_input("Phone: ")

    while True:
        birthday_input = raw_input("Date of birth (dd.mm.yyyy): ")

        if is_valid_date(birthday_input):
            break
        else:
            raise ValidationError("The date {birthday} is invalid."
                                  "Format should be dd.mm.yyyy!"
                                  .format(birthday=birthday_input))

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
        raise AlreadyExistError("You have the '{name}' in your book already. "
                                "He's info above.".format(**person))
