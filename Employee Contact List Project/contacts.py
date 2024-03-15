# Emmanuel Ifeanyi, 2/2/2023, Lab 01(Employee Contact list functions)

def print_list(contacts = []):
    """ Prints the list of Contacts Available """
    print("============ CONTACT LIST ===============")
    print("Index     First Name         Last Name")
    print("======    =================  ============")
    
    for i in range(len(contacts)):
       print(f'{str(i):10}{contacts[i][0]:19}{contacts[i][1]}')

       
def add_contact(contacts = []):
    """ Creates a new sublist and appends it to an existing list """
    newlist =[]
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")
    newlist += [fname]
    newlist += [lname]
    contacts.append(newlist)
    return contacts
    
def modify_contact(contacts = []):
    """ Modifies content of a sublist with user input """
    try:
        x = int(input(" What index number would you like to modify: "))
    except:
        print("Invalid Input")
    else:
        if x<=5 and x>=1:
            fname = input("Enter the first name: ")
            lname = input("Enter the last name: ")
            contacts[x][0] = fname
            contacts[x][1] = lname
            return contacts
        else:
           print("Invalid Input") 

def delete_contact(contacts = []):
    """ Deletes a sublist from an existing list """
    try:
        x = int(input(" What index number would you like to delete: "))
    except:
        print("Invalid Input")
    else:
        #for i in contacts:
            #if x == i:
                del contacts[x]
                return contacts
            #else:
                #print("Invalid Input")
        

