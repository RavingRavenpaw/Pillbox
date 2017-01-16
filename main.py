#Define some variables that will be used across functions
hour = 0
amOrPm = 0
amPmVar = ""
months = ["January", "February", "March", "April", "May", "June" "July", "August", "September", "October", "November", "December"]
year = 0
month = 0
day = 0
alarmHour = 0
alarmMinute = -1
alarmAmOrPm = -1

#Function to convert from 12hr time to 24hr time
def to24Hr(hour, amOrPm):
	if amOrPm == 1:
		amPmVar = "AM"
		
	if amOrPm == 2:
		amPmVar = "PM"
		
	#If 12AM (midnight), return 0 (12hr time starts at 12am, 24hr starts at 0)
	if amOrPm == 1 and hour == 12:
		return(0)
		
	#If AM and not 12 (so past midnight), return the existing hour
	if amOrPm ==1 and hour != 12:
		return(hour)
	
	#If 12PM (noon), just return 12
	if amOrPm == 2 and hour == 12:
		return(hour)
	
	#If PM and not 12PM (so past noon),  add 12 hours to convert to 24 hour time
	if amOrPm == 2 and hour != 12:
		return(hour + 12)


def to12Hr(hour, minute):
	if hour == 0:
		return("" + "12" + ":" + minute + " AM")
	
	if hour > 0 and hour < 12:
		return("" + hour + ":" + minute + " AM")
		
	if hour == 12:
		return("" + "12" + ":" + minute + " PM")
		
	if hour > 12:
		return("" + (hour - 12) + ":" + minute + " PM")
	
	
#Initialization - get current time
while (1==1):
	hour = -1
	minute = -1
	amOrPm = -1
	
	while hour < 1 or hour > 12:
		hour = int(input("Current hour: "))
		
		if hour < 1 or hour > 12:
			print("Please enter an hour from 1 to 12.")
			
	while minute < 0 or minute > 59:
		minute = int(input("Current minute: "))
		
		if minute < 0 or minute > 59:
			print("Please enter a minute from 0 to 59")
			
	while amOrPm != 1 and amOrPm != 2:
		amOrPm = int(input("AM (1) or PM (2)? "))
		print("")

	
	#CONVERT TO 24 HR
	hour = to24Hr(hour, amOrPm)
	
	
	#Get date (with basic error handling!)
	while len(str(year)) != 4:
		year = input("Year: ")
		
		if len(year) != 4:
			print("Please enter a valid year.")
	
	while int(month) < 1 or int(month) > 12:
		month = input("Month: ")
		
		if int(month) < 1 or int(month) > 12:
			print("Please enter the number of a valid month (1 to 12).")

	while int(day) < 1 or int(day) > 31:
		day = input("Day: ")
		
		if int(day) < 1 or int(day) > 31:
			print("Please enter a valid day (1 - 31).")
		print("")
	
	
	#Get date and time ready for time_tuple
	#
	#year defined when getting date
	#month defined when getting date
	#day defined when getting date
	#hour defined when getting time
	#minute defined when getting time
	#second will just use 0
	#millisecond wil just use 0
	
	#Ask if that is correct, and if not, ask repeat time & date setting
	correct = 0
	print(months[int(month) - 1] + " " + str(day) + " " + str(year) + ", " + str(hour) + ":" + str(minute) + amPmVar)
	print("Is that correct? (0 - no, 1 - yes)")
	correct = int(input())
	if correct == 1:
		break
	else:
		continue


#Set Linux time and date
global time_tuple
time_tuple = ( year, # Year 
							month, # Month 
							  day, # Day 
							 hour, # Hour 
						 minute, # Minute 
									0, # Second 
									0, # Millisecond 
							) 


#python set_time




#Set the alarm time
while (1==1):
	while alarmHour < 1 or alarmHour > 12:
		alarmHour = int(input("Alarm hour: "))
		
		if alarmHour < 1 or alarmHour > 12:
			print("Please enter an hour from 1 to 12.")
		
	while alarmMinute < 0 or alarmMinute > 59:
		alarmMinute = int(input("Alarm minute: "))
		
		if alarmMinute < 0 or alarmMinute > 59:
			print("Please enter a minute from 0 - 59.")
			
	while alarmAmOrPm != 1 and alarmAmOrPm != 2:
		alarmAmOrPm = int(input("AM (1) or PM (2)? "))
		print("")
			
		correct = 0
		print("" + str(to24Hr(alarmHour, alarmAmOrPm)) + ":" + str(alarmMinute) + " " + amPmVar)
		print("Is that correct? (0 - no, 1 - yes)")
		correct = int(input())
		if correct == 1:
			break
		else:
			continue

''' REGULAR BACKGROUND PROCESSES
VIA THREADING, MULTIPROCESSING, OR RUNNING MULTIPLE PYTHON FILES


check time every five minutes or so
if not alarm time
    do nothing, go back to background process

if it is alarm time
    while corresponding pillbox switch is pressed down/until it is depressed
        1. Display message to take pills on LCD and flash LCD
        2. Flash an LED
        3. Play music
		
	if wrong pillbox switch depressed
		1. Change music to a warning tone
		2. Flash LCD and display message that wrong pillbox was removed
		3. Wait until switch pressed back in

    When corresponding pillbox switch is depressed and user removes box
        1. Change LCD back to normal
        2. Turn off LED
        3. Stop music
Go back to background process
''' 
