hour = 0
amOrPm = 0
def twelveHeto24Hr(hour, amOrPm):


	#If AM and 12AM (so midnight), subtract 12 hours to convert to 24 hour time
	if amOrPm == 1 and hour == 12:
		return(0)
	
	#If PM and not 12PM (so past noon),  add 12 hours to convert to 24 hour time
	if amOrPm == 2 and hour != 12:
		return(hour + 12)
		
	#If user does not enter 1 (AM) or 2 (PM), return to start of loop
	if amOrPm != 1 and amOrPm != 2:
		print("Error: AM (1) or PM (2) not entered")
	

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
		
	
	amPmVar = ""
	
	#If AM and 12AM (so midnight), subtract 12 hours to convert to 24 hour time
	if amOrPm == 1 and hour == 12:
		hour == 0
	
	#If PM and not 12PM (so past noon),  add 12 hours to convert to 24 hour time
	if amOrPm == 2 and hour != 12:
		hour += 12
		
	#If user does not enter 1 (AM) or 2 (PM), return to start of loop
	if amOrPm != 1 and amOrPm != 2:
		continue
		
	#Set variable for AM or PM
	if amOrPm == 1:
		amPmVar = "AM"

	if amOrPm == 2:
		amPmVar = "PM"
	
	months = ["January", "February", "March", "April", "May", "June" "July", "August", "September", "October", "November", "December"]
	year = 0
	month = 0
	day = 0
	
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

alarm = int(input("Alarm time: "))

'''
#Enter time of 1st alarm and ask if 2nd needed
alarm1 = input("Time of 1st alarm: ")
answer = input("Do you need a 2nd alarm? (yes/no)")

#Enter time of 2nd alarm if needed and ask for 3rd
if answer == yes or answer == y:
	alarm2 = input("Time of 2nd alarm: ")
	answer = input("Do you need a 3rd alarm? (yes/no)")
	
	#Enter time of 3rd alarm
	if answer == yes or answer == y:
		alarm3 = input("Time of 3rd alarm: ")
'''

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

