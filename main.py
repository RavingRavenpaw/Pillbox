#Initialization - get current time
correct = False

while correct == False:
	correct = False
	time12hr = input("Current time (HHMM): ")
	amOrPm = input("AM (1) or PM (2)? ")
	if amOrPm == 1:
		hour = time12hr[0:2]
		minute = time12hr[2:4]
		
	if amOrPm == 2:
		hour = int(time12hr[0:2]) + 12
		minute = time12hr[2:4]
		
	#If user does not enter 1 (AM) or 2 (PM), return to start of loop
	else:
		continue
	
	#Get date
	print("Current date (format MMDDYYYY): ")
	date = input("")
	months = ["January", "February", "March", "April", "May", "June" "July", "August", "September", "October", "November", "December"]
	
	#Get date and time ready for time_tuple
	year = date[4:8]
	month = date[0:2]
	day = date[2:4]
	#hour already defined when setting time
	#minute already defined when setting time
	#second will just use 0
	#millisecond wil just use 0
	
	print(months[date[0:2]] + " " + )

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

python set_time

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
