import datetime
import json

class Flights:

    def __init__(self,/,filename):
        self.filename = filename
        self.data = []
        try:
            with open(self.filename,'r') as openfile:
                self.data = json.load(openfile)
                print("File Acquired:", self.filename)
                #print("BREAK------")
                #print(self.data)
        except FileNotFoundError:
            print("Set File: ",self.filename)
            pass

    def add_flight(self,/,origin, destination, flight_numb, departure, arrival ,next_day):
        flight_list = []
        self.origin = origin
        self.destin = destination
        self.flight_numb = flight_numb
        self.depart = departure
        self.arrival = arrival
        self.next_day = next_day

        #Check for Non-numerical Inputs
        try:
            depart_hour = int(self.depart[0:2])
            #print("DP: ",depart_hour)
        except ValueError:
            print("Non-Numerical Departure Hour Input")
            return False

        try:
            depart_mins = int(self.depart[2:])
            #print("DM: ",depart_mins)
        except ValueError:
            print("Non-Numerical Departure Minutes Input")
            return False

        try:
            arrival_hour = int(self.arrival[0:2])
            #print("AH: ",arrival_hour)
        except ValueError:
            print("Non-Numerical Arrival Hour Input")
            return False

        try:
            arrival_mins = int(self.arrival[2:])
            #print("AM: ",arrival_mins)
        except ValueError:
            print("Non-Numerical Arrival Minutes Input")
            return False

        #check if the departure and arrival minutes and hours are valid for datetime conversion
        if(00 <= depart_hour <= 23) and (00 <= arrival_hour <= 23):
            pass
        else:
            print("(HOUR)Input Exceeds Limit")
            return False     

        if(00 <= depart_mins <= 59) and (00 <= arrival_mins <= 59):
            pass
        else:
            print("(MINUTE)Input Exceeds Limit")
            return False

           
        self.depart = datetime.time(depart_hour,depart_mins)
        #convert self.depart datetime into a formated time string
        self.depart = self.depart.strftime("%#I:%M%p").lower()
        #print(self.depart)
        
        self.arrival = datetime.time(arrival_hour, arrival_mins)
        #convert self.arrival datetime into a formated time string
        self.arrival = self.arrival.strftime("%#I:%M%p").lower()
        #print(self.arrival)

        if self.next_day == 1:
            self.arrival = "+" + self.arrival
            arrive = datetime.timedelta(days = self.next_day, hours = arrival_hour , minutes = arrival_mins)
            depart = datetime.timedelta(hours = depart_hour, minutes = depart_mins)
            duration = arrive - depart
            duration = ':'.join(str(duration).split(':')[:2])
        
        elif self.next_day == 0:
            arrive = datetime.timedelta(days = self.next_day, hours = arrival_hour , minutes = arrival_mins)
            depart = datetime.timedelta(hours = depart_hour, minutes = depart_mins)
            duration = arrive - depart
            duration = ':'.join(str(duration).split(':')[:2])

        flight_list = [self.origin ,self.destin ,self.flight_numb ,self.depart ,self.arrival ,duration]
        #print(flight_list)
        #print("BREAK ---------")
        self.data.append(flight_list)
        #print(self.data)

        #write to file
        with open(self.filename, 'w') as outfile:
            json.dump(self.data, outfile)
        return True

    def get_flights(self):
        if self.data == []:
            print("Flight Schedule Empty")
            return 
        print("""================== FLIGHT SCHEDULE =======================
Origin Destination Number Departure Arrival     Duration
====== =========== ====== ========= ======== =============""")
        for i in range(0,len(self.data)):
            print(f'{self.data[i][0]:<7}{self.data[i][1]:<12}{self.data[i][2]:>6}{self.data[i][3]:>10}{self.data[i][4]:>9}{self.data[i][5]:>14}')
            


     
