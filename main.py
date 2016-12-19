#Initialization - get current time & date
time12hr = input("Current time: ")
amOrPm = input("AM (1) or PM (2)? ")

print("Current date (format MMDDYYYY): ")
date = input("")
months = ["January", "February", "March", "April", "May", "June" "July", "August", "September", "October", "November", "December"]

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
