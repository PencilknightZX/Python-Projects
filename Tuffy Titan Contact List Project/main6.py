# Emmanuel Ifeanyi, 3/23/2023, Lab 06 (Tuffy Titan Contact list main program)
from contacts6 import *

file = ""

while True:
    print("*** TUFFY TITAN CONTACT MAIN MENU")
    print("1.Add contact")
    print("2.Modify contact")
    print("3.Delete contact")
    print("4.Print contact list")
    print("5.Set contact filename")
    print("6.Exit Program")
    
# Checks menu_input for non-numerical and out of range inputs
    menu_input = 0
    try:
        x = int(input("Enter menu choice: "))
        if x >=1 and x <=6:
            menu_input = x
        else:
            print("Input not within range")
    except:
        print("Invalid Input")

#(1) Adds contact to dictionary
# when writing a file write back the whole dict since json 'w' overwrites the file
    if menu_input == 1:
        #print(1)
        if file == "":
            print("No File has been Set")
        else:
            numb = str(input("Enter phone number: "))
            numb_check = numb.isdigit()
            if numb_check != True:
                print("Must be a Numerical Input")
                continue
            else:
                f_name = str(input("Enter First name: "))
                l_name = str(input("Enter last name: "))

            temp_contact = []
            try:
                temp_contact = contact.add_contact(ID = numb, first_name = f_name, last_name = l_name)
                #print("break---")
                #print(temp_contact)
                print("Added:",temp_contact[0],"",temp_contact[1])
            except TypeError:
                print("Phone Number Already Exists")
                continue


#(2) Modifies a contact in tuffy_files
    elif menu_input == 2:
        #print(2)
        if file == "":
            print("No File has been Set")
        else:
            numb = str(input("Enter phone number: "))
            numb_check = numb.isdigit()
            if numb_check != True:
                print("Must be a Numerical Input")
                continue
            else:
                f_name = str(input("Enter First name: "))
                l_name = str(input("Enter last name: "))
                temp_contact = []
                try:
                    temp_contact = contact.modify_contact(ID = numb , first_name = f_name, last_name = l_name)
                    print("Modified:",temp_contact[0],"",temp_contact[1])
                except TypeError:
                    print("Error: ID not Found")
                    continue

        
        
        
#(3) Deletes a contact in tuffy_files
    elif menu_input == 3:
        #print(3)
        if file == "":
            print("No File has been Set")
        else:
            numb = str(input("Enter phone number: "))
            numb_check = numb.isdigit()
            if numb_check != True:
                print("Must be a Numerical Input")
                continue
            else:
                temp_contact = []
                try:
                    temp_contact = contact.delete_contact(ID = numb)
                    print("Deleted:",temp_contact[0],"",temp_contact[1])
                except TypeError:
                    print("Error: ID not Found")
                    continue
        
        
        
#(4) Prints tuffy_files contact list 
    elif menu_input == 4:
        if file == "":
            print("No File has been Set")
        else:    
            print( """==================== CONTACT LIST ====================
Last Name            First Name           Phone
==================== ==================== ==========""")
            for ID in contact.data:
                print(f'{contact.data[ID][1]:<21}{contact.data[ID][0]:<21}{ID}')


#(5) Sets file to a contact filename
    elif menu_input == 5:
        #print(5)
        file = input("Enter contact filename: ")
        contact = Contacts(filename = file)
        
#(6) exits the program
    elif menu_input == 6:
        print("Program Closed")
        break

