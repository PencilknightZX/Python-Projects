#lab 10 Emmanuel Ifeanyi 5/9/2023
import csv

filename = 'students.csv'
with open(filename ,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
   
# Calculate and print the total number of students in the file
    student_count = 0
    student_files = []
    for line in csv_reader:
        student_files.append(line)
        student_count += 1
    print("Total Number of Student in",filename,":",student_count)
    #print(student_files)

# Calculate and print the average age of the students
    total_age = 0
    for i in range(len(student_files)):
        total_age = total_age + int(student_files[i]['Age'])
    average_age = total_age / len(student_files)
    #print(total_age)
    print("Average age of all students in",filename,":",average_age)

# Create a new CSV file that contains only the names and
# roll numbers of the students who belong to 10th grade class
    newfile = '10th_grade_students.csv'
    with open(newfile, 'w', newline = '') as new_file:
        field = ['Name','Roll No.']
        csv_writer = csv.DictWriter(new_file, fieldnames = field)
        csv_writer.writeheader()
        for line in student_files:
            if line['Class'] == '10th':
                del line['Age']
                del line['Gender']
                del line['Section']
                del line['Class']
                csv_writer.writerow(line)
        print("CSV File Created:",newfile)
                

 
