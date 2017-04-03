'''Quick note:
To any nerds reading this, the reason why I'm checking if the system platform is
linux before doing a command so often, it's because I'm developing & debugging
on Win10, but the program is actually meant to run on a Raspberry Pi, which
obviously runs linux.

I don't want certain things to be run on Windows (ex.
setting the time or trying to import modules that don't exist on windows,
such as RPi.GPIO), so that's why. I think I could clear up some of this with
'try except' or whatever, but eh, that's for another day.

If you're actually trying to modify this on a linux machine, sorry about that!
'''




#Display loading message
print("Loading...")

import os
import sys
if sys.platform == "win32": #Windows
    #Just do nothing when LCD functions are called
    import pass_empty as LCD

if sys.platform == "linux" or sys.platform == "linux2": #Linux
    #Import those regularly when run on RasPi
    import RPi.GPIO as GPIO
    import Adafruit_CharLCD as LCD
import time
import datetime
import set_time


def piPrint(text):
    #Function to print only to console while debugging on Windows, and
    #to both console and Pi display while on linux (so the RasPi).
    #This lets me debug on Windows, yay!
    #
    #p = text to print, remember to include quotes/format as a string!

    if sys.platform == "win32": #Windows
    #prints to console only
        print(text)

    if sys.platform == "linux" or sys.platform == "linux2": #Linux
    #print to console and RasPi display
        print(text)
        lcd.message(text)

def mondaySwitchPressed(channel): #BCM 36
	#Code for checking if right switch pressed/depressed
	pass

def tuesdaySwitchPressed(channel): #BCM 38
	#Code for checking if right switch pressed/depressed
	pass

def wednsdaySwitchPressed(channel): #BCM 40
	#Code for checking if right switch pressed/depressed
	pass

def thursdaySwitchPressed(channel): #BCM 31
	#Code for checking if right switch pressed/depressed
	pass

def fridaySwitchPressed(channel): #BCM 33
	#Code for checking if right switch pressed/depressed
	pass

def saturdaySwitchPressed(channel): #BCM 35
	#Code for checking if right switch pressed/depressed
	pass

def sundaySwitchPressed(channel): #BCM 37
	#Code for checking if right switch pressed/depressed
	pass

# Raspberry Pi pin configuration for LCD:
lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4


# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above only when on RasPi.
if sys.platform == "linux" or sys.platform == "linux2": #Linux
    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Initialize dummy LCD if on Windows.
if sys.platform == "win32": #Windows
    lcd = LCD.Adafruit_CharLCD()

#Turn on LCD backlight
lcd.set_backlight(1)

#Define some variables that will be used across functions
hour = 0
amOrPm = 0
amPmVar = ""
months = ["Jan", "Feb", "Mar", "Apr", "May", "June" "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
days = ["Mon", "Tues", "Wedns", "Thurs", "Fri", "Sat", "Sun"]
year = 0
month = 0
day = 0
alarmHour = 0
alarmMinute = -1
alarmAmOrPm = -1

#Set GPIO mode and initialize pins when on Pi
if sys.platform == "linux" or sys.platform == "linux2":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Monday, 0
    GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Tuesday, 1
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Wednsday, 2
    GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Thursday, 3
    GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Friday, 4
    GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) #SAturday, 5
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Wednsday, 6

#Function to convert from 12hr time to 24hr time
def to24Hr(hour, amOrPm):

	#If 12AM (midnight), return 0 (12hr time starts at 12am, 24hr starts at 0)
    if amOrPm == 1 and hour == 12:
        return(0)

	#If AM and not 12 (so past midnight), return the existing hour
    if amOrPm == 1 and hour != 12:
        return(hour)

	#If 12PM (noon), just return 12
    if amOrPm == 2 and hour == 12:
    	return(12)

	#If PM and not 12PM (so past noon),  add 12 hours to convert to 24 hour time
    if amOrPm == 2 and hour != 12:
    	return(hour + 12)


#Functoin to convert 24 hour time into 12 hour time and something suitable to
#display to the user
def to12HrDisplay(hour24, minute):
    #Add a 0 before the minute if under 10
    #ex. 5 --> 05
    #Makes the output look nicer
    if minute < 10:
        minute = "0" + str(minute)

    #If hour is midnight
    if hour24 == 0:
        return("" + "12" + ":" + str(minute) + " AM")

    #If after midnight and before noon
    if hour24 > 0 and hour24 < 12:
    	return("" + str(hour24) + ":" + minute + " AM")

    #If noon
    if hour24 == 12:
    	return("" + "12" + ":" + str(minute) + " PM")

    #If past noon
    if hour24 > 12:
        return("" + str((hour24 - 12)) + ":" + str(minute) + " PM")





