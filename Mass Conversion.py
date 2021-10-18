secondsInput = 0
minutesInput = 0
hoursInput = 0
daysInput = 0


def userInputFunction():
    global secondsInput
    global minutesInput
    global hoursInput
    global daysInput
    userInput = input("Seconds, minutes, hours, or days?")
    if userInput.lower() == 'seconds':
        secondsInput = int(input("Input number of seconds: "))
    elif userInput == 'minutes':
        minutesInput = int(input("Input number of minutes: "))
    elif userInput == 'hours':
        hoursInput = int(input("Input number of hours: "))
    elif userInput == 'days':
        daysInput = int(input("Input number of days: "))
    else:
        userInput = input("Seconds, minutes, hours, or days?")
        userInputFunction()
    return userInput


userOutput = userInputFunction()


def unitConverter(unit):
    global userOutput
    if unit == 'seconds':
        print(f"Minutes = {secondsInput / 60}, Hours = {secondsInput / 3600}, Days = {secondsInput / 86400}")
    elif unit == 'minutes':
        print(f"Seconds = {minutesInput * 60}, Hours = {minutesInput / 60}, Days = {minutesInput / 3600}")
    elif unit == 'hours':
        print(f"Seconds = {hoursInput * 3600}, Minutes = {hoursInput * 60}, Days = {hoursInput / 24}")
    elif unit == 'days':
        print(f"Seconds = {daysInput * 86400}, Minutes = {daysInput * 3600}, Hours = {daysInput * 24}")


unitConverter(userOutput)
