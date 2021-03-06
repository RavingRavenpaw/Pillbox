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

#Dependencies
#Adafruit_CharLCD - python package on GitHub
#aplay - linux program on some website
#RPi.GPIO - python package, already installed on Pi


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

switchWeekdays = {36 : "Monday", 38 : "Tuesday", 40 : "Wednsday",
31 : "Thursday", 33 : "Friday", 35 : "Saturday", 37 : "Sunday"}

switchWeekdaysInt = {36 : 0, 38 : 1, 40 : 2,
31 : 3, 33 : 4, 35 : 5, 37 : 6}

def switchPress(channel):
    #Code for checking if right switch pressed/depressed
    #
    #Check if the matching day of the week of the switch number we just pressed
    #corressponds with the weekday of the switch we SHOULD be pressing
    print("Pin: " + str(channel) + " voltage changed to " + str(GPIO.input(channel)))
    if switchWeekdaysInt[channel] == datetime.datetime.today().weekday():
        alarmTriggered = False

    else:
        dayOfWeek = months[datetime.datetime.today().weekday()]
        lcd.clear()
        piPrint("Wrong pillbox!")
        #os.system("aplay command_to_stop_audio")
        #os.system("aplay some_error_sound")
        time.sleep(2)
        lcd.clear()
        piPrint("Put box back\nin " + switchWeekdays[channel] + " slot!")
        time.sleep(3)


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
daysLong = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
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
    GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Saturday, 5
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
    	return("" + str(hour24) + ":" + str(minute) + " AM")

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
        #If that's okay, exit the loop and continue on....
        lcd.clear()
        piPrint("Setting time,\njust a moment...")
        break
    else:
        #If that's not okay, keep looping until the user sets
        #the correct time.
    	pass


#Set Linux time and date
time_tuple = (     year, # Year
                  month, # Month
                    day, # Day
                   hour, # Hour
    		     minute, # Minute
    		          0, # Second
    			      0, # Millisecond
                      )


#Set time if on Pi...
if sys.platform == "linux" or sys.platform == "linux2":
    os.system("sudo date -s \"" + str(day) + " " + months[month] + " " + str(year) + " " + str(hour) + ":" + str(minute) + ":" + "00\"")



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
        time.sleep(2)
        lcd.clear()
        piPrint("Is that correct?\n(0 no, 1 yes) ")
        correct = int(input())
        if correct == 1:
            break
        else:
            continue

#Alarm time checker loop
alarmTriggered = False
while 1==1:
    now = datetime.datetime.now()
    #If actual time and alarm time match, trigger alarm
    if alarmHour == now.hour and alarmMinute == now.minute:
        #Play audio using aplay
        os.system("aplay /home/pi/Pillbox/alarm.wav")

    	#Listen for GPIO pins change if on Pi
        if sys.platform == "linux" or sys.platform == "linux2":
            GPIO.add_event_detect(36, GPIO.BOTH, callback=switchPress, bouncetime=300) #Monday
            GPIO.add_event_detect(38, GPIO.BOTH, callback=switchPress, bouncetime=300) #Tuesday
            GPIO.add_event_detect(40, GPIO.BOTH, callback=switchPress, bouncetime=300) #Wednsday
            GPIO.add_event_detect(31, GPIO.BOTH, callback=switchPress, bouncetime=300) #Thursday
            GPIO.add_event_detect(33, GPIO.BOTH, callback=switchPress, bouncetime=300) #Friday
            GPIO.add_event_detect(35, GPIO.BOTH, callback=switchPress, bouncetime=300) #Saturday
            GPIO.add_event_detect(37, GPIO.BOTH, callback=switchPress, bouncetime=300) #Sunday

        alarmTriggered = True
        timesDone = 0
    while alarmTriggered == True:
        #Print alarm and flash display
        timesDone += 1
        lcd.clear()
        piPrint("Time to take\n" +
        daysLong[datetime.datetime.today().weekday()] + " pills.")
        lcd.set_backlight(0)
        time.sleep(1)
        lcd.set_backlight(1)
        time.sleep(2)
        lcd.clear()
        if timesDone > 30:
            alarmTriggered = False

    #Just print that we're still waiting for the alarm time...
    lcd.clear()
    piPrint("" + to12HrDisplay(now.hour, now.minute) + " " + days[datetime.datetime.today().weekday()] + ",\n"
    + months[now.month - 1] + " " + str(now.day) + ", " + str(now.year))
    print("Waiting for alarm...")
    time.sleep(3)
