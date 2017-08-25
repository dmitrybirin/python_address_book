import csv

def yield_dicts_from_file(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def save_to_file(list, path):
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'birthday'])
        writer.writeheader()
        for person in list:
            writer.writerow(person)