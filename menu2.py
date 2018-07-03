# menu = """
# Electronic Phone Book
# =====================
# 1. Look up a number
# 2. Create an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# """



# def phonebook(): 
#     print menu
#     keep_running = True
#     while keep_running:        
#         user_input = raw_input('What do you want to do?(1-5)?')
#         dictionary = {'andy': '111-1111'}
#         if user_input == '1':
#             look_up = raw_input('Name:')
#             if look_up in dictionary:   
#                 print dictionary[look_up]
#             return phonebook()
            
#         elif user_input == '2':
#             name = raw_input('Name:')
#             number = raw_input('Phone Number:')
#             dictionary[name] = number 
#             return phonebook()   
            
#         elif user_input == '3':
#             delete_name = raw_input('Name:')
#             if delete_name in dictionary:
#                 del dictionary[delete_name]
#             print dictionary
#             return phonebook()    
            
#         elif user_input == '4':
#             print dictionary
#             return phonebook()
            
#         elif user_input == '5':
#             return 'Bye!'
#             False
#         else:
#             print 'That is not     an option!'
#         return phonebook()




# phonebook()

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

class Phonebook(object):

    def __init__(self):
        self.contacts = []

# def run_phonebook():
#     print menu
#     option = raw_input('What do you want to do? (1-5)')
#     if option in menu_options:
#             menu_option = menu_options[option]
#             print menu_option()
#     else:
#         print 'Invalid, try again'
#     return option != '5'

# def find_contact():
#     name = raw_input('Enter Name:')
#     if name in phonebook:
#         return phonebook[name]
#     else:
#         return 'Not Valid' 

# def make_contact():
#     name = raw_input('Enter name:')
#     phone = raw_input('Enter phone number:')
#     phonebook[name] = phone
#     return phonebook   

def make_contact(self):
    name = raw_input('Enter name:')
    phone = raw_input('Enter phone number:')



# def delete_contact():
#     name = raw_input('Enter name:')
#     del phonebook[name]
#     return phonebook

# def list_contacts():
#     return phonebook

# def goodbye():
#     return 'Bye!'

# menu_options = {
#     '1': find_contact,
#     '2': make_contact,
#     '3': delete_contact,
#     '4': list_contacts,
#     '5': goodbye
# }

# keep_running = True
# while keep_running:
#     keep_running = run_phonebook()