#Initialization - get current time
lcd.show_cursor(True)
while (1==1):
    hour = -1
    minute = -1
    amOrPm = -1
    year = -1
    month = -1
    day = -1

    while hour < 1 or hour > 12:
        lcd.clear()
        lcd.message("Current hour: ")
        hour = int(input("Current hour: "))

        #Validate hour is between 1 and 12
        if hour < 1 or hour > 12:
            lcd.clear()
            piPrint("Enter hour from\n1 to 12: ")

    while minute < 0 or minute > 59:
        lcd.clear()
        lcd.message("Current minute: ")
        minute = int(input("Current minute: "))

        #Validate minute is between 0 and 59
        if minute < 0 or minute > 59:
            lcd.clear()
            piPrint("Enter minute \nfrom 0 to 59: ")

    #Confirm this is correct
    while amOrPm != 1 and amOrPm != 2:
        lcd.clear()
        lcd.message("AM(1) or PM(2)?\n")
        amOrPm = int(input("AM (1) or PM (2)? "))
        print("")


    #CONVERT TO 24 HR
    hour = to24Hr(hour, amOrPm)


    #Get date (with basic error handling!)
    while len(str(year)) != 4:
        lcd.clear()
        lcd.message("Year:")
        year = input("Year: ")

        if len(str(year)) != 4:
            lcd.clear()
            piPrint("Enter a valid\nyear: ")

    while int(month) < 1 or int(month) > 12:
        lcd.clear()
        lcd.message("Month (as\nnumber): ")
        month = input("Month (as number): ")

        if int(month) < 1 or int(month) > 12:
            lcd.clear()
            lcd.message("Month (as\nnumber): ")
            month = input("Month (as number): ")

    while int(day) < 1 or int(day) > 31:
        lcd.clear()
        lcd.message("Day: ")
        day = input("Day: ")

        if int(day) < 1 or int(day) > 31:
            lcd.clear()
            lcd.message("Enter valid day\n(1 - 31): ")
            day = input("Enter valid day\n(1 - 31): ")
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
    lcd.clear()
    correct = 0
    piPrint(months[int(month) - 1] + " " + str(day) + " " + str(year) + "\n" + to12HrDisplay(hour, minute))
    time.sleep(3.5)
    lcd.clear()
    piPrint("Is that correct?\n(0 no, 1 yes) ")
    correct = int(input())
    if correct == 1:
        #If that's okay, exit the look and continue on....
        break
    else:
        #If that's not okay, keep looping until the user sets
        #the correct time.
    	pass


#Set Linux time and date
if sys.platform == "linux" or sys.platform == "linux2": #Linux
    time_tuple = ( year, # Year
                  month, # Month
                    day, # Day
                   hour, # Hour
    		     minute, # Minute
    		          0, # Second
    			      0, # Millisecond
                      )


#Set time if on Pi...
if sys.platform == "linux" or sys.platform == "linux2":
    set_time._linux_set_time(time_tuple)



#Set the alarm time
correct = 0
while correct == 0:
    while alarmHour < 1 or alarmHour > 12:
        lcd.clear()
        lcd.message("Alarm hour: ")
        alarmHour = int(input("Alarm hour: "))

        if alarmHour < 1 or alarmHour > 12:
            lcd.clear()
            lcd.message("Enter hour from\n 1 to 12.")
            print("Please enter an hour from 1 to 12.")

    while alarmMinute < 0 or alarmMinute > 59:
        lcd.clear()
        lcd.message("Alarm minute: ")
        alarmMinute = int(input("Alarm minute: "))

        if alarmMinute < 0 or alarmMinute > 59:
            lcd.clear()
            lcd.message("Enter min from\n0 - 59.")
            print("Please enter a minute from 0 - 59.")

    while alarmAmOrPm != 1 and alarmAmOrPm != 2:
        lcd.clear()
        lcd.message("AM (1) or PM (2)? ")
        alarmAmOrPm = int(input("AM (1) or PM (2)? "))
        print("")

        #Convert alarm hour from 12hr time to 24he time
        alarmHour = to24Hr(alarmHour, alarmAmOrPm)

        #Confirm date and time are correct
        lcd.clear()
        piPrint("" + str(to12HrDisplay(alarmHour, alarmMinute)))
        lcd.clear()
        piPrint("Is that correct?\n(0 no, 1 yes) ")
        correct = int(input())
        if correct == 1:
            break
        else:
            continue

#Alarm time checker loop
while 1==1:
    now = datetime.datetime.now()
    #If actual time and alarm time match, trigger alarm
    if alarmHour == now.hour and alarmMinute == now.minute:
        #Play audio using aplay
        os.system("aplay /home/Pillbox/alarm.ogg")

	#Listen for GPIO pins fall (so listen for switches being let up) if on Pi
    if sys.platform == "linux" or sys.platform == "linux2":
    	GPIO.add_event_detect(36, GPIO.FALLING, callback=mondaySwitchPressed, bouncetime=300) #Monday
    	GPIO.add_event_detect(38, GPIO.FALLING, callback=tuesdaySwitchPressed, bouncetime=300) #Tuesday
    	GPIO.add_event_detect(40, GPIO.FALLING, callback=wednsdaySwitchPressed, bouncetime=300) #Wednsday
    	GPIO.add_event_detect(31, GPIO.FALLING, callback=thursdaySwitchPressed, bouncetime=300) #Thursday
    	GPIO.add_event_detect(33, GPIO.FALLING, callback=fridaySwitchPressed, bouncetime=300) #Friday
    	GPIO.add_event_detect(35, GPIO.FALLING, callback=GPIO_callback, bouncetime=300) #Saturday
    	GPIO.add_event_detect(37, GPIO.FALLING, callback=GPIO_callback, bouncetime=300) #Sunday

    while alarmHour == now.hour and alarmMinute == now.minute:
        #Print alarm and flash display
        lcd.clear()
        piPrint("Alarm!")
        lcd.set_backlight(0)
        time.sleep(1)
        lcd.set_backlight(1)
        time.sleep(2)
        lcd.clear()

    #Just print that we're still waiting for the alarm time...
    else:
        lcd.clear()
        piPrint("" + to12HrDisplay(now.hour, now.minute) + "\n"
        + days[datetime.datetime.today().weekday()] + ", " + months[now.month - 1] + " " + str(now.day) + ", " + str(now.year))
        print("Waiting for alarm...")
        time.sleep(3)

        '''if sys.platform == "win32": #Clear screen on Windows
            os.system("cls")
        else:
            os.system("clear") #Clear screen elsewhere
        lcd.clear()'''


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
