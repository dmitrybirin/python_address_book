import datetime


def print_person(person):
    print '{name:<30}\t{phone:<20}\t{birthday:<20}'.format(**person)


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False