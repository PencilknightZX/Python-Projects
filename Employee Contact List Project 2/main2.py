# Emmanuel Ifeanyi, 2/9/2023, Lab 02 (Employee Contact list main program) 
from contacts2 import *

a=1
employ_list = []

#infinite loop
while a==1:
    print("*** EMPLOYEE CONTACT MAIN MENU")
    print("1.Print list")
    print("2.Add contact")
    print("3.Modify contact")
    print("4.Delete contact")
    print("5.Sort list by first name")
    print("6.Sort list by last name")
    print("7.Exit program")

    menu_input =0
    try:
        x = int(input("Enter menu choice: "))
        if x >=1 and x <=7:
            menu_input = x
        else:
            print("Input not within range")
    except:
        print("Invalid Input")

    #(1) calls function that prints employee list
    if menu_input == 1:
        print_list(employ_list)

    #(2) calls funcation that add a new list to employ_list
    elif menu_input == 2:
        fname = input("Enter the first name: ")
        if fname == '':
            print("No Blanks Please!!")
            continue
        lname = input("Enter the last name: ")
        if lname == '':
            print("No Blanks Please!!")
            continue
        else:
            add_contact(employ_list, first_name = fname, last_name = lname)
        
    #(3) calls function that replaces elements of a sublist
    elif menu_input == 3:
        try:
            x = int(input(" What index number would you like to modify: "))
        except:
            print("Invalid Input")
            
        if x <= (len(employ_list)-1) and x >= 0:    
            fname = input("Enter the first name: ")
            if fname == '':
                print("No Blanks Please!!")
                continue
            lname = input("Enter the last name: ")
            if lname == '':
                print("No Blanks Please!!")
                continue
            modify_contact(employ_list,first_name = fname, last_name = lname, index = x)
        else:
            print("Index not within range")

    #(4) calls function that delete an element from employ_list
    elif menu_input == 4:
        try:
            x = int(input(" What index number would you like to delete: "))
        except:
            print("Invalid Input")
        if x <= (len(employ_list)-1) and x >= 0: 
            delete_contact(employ_list,index = x)
        else:
            print("Index not within range")

    #(5) calls function that sorts the list by first name
    elif menu_input == 5:
        employ_list = sort_contact(employ_list,column=0)

    #(6) calls function that sorts the list by last name
    elif menu_input == 6:
        employ_list = sort_contact(employ_list,column=1)
        
    #(7) exits the program
    elif menu_input == 7:
        print("You're Done")
        break


        


    

    
