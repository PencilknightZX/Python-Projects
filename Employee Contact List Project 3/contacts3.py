# Emmanuel Ifeanyi, 2/16/2023, Lab 03 (Employee Contact list functions)


def add_contact(contacts = {},/,*, ID, first_name, last_name):
    """ Creates a new dictionary key and adds it to an existing dictionary """
    contacts[ID] = [first_name,last_name]
    print("Added:",first_name,'',last_name)
    return contacts

def modify_contact(contacts = {},/,*, ID, first_name, last_name):
    """ Modifies the contents of an existing dictionary key """
    if ID in contacts:
        contacts[ID] = [first_name,last_name]
        print("Modified:",first_name,'',last_name)
        return contacts
    else:
        print("Error: Phone Number Doesn't exists")
        return None

    
def print_contact(contacts = {},/):
    """ Prints the dictionary of Contacts Available """
    print("============ CONTACT LIST ====================")
    print("Last Name     First Name         Phone")
    print("============  =================  =============")
    for ID, names in contacts.items():
        print(f'{names[1]:14}{names[0]:19}{ID}')   

def delete_contact(contacts = {},/,*, ID):
    """ Removes a dictionary key from an existing dictrionary """
    if ID in contacts:
       print("Deleted:",contacts[ID][0],'',contacts[ID][1])
       x = contacts.pop(ID) 
       return contacts
    else:
       print("Error: Phone Number Doesn't exists")
       return None   

def sort_contact(contacts = {},/):
    """ Sorts dictionary in Alphabetical order either by lastname """
    sorted_files = dict(sorted(contacts.items(), key = lambda x:(x[1][0],x[1][0])))
    return sorted_files

def find_contact(contacts = {},/,*, find):
    """ Find a contact from dictionary using a numeric key or string input"""
    new_files = {}
    if find.isdigit():
        key = int(find)
        
        if key in contacts.keys():
            new_files[key] = contacts[key]
            print("============ FOUND CONTACT(S) ================")
            print("Last Name     First Name         Phone")
            print("============  =================  =============")
            for key, names in new_files.items():
                print(f'{names[1]:14}{names[0]:19}{key}')
            
        elif key not in contacts:
            print("Error: Number not Found")
            return None
        
    else:
        string = str(find)
        for keys in contacts:
            if string == contacts[keys][0]:
                new_files[keys] = contacts[keys]
            elif string == contacts[keys][1]:
                new_files[keys] = contacts[keys]
            else:
                continue
        if new_files == {}:
            print("Error: Name not Found")
            return None
        else:
            found_files = {}
            found_files = sort_contact(new_files)
            print("============ FOUND CONTACT(S) ================")
            print("Last Name     First Name         Phone")
            print("============  =================  =============")
            for keys, names in found_files.items():
                print(f'{names[1]:14}{names[0]:19}{keys}')




    
