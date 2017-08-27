Address book implemetation as task

## Task content:

Develop standart Adress Book functionality with Python 2.7 with storing the following data:
- Full Name
- Phone number
- Birthday

As a plus, develop 'Reminder' feature to remind about friend's birthdays upon run

## Implementation details and choices

I've decided to go with the interactive pattern instead of arguments.

I've decided to use csv instead of familiar json, cause it be more easy to implement import/export from customer files in future, for example:)

## Config Values
```
BOOK_FILE 
```
The address book in csv format. Default to './book.csv'

```
DAYS_TO_REMIND
```
Days in the future to remind about birthdays. Default is 7

## Run

```
python run.py
```

## Features

You can use the following commands:

### list
lists the whole address book info

### add
add new person to the list
you can't add the person with the same name as already existed

### delete
delete teh person by exact name
you can't delete the person that doesn't exist

### search
search the whole book names for the query
if the query is inside name, it will be in the reult list

### exit
exit the app

## What hasn't been done yet

- [x] Commands refactoring, too messy in the run.py
- [x] Date validation
- [x] Reminder feature
- [x] Pep8 for God's sake
- [ ] Document functions properly
- [ ] Use Docker for 2.7 if there will be additional modules ?
- [ ] Replace interactive implementation with the argument one ? 