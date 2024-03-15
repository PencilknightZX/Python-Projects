# Emmanuel Ifeanyi, 2/16/2023, Lab 03 (Employee Contact list main program) 
from contacts3 import *

employ_files = {}


while True:
    print("*** EMPLOYEE CONTACT MAIN MENU")
    print("1.Add contact")
    print("2.Modify contact")
    print("3.Delete contact")
    print("4.Print contact list")
    print("5.Find contact")
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
    if menu_input == 1:
        try:
            x = int(input("Enter Phone Number: "))
        except:
            print("Invalid Input")
            continue
        fname = input("Enter the first name: ")
        if fname == '':
            print("No Blanks Please!!")
            continue
        lname = input("Enter the last name: ")
        if lname == '':
            print("No Blanks Please!!")
            continue
        else:
            add_contact(employ_files, ID = x, first_name = fname, last_name = lname)

#(2) Modifies a contact in employ_files
    elif menu_input == 2:
        try:
            x = int(input("Enter Phone Number: "))
        except:
            print("Invalid Input")
            continue
       
        fname = input("Enter the first name: ")
        if fname == '':
            print("No Blanks Please!!")
            continue
        lname = input("Enter the last name: ")
        if lname == '':
            print("No Blanks Please!!")
            continue
        else:
            modify_contact(employ_files, ID = x, first_name = fname, last_name = lname)
        
#(3) Deletes a contact in employ_files
    elif menu_input == 3:
        try:
            x = int(input("Enter Phone Number: "))
        except:
            print("Invalid Input")
            continue
        delete_contact(employ_files, ID = x)
        
#(4) Prints employ_files contact list 
    elif menu_input == 4:
        print_contact(employ_files)

#(5) Find contacts in employ_files and prints found contacts
    elif menu_input == 5:
        x = input("Enter search string: ")
        find_contact(employ_files, find = x)
        
#(6) exits the program
    elif menu_input == 6:
        print("You're Done")
        break
    
  
