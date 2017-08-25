from config import BOOK_FILE
import json

def open_from_file():
    with open(BOOK_FILE, 'r') as file:
        return json.load(file)

def save_to_file(list):
    json_string = json.dumps(list, indent=4)
    print(json_string)
    with open(BOOK_FILE, 'w') as file:
        file.write(json_string)