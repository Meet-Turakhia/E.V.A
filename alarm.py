import datetime
import winsound  # exclusively for windows only,
# if you are on any other system you can use 'playsound' or 'simpleaudio' module.

alarm_hour = int(input("Set hour: "))
alarm_minutes = int(input("Set minutes: "))
am_pm = input("am or pm? ")

print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")

# time conversion
# because datetime module returns time in military form i.e. 24 hrs format
if am_pm == 'pm':  # to convert pm to military time
    alarm_hour += 12

elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
    alarm_hour -= 12

else:
    pass

while True:  # infinite loop starts to make the program running until time matches alarm time

    # ringing alarm + execution condition for alarm
    if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:
        print("\nIt's the time!")
        winsound.Beep(1000, 1000)
        break
