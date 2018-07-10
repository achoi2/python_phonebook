menu = """
Electronic Phone Book
=====================
1. Look up a number
2. Create an entry
3. Delete an entry
4. List all entries
5. Quit
"""

phonebook = {
    'matt': '111-1111',
    'john': '222-2222',
    'sara': '333-3333'
}

def run_phonebook():
    print menu
    option = raw_input('What do you want to do? (1-5)')
    if option in menu_options:
            menu_option = menu_options[option]
            print menu_option()
    else:
        print 'Invalid, try again'
    return option != '5'

def find_contact():
    name = raw_input('Enter Name:')
    if name in phonebook:
        return phonebook[name]
    else:
        return 'Not Valid' 

def make_contact():
    name = raw_input('Enter name:')
    phone = raw_input('Enter phone number:')
    phonebook[name] = phone
    return phonebook   

def delete_contact():
    name = raw_input('Enter name:')
    del phonebook[name]
    return phonebook

def list_contacts():
    return phonebook

def goodbye():
    return 'Bye!'

menu_options = {
    '1': find_contact,
    '2': make_contact,
    '3': delete_contact,
    '4': list_contacts,
    '5': goodbye
}

keep_running = True
while keep_running:
    keep_running = run_phonebook()