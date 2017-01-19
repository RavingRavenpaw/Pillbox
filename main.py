import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import time

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

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,

                           lcd_columns, lcd_rows, lcd_backlight)



#Display loading message
print("Loading...")
lcd.message("Loading...")

#Define some variables that will be used across functions
hour = 0
amOrPm = 0
amPmVar = ""
months = ["Jan", "Feb", "Mar", "Apr", "May", "June" "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
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
lcd.show_cursor(True)
while (1==1):
	hour = -1
	minute = -1
	amOrPm = -1
	
	while hour < 1 or hour > 12:
		lcd.clear()
		lcd.message("Current hour: ")
		hour = int(input("Current hour: "))
		
		if hour < 1 or hour > 12:
			lcd.clear()
			lcd.message("Enter hour from\n1 to 12: ")
			print("Please enter an hour from 1 to 12.")
			
	while minute < 0 or minute > 59:
		lcd.clear()
		lcd.message("Current minute: ")
		minute = int(input("Current minute: "))
		
		if minute < 0 or minute > 59:
			lcd.clear()
			lcd.message("Enter minute \nfrom 0 to 59: ")
			print("Please enter a minute from 0 to 59")
			
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
		
		if len(year) != 4:
			lcd.clear()
			lcd.message("Enter a valid\nyear: ")
			print("Please enter a valid year.")
	
	while int(month) < 1 or int(month) > 12:
		lcd.clear()
		lcd.message("Month (as\nnumber): ")
		month = input("Month (as number): ")
		
		if int(month) < 1 or int(month) > 12:
			lcd.clear()
			lcd.message("Enter valid\nmonth (1-12): ")
			print("Please enter the number of a valid month (1 to 12).")

	while int(day) < 1 or int(day) > 31:
		lcd.clear()
		lcd.message("Day: ")
		day = input("Day: ")
		
		if int(day) < 1 or int(day) > 31:
			lcd.clear()
			lcd.message("Enter valid day\n(1 - 31): ")
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
	lcd.clear()
	correct = 0
	print(months[int(month) - 1] + " " + str(day) + " " + str(year) + ", " + str(hour) + ":" + str(minute) + amPmVar)
	
	lcd.message(months[int(month) - 1] + " " + str(day) + " " + str(year) + "\n" + str(hour) + ":" + str(minute) + amPmVar)
	time.sleep(3.5)
	print("Is that correct? (0 - no, 1 - yes)")
	lcd.clear()
	lcd.message("Is that correct?\n(0 no, 1 yes) ")
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

while 1==1:
	if alarmHour == datetime.datetime.time(datetime.datetime.now()[1])
	
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
