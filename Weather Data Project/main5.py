#Emmanuel Ifeanyi Lab05 Main Module 3/17/2023
from weather import *

weather_files = {}
file = ""

while True:
    print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU ***")
    print("1. Set Data Filename")
    print('2. Add Weather Data')
    print("3. Print Daily Report")
    print("4. Print Historical Report")
    print("5. Exit The Progam")

# Checks menu_input for non-numerical and out of range inputs
    menu_input = 0
    try:
        x = int(input("Enter menu choice: "))
        if x >=1 and x <=5:
            menu_input = x
        else:
            print("Input not within range")
    except ValueError:
        print("Invalid Input")
       
#(1) Set data Filename
    if menu_input == 1:
        file = input("Enter data filename: ")
        weather_files = read_data(filename = file)
        #print(weather_files)

#(2) Add weather data
    elif menu_input == 2:
        #call the write_date function        
        write_data(data = weather_files , filename = file)
        #print(weather_files)
        
#(3) Print Daily Report
    elif menu_input == 3:
        if weather_files == {}:
            print("No File Data Found")
            continue
        else:
            x = str(input("Enter Date(YYYYMMDD): "))
            if len(x)!= 8:
                print("Invalid Input")
            else:
                report_daily(data = weather_files, date = x)

#(4) Print Historical Report
    elif menu_input == 4:
        report_historical(data = weather_files)    

#(5) Exit Program
    elif menu_input == 5:
        print("Program Closed")
        break



            
    
