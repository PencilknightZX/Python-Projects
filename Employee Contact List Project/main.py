#Emmanuel Ifeanyi, 2/2/2023, Lab 01 (Employee Contact list main program) 
from contacts import *

a = 1
employ_list = []

#infinite loop
while a == 1:
    print("*** EMPLOYEE CONTACT MAIN MENU")
    print("1.Print list")
    print("2.Add contact")
    print("3.Modify contact")
    print("4.Delete contact")
    print("5.Exit program")
    
    menu_input = int(input("Enter menu choice: "))
    #(1) calls function that prints employee list
    if menu_input == 1:
        print_list(employ_list)
    #(2) calls funcation that add a new list to employ_list
    elif menu_input == 2:
        add_contact(employ_list)
    #(3) calls function that replaces elements of a sublist
    elif menu_input == 3:
        modify_contact(employ_list)
    #(4) calls function that delete an element from employ_list
    elif menu_input == 4:
        delete_contact(employ_list)
    #(5) exits the program
    elif menu_input == 5:
        print("You're Done")
        break


        


    

    
