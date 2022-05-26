alarm_string = input("Enter the time u want to wake up: ")
med_alarm_morn_string = input("Enter the time u want your medicine alarm to be set in the morning: ")
med_alarm_night_string = input("Enter the time u want your medicine alarm to be set in the night: ")
excercise_alarm_string = input("Enter the time u want to excercise: ")
breakfast_alarm_string = input("Enter the time u want to have breakfast: ")
lunch_alarm_string = input("Enter the time u want to have lunch: ")
dinner_alarm_string = input("Enter the time u want to have dinner: ")
reading_alarm_string = input("Enter the time u want to read: ")
sleeping_alarm_string = input("Enter the time u want to sleep: ")

if (alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The alarm has been cancelled")
else:
    print("  "  "  "  "  "  "  "  "  "  "   "  "  "  "  "  "  " "  "  "  "  "  "  "  "  "  "        "   ""Your wake up alarm has been set for " + alarm_string)


if (sleeping_alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The sleeping alarm has been cancelled")
else:          
    print( "Your sleeping alarm has been set for " + sleeping_alarm_string)


if (med_alarm_morn_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The morning medicine alarm has been cancelled")
else:
    print("Your medicine alarm for morning has been set for " + med_alarm_morn_string)


if (excercise_alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The excercise alarm has been cancelled")
else:
    print("Your excercise alarm has been set for " + excercise_alarm_string)


if (breakfast_alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The breakfast alarm has been cancelled")
else:
    print("Your breakfast alarm has been set for " + breakfast_alarm_string)

if (lunch_alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The lunch alarm has been cancelled")
else:
    print("Your lunch alarm has been set for " + lunch_alarm_string)

if (dinner_alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The dinner alarm has been cancelled")
else:
    print("Your dinner alarm has been set for " + dinner_alarm_string)

if (reading_alarm_string == ''):
    print("  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  "  " "  "  "        "   ""The reading alarm has been cancelled")
else:
    print("Your reading alarm has been set for " + reading_alarm_string)
