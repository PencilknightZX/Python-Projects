# Emmanuel Ifeanyi, 2/9/2023, Lab 02(Employee Contact list functions)

def print_list(contacts = []):
    """ Prints the list of Contacts Available """
    print("============ CONTACT LIST ===============")
    print("Index     First Name         Last Name")
    print("======    =================  ============")
    
    for i in range(len(contacts)):
       print(f'{str(i):10}{contacts[i][0]:19}{contacts[i][1]}')

       
def add_contact(contacts = [],*,first_name,last_name):
    #check for blank spaces
    """ Creates a new sublist and appends it to an existing list """
    newlist = []
    newlist += [first_name]
    newlist += [last_name]
    contacts.append(newlist)
    return contacts
    
def modify_contact(contacts = [],*,first_name,last_name,index):
    """ Modifies content of a sublist with user input """
    if index <= (len(contacts)-1) and index >= 0:
        contacts[index][0] = first_name
        contacts[index][1] = last_name
        return True
    else:
        print("Invalid Input")
        return False

def sort_contact(contacts = [],*,column):
    """ Sorts List in Alphabetical order either by first or lastname """
    contacts = sorted(contacts, key = lambda x: x[column])
    return contacts

def delete_contact(contacts = [],*,index):
    """ Deletes a sublist from an existing list """
    if index >= 0 and index <= (len(contacts)-1):
        del contacts[index]
        return True
    else:
        print("Input not within range")
        return False
