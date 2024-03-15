#Emmanuel Ifeanyi Lab07
from people import Faculty, Student

faculty_list = []
student_list = []

while True:
    print("   *** TUFFY TITAN STUDENT/FACULTY MAIN MENU *** \n")
    print("1.Add Faculty")
    print("2.Print Faculty")
    print("3.Add Student")
    print("4.Print Student")
    print("9.Exit the Program \n")
    
# Checks menu_input for non-numerical and out of range inputs
    menu_input = 0
    try:
        x = int(input("Enter menu choice: "))
        if x >=1 and x <=4 or x == 9:
            menu_input = x
        else:
            print("Input not within range \n")
    except:
        print("Invalid Input \n")

#(1) Adds Faculty to the Dictionary
    if menu_input == 1:
        #print(1)
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        dept = input("Enter Department: ")
        
        # instantiates a faculty object
        faculty = Faculty(f_name, l_name, dept)
        # Adds object to the faculty list
        faculty_list.append(faculty)

#(2) Prints List of Faculty with their Info
    elif menu_input == 2:
        #print(2)
        if faculty_list != []:
            print("""======================= FACULTY =======================
Record  Name                 Department
======  ==================== ==========================""")
            for i in range(len(faculty_list)):
                full_name = faculty_list[i].first_name + " " + faculty_list[i].last_name
                print(f'{i:<8}{full_name:<21}{faculty_list[i].department}')
        else:
            print("Faculty List is Empty \n")
#(3) Adds Student to the Dictionary
    elif menu_input == 3:
        #print(3)
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        class_year = input("Enter Class Year: ")
        major = input("Enter Major: ")
        try:
            advisor = int(input("Enter Faculty Advisor Record Number: "))
        except ValueError:
            print("Error: Enter Numerical Input Only ")
            continue
        for i in range(len(faculty_list)):
            if i == advisor:
                # Instantiates a student object
                student = Student(f_name, l_name)

                # Set student variables
                student.set_class(class_year)
                student.set_major(major)
                student.set_advisor(faculty_list[advisor])

                #Add student to student list
                student_list.append(student)
                break   
        else:
            print("Advisor Does Not Exist")         
        
#(4) Prints List of Students with their Info
    elif menu_input == 4:
        #print(4)
        if student_list != []:
            print("""===================================== STUDENTS ======================================
Name                  Class      Major                      Advisor
====================  =========  =========================  =========================""")
            for i in range(len(student_list)):
                full_name = student_list[i].first_name + " " + student_list[i].last_name
                advisor_name = student_list[i].advisor.first_name + " " + student_list[i].advisor.last_name
                print(f'{full_name:<22}{student_list[i].class_year:<11}{student_list[i].major:<27}{advisor_name}')
        else:
            print("Student List is Empty \n")
#(9) Exits the program
    elif menu_input == 9:
        print("Program Closed")
        break





        
