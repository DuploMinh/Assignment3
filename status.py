import time 
from datetime import datetime
import os 
def time_traveled():
    """Get the time passed since the launched time"""
    outfile          = open("time.txt","r")
    init_time        = outfile.readlines()[0]
    outfile.close()
    #Convert the time_stamp back to datetime format
    init_time        = datetime.fromtimestamp(float(init_time))
    cur_time         = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    #Calculate the time interval in seconds
    time_passed      = (cur_time - init_time).total_seconds()
    return time_passed
def time_init():
    """Initialize start time and keep records of timestamp"""
    #Get the time when the spaceship is launched with datetime format
    init_time  = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    #Convert datetime to time stamp for storing into database/text file
    time_stamp = time.mktime(init_time.timetuple())
    #Store data
    infile     = open("time.txt","a")
    infile.write(str(time_stamp) + "\n")
    infile.close()
    return
def clear_screen():
    """Clear Screen Each second"""
    unit = os.system('cls')
def status():     
    """Ship Status"""   
    time_init()    #Store time log each time the program runs
    time_passed = time_traveled() #Important for data initialized
    """Initialize Data"""
    v                   = 39500 #km/h
    total_distance      = 305000000#km
    distance_from_E     = v * (time_passed/3600) 
    distance_to_M       = total_distance - distance_from_E
    arrival_time        = distance_to_M/v
    time_travel         = distance_from_E/v
    fuel_level          = 1000000 #liters
    fuel_burn_rate      = 0.01 #liters/km
    ship_health         = 0 #percentage
    crew_members_health = 0 #percentage
    """Display Data"""
    while distance_to_M != 0:       
        clear_screen()  
        time_passed += 1 #Constantly display data every second            
        #Distance From Earth, updating every second
        distance_from_E = v * (time_passed/3600)      
        #Distance To Mars, updating every second
        distance_to_M = total_distance - distance_from_E
        #Arrival Time Calculation
        arrival_time = distance_to_M/v
        #Time Traveled Calculation
        time_travel  = distance_from_E/v
        #Fuel Level Calculation
        fuel_level = fuel_level - distance_from_E * fuel_burn_rate
        #Ship Health is deteriorated by 1% every hour
        ship_health = 100 - int(distance_from_E/10000)
        #Crew Member Health
        crew_members_health = 100 - int(distance_from_E/50000)
        #Print Data
        print("Local Time: ",time.ctime())
        print("Velocity             |" + str(v) + " Kilometer/Hour")
        print("_____________________|____________________________")
        print("Total_distance       |" + str(total_distance) + " Kilometers")
        print("_____________________|____________________________")
        print("Fuel Burn Rate       |" + str(fuel_burn_rate) + " Liter/Kilometer")
        print("_____________________|____________________________")
        print("Distance From Earth  |" + str('%.2f' % distance_from_E) + " Kilometers") 
        print("_____________________|____________________________")
        print("Distance To Mars     |" + str('%.2f' % distance_to_M) + " Kilometers")
        print("_____________________|____________________________")
        print("Time Of Arrival      |" + str('%.2f' % arrival_time) + " Hours")
        print("_____________________|____________________________")
        print("Time Traveled        |" + str('%.2f' % time_travel) + " Hours")
        print("_____________________|____________________________")
        print("Fuel Level           |" + str('%.2f' % fuel_level) + " Liters")
        print("_____________________|____________________________")
        print("Ship Health Status   |" + str(ship_health) + " %")
        print("_____________________|____________________________")
        print("Crew Health Status   |" + str(crew_members_health) + " %")
        print("_____________________|____________________________")
        time.sleep(1)           
status()
