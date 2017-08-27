from config import DAYS_TO_REMIND
from errors import ValidationError
from datetime import datetime, timedelta
from helpers import print_person


def remind(book):
    current_year = datetime.now().year
    in_a_days_to_remind = datetime.now() + timedelta(days=DAYS_TO_REMIND)
    persons_to_remind_of = []
    for person in book.get_list():
        try:
            birthday = datetime.strptime(person["birthday"], '%d.%m.%Y')
            current_year_birthday = birthday.replace(year=current_year)

            if current_year_birthday > datetime.now() and current_year_birthday < in_a_days_to_remind:
                persons_to_remind_of.append(person)

        except ValueError:
            raise ValidationError("The {birthday} date in your book "
                                  "is not valid. Please check {name}"
                                  .format(**person))
        
    if len(persons_to_remind_of) > 0:
        print "The following persons are celebrating birthday "
        "in the next {days} days".format(days=DAYS_TO_REMIND)
        
        for person in persons_to_remind_of:
            print_person(person)

    else:
        print "There is nobody celebrating birthday in {days} days. "
        "Call parents!".format(days=DAYS_TO_REMIND)
    