#Emmanuel Ifeanyi Lab05 Weather Module 3/17/2023
import calendar
import os.path
import json

def read_data(*,filename):
    """ Reads file and returns a dictonary of decoded JSON content """
    decoded_obj = {}
    try:
        with open(filename,'r') as openfile:
            decoded_obj = json.load(openfile)
            #print(type(decoded_obj))
            return decoded_obj
    except FileNotFoundError:
        print("File not Found")
        return decoded_obj

def write_data(*,data, filename):
    """ Opens file and writes data into file """
    file_exists = os.path.exists(filename)
    if file_exists == True:
        with open(filename, 'w') as outfile:
            json.dump(data,outfile)
        #prompt the user for the date, time, temp, humidity ,and rainfall
        date = str(input("Enter Date(YYYYMMDD): "))
        if len(date)!= 8:
                print("Invalid Input please follow prompt")
                return None
        else:
            x = date.isdigit()
            if x == False:
                print("Non-numerical Input")
                return None
            
        time = str(input("Enter Time(hhmmss): "))
        if len(time)!= 6:
                print("Invalid Input please follow prompt")
                return None
        else:
            y = time.isdigit()
            if y == False:
                print("Non-numerical Input")
                return None
            
        try:
            temp = int(input("Enter Temperature: "))
        except ValueError:
            print("Non-numerical Input")
            return None
        try:
            humid = int(input("Enter Humidity: "))
        except ValueError:
            print("Non-numerical Input")
            return None
        try:
            rainfall = float(input("Enter Rainfall: "))
        except ValueError:
            print("Non-numerical Input")
            return None
        #combine input for date and time to form a key
        key = date + time
        #Add key and value to weather_files                 
        data[key]={"t": temp, "h": humid, "r":rainfall}
    else:
        print("No File to Add Data")   

def max_temperature(*,data, date):
    """ Returns max temp for all dictionary data """
    temp_dict = {key: val for key, val in data.items() if key.startswith(date)}
    #print(temp_dict)

    max_temp = 0
    for key in temp_dict:
        if temp_dict[key]['t'] > max_temp:
            max_temp = temp_dict[key]['t']
    return max_temp           
    
def min_temperature(*,data, date):
    """ Returns minimum temp for all dictionary data """
    temp_dict = {key: val for key, val in data.items() if key.startswith(date)}
    #print(temp_dict)
    temp_key = next(iter(temp_dict))
    min_temp = temp_dict[temp_key]['t']
    
    for key in temp_dict:
        if temp_dict[key]['t'] < min_temp:
            min_temp = temp_dict[key]['t']
    return min_temp
    
    
def max_humidity(*,data, date):
    """ Returns max humidity for all dictionary data """
    temp_dict = {key: val for key, val in data.items() if key.startswith(date)}
    #print(temp_dict)

    max_humid = 0
    for key in temp_dict:
        if temp_dict[key]['h'] > max_humid:
            max_humid = temp_dict[key]['h']
    return max_humid
    
def min_humidity(*,data, date):
    """ Returns minimum humidity for all dictionary data """
    temp_dict = {key: val for key, val in data.items() if key.startswith(date)}
    #print(temp_dict)
    temp_key = next(iter(temp_dict))
    min_humid = temp_dict[temp_key]['h']
    
    for key in temp_dict:
        if temp_dict[key]['h'] < min_humid:
            min_humid = temp_dict[key]['h']
    return min_humid
    
def tot_rain(*,data, date):
    """ Returns sum of rainfall for all dictionary data """
    temp_dict = {key: val for key, val in data.items() if key.startswith(date)}
    #print(temp_dict)

    total = 0
    for key in temp_dict:
        total = total + temp_dict[key]['r']
    return total

def report_daily(*,data, date):
    """ Prints the Daily Report given a dictionary key """
    temp_dict = {key: val for key, val in data.items() if key.startswith(date)}
    if temp_dict == {}:
        print("Date not Found")
        return None
    else:
        #print(temp_dict)
        daily = """========================= DAILY REPORT ====================================
Date                      Time        Temperature    Humidity     Rainfall
==================== ============== ============== ============ ===========\n"""
        for key in temp_dict:
            m_name = int(key[4:6])
            day = int(key[-8:-6])
            year = int(key[0:4]) 
            hour = key[-6:-4]
            mins = key[-4:-2] 
            sec = key[-2:] 
            dates = f'{calendar.month_name[m_name]}{day:>3}{",":<2}'
            time = f'{year:<14}{hour}{":"}{mins}{":"}{sec}'
            stats = f'{temp_dict[key]["t"]:>15}{temp_dict[key]["h"]:>13}{temp_dict[key]["r"]:>12}'
            output = dates + time + stats
            daily = daily + output + '\n'
        print(daily)

              
def report_historical(*,data):
    """ Prints the historical report given a dictionary key """
    if data == {}:
        print("No File Data Found")
        return None
    else:
    
        report ="""========================= HISTORICAL REPORT ===========================
                      Minimum     Maximum    Minumum  Maximum  Total
Date                 Temperature Temperature Humidity Humidity Rainfall
==================== =========== =========== ======== ======== ========\n"""
        #Create a list of sort keys with non-duplicates
        key_list = []
        for key in data:
            new_key = key[0:8]
            key_list.append(new_key)
        
        key_list =[*set(key_list)]
        #print("SORTED LIST")
        key_list.sort()
        #print(key_list)
        #print("BREAK-----------")   
        

        #Create a list of strings of formated dates(Month name day, year)
        date_list = []
        
        #create a list of max temps using key_list
        max_temp_list = []
        
        #create a list of min temps using key_list
        min_temp_list = []
        
        #create a list of max humidities using key_list
        max_humid_list = []
        
        #create a list of min humidities using key_list
        min_humid_list = []
        
        #create a list of total rainfalls using key_list
        tot_rain_list = []
        
        for i in range(len(key_list)):

            m_name = int(key_list[i][4:6])
            day = int(key_list[i][-2:])
            year = int(key_list[i][0:4])
            dates = f'{calendar.month_name[m_name]}{day:>3}{",":<2}{year}'
            date_list.append(dates)

            #maxtemp
            a = max_temperature(data = data, date = key_list[i])
            max_temp_list.append(a)

            #mintemp
            b = min_temperature(data = data, date = key_list[i])
            min_temp_list.append(b)

            #maxhumid
            c = max_humidity(data = data, date = key_list[i])
            max_humid_list.append(c)

            #minhumid
            d = min_humidity(data = data, date = key_list[i])
            min_humid_list.append(d)

            #totrain
            e = tot_rain(data = data, date = key_list[i])
            tot_rain_list.append(e)

        #print(date_list)
        #print("BREAK-----------")
        #print(max_temp_list)
        #print("BREAK-----------")
        #print(min_temp_list)
        #print("BREAK-----------")
        #print(max_humid_list)
        #print("BREAK-----------")
        #print(min_humid_list)
        #print("BREAK-----------")
        #print(tot_rain_list)

        for i in range(len(date_list)):
            history = date_list[i].ljust(29) + str(max_temp_list[i]).rjust(3) + str(min_temp_list[i]).rjust(12) + str(min_humid_list[i]).rjust(9) + str(max_humid_list[i]).rjust(9) + str(tot_rain_list[i]).rjust(9)
            report = report + history + '\n'
        print(report)



        
    





            
