#Lab 09 Emmanuel Ifeanyi
from flights import *


file = "Travel"
flight = Flights(file)

while True:
    print("      *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    print("1. Add Flight")
    print("2. Print Flight Schedule")
    print("3. Set Flight Schedule filename")
    print("9. Exit the Program")
    try:
        menu_input = 0
        x = int(input("Enter menu choice: "))
        if (1 <= x <= 3) or x == 9:
            menu_input = x
        else:
            print("Input not within range")
    except ValueError:
        print("Invalid Input")

#(1) Adds Flight
    if menu_input == 1:
        origin = input("Enter Origin: ")
        destination = input("Enter Destination: ")
        flight_numb = input("Enter Flight number: ")
        if not flight_numb.isdigit():
            print("Error: Non-nuemrial Input")
            continue
        depart = input("Enter Departure Time(HHMM): ")
        arrival= input("Enter Arrival Time(HHMM): ")
        next_day = input("Is Arrival Next Day(Y/N): ")
        if next_day.upper() == "Y":
            next_day = 1
            flight.add_flight(origin, destination, flight_numb, depart, arrival, next_day)
        elif next_day.upper() == "N":
            next_day = 0
            flight.add_flight(origin, destination, flight_numb, depart, arrival, next_day)
        else:
            print("Invalid Input")
            continue
        
        
#(2) Prints the flight schedule
    elif menu_input == 2:
        flight.get_flights()

#(3) Sets flight schedule filename
    elif menu_input == 3:
        file = input("Enter Flight Schedule Filename:" )
        flight = Flights(filename = file)

#(9) Closes the Program       
    elif menu_input == 9:
        print("Program Closed")
        break